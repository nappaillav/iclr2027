# ICLR 2027 JEPA reading plan

The saved search export contains 337 matching papers. All have distinct titles
and PDF URLs. Search completeness has not been established. A keyword match does
not necessarily indicate that a paper proposes a new JEPA method.

This initial shortlist is based only on the supplied titles and abstracts.
Descriptions report the authors' proposed mechanisms; they are not conclusions
from reading the main papers. No PDFs have been downloaded or read.

## Initial shortlist for general JEPA methods

| Paper | Proposed mechanism described in the abstract | What to check in the main paper |
| --- | --- | --- |
| [$\lambda$-JEPA](https://openreview.net/pdf?id=r1H9TwpMFX) | Applies spectral anti-collapse regularization to the backbone, motivated by balancing weight scales across layers. | Exact SACReg objective; linear-theory assumptions; whether the backbone intervention explains transfer gains at comparable compute. |
| [LeVJEPA](https://openreview.net/pdf?id=p6BV8mTYj3) | Trains one video encoder with global/local view invariance and SIGReg; uses random token dropping and supports causal attention. | How the view loss and regularizer are implemented; video/motion evaluation; data and compute matching. |
| [K-JEPA](https://openreview.net/pdf?id=GMRGQIf7n4) | Predicts a kernel feature map of targets to represent a conditional distribution rather than only a point estimate. | Kernel approximation, predictor output, training loss, distribution-identification assumptions, and calibration/retrieval evidence. |
| [DiJEPA](https://openreview.net/pdf?id=zejU11C6Hc) | Jointly learns a feature autoencoder and predicts its low-dimensional target latents with a diffusion denoiser. | Joint optimization, gradient/target handling, prediction cost, and contribution of the feature autoencoder versus diffusion. |
| [SiamJEPA](https://openreview.net/pdf?id=rnGKOcquJa) | Uses masked Siamese student encoders, an EMA teacher, shuffled teacher targets, and a semantic-to-spatial curriculum. | Architectural sharing, exact Siamese loss, curriculum schedule, and ablations separating the proposed components. |
| [LocaLeJEPA](https://openreview.net/pdf?id=X4kZhguynv) | Uses locally Euclidean distribution regularization to accommodate geometric priors and non-Euclidean embeddings. | Definition and implementation of LocaLeReg, geometric assumptions, and comparisons controlling for backbone choice. |

## Companion papers on representation selection and failure modes

| Paper | Abstract-based observation | What to check in the main paper |
| --- | --- | --- |
| [Characterizing How JEPA Constructs Representations](https://openreview.net/pdf?id=8rftN5ad3o) | Describes feature selection through joint predictive relationships, called predictive closure, rather than individual predictability alone. | Objective reformulation, scope of the characterization, and experiments that manipulate predictive relationships. |
| [Predicting the Predictable](https://openreview.net/pdf?id=2hxylt8J0e) | Attributes feature suppression under fixed-distribution constraints to competition for variance and introduces an additional penalty. | Exact penalty, meaning of numerical/effective rank, augmentation conditions, and controls against I-JEPA. |
| [Lower Loss by Forgetting](https://openreview.net/pdf?id=jUDCutOLmH) | Links gradients through trainable targets to suppression of high-innovation features and to planning-distance failures. | Which target configurations the analysis covers; retention thresholds; causal interventions and control-task evidence. |
| [You Only Live Once](https://openreview.net/pdf?id=3oyf1wlIWQ) | Studies finite streamed experience and proposes removing stop-gradient, adding a variance floor, and replaying experience. | Finite-data assumptions; replay budget; variance estimation; comparability with standard stop-gradient targets. |

## Next steps

1. Select a focus: general representation learning, world-model planning/control,
   or a broad application survey. This shortlist emphasizes general methods.
2. Triage the catalog into method proposals, theory/diagnostics, and applications.
   Treat the first pass as provisional until checked against the main papers.
3. Read a small first batch of main-paper PDFs. For each, record the encoder,
   predictor, target construction, objective, collapse prevention, data, compute,
   evaluation, and what changes relative to its stated baselines.
4. Write `jepa_method_summaries.md` with evidence from the main body and specific
   section/page citations. Keep authors' claims distinct from the evidence shown.
5. Expand the batch and build a comparison table of objectives, target handling,
   regularization, and applications. Avoid ranking methods solely by headline
   scores across different data or compute budgets.

Abstracts often omit the exact loss, gradients, masking, architecture, and training
recipe. Those details remain unknown until the main paper is read. Main-paper
reading excludes supplementary files, reviews, and appendices, as requested.
