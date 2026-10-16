import contextlib
import io
import json
from pathlib import Path
import shutil
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import download_jepa_papers as downloader


def blank_pdf():
    objects = [
        b'<< /Type /Catalog /Pages 2 0 R >>',
        b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 100 100] /Resources << >> >>',
    ]
    data = b'%PDF-1.4\n'
    offsets = []
    for index, obj in enumerate(objects, 1):
        offsets.append(len(data))
        data += f'{index} 0 obj\n'.encode() + obj + b'\nendobj\n'
    xref = len(data)
    data += b'xref\n0 4\n0000000000 65535 f \n'
    data += b''.join(f'{offset:010d} 00000 n \n'.encode() for offset in offsets)
    data += f'trailer\n<< /Size 4 /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode()
    return data


class DownloadTests(unittest.TestCase):
    def test_first_ten_in_json_order_are_downloaded_and_reused(self):
        papers = [
            {'title': f'Paper {index}', 'pdf_url': f'https://openreview.net/pdf?id=id{index}'}
            for index in range(11)
        ]
        calls = []
        def attachment(**kwargs):
            calls.append(kwargs['id'])
            return blank_pdf()
        client = SimpleNamespace(get_attachment=attachment)
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'papers.json'
            source.write_text(json.dumps(papers))
            output = Path(directory) / 'pdfs'
            with patch('openreview.api.OpenReviewClient', return_value=client):
                with contextlib.redirect_stdout(io.StringIO()):
                    result = downloader.main(['--input', str(source), '--output-dir', str(output)])
                    second_result = downloader.main(['--input', str(source), '--output-dir', str(output)])
            self.assertEqual((result, second_result), (0, 0))
            self.assertEqual(calls, [f'id{index}' for index in range(10)])
            self.assertEqual(len(list(output.glob('*.pdf'))), 10)
            report = json.loads((output / 'download_report.json').read_text())
            self.assertTrue(all(item['status'] == 'cached' for item in report))

    def test_html_response_is_rejected_and_next_paper_is_attempted(self):
        papers = [
            {'title': 'Blocked', 'pdf_url': 'https://openreview.net/pdf?id=blocked'},
            {'title': 'Available', 'pdf_url': 'https://openreview.net/pdf?id=available'},
        ]
        client = SimpleNamespace(get_attachment=lambda **kwargs: (
            b'<html>Challenge required</html>' if kwargs['id'] == 'blocked' else blank_pdf()
        ))
        with tempfile.TemporaryDirectory() as directory:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                report = downloader.download_batch(client, papers, directory)
            self.assertEqual([item['status'] for item in report], ['failed', 'downloaded'])
            self.assertFalse((Path(directory) / 'blocked.pdf').exists())
            self.assertEqual(list(Path(directory).glob('*.part')), [])

    @unittest.skipUnless(shutil.which('pdfinfo'), 'pdfinfo is required to check corruption')
    def test_truncated_pdf_is_not_saved_as_success(self):
        client = SimpleNamespace(get_attachment=lambda **kwargs: b'%PDF-1.4\ntruncated')
        paper = {'title': 'Corrupt', 'pdf_url': 'https://openreview.net/pdf?id=corrupt'}
        with tempfile.TemporaryDirectory() as directory:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                report = downloader.download_batch(client, [paper], directory)
            self.assertEqual(report[0]['status'], 'failed')
            self.assertEqual(list(Path(directory).glob('*.pdf')), [])
            self.assertEqual(list(Path(directory).glob('*.part')), [])

    def test_interactive_login_uses_credentials_without_writing_them(self):
        paper = {'title': 'Paper', 'pdf_url': 'https://openreview.net/pdf?id=one'}
        client = SimpleNamespace(get_attachment=lambda **kwargs: blank_pdf())
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'papers.json'
            source.write_text(json.dumps([paper]))
            output = Path(directory) / 'pdfs'
            stdout = io.StringIO()
            with patch.dict('os.environ', {'OPENREVIEW_TOKEN': 'unused-test-token'}, clear=True):
                with patch('builtins.input', return_value='test@example.com'):
                    with patch('download_jepa_papers.getpass.getpass', return_value='test-password'):
                        with patch('openreview.api.OpenReviewClient', return_value=client) as constructor:
                            with contextlib.redirect_stdout(stdout):
                                result = downloader.main([
                                    '--login', '--limit', '1', '--input', str(source),
                                    '--output-dir', str(output),
                                ])
            self.assertEqual(result, 0)
            constructor.assert_called_once_with(
                baseurl=downloader.API_URL, username='test@example.com', password='test-password',
            )
            report = (output / 'download_report.json').read_text()
            self.assertNotIn('test-password', stdout.getvalue() + report)
            self.assertNotIn('unused-test-token', stdout.getvalue() + report)


if __name__ == '__main__':
    unittest.main()
