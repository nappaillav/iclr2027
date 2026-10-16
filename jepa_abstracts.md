# ICLR 2027 JEPA abstract catalog

337 matching papers in the saved OpenReview search export.

Source: `jepa_papers.json`. This reflects indexed, visible submissions at the time of the fetch; completeness across the venue has not been verified.

The abstracts below are the submitted authors’ text, not independently verified findings or main-paper method summaries. PDFs have not been downloaded.

## 1. $\lambda$-JEPA: Self-Supervised Learning with Spectral Anti-Collapse Regularization

**Keywords:** self-supervised learning, joint-embedding learning, spectral regularization, anti-collapse regularization, JEPA

[Main paper PDF](https://openreview.net/pdf?id=r1H9TwpMFX)

Joint-embedding self-supervised learning typically combines an invariance objective across augmented views with additional mechanisms to prevent representational collapse. These objectives are often applied after a projection head, while downstream tasks use the backbone representation before the projector. We find that this mismatch does not necessarily prevent dimensional collapse in the backbone, which can retain low effective rank and potentially limit downstream transfer. To address this, we introduce SACReg, a spectral anti-collapse regularizer motivated by an analysis of $\lambda$-balance, which captures the relative scale of weight matrices across layers. In a two-layer linear network, we show that (i) $\lambda$-balance prevents collapse, and (ii) our regularizer applied to the backbone induces $\lambda$-balance. In the nonlinear case, this regularizer leads to anti-collapse as well and, in realistic architectures on ImageNet100, it empirically increases the representations' ranks. We apply SACReg to JEPA and propose $\lambda$-JEPA, which improves over LeJEPA and VISReg on ImageNet-1k classification and in average linear-probe transfer performance across eight downstream image datasets. On video self-supervised learning, $\lambda$-JEPA improves over LeVJEPA and V-JEPA~2 on the Something-Something-v2 and Kinetics-400 benchmarks.

## 2. $k$-WM: Predicting $k$ Steps at Once for Long-Horizon Planning with World Models

**Keywords:** World Models, JEPA, Planning

[Main paper PDF](https://openreview.net/pdf?id=ss7n6VFUW4)

Latent world models have become an appealing approach to visual control, enabling goal-conditioned optimization at test time and generalization across tasks with a single model. In practice, however, planning success remains limited to short horizons, and gradient-based planners driven by autoregressive rollouts still underperform sampling-based methods, despite their potential to optimize action sequences efficiently through model gradients. We hypothesize that two properties of next-step prediction contribute to these limitations: autoregressive rollouts compound prediction errors, and planning gradients must traverse a chain of nested model calls. We study a simple alternative: predicting the entire future sequence in a single forward pass. We introduce $k$-WM, a minimal extension to transformer-based JEPA world models: a multi-horizon training objective and input layout that let the predictor map a variable-length action sequence directly to the corresponding sequence of future latent states in a single forward pass. We apply $k$-WM to three classes of JEPA world models and evaluate on four environments. Overall, $k$-WM improves gradient-based planning by 37\% and sampling-based planning by 15\% over the existing next-step world models it extends. Our analysis shows that the gains cannot be explained by parallel rollout alone: improvements persist under autoregressive inference and coincide with substantial changes in the learned representation. Parallel prediction additionally reduces long-horizon inference cost. Together, $k$-WM offers a simple, broadly applicable path to more accurate and efficient long-horizon control. Videos are available at https://anon-k-wm.github.io.

## 3. 4DGS-JEPA: Temporally Compositional Joint-Embedding Prediction for Dynamic Gaussian Splatting

**Keywords:** 4D Gaussian Splatting, JEPA, world models, temporal composition

[Main paper PDF](https://openreview.net/pdf?id=sW3PNIm1ja)

Dynamic Gaussian Splatting explicitly represents evolving 3D scenes, but is typically optimized for reconstruction, rendering, or future-state generation rather than reusable predictive dynamics. We propose 4DGS-JEPA, a Gaussian-native joint-embedding predictive architecture for causal multi-horizon prediction. It combines hierarchical scene, motion-group, and Gaussian-level representations with a horizon-conditioned transition supporting both direct prediction and recursive rollout. Its central principle is temporal composition: different chronological transition paths reaching the same future endpoint should produce compatible predictive states. Endpoint and multi-horizon path supervision anchor predictions to future target embeddings, while a selective geometry decoder and geometry-level composition ground the learned dynamics in coherent group motion and Gaussian geometry without reconstructing complete future appearance. We further introduce hybrid correspondence that preserves reliable persistent canonical identity and applies residual optimal transport when correspondence becomes ambiguous under reordering or topology change. We theoretically characterize zero-loss path agreement and finite-error rollout accumulation. In controlled dynamic Gaussian worlds, temporal composition reduces direct--composed latent discrepancy by about 61\% while slightly improving predictive accuracy, geometry-level composition reduces group-motion path discrepancy by about 72\%, hybrid correspondence remains robust under reordering and topology change, and predicted Gaussian geometry can be rendered into held-out future frames without pixel-level training. These results establish 4DGS-JEPA as a predictive, temporally compositional formulation of dynamic Gaussian worlds.

## 4. 4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling

**Keywords:** 4D World Model, Video Generation, Latent Cache

[Main paper PDF](https://openreview.net/pdf?id=BwY0xgB9vw)

For video generation in dynamic world modeling, observed static and dynamic content should be efficiently reused to provide conditions for repeated generation at different times and viewpoints. We introduce 4LC, a 4D latent cache with composite visual representations and a flexible spatiotemporal access interface. As a latent cache, 4LC directly reuses visual representations of static and dynamic content to provide generation conditions, avoiding per-request RGB rendering and re-encoding. As a composite cache, 4LC binds visual representations from multiple visual encoders (e.g., VAE, DINO, V-JEPA, VGGT) to shared geometry and motion, allowing the composite representations to describe the dynamic world with rich information. Besides, we design a flexible spatiotemporal interface, which directly reads the cache at independently specified times and viewpoints and combines readouts across observations, providing a common conditioning format for diverse downstream tasks. Building on 4LC, we develop 4LC-Video to address multiple video generation tasks through different configurations of source observations, spatiotemporal requests, and historical reuse, including camera control, temporal control, novel-view synthesis, scene revisits, and long-term generation. Our experiments show more efficient condition acquisition, effective spatiotemporal controllability, and scene consistency across tasks using a single 4LC-Video model without task-specific fine-tuning.

## 5. A Controlled Comparison of Self-Supervised Pretraining Objectives and Corpora for Intracortical Neural Decoding

**Keywords:** self-supervised learning; intracortical recordings; neural decoding; brain-computer interfaces

[Main paper PDF](https://openreview.net/pdf?id=n1Zr81aHsx)

Brain-computer interfaces (BCIs) have recently made impressive progress in restoring communication by decoding intended behavior directly from intracortical neural activity. Inspired by the success of foundation models in computer vision and natural language processing, recent work has begun to explore large-scale self-supervised pretraining for neural decoding. However, it is unclear whether these approaches already provide consistent advantages at the scale of data currently available, which is still limited and highly fragmented. In this work we present the first controlled comparison of three self-supervised objective families for intracortical sequence decoding under a unified experimental framework. Using a common transformer backbone, we compare masked autoencoding (MAE), Joint-Embedding Predictive Architectures (JEPA), autoregressive (AR) pretraining, and training from scratch across corpora spanning multiple subjects, behaviors and species: up to 345 hours of intracortical recordings, combining 208 hours from 6 human participants performing attempted and imagined speech, handwriting, typing and cursor control with 137 hours of motor tasks from 19 non-human primates. Our results show that the gains pretraining provides on downstream tasks strongly depend on the amount and diversity of available data, and the resulting performance is often comparable to that of carefully tuned task-specific training. 
These findings establish a controlled benchmark for future research on neural foundation models.

## 6. A Faithful Attribution Reports Its Head, Not Its Model: The Limits of Completeness in Additively Decomposed Representations

**Keywords:** interpretability, attribution, additive models, self-supervised learning, joint-embedding predictive architecture, time series, biosignals, faithfulness

[Main paper PDF](https://openreview.net/pdf?id=Rf8engazGm)

Additive models promise an explanation readable off the architecture: the latent is a sum of per-component terms, so each contribution is available without a post-hoc estimator. That promise is bounded by the downstream head. A completeness-satisfying attribution decomposes a head's output, so what it can say is fixed by the head you chose, not by the model.

On MD-TJEPA, a JEPA whose latent decomposes over channel $\times$ band $\times$ scale, channel identity is $0.998$ decodable from the components and only $0.274$ (chance $0.25$) from the sum they form. Fit the head for the channel and its exact decomposition $\phi_u=\alpha_u\langle w,z_u\rangle$ closes $11%$ of the gap to a pre-aggregation score ($0.319\pm0.057$, $n=10$); on a plain NAM the same construction is not weak but arbitrary, $0$ or $1$ in most seeds. Fit it for the model's own task — a band detector whose labels contain no channel — and an equally exact decomposition names the channel at $0.743\pm0.080$. An input intervention separates the two: resampling the injected channel moves both heads' outputs, moving its content to another channel barely does, so the sum hides which channel contributed, not whether it did. The band head's map agrees with that intervention on $76%$ of windows, the channel head's on $41%$; most of each map's disagreement is its implicit reference, the latent origin. Re-referenced to the training-mean contribution — on this synthetic benchmark an estimate of the expected intervention — they agree on $95%$ and $73%$. Completeness pins the sum, not the head and not the reference.

We are scoped on faithfulness, not accuracy — TS2Vec outperforms MD-TJEPA under a matched probe, though an untrained MD-TJEPA read through its components outperforms TS2Vec — and the axes conflated as "interpretability" disagree on the same checkpoints.

What this buys is a check worth running first: probe the aggregate for the axis, and intervene on the input for it, before trusting any attribution over it — a probe near chance says the aggregate hides which channel was active, not that its content goes unused. $\mathrm{overlap}@k$ between $\|z_u\|$ and $\alpha_u\|z_u\|$ costs one line and exposed a gate collapse here — the JEPA objective shares the gate between prediction and target, so an unopposed sparsity penalty switches components off. In a minimal additive stand-in, removing the gate from the target prevents that shrinkage outright. We close with three checks to run before reading any additive attribution.

## 7. A Generalization Theory for JEPA-Based World Models

**Keywords:** JEPA, spectral graph theory, generalization theory

[Main paper PDF](https://openreview.net/pdf?id=tkpkXM7IFR)

Joint Embedding Predictive Architectures (JEPAs) have emerged as a promising paradigm for world modeling by predicting future representations rather than reconstructing observations. Despite their empirical success, the theoretical understanding of JEPA-based world models remains limited. In this paper, we develop the first generalization theory for JEPA-based world models. We formulate JEPA pretraining as a conditional spectral graph learning problem and show that the JEPA objective is equivalent to a low-rank factorization of an action-conditioned co-occurrence matrix. Building on this characterization, we establish a connection between JEPA pretraining error and downstream planning regret, leading to a finite-sample generalization bound for JEPA-based world models. Our analysis reveals an approximation--sample error trade-off governed by latent dimensionality, providing insights into latent- versus input-level prediction. The theoretical trade-off motivates us to investigate a simple Multi-Depth JEPA extension that combines representations from different network depths. In validation experiments, latent-level prediction exhibits greater robustness under unpredictable observations and difficult planning tasks. Multi-depth representations further improve planning success over single-depth representations and a dimensionality-matched control.

## 8. A Perfect Model Is Not Enough: A case study on long horizon planning in LeWorldModel

**Keywords:** JEPA, representation learning, world models, goal-conditioned rl, planning, temporal distance

[Main paper PDF](https://openreview.net/pdf?id=WdM4R4mdWy)

We study what limits long-horizon planning in JEPA world models through a case study on LeWorldModel (LeWM), a compact world model trained end-to-end offline on pixels whose evaluation protocol has become standard in subsequent work. Several of LeWM’s successors attribute its failures at long horizons to compounding rollout error. We first show that extensions of the standard protocol that simply increase the goal offset cannot test this claim: seemingly minor details of several environments and datasets make them poor tests of long-horizon planning at larger goal offsets. On environments that avoid these pitfalls, we evaluate LeWM on held out episodes across increasing start-goal offsets, varying its rollout source and terminal cost separately. Our results show that (a) planning with a perfect model (by executing each candidate in the simulator) improves long horizon success only modestly, while (b) replacing only the Euclidean terminal cost with a cost-to-go learned on frozen embeddings can achieve similar or greater outcomes without retraining the world model. These insights suggest that evaluation protocol and planner costs inherited by follow up work deserve as much scrutiny as the predictive world model itself.

## 9. Abductive World Modeling via Causal Representation Learning

**Keywords:** World Models, Abductive Inference, Latent Dynamics

[Main paper PDF](https://openreview.net/pdf?id=ksbAwDirSy)

The central challenge of world modeling is to learn representations that capture how the world evolves. However, existing world models predominantly represent future states without explicitly capturing the latent causes underlying their evolution, limiting their ability to reason about why and how the world changes.
To address this limitation, we propose *Abductive World Modeling (AWM)*, a framework that learns structured causal representations by abductively inferring latent causes from predicted futures.
Specifically, we realize AWM through the Hierarchical Abductive State Pyramid (HASP), which organizes the inferred world state into three complementary components—*Entity*, *Dynamic*, and *Relation*—capturing what exists, how it changes, and how entities interact, respectively.
By jointly reasoning over the current observation and its predicted future, HASP abductively infers these latent factors and integrates them into a structured state representation for downstream reasoning.
To the best of our knowledge, AWM is the first framework to introduce abductive state inference into latent-space world modeling for learning structured representations of world dynamics. Experiments across physical prediction, causal reasoning, and action understanding demonstrate the effectiveness of our approach. Compared with V-JEPA 2, a state-of-the-art latent-space world model, AWM improves physical prediction AUROC by 10.7\%, causal reasoning accuracy by 16.8\%, and action Top-1 accuracy by 68.0\%.

## 10. Acting at the Moment of Consequence: Physical Foresight for VLA Action Refinement

**Keywords:** Test-time Optimization, World Models, Physical Reasoning, Robot Manipulation

[Main paper PDF](https://openreview.net/pdf?id=lbj5tPHwJT)

Vision-language-action (VLA) models can produce coherent manipulation behavior yet fail during physical interactions that require precise control. Refining their actions requires identifying when local adjustments can still affect an operation’s outcome. We introduce PREEMPT, a framework for selectively refining the actions of a fixed VLA policy. A V-JEPA-based anticipator foresees physical decision windows and initiates local correction. A latent world model predicts short candidate trajectories, and a completion-time evaluator relates these forecasts to the likelihood and timing of operation completion. These estimates guide smooth corrections constrained by the policy’s intended motion, while predicted trajectory diversity guides further search allocation. We evaluate PREEMPT on LIBERO and RoboCasa with $\pi_{0.5}$, on LIBERO with OpenVLA-OFT, and on four real-robot tasks with an Agilex dual-arm robot. With $\pi_{0.5}$, PREEMPT increases success from 96.7% to 97.1% on LIBERO and from 64.9% to 68.6% on RoboCasa. Real-robot success rises from 72.5% to 82.5%, a gain of 10 percentage points. In a LIBERO-10 scheduling comparison, window-based search uses 58.4% fewer candidate evaluations than searching at every replan.

## 11. ACTOR-JEPA: MULTI-AGENT MOTION FORECASTING USING LATENT-PREDICTIVE PRETRAINING

**Keywords:** self-supervised learning, joint-embedding predictive architecture, motion forecasting, autonomous driving

[Main paper PDF](https://openreview.net/pdf?id=PcxM438rJx)

Motion forecasting models must capture how agents influence one another, and are
trained on large labeled trajectory datasets. Self-supervised pretraining promises
to reduce that dependence on labels, yet reported results conflict, ranging from
substantial gains to null results. We introduce
Actor-JEPA, which applies the Joint-Embedding Predictive Architecture to
multi-agent scene encoding. Its encoder factorizes the scene into a cross-agent
interaction stage followed by per-agent temporal encoding, and that factorization
defines the prediction target: agents are mixed before masking, so the
model predicts masked agent-timestep positions in a representation that already
carries interaction context, rather than reconstructing coordinates. Across four label
regimes and $14$ independent pretraining runs on the Waymo Open Motion Dataset, Actor-JEPA raises
peak mAP from $0.2089 \pm 0.0111$ to $0.2245 \pm 0.0159$ at $20\%$ labels
($+7.4\%$ relative, $p=0.006$, $n=14$) and from $0.2799 \pm 0.0086$ to
$0.2938 \pm 0.0096$ at full labels ($+5.0\%$, $p=0.026$, $n=6$), in each case against the identical
architecture trained from scratch. Within a dataset, two conditions govern
whether any benefit appears: the cross-agent stage must be transferred, since the
per-agent core alone performs at from-scratch level, and pretraining must stop before a representation
collapse that neither the pretext loss nor the variance regularizer reveals, which
we detect by monitoring the effective rank of the encoder's features. Code will be
made publicly available.

## 12. AD-E2E-JEPA: A Joint-Embedding Predictive Architecture For End-to-End Autonomous Driving

**Keywords:** end-to-end autonomous driving, world models, joint-embedding predictive architecture, self-supervised learning

[Main paper PDF](https://openreview.net/pdf?id=f53EbzGFqv)

Autonomous driving requires $\textit{world models}$ that can understand the physical world, reason and plan, and operate safely. In this paper, we first systematically evaluate existing action-conditioned joint-embedding predictive architecture (JEPA) world models, including LeWM, DINO-WM, and JEPA-WM for end-to-end autonomous driving (E2EAD). To isolate world-model quality from policy learning, we employ a goal-conditioned zero-shot planning setting that evaluates these models using ground-truth future observations as goals, without training any driving policy. We find that existing JEPA-based world models are either accurate for driving but computationally expensive, or computationally efficient but insufficient for planning. To address this trade-off, we propose $\textbf{AD-E2E-JEPA}$, which introduces a SIGReg-regularized learnable projector applied to projected patch embeddings. The projector reduces the number of planning patches by $16\times$ and the embedding dimension by $4\times$, achieving a $100\times$ inference speedup while retaining planning performance, with a 0.8-second runtime for an 8-frame rollout over 256 candidate trajectories. \textit{Without} training any driving policy, the world model itself reaches the goals located 20 meters away on average within the displacement of respectively 4.0/3.0 meters, using world-model rollouts over trajectory vocabularies of respectively 256/2,048 candidates. On the NAVSIMv2 benchmark, it achieves 67.3/71.5 EPDMS with multiplicative safety metrics and 84.1/86.0 EPDMS$^{\dagger}$ without them in goal-conditioned zero-shot planning. Experiments further show that the self-supervised pretrained projector improves downstream imitation learning performance from 80.2 to 85.4 EPDMS.

## 13. AdaJEPA: An Adaptive Latent World Model

**Keywords:** World Model, Test-Time Adaptation, JEPA, Latent Planning

[Main paper PDF](https://openreview.net/pdf?id=9QeEKHrDn6)

Latent world models enable planning from high-dimensional observations by predicting future states in a compact latent space. However, these models are typically kept frozen at test time: when their predictions become inaccurate, planning can fail, especially under test-time distribution shift. To address this, we propose AdaJEPA, an adaptive latent world model that performs test-time adaptation within the closed loop of model predictive control (MPC). After training, AdaJEPA plans and executes the first action chunk, uses the observed next-state transition as a self-supervised adaptation signal, and replans with the updated model. This closed-loop update continuously recalibrates the world model without additional expert demonstrations. Across a range of goal-reaching tasks, AdaJEPA substantially improves planning success with as few as one gradient step per MPC replanning step.

## 14. Adapt for Planning, Not Just Prediction: Optimistic Test-Time World Model Adaptation

**Keywords:** test-time adaptation, world models, joint-embedding predictive architecture (JEPA), goal-conditioned planning, optimism in the face of uncertainty, adaptive control

[Main paper PDF](https://openreview.net/pdf?id=hUehdaNbr4)

Latent world models are typically pre-trained offline and kept frozen at test time, so planning with them can degrade under distribution shift. Test-time adaptation (TTA) can mitigate this degradation by updating the model during deployment. Unlike pre-training on fixed data, TTA for planning is closed-loop: the planner uses model rollouts to select actions, and the resulting transitions drive the next update. This raises the question: which objective should guide TTA for planning? Under a prediction-only objective, the model is fit only to the outcomes of its own actions, so it can remain wrong about the actions that would reach the goal, and low prediction error need not translate into better planning. Inspired by reward-biased maximum likelihood from adaptive control, we introduce Optimistic Test-Time Adaptation (OpTTA). Its objective has two terms, the prediction loss on observed transitions and the planner's goal-reaching cost on its candidate rollouts, both minimized over the model parameters. The planning term biases adaptation toward models that are optimistic about reaching the goal, without any additional environment interaction. Across visual and environment shifts on manipulation, reaching and navigation tasks, OpTTA raises final planning success over the frozen model by 13.5 percentage points on average, compared with 6.9 for the prediction-only objective (AdaJEPA), when only the predictor is adapted. When the encoder is adapted as well, the gains are 13.5 and 7.5 points. These experiments span three JEPA world models with different encoders and training objectives and, for temporal straightening, both CEM and gradient-based planners. Our results suggest that test-time adaptation of world models for planning benefits from an optimistic, task-aware term in addition to the prediction loss.

## 15. Adaptation-Ready JEPA: Source Training for Test-Time Adaptive World Models

**Keywords:** World Models; JEPA; Test-Time Adaptation; Meta-Learning; Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=7owSB84uah)

Latent world models often require test-time adaptation under deployment shifts,
while existing methods mainly rely on self-supervised objectives that can be con-
structed directly at deployment. In contrast, supervision that explicitly shapes
control-related representations, such as physical states, is often available only
during source training. Such source-only supervision can improve the initial rep-
resentation, but its constraints do not automatically carry over once the model
is further updated by a different self-supervised objective. We therefore study
a supervision-availability mismatch under a fixed deployment update: how can
training-only supervision improve the model produced by that update? We pro-
pose Adaptation-Ready JEPA (AR-JEPA), which keeps AdaJEPA’s deployment
update unchanged, differentiably simulates it during source training, and opti-
mizes the source model through the resulting adapted model. A meta-learning-
style post-update physical objective alone is insufficient in this setting, because
the adapted object is itself the world model that must continue to support dy-
namics prediction and MPC. AR-JEPA therefore uses Post-Phys to preserve
control-related physical information in the updated representation and Post-Dyn
to preserve future latent-dynamics prediction of the same model, jointly main-
tainingrepresentation content and predictive functionality after adaptation. After
training, physical labels and the auxiliary head are removed, while real deploy-
ment retains AdaJEPA’s original adaptation loss, updatable parameters, and MPC
procedure. On Push-Object, AR-JEPA achieves the highest 13-OOD adapted
success among the compared configurations (40.56%) and shows smaller future-
dynamics and physical-representation degradation under an identical AdaJEPA
update. PointMaze further shows that the relative roles of pre- and post-adaptation
physical supervision depend on the environment

## 16. Adaptive Latent Capacity for World Models

**Keywords:** LeWorldModel, JEPA, Nested dropout, Adaptive latent embedding size

[Main paper PDF](https://openreview.net/pdf?id=gwKbYJF6ui)

We introduce Adaptive LeWorldModel (ALeWM), a world model based on a joint-embedding predictive architecture (JEPA) that learns to concentrate predictive information in compact prefixes of a wide latent representation. To encourage this ordering, ALeWM learns a sequence-conditioned distribution over prefix lengths and trains the predictor to estimate the full next embedding from a sampled input prefix. As standard anti-collapse objectives encourage variation across latent coordinates but do not organize them by predictive importance, we also introduce MixSIGReg. MixSIGReg regularizes the masked embeddings against a prior-weighted mixture with Gaussian active prefixes and zeros in the remaining coordinates. As a result, the ALeWM objective encourages early coordinates to retain information useful for prediction and recursive planning. Our analysis shows that the mixture distribution used by MixSIGReg assigns higher variance to earlier coordinate blocks and lower variance to later ones. In addition, we show that, under specified assumptions, prediction error is minimized by placing the information most useful for prediction in earlier blocks. Empirically, we study the behavior of ALeWM in a controlled dynamical system with known state variables and in goal-conditioned visual control. We show that ALeWM consistently achieves higher mean success rates than tuned fixed-width LeWM, with lower planning capacity on average.

## 17. AGR-JEPA: Action-Grounded Residual Joint-Embedding Predictive Architecture for Planning

**Keywords:** JEPA, latent world model, Control Grounding

[Main paper PDF](https://openreview.net/pdf?id=gvMH4B7N1x)

In this research, we propose Action-Grounded Residual Joint-Embedding Predictive Architecture (AGR-JEPA), a reconstruction-free latent world model for planning. Our work is based on a key observation: existing approaches typically trained to minimize next-embedding prediction error, whereas effective planning additionally requires the consequences of different actions to remain distinguishable in latent space. Through controlled experiments, we find that lower prediction error does not consistently correspond to higher planning success, indicating that latent predictability alone is not a reliable proxy for planning utility. We refer to this mismatch as the prediction--planning gap. To address this gap, AGR-JEPA adopts a residual parameterization that represents the future latent state as the combination of the current latent state and an action-conditioned latent update, focusing dynamics learning on action-induced state changes. Furthermore, AGR-JEPA introduces a control-grounding objective that uses action recoverability as a training signal, encouraging latent updates to retain information relevant to their conditioning actions and thereby improving the behavioral discriminability of action outcomes. This auxiliary objective is used only during training and incurs no additional computation at planning time. Across multiple 2D and 3D control tasks, AGR-JEPA achieves an average planning success rate of 92.06\%, delivering consistent improvements over leading baselines across multiple tasks.

## 18. AhJEPA: A single branch framework that captures granular details for JEPA methods

**Keywords:** Representation Learning, World Model, Contextual Learning

[Main paper PDF](https://openreview.net/pdf?id=lcJyOrWTB1)

Regularization-based self-supervised learning methods enable stable training
without additional heuristic designs. However, such methods do not encourage
learning of fine-grained relationships, which limits their applicability on downstream tasks. We mathematically characterize contextual prediction from incomplete observations and derive its implementation through a shared backbone, without a separately parameterized teacher or EMA updates. Our analysis interprets
stop-gradient (SG) as a restriction on target-side adaptation, and an exploratory
complementary-subset objective illustrates a possible implementation without SG.
Inspired by previous masked-image-modeling (MIM) methods, we propose AhJEPA, a simple yet effective architecture that is broadly Applicable to heuristic-free JEPA losses to encourage learning of fine-grained relationships of the input
data while maintaining the training simplicity and stability. Similar to previous
works, we add a reconstruction loss to force the model to learn the fine-grained
details. Different from them, AhJEPA maintains a one-branch training paradigm
and applies the reconstruction loss to CLS tokens rather than patch tokens. We
retain SG in the final method for its stronger empirical performance. We find that
this contextual learning approach is a more general way to improve JEPA methods
with different special designs (e.g., sparsity creation). This simple method consistently improves the performance of heuristic-free JEPA regularization methods
across in-domain and out-of-domain classification, segmentation, depth estimation, and latent world model planning. Specifically, it helps the VISReg method
achieve the best OOD accuracy and reduce the gap between heuristic-free methods
and iBOT on fine-grained tasks. Also, it boosts the LeWorldModel performance
to SOTA on OGBench-Cube and Two-Room datasets.

## 19. Anisotropic Representations Improve Planning in JEPA World Models

**Keywords:** JEPA, World Model, Robotics

[Main paper PDF](https://openreview.net/pdf?id=SDTfkFAJrF)

Latent world models learn action-conditioned dynamics in representation space and often score candidate actions by Euclidean distance to a goal representation.
Joint training typically regularizes the representation to prevent collapse, but the resulting representation geometry also determines how terminal errors are weighted during planning.
We show that accurate prediction and noncollapsed representations do not guarantee a task-aligned latent planning cost: isotropic Gaussian regularization can induce a geometry that ranks feasible outcomes differently from the task cost.
To address this mismatch, we introduce AnisoWM with $\Lambda$Reg, which replaces the fixed isotropic Gaussian target with a learnable diagonal covariance under fixed-trace and anisotropy constraints.
The prediction objective, predictor architecture, and Euclidean planner remain unchanged; the target is used only during training.
Our analysis characterizes the prediction-driven allocation of target variance, its dependence on the training distribution, and the conditions under which the induced metric reduces planning regret.
Across four visual control environments, AnisoWM improves planning success over LeWorldModel in all four.
Its latent planning cost also shows better agreement with task outcomes.

## 20. Any-to-Any Video Modeling: Modeling the World by Traversing Time and Modalities

**Keywords:** video modeling, multimodal learning, multi-task learning

[Main paper PDF](https://openreview.net/pdf?id=rwI0uJi435)

Video modeling captures how the world is structured in space and how it evolves over time. Most approaches model this structure in a single representation space: RGB or a semantic representation (e.g., DINOv2, V-JEPA). However, different spaces capture different aspects of the underlying world and serve complementary roles, e.g., DINOv2 and V-JEPA excel at high-level semantic understanding, while RGB preserves fine-grained detail. In this work, we move beyond modeling the world in a single representation space and study video modeling jointly across time and modalities, each serving as a representation space (e.g., RGB, depth, optical flow, feature maps, and bounding boxes etc.). We develop an any-to-any multimodal video model that can predict any modality at any point in time, given any combination of input modalities at any time steps. Flexibly traversing this time-modality grid gives rise to higher-level inference capabilities that are not supported by specialist video models. First, in chained generation, we decompose a task (e.g., caption-to-video) into a chain of potentially simpler sub-tasks of predicting intermediate modalities, and find that this yields higher-quality generations than direct generation. Second, we study future prediction in different modality spaces and find that no single space is optimal: the best prediction space varies across samples, and selecting it per sample yields substantially more accurate forecasts than committing to any single space. Finally, we show that the flexible modality-time conditioning enables counterfactual generation, where conditioning modalities act as actions that steer generation, from coarse (e.g., captions) to fine-grained (e.g., depth or bounding boxes) control.

## 21. Atom-JEPA: Joint-Embedding Predictive Architecture for 3D Atomistic Systems

**Keywords:** Foundation Models, Self-supervised learning, Atomic Systems, Molecular Modelling, AI4Science, ADMET, ADME

[Main paper PDF](https://openreview.net/pdf?id=iecHBfO8uc)

Large-scale self-supervised pretraining has reshaped modern machine learning, substantially advancing the ability of language and vision models to generalize across downstream tasks.
While deep learning has driven considerable progress in modeling atomistic systems in recent years, self-supervised pretraining in this domain has not yet achieved comparable downstream generalization.
To address this, we introduce Atom-JEPA, a self-supervised pretraining framework that learns latent representations from unlabeled 3D structures through complementary atom-level and substructure-level objectives inspired by joint-embedding predictive architectures.
We pretrain Atom-JEPA on large-scale molecular and crystalline datasets and evaluate its transfer performance by fine-tuning on a diverse set of downstream property prediction tasks.
Atom-JEPA achieves state-of-the-art performance on molecular ADMET and quantum-chemical property prediction tasks, and is highly competitive in predicting the physical properties of crystalline materials.
These results demonstrate the potential of latent-space predictive pretraining to support broad downstream generalization from structural data alone.

## 22. Attacking Action Discriminability in Latent World Models

**Keywords:** adversarial attack, latent predictive world models, action-conditioned dynamics, model-based planning

[Main paper PDF](https://openreview.net/pdf?id=RsRxs7m9PC)

Latent world models support model-based control by learning action-conditioned state transitions in representation space. A key requirement of such models is that their predicted dynamics faithfully reflect the consequences of different actions, allowing downstream planners to distinguish alternative future trajectories. Many existing attacks are tied to specific action sequences or trajectories, whereas multiple alternative action sequences may reach the same goal, making persistence across plan variations and repeated replanning challenging. We instead target the action dependence of the latent dynamics itself, aiming to produce perturbations that are less tied to particular action sequences and remain persistent across multi-step rollout and replanning. Specifically, our attack operates at two complementary levels: action sensitivity suppression and multi-step discrepancy propagation. For the former, we construct action ensembles and directly reduce the dispersion of their predicted latent states, weakening the model's sensitivity to action variations. To further suppress the propagation of action-induced discrepancies over future rollout steps, we derive a finite-horizon sensitivity bound and reduce the dominant sensitivity of the latent transition dynamics. Additionally, we steer the attacked predictions away from their clean counterparts to induce erroneous rather than merely insensitive predictions. The proposed attack is evaluated on multiple JEPA-style latent world models across two control environments, demonstrating that suppressing action sensitivity in latent dynamics can effectively disrupt future-state prediction and downstream planning.

## 23. Auto-JEPA: A Latent World Model of Continuous Intent for End-to-End Autonomous Driving

**Keywords:** Autonomous Driving, World Models, Joint-Embedding Predictive Architecture, Latent Intent Prediction, Trajectory Planning

[Main paper PDF](https://openreview.net/pdf?id=PRpfQ1aXrk)

Existing autonomous-driving world models typically perform dense prediction of future videos, occupancy states, BEV representations, or agent motion. We argue that planning need not reconstruct the complete future world, but only focus on scene features that affect future ego action. Based on this perspective, we propose Auto-JEPA, an action-oriented latent world model that learns continuous future driving intent through joint-embedding prediction. Given visual observations, ego-motion history, and navigation commands, Auto-JEPA predicts an intent embedding aligned with the latent representation of the future ego trajectory. The predicted intent retrieves executable trajectories from a fixed trajectory memory, which are then ranked by a scene-conditioned candidate selection module. Auto-JEPA keeps the visual encoder frozen, requires no explicit perception annotations, and uses no learned trajectory generator. By optimizing only task-specific modules for trajectory representation, intent prediction, and candidate selection, Auto-JEPA achieves 91.3 PDMS on NAVSIM v1 and 89.1 EPDMS on NAVSIM v2. Semantic occlusion experiments show that masking dynamic-agent regions induces an average intent change 2.97× that of equal-area random masking. Moreover, occluding vehicles that affect future driving substantially changes the predicted intent and selected trajectory, whereas both remain essentially unchanged when non-influential vehicles are occluded. These results show that future-intent prediction encourages the model to focus on planning-relevant visual features and supports high-quality planning without dense future-world modeling.

## 24. AVL-JEPA: PREVENTING CAUSAL DYNAMICS INFORMATION COLLAPSE IN JOINT EMBEDDING PREDICTIVE ARCHITECTURE WORLD MODELS

**Keywords:** Joint Embedding Predictive Architecture, Latent World Models, Self-Supervised Representation Learning, Latent Dynamics, Visual Invariance

[Main paper PDF](https://openreview.net/pdf?id=d3w1DyhnGC)

Joint embedding predictive architectures (JEPAs) predict future latent representations without reconstructing observations, enabling world models to focus on high-level semantic dynamics. However, a JEPA can preserve high-dimensional visual information while discarding information about the physical consequences of actions. We call this failure mode causal dynamics information collapse and propose action-grounded vision-invariance latent (AVL) to prevent this collapse. We first use the executed action as an auxiliary dynamics anchor that encourages the model to preserve dynamics information, and then use a vision-invariance pathway which aligns perturbed and clean latent predictions without discarding dynamics information, forcing the model to fully understand and utilize causal dynamics information. We validate AVL on four robotic control tasks (TwoRoom, PushT, OGBench Cube, and Reacher), showing that it substantially improves success rates under visual perturbations while preserving clean-environment performance. We further evaluate physical-consequence alignment, clean--noisy dynamics consistency, and the causal effect of targeted transition subspace erasure. Collectively, these results indicate that dynamic information causally relevant to planning is preserved from collapse under AVL.

## 25. Balancing Invariance and Information Preservation in Single-Cell JEPA

**Keywords:** Single Cell Transcriptomics, Joint Embedding Predictive Architectures, Self-Supervised Learning

[Main paper PDF](https://openreview.net/pdf?id=iDT8UhdSkV)

Self-supervised learning for single-cell genomics must balance invariance to nuisance variation against preservation of biological information. Existing single-cell Joint-Embedding Predictive Architecture (JEPA) adaptations change backbones,
anti-collapse mechanisms, and auxiliary objectives at the same time, so it is unclear which choice actually drives transfer. We therefore fix the encoder, view construction, training budget, and evaluation protocol, and vary only two axes: the anti-collapse regularizer and the observation-space preservation target. Within this setting we introduce PCG-BCE, a per-cell-balanced and gene-entropy-weighted
binary cross-entropy loss that supervises gene detection rather than expressionmagnitude, and DET-JEPA (detection-aware JEPA), which couples PCG-BCE with projector-space latent prediction. Three findings emerge. First, preventing collapse is not sufficient: variants trained with latent prediction alone, including one built on a provably collapse-free regularizer, fall below both a plain masked
autoencoder and PCA on zero-shot cell-type annotation and on scIB biological conservation. Second, which observation-space target is preserved matters more than whether one is used: detection prediction outperforms magnitude reconstruction on every out-of-distribution cohort, consistent with a sampling analysis showing that detection labels are insensitive to positive-count magnitude. Third, PCG-
BCE alone is already a strong representation learner; adding latent prediction improves 11 of 12 downstream metrics, but each gain is small and not individually significant over five seeds. Across zero-shot cell-type annotation, multi-batch integration, and protein-abundance prediction, DET-JEPA is the best matched JEPA variant, with VISReg as the preferred regularizer. Our study localizes where the
gains in single-cell JEPAs come from and gives concrete guidance for designing preservation objectives.

## 26. Before the Next Outcome: History-Aware Test-Time Adaptation for Latent World Models

**Keywords:** Test-Time Adaptation, World Models, JEPA

[Main paper PDF](https://openreview.net/pdf?id=LYjxQbgWuH)

Test-time adaptation of latent world models typically relies on real transitions
observed after the agent acts, leaving the model unadapted at the beginning of
deployment. We study pre-outcome test-time adaptation: adapting a pretrained
world model using only the target-domain history that is already available, be-
fore the next real state is observed. This setting is challenging because historical
variation mixes appearance nuisance with genuine dynamics changes, while repre-
sentation and dynamics adaptation are coupled through a shared latent space. We
propose HATTA (History-Aware Test-Time Adaptation), which exploits the two
forms of evidence already present in the observed history. HATTA uses historical
transition compatibility to select counterfactual visual hypotheses and construct
a dynamics-aware representation correction, while observed local motion is used
to calibrate the action-conditioned dynamics predictor. A latent-space coordina-
tion step controls the accepted representation update and re-encodes the original
history before dynamics adaptation. HATTA requires no new future outcome,
source-domain data, reward, goal, or shift label. Experiments on PushT visual
shifts and PointMaze dynamics shifts show that short histories provide useful pre-
outcome signals for both visual and dynamics adaptation. The unified method
retains most of the gains of the two specialized branches and achieves overall
point estimates close to a feedback-based AdaJEPA reference without using new
real transition feedback. These results suggest that target-domain history can sup-
port meaningful world-model adaptation before additional interaction feedback
becomes available.

## 27. BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL

**Keywords:** Humanoid Whole-Body Control, World Models, robotics, Unsupervised Reinforcement Learning

[Main paper PDF](https://openreview.net/pdf?id=0Krw9xEhhn)

Humanoid control requires coordinating whole-body posture with position and heading in the world frame.
Mainstream controllers imitate trajectories in the root frame, but struggle to regain the target world pose after displacement.
We introduce BeJEPA, a goal-conditioned Behavior World Model learned through unsupervised
reinforcement learning from human motion priors and robot interaction.
BeJEPA learns a shared representation of body configuration and world placement
through a joint-embedding predictive architecture (JEPA).
A Dynamic Predictor predicts the next state embedding under an action, while a Successor Predictor
summarizes a goal-conditioned policy's expected discounted future state embeddings in a single vector.
During joint training, Dynamic grounds the initial representation in observed physical transitions,
while Successor increasingly organizes it around long-term behavior.
Their composition guides policy improvement through one physical prediction and one behavioral summary,
without long imagined rollouts.
In 20-second motion-tracking experiments, BeJEPA with online action refinement using Dynamic outperforms
all evaluated baselines in global body-position error, reducing it on AMASS
by 61.7% relative to BFM-Zero with world-pose inputs and 58.7% relative to SONIC.
Physical deployment on a Unitree G1 demonstrates joint attainment of posture, world position,
and heading goals, recovery from the ground, and closed-loop return after disturbances and goal changes.

## 28. BeliefGraph-JEPA: Structured Latent World Models for Action-Conditioned Time Series

**Keywords:** action-conditioned forecasting, time-series forecasting, latent world models, structured latent dynamics, graph-based forecasting, joint-embedding predictive architectures

[Main paper PDF](https://openreview.net/pdf?id=Ni8Xe7OvQf)

Action-conditioned time-series forecasting requires accounting for how
future actions and exogenous forcings influence multiple targets through
partially observed effects with different delays and persistence.
Direct conditioning leaves the evolution and target-specific influence
of these effects implicit in the predictor, while static relational
graphs specify connections without tracking evolving effects.
This motivates representing future-driver influence through structured
latent states that evolve over the forecast horizon and route
information to individual targets.
We introduce BeliefGraph-JEPA, a structured latent world model that factorizes
driver influence into typed latent-effect states.
These states are rolled forward under future drivers and routed through
a graph to target-specific nodes, forming the predictive base of a
joint-embedding predictive architecture.
A capacity-controlled residual supplements this base with direct
driver information.
On four multi-target clinical, agricultural, environmental, and
industrial systems, the framework outperforms a range of pretrained
and supervised known-future-covariate baselines.
Matched controls isolate latent dynamics, future rollout, graph routing,
and residual capacity; future rollout and graph-first residual routing
improve forecasting across all four systems.

## 29. Beyond a Single Latent Space: A Dual-Latent World Model for Long-Horizon Planning

**Keywords:** World Model, Latent Planning, JEPA, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=owCbHb5DNy)

Latent world models often struggle with long-horizon planning, even when their short-term predictions are accurate. Prediction errors accumulate during recursive rollout, while distance concentration in high-dimensional latent spaces can weaken the distinction between states at different distances from a goal. We introduce the Dual-Latent World Model (Dual-WM), which separates local execution from long-range planning through two distinct state representations and dynamics models. The low-level model captures fine-grained action-conditioned transitions, while the high-level model uses learned macro-actions to plan over longer temporal spans. We further propose Long-Horizon Representation Learning with Weighted Rollout (LoRe), which supervises self-generated predictions at both levels. Motivated by an analysis of recursive error propagation, LoRe uses exponential horizon weights with separate decay rates to balance multi-step supervision at each temporal scale. During planning, the high-level model generates latent subgoals, and the low-level model refines them into actions for precise execution. We evaluate from-scratch Dual-WM on five goal-conditioned visual control tasks against the task-wise strongest baselines without actor-guided proposals. At goal offsets of 50 and 100 environment steps, mean success increases from 75.9\% to 84.4\% and from 61.4\% to 69.5\%, respectively. At offset 100, Dual-WM outperforms these baselines on all five tasks and improves mean success over LeWM by 30.8 percentage points. Ablations and supporting analyses provide evidence that the proposed design learns more informative state representations for goal evaluation and improves consistency under recursive prediction. These results highlight the value of separating temporal roles and training across multiple horizons for reliable latent planning.
Our core implementation is available in an anonymous repository at \url{https://anonymous.4open.science/r/Dual-WM-2411/}.

## 30. Beyond Action Prediction: Learning Search-Free Planning in Latent Space

**Keywords:** Latent World Models, Goal-Conditioned Visual Control, Inverse Dynamics, Search-Free Planning

[Main paper PDF](https://openreview.net/pdf?id=VpgGkAfZHQ)

Latent world models learn action-conditioned state transitions in a compact representation space, providing a predictive model for visual planning and control. However, planning with these models typically requires costly test-time optimization over action sequences. We propose to replace this online search with a goal-conditioned inverse model that directly predicts actions from current and goal observations. A key challenge is that action prediction alone neither ensures that goal representations encode action-relevant information nor that predicted actions are consistent with the learned latent prediction model. We introduce Hindsight Inverse JEPA Planning (HIJP), a search-free framework that addresses both aspects during training. HIJP relabels future observations along offline trajectories as goals, providing action supervision across multiple temporal horizons. By retaining gradients through the goal representations, this supervision directly shapes the visual representation. HIJP further feeds predicted actions into the latent predictor model and aligns the resulting next-state representations with encoded successor observations, enforcing action-transition consistency. At inference time, the inverse dynamics model and latent predictor models are applied alternately to generate multi-step action sequences without online search. Across four visual control tasks, HIJP achieves 86.8\% overall success and a 1.9–16.5× planning speedup over search-based planning.

## 31. Beyond Frame-Wise Encoding: When Do Video-Native Representations Help Gait Recognition?

**Keywords:** gait recognition, video representation learning

[Main paper PDF](https://openreview.net/pdf?id=RpdKHNrEWZ)

Large vision models (LVMs) have advanced gait recognition, but most pipelines retain the GaitSet-style design: an image LVM encodes each frame independently before a gait head aggregates the sequence. Video LVMs instead encode clips jointly, producing \emph{video-native representations} shaped by cross-frame context. We study when these representations help and what they change before the gait head. Across several benchmarks, frozen video LVMs remain competitive on within-domain evaluations and transfer better to unseen domains. To isolate the effect of clip-wise encoding, we evaluate the same V-JEPA~2.1 checkpoint frame-wise and clip-wise, using the same training samples and gait-head architecture. Clip-wise encoding has little effect on within-domain accuracy but improves cross-domain recognition, with the largest gains under nighttime capture and clothing changes. Under controlled occlusion, its advantage depends on temporal coherence rather than on whether hidden regions reappear: the advantage grows when a body region remains hidden throughout the sequence but reverses when visibility shifts randomly across frames, in which case frame-wise representations perform better. At the frozen-encoder level, clip-wise context stabilizes representations of still-visible regions and makes unchanged observations more identity-discriminative, thereby changing what the gait head pools rather than merely how it pools. Gait research has long focused on refining how features are pooled; video-native representations offer a way to improve the features themselves. Our results identify where this benefit emerges and where clip-wise context becomes a liability, positioning video-native representations as a promising foundation for robust gait recognition.

## 32. BEYOND GAUSSIAN WORLDS: LATENT GEOMETRY MATTERS FOR JEPAS

**Keywords:** JEPA, GEOMETRY

[Main paper PDF](https://openreview.net/pdf?id=OmQHSMNyY5)

Recent Joint-Embedding Predictive Architectures (JEPAs) prevent representation collapse by constraining learned representations to follow a prescribed target distribution, such as an isotropic Gaussian or the uniform distribution on a hypersphere. 
Klindt et al. (2026) showed that, under their Euclidean assumptions, matching a Gaussian target can recover Gaussian latent variables up to a linear transformation, and that the Gaussian is the unique distribution with this guarantee.
We extend their analysis to latent variables supported on embedded Riemannian manifolds and derive conditions on the latent geometry and positive-pair dynamics under which alignment and exact distribution matching guarantee linear recovery.
In particular, when the latent variables are uniformly distributed on a sphere and the representations are matched to the same spherical distribution, every optimal representation recovers the latent state up to an orthogonal transformation.
This shows that Gaussian uniqueness is not a universal property of distribution-matched JEPAs: non-Euclidean latent geometries can admit other linearly recoverable distributions.
We further derive an approximate-recovery bound that is strictly tighter for the spherical world than for the Gaussian world.
Experiments on Gaussian, spherical, and toroidal latent spaces show that geometrically compatible targets yield better linear recovery when optimization succeeds, whereas mismatched targets distort the latent structure.
This advantage persists in high-dimensional Clifford-torus worlds.

## 33. Beyond Spread: Distinct Organizational Pathways in Predictive JEPA

**Keywords:** Joint-Embedding Predictive Architecture, Self-Supervised Learning, Representation Learning, Representation Geometry, Regularization, Learning Dynamics

[Main paper PDF](https://openreview.net/pdf?id=LtrgTUjYVy)

Existing analyses of geometric regularization in predictive JEPA often emphasize endpoint properties such as feature spread, isotropy, or collapse avoidance. We argue that these endpoint summaries are too coarse to explain how different regularizers shape predictive representations during training. Motivated by observations from a shell-based neighborhood regularization strategy, we compare shell-based neighborhood regularization (shell_context_knn), whitening decorrelation, VICReg-style regularization (vicreg_like), and a repaired SIGReg-like Gaussian matching configuration (sigreg_like) in a controlled PatchJEPA setting. We observe consistent differences in linear probe accuracy, effective rank, and trajectory dynamics across methods. In particular, shell and whitening reach similar endpoint probe performance through visibly different training trajectories, while SIGReg exhibits stronger context-prediction coupling but weaker structural expansion and lower final probe. We further show that these pathway differences remain visible in a joint rank-coupling state space, persist under low-cost hyperparameter perturbations, and respond sharply to mid-training intervention. When the regularizer is switched at step 100, context-prediction coupling rapidly follows the new regularizer style, whereas final probe remains only partially plastic. These patterns motivate an organizational view of regularization in which fast coupling variables and slower predictive-structural variables separate in time. In our controlled setting, these pathways provide a diagnostic observational framework that complements spread-based summaries for understanding downstream behavior.

## 34. Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning

**Keywords:** Latent world model, long-horizon planning

[Main paper PDF](https://openreview.net/pdf?id=qqwATQYvvA)

Recently, world models have emerged as a promising paradigm for building intelligent agents by learning predictive models that estimate future environment states conditioned on observations and actions. In particular, JEPA-style latent world models provide an efficient alternative to pixel space prediction by learning action-conditioned dynamics in compact representation spaces. However, existing latent world models typically rely on one-step prediction and must be recursively rolled out for long-horizon planning, which leads to compounding errors and a mismatch between training objectives and downstream planning tasks. To address this limitation, we propose Variable-length Latent World Models (VLWMs), a framework that learns to predict future latent states conditioned on action sequences of variable lengths. Instead of training only on one-step transitions, VLWMs directly model temporally extended dynamics, allowing the same predictor to evaluate action plans over different horizons. We further introduce a curriculum training strategy that progressively expands the action horizon, stabilizing optimization from short-range dynamics to long-range prediction. At test time, we design planning methods tailored to VLWMs to better exploit their variable-length predictive capabilities. Experiments on long-horizon control tasks show that VLWMs significantly improve latent space world models, achieving 13\% average improvement over the state-of-the-art LeWM across different datasets, with especially large gains on tasks requiring extended planning. These results suggest that VLWM provides a simple yet effective paradigm for improving long-horizon prediction and planning in latent world models.

## 35. Bilinear World Models: Learning Representations with Structured Dynamics for Efficient Control.

**Keywords:** World models, JEPA, representation learning, latent dynamics, model-based control, bilinear systems, vision transformers

[Main paper PDF](https://openreview.net/pdf?id=EKdVFcc2Vm)

World models jointly learn latent representations and dynamics that predict how high-dimensional observations evolve under actions.
In this work, we propose a JEPA-style world model in which, rather than learning arbitrary latent dynamics, we restrict them to follow a bilinear parameterization. This structure enables efficient planning and control while shifting the modeling burden onto the encoder, encouraging richer representations that expose the controllable geometry of the system. In particular, this structured parameterization allows us to structurally enforce action recoverability, thereby preventing representation collapse by construction.
Although prescribing a bilinear parametrization may appear restrictive, we show that a broad class of nonlinear dynamical systems admits a transformation under which the dynamics become bilinear.
Empirically, we show across standard 2D and 3D control tasks that representations with bilinear-parameterized dynamics can be learned directly from high-dimensional observations, reducing planning time by nearly three orders of magnitude while retaining or even improving control accuracy.
We also propose more demanding regimes of longer-horizon planning and real-time control, and demonstrate that our method succeeds in both, moving JEPA-style world models beyond short-horizon offline planning.

## 36. Brain-Inspired Prior Regulation for Efficient Planning with World Models

**Keywords:** World Models; Brain-Inspired Planning; Action-Prior Regularization

[Main paper PDF](https://openreview.net/pdf?id=GJAUZTeETT)

Advances in world models enable predictive reasoning about action consequences, supporting goal-directed decision-making in robotic manipulation and visual navigation. However, action search remains computationally expensive, and existing prior-guided methods improve sampling efficiency through initialization but lack persistent regulation of subsequent optimization, leaving search vulnerable to deviations from the learned action prior. To address this limitation, we propose Brain-Inspired Prior Regulation (BIPR), a framework for efficient planning with world models through coordinated prior regulation across multiple timescales. Specifically, prior anchoring penalizes deviations from the action prior throughout search, uncertainty–conflict arbitration adapts regularization to current search evidence, and metaplastic calibration uses offline learning history to modulate this adaptive response. Experiments on established benchmarks for world-model-based control show that BIPR improves macro-average success rates with LeWorldModel and Sub-JEPA by 30.33 and 26.33 percentage points, respectively, over the MPPI baseline, while complementary efficiency evaluations demonstrate a 46.73% reduction in evaluation wall time relative to CEM under a matched candidate budget. Beyond task success, computational cost analysis shows that BIPR requires no additional trainable parameters compared with prior-guided planning, while incurring only 0.82% additional evaluation overhead. These findings suggest that brain-inspired prior regulation offers a promising approach to improving the performance–efficiency trade-off of world-model-based planning.

## 37. Brain-VisA: Brain-Vision Alignment via Self-Supervised Brain Representation

**Keywords:** Self-supervised learning, Brain–vision alignment, Semantic generalization, Relational alignment, Variance-Invariance-Sketching Regularization

[Main paper PDF](https://openreview.net/pdf?id=2HHSowOcIJ)

Human brain activity contains rich perceptual and semantic information that could complement pretrained models, yet exploiting this information is challenging. We investigate whether brain–vision alignment can improve the representations and generalization of pretrained vision models using paired image–fMRI data alone, without any behavioral supervision or category information. 
To enable vision models to benefit from brain–vision alignment, we leverage self-supervised learning to enhance the conceptual and semantic structure of brain representations. Specifically, we propose a two-stage **Brain-Vis**ion **A**lignment (**Brain-VisA**) framework. 
First, a joint-embedding predictive architecture (JEPA) learns structured brain representations through self-supervision, using repeated fMRI responses to the same image as natural positive views. 
Second, relational alignment jointly adapts brain and visual representations while retaining brain self-supervision. 
We find that the learned brain representations exhibit semantic concept structure across eight pretrained vision models from SimCLR, CLIP, and DINOv2, despite the absence of semantic supervision. 
Specifically, Brain-VisA improves one-shot classification accuracy for high-level semantic concepts by an average of 13.70\% over the unadapted models.
It further exceeds the category-informed brain–vision alignment baseline by an average of 10.14\% on high-level abstract semantic classification, while requiring less training data and time. 
The aligned models also improve on generalization tasks including out-of-distribution recognition and the odd-one-out task. 
These results suggest that self-supervised learning can extract useful representational structure from limited, noisy brain signals, and that brain–vision alignment can improve the semantic representation structure and generalization of pretrained vision models without relying on any behavioral or category information.

## 38. Branch-JEPA: Learning Dynamics-Aware State Representations through Dual-Branch Patch Routing

**Keywords:** World models, joint-embedding predictive architectures, semantic collapse, dynamics-aware representation learning, patch routing, mutual information, visual robustness

[Main paper PDF](https://openreview.net/pdf?id=92vqQk83fk)

Predicting future embeddings offers a compact route to learning visual world models, but a well-dispersed latent space need not expose the state changes that distinguish actions. We present Branch-JEPA, a representation-level extension of an end-to-end joint-embedding world model. Two independent spatial routers aggregate shared Patch features into State and Act residuals, which augment rather than replace a global CLS pathway. A contrastive action-alignment objective supervises changes in the fused Act coordinates, while one shared Predictor models the complete representation. The design preserves latent prediction, global anticollapse regularization and goal-conditioned planning without a pretrained visual backbone or a denoising frontend. Across PushT, TwoRoom, Reacher and Cube, task-averaged planning success increases from 83.25% to 88.25% on clean observations and from 35.50% to 59.75% under Gaussian corruption. Direct actionregression controls show that action supervision and Patch access account for much of the gain. Paired intervals resolve smaller improvements from separate routing and Act-only alignment under Gaussian noise; their clean intervals include zero. Frozen readouts, interventions and success-aligned candidate ranking connect these behavioral results to relative specialization within the shared representation.

## 39. Breaking the Rotation Barrier in JEPA World Models with Anisotropic Predictors

**Keywords:** JEPA, World Models, Identification, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=S7H9h3eNjo)

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space, but their predictor can absorb any rotation of that space without changing the loss, leaving physical factors mixed across coordinates and hard to monitor or control individually. Recovering one factor per coordinate requires the right subspace, which contains the factors, and the right basis, which gives each factor its own coordinate. We break this rotation barrier with a minimal change, replacing the dense predictor by an anisotropic predictor (**AP-JEPA**), and prove that its loss splits exactly into two terms: a rotation-invariant ***dense-predictor term***, which selects the subspace, and a ***cross-talk term***, which selects the basis and aligns coordinates with factors that evolve on distinct timescales. However, the encoder can produce features that are more predictable than genuine factors, such as the square of a slow factor, so the selected subspace may miss some factors. We characterize when two existing regularizers, whitening and SIGReg, rule out such features, and propose a new regularizer, PairSIGReg, which constrains consecutive representations jointly and recovers the factor subspace for every spectrum of distinct timescales. Across six dynamical and image benchmarks, AP-JEPA with PairSIGReg raises the average mean correlation coefficient (MCC) from $63.6\%$ for the strongest baseline to $77.8\%$, while also achieving the highest average linear readout ($90.2\%$). Beyond training from scratch, AP-JEPA also applies to existing JEPAs trained with dense predictors: since the cross-talk term depends only on the basis, minimizing it alone yields a closed-form change of coordinates that raises the single-coordinate $R^2$ of released I-JEPA and V-JEPA models from about $10\%$ to $81\%$ without information loss.

## 40. Breaking the Staleness Phase: Understanding and Accelerating JEPA Training

**Keywords:** Joint-Embedding Predictive Architecture (JEPA), Exponential Moving Average (EMA)

[Main paper PDF](https://openreview.net/pdf?id=xqzeKvOWTJ)

The exponential moving average (EMA) mechanism, introduced to stabilize self-supervised learning, coincides with a surprising failure mode in Joint-Embedding Predictive Architectures (JEPAs): during early training, the reconstruction loss plummets while learned representations remain useless for downstream tasks. We call this the ``staleness'' phase. It arises from two interacting effects: the EMA keeps the target encoder tightly coupled to the main encoder in parameter space, and the predictor, which trains much faster than the encoder, fits the targets of the still uninformative encoder, minimizing the objective while starving the encoder of gradient. We derive an upper bound showing that the coupling depends on the interplay between momentum dynamics and augmentation strategy, and that escape requires the encoder's updates to outpace the EMA's smoothing. This reframes staleness not as an objective flaw but as a transient regime with predictable onset and recovery. The analysis suggests a simple fix: perturbing encoder weights at the start of training breaks the initial symmetry between encoder and target, while the perturbation is quickly absorbed by the EMA and vanishes as training matures. Experiments on images and time-series support the analysis and show that noise injection accelerates recovery and improves final performance.

## 41. Can a world model predict a deepfake video? A Consistency Margin Prior for Deepfake Detection

**Keywords:** Deepfake Detection, VJPEA2, Forensic Residual, Video Foundation Model

[Main paper PDF](https://openreview.net/pdf?id=AHZGp7TsW6)

Deepfake detectors often perform well on the dataset they are trained on,
but their performance drops when tested on videos from different datasets.
In this paper, we study whether a predictive video model can provide a
signal that generalizes better across datasets. Instead of relying only on
generator-specific artifacts, as many existing detectors do, we use a model
trained to predict natural video and measure the difference between what it
predicts and what it observes in a video.

Using V-JEPA~2.1, we keep the encoder frozen and adapt the predictor using
rank-16 LoRA. We define the difference between the predictor output and the
frozen encoder target as the prediction residual. We hypothesize that
manipulated clips produce, on average, larger prediction residuals than
authentic clips, and use this as our consistency-margin prior. We process
these residuals using a lightweight Latent Consistency Head (LCH), which
separates residual magnitude from direction for training and classification.

To test whether the direction of the consistency margin affects cross-dataset generalization, we compare standard and reversed margin objectives while keeping the remaining training setup fixed. We match the two settings on FF++ validation performance before evaluating them on unseen data. The reversed-margin setting exhibits a larger cross dataset generalization gap on average, providing evidence that the direction of the consistency margin affects cross-dataset transfer.
Our complete model adds only $8.25$M trainable parameters, which is
2.47\% of the total $334$M parameters. Trained only on FF++, it
achieves an AUC of $90.5$ on Celeb-DFv2 and performs well across several
other cross-dataset benchmarks. Our ablations show that separating residual
magnitude from direction, reducing dataset-specific variation, and using a
low-rank projection improve cross-dataset generalization in our experiments.

## 42. CardiacState: Learning Cyclic Cardiac State through Predictive Video Pretraining

**Keywords:** Echocardiography, Medical video analysis, Cardiac functional assessment, Self-supervised video representation learning, Temporal representation learning

[Main paper PDF](https://openreview.net/pdf?id=8Sii4peZI1)

Predicting how an observed physical system will evolve requires inferring the underlying state that governs its motion. While controllable video generation relies on external action or text signals, action-free predictive models leave this conditioning implicit within high-dimensional representations. Autonomous biological systems, such as the beating heart, lack external controllers—their driving dynamics unfold continuously within the visual stream itself. Yet, core clinical tasks like keyframe localization and Left Ventricular Ejection Fraction (LVEF) estimation depend heavily on tracking this physiological state. We introduce CardiacState, a joint-embedding predictive architecture (JEPA) that addresses this by formulating physiological progression as an explicit, self-derived conditioning state on a continuous cyclic manifold $S^1$. By imposing a causal temporal bottleneck that denies the future-feature predictor direct access to historical frames, CardiacState forces all temporal context to route exclusively through this $S^1$ state alongside physical elapsed time $\Delta \tau_t$. Pretrained on 1.88 million clinical echocardiogram videos without external text, action labels, or hardware ECG gating, CardiacState advances both feature representation and structural interpretability. Its frozen visual representations achieve $4.87 \pm 0.12\%$ LVEF MAE on EchoNet-Dynamic and $4.73 \pm 0.18\%$ on EchoNet-Pediatric—outperforming prior self-supervised baselines ($5.76\%$ and $5.12\%$). Furthermore, unlike implicit representations, this explicit cyclic state directly enables non-parametric keyframe localization across diverse acoustic views via phase-anchor matching, reducing mean localization error from $2.25$ frames to $1.99 \pm 0.02$ frames. Controlled ablations show that cardiac progression regularization is important for learning a useful cyclic coordinate, while the temporal bottleneck provides further gains in localization and representation quality. These results support cyclic state conditioning for predictive learning in quasi-periodic systems.

## 43. Characterizing How JEPA Constructs Representations

**Keywords:** Joint-embedding predictive architectures, JEPA, world models, predictive closure, representation learning, feature selection, self-supervised learning.

[Main paper PDF](https://openreview.net/pdf?id=8rftN5ad3o)

In joint-embedding predictive architectures (JEPA), an encoder and a predictor are trained together to produce a representation that minimizes the error in predicting the representation of the next observation. Because the representations of both the current and the next observation are learned, it is unclear which features they will include. Earlier works portray JEPA as selecting features based on their individual predictability, raising the concern that control-relevant features may be omitted if they are hard to predict. To address this concern and better understand how JEPA selects which features to encode, we propose the predictive closure characterization. Based on a reformulation of the JEPA training objective, we show that selection depends on joint properties of features. We support this characterization with experiments showing that unpredictable features can become better represented when they help predict other features, and that changing a feature's predictive relationships can affect how well others are represented. We also demonstrate implications for steering feature selection: adding an auxiliary objective targeting one feature can strengthen the representation of others, and supplying a feature as side information to the predictor can change how well other features are represented. We hope this work helps practitioners understand and steer JEPA representations and guides researchers in improving how these systems learn.

## 44. Closing the Loop on Masking Difficulty for Joint-Embedding Predictive Learning

**Keywords:** Computer vision, self-supervised learning, representation learning, data augmentation

[Main paper PDF](https://openreview.net/pdf?id=mlVqTuV7b8)

Joint-embedding predictive architectures such as I-JEPA learn visual representations by predicting the embeddings of target blocks from a visible context. The masking policy that defines this task is typically fixed (I-JEPA samples M=4 target blocks throughout training), even as the representation it shapes evolves. However, a fixed mask does not imply fixed difficulty: the same masking operation can displace the representation differently at different stages of learning. We introduce Feedback-Controlled Data Augmentation (FCDA), a closed-loop
framework that adapts masking using online feedback from representation geometry. A gradient-free sensor measures masking-induced displacement along weak but reliably estimated directions of the feature covariance, and a controller adapts the number of target blocks M so that this displacement tracks a reference calibrated on the original I-JEPA baseline, leaving the training objective untouched. In a matched-
seed ImageNet-1K study with ViT-Tiny/16, FCDA improves linear-probe top-1 accuracy by 3.13 percentage points over the original baseline and also outperforms fixed and approximately target-count-matched open-loop controls. Transfer gains on natural-image recognition and a broader final covariance spectrum support the approach, while best-of-four CLEVR performance remains close to baseline. These
results demonstrate that FCDA learns stronger representations by treating masking as a feedback-controlled component of predictive learning, one that adapts to the representations it helps shape.

## 45. Coarse Intent, Fine Physics: Equipping VLM Agents with Latent World Model Foresight for Open-Loop Manipulation

**Keywords:** World Models, VLM

[Main paper PDF](https://openreview.net/pdf?id=9adX0WL1tJ)

Frontier agents such as Claude Code with Claude Opus 5.5 and Codex with GPT-6 Astra are increasingly used out of the box in robotics, yet they cannot reliably anticipate the physical consequences of low-level actions. JEPA-style latent world models predict these consequences quickly, but planners built on them need goal images and exploit optimistic prediction errors, a failure we call hallucination. We give Claude Code access to DDP-WM through two tools, one previewing a proposed plan as keypoint clouds predicted under one hundred perturbations and one running a local cross-entropy search seeded by that plan, and the agent learns to use both from a single exploratory episode. On a Push-T protocol that requires moving the block 61 pixels and rotating it 77 degrees on average within one open-loop plan 2.4 times shorter than human demonstrations, MPC with DDP-WM solves 2 of 21 episodes and the agent alone 7, while the two tools raise this to 14 and 16. Replacing the clouds by single predictions lowers these numbers to 12 and 13, showing that the agent uses the predicted distribution to avoid hallucinated plans.

## 46. ConTent: Contact-Force Prediction for Latent World Models Enhances Dynamic Manipulation

**Keywords:** world models, joint-embedding predictive architecture, JEPA, contact force, auxiliary prediction, dynamic manipulation, non-prehensile manipulation, model predictive control, representation learning, robot learning

[Main paper PDF](https://openreview.net/pdf?id=QSfsjYR6HP)

Latent world models are powerful encoders of both observations and environment dynamics in robot learning. This study applies a world model to a dynamic manipulation task in which a robot uses a stick to push a ball rolling down a tilted board up into a goal zone. In this task, it is crucial that the observed task-relevant world state, such as the ball state, be accurately encoded in the latent space. Yet, although the regularisers of world models prevent collapse of the latent space, the representation can still degenerate and discard such information, thereby degrading the performance of model predictive control. We show that the discarded information can be recovered by predicting contact forces, which anchor the object representation in the latent space. We exploit this recovery to propose ConTent, contact-force prediction for latent world models, which outperforms the LeWorldModel baseline on our manipulation task. Our method predicts contact forces at training time and raises the success rate from 2% to 52% when planning with the cross-entropy method. Fine-tuning the predictor on on-policy data further improves it to 77%.

## 47. Controllability of Pretrained Visual Representations under Start-Controlled Evaluation on Multi-Object Scenes

**Keywords:** Pretrained vision representations, Self-supervised learning, Representation learning for control

[Main paper PDF](https://openreview.net/pdf?id=cXr1yFCvSd)

Turning pretrained visual representations into behavior requires a procedure for sequential decision making, such as test-time search (CEM) via model-predictive control in the latent space or a goal-conditioned inverse-dynamics model (GC-IDM). We contribute a start-controlled evaluation protocol, an extended evaluation suite with progressively greater object counts, and a long-horizon predictive architecture for learning visual representations. Our start-controlled protocol shows that test-time search methods fail on 3D cube manipulation (0.0% success rate) and that GC-IDM still succeeds (68.9–84.9% success rate). Our extended evaluation suite scales the cube count up to four cubes, revealing that prior work's (LeWM and Sub-JEPA) representations become insufficient for downstream control under GC-IDM. The prior work's random-start evaluation protocol hides both issues, inflating LeWM's four-cube performance from 17.1% to 72.6%. In contrast, on four-cube tasks our proposed architecture learns representations that outperform those of LeWM and Sub-JEPA by up to 20.4 and 35.6 percentage points respectively. Our architecture predicts 50 environment steps of future latents in one pass and, through a structured attention mask, simultaneously learns inverse dynamics from its internal representations of consecutive states; a patch decoder maps each latent back to the encoder's patch representation, retaining object-level detail. Our representations are also more robust to colour distractors in one-cube pick-and-place. Ablations show that our method depends strongly on the training horizon, inverse-dynamics loss, and patch representation reconstruction loss, with the inverse-dynamics term alone worth a third to two fifths of control performance.

## 48. CopuAdapt: An Attentional Copula Adapter for Improved Joint-Distribution Sampling in Probabilistic Time-Series Forecasting

**Keywords:** Time series foundation model, probabilistic forecasting, adaptor, copula

[Main paper PDF](https://openreview.net/pdf?id=o9P8dbS9oT)

Time-series Foundation Models (TSFMs) have demonstrated strong forecasting performance and generalization across diverse domains. For multivariate forecasting, many TSFMs adopt channel-independent modelling. These approaches, however, can struggle to capture cross-variable dependencies in joint forecast samples. We introduce CopuAdapt, a novel attentional copula adapter that augments frozen TSFMs with a learned multivariate dependence model without requiring foundation-model retraining. CopuAdapt constructs empirical marginal distributions from the backbone's forecast samples or quantiles and couples them through an attentional copula architecture operating in probability space. To capture regime-aware dependence, we employ a sparse attention mechanism that infers a directed acyclic graph of conditional independences for each forecasting window, supported by a JEPA-inspired auxiliary objective that learns forecast-relevant temporal memory representations. By leveraging these structural details to dynamically re-order marginal sampling, CopuAdapt strictly preserves the backbone's empirical marginals. Consequently, CopuAdapt, evaluated across the TSLib datasets, exactly preserves the Continuous Ranked Probability Score (CRPS) of the underlying TSFM while significantly improving joint-sampling sensitive metrics, including the Variogram Score (VS), and RBF-MMD, with a median improvement of 4 to 18\% across metrics. Code for this paper can be found at https://anonymous.4open.science/r/CopuAdapt-6C85.

## 49. Cross-attention encoding models reveal dynamic spatiotemporal routing across human higher visual cortex

**Keywords:** Encoding model, fMRI, neuroscience, visual cortex, video, dynamic, spatiotemporal

[Main paper PDF](https://openreview.net/pdf?id=vI9sDMoXj0)

Understanding how the brain parses actions and events from time-varying natural inputs is a central challenge in neuroscience. Recent work has used deep neural network (DNN) models to build stimulus-computable fMRI encoding models that predict single-voxel responses to complex natural videos. However, the majority of video-computable encoding models predict responses using simple linear mappings from model tokens, overlooking the spatiotemporal structure shared by video representations and neural responses. Recent cross-attention encoding models address this limitation for static images, enabling flexible stimulus-dependent weighting of image content across space. Here, we extend this framework to naturalistic video, using per-parcel cross-attention to dynamically route features from a self-supervised video model (V-JEPA-2) across both space and time, fitting this model to fMRI responses to short video clips. We compare joint spatiotemporal attention with factorized and selectively constrained alternatives, and find that joint routing improves predictions of brain responses to held-out videos across higher visual regions, most consistently in lateral and dorsal visual areas associated with dynamic motion perception. Moreover, our method provides interpretable, stimulus-specific attention maps that dynamically follow moving objects, revealing which locations and temporal moments contribute to each neural response. We further show that attention maps from parcels in different category-selective networks (face-, body-, scene-selective) differentially weight content in accordance with expected semantic selectivity. Together, this work provides a new computational framework for understanding how visual information is adaptively weighted by cortical populations during dynamic visual perception.

## 50. Cross-Scale Latent Predictive Pretraining for Whole-Slide Image

**Keywords:** Computational Pathology, Whole-Slide Image Analysis, Self-Supervised Learning, Latent Predictive Learning

[Main paper PDF](https://openreview.net/pdf?id=ruXlRUW0iX)

Whole-slide images (WSIs) contain diagnostic information across magnifications, from tissue architecture to cellular morphology. Multi-scale MIL methods often encode patches from different magnifications independently and combine their representations post hoc, so the coarse representation may fail to preserve cues predictive of fine-scale morphology. Using both scales also requires fine patch encoding at inference. Cross-scale self-supervised learning (SSL) introduces interaction during pretraining, but direct representation matching or fine-patch reconstruction does not account for cross-scale asymmetry because fine views contain details unavailable from coarse inputs. We introduce **Patch-JEPA**, a cross-scale latent predictive pretraining framework. A frozen fine-scale target encoder produces an ordered fine-scale latent field from aligned fine patches. Separate prediction branches map coarse representations to this field and an aggregated coarse-scale target, training the coarse-scale context encoder without direct cross-scale matching or fine-patch reconstruction. Fine-scale representations are used only as pretraining targets, and the retained context encoder uses only coarse patches for coarse-only inference. Patch-JEPA is competitive with standard SSL, cross-scale SSL, and post-hoc multi-scale WSI pipelines on four pathology benchmarks. On RCC, ridge probing yields \(R^2 = 0.450\) for aligned fine-scale latent-field prediction, compared with \(0.231\) for Cross-MAE. Model-side inference cost remains close to a single-scale baseline under a fixed-bag timing protocol.

## 51. CSWAM: Better Causal Semantic Representations for Out-of-Distribution Generalization in World Action Models

**Keywords:** world action model, vjpea, out of distribution

[Main paper PDF](https://openreview.net/pdf?id=VSkLTdtiir)

FastWAM-style world action models enable efficient action-only inference, but generalize poorly under visual distribution shifts. Their reconstruction-oriented representations emphasize appearance-specific details, limiting generalization to unseen scenes and objects. Without observation history, the model also lacks temporal evidence for robustly identifying task-relevant state changes and motion in unfamiliar visual conditions. To address these limitations, we present the Causal Semantic World Action Model (CSWAM), which augments FastWAM with a causal semantic expert built on V-JEPA 2.1. V-JEPA provides temporally grounded representations of semantic state changes and motion with less dependence on appearance-specific details. The expert learns their future evolution from a sparse history of current and past observations and shares the history-derived context with both the video and action streams through causal attention. At inference, CSWAM conditions action denoising on the current video state and observed semantic history, retaining efficient action-only inference. We conduct simulation and real-robot experiments to evaluate generalization under distribution shifts. With embodied pretraining, CSWAM raises Randomized success on RoboTwin 2.0 Clean-to-Randomized transfer from 10.16% to 45.18%, a gain of 35.02 percentage points over FastWAM. Across two real-robot tasks and three OOD difficulty levels, CSWAM improves average success over FastWAM by 42.5 percentage points, from 27.5% to 70.0%.

## 52. CUG-JEPA: Continual Test-Time Adaptation of Latent World Models under Visual Condition Shifts

**Keywords:** continual test-time adaptation, latent world models, continual learning, model predictive control, visual distribution shift

[Main paper PDF](https://openreview.net/pdf?id=b5Zqi8JmqB)

Latent world models can exploit interactive feedback to improve planning, yet single-episode adaptation does not amount to reliable learning under continual deployment: resetting the model after each episode discards previously acquired corrections, whereas unconstrained continual updates may accumulate negative transfer and catastrophic forgetting. To address this challenge, we propose CUG-JEPA, a continual test-time adaptation framework for sequential shifts in visual conditions. Within the closed loop of model predictive control, CUG-JEPA jointly combines non-monotonic uncertainty weighting, online parameter-importance protection, and conditional local restoration, preserving model state across episodes while balancing adaptation to the current environment against long-term knowledge retention. At deployment time, the model uses real transitions naturally observed after action execution as self-supervision, without requiring additional expert demonstrations. Under the primary continual visual-stream protocol on PushObj, spanning three unseen shapes and five random seeds, CUG-JEPA performs one gradient update per feedback step and improves AdaJEPA's overall success rate from 37.3\% to 42.9\%, an absolute gain of 5.6 percentage points. Results on disjoint task batches further reveal that the gains depend on the task set, providing practical evidence for moving world models beyond short-term error correction toward controlled self-updating under continual deployment.

## 53. D-JEPA: A Decision-Aligned Latent World Model

**Keywords:** latent world models, joint-embedding predictive architectures, decision alignment, representation learning

[Main paper PDF](https://openreview.net/pdf?id=7qpkedfwN3)

Latent world models predict the consequences of actions, but accurate prediction does not guarantee that latent distance reflects which candidate will execute successfully. We identify a decision-local prediction gap: among the few futures competing for execution, a candidate predicted closer to the goal can produce a worse realized outcome than an available alternative. We introduce D-JEPA, a decision-aligned latent world model that learns decision-relevant relations among candidate futures from executed outcomes. A bounded, permutation-equivariant operator jointly reasons over goal-relative predictive features and ordinal evidence, refining pretrained predictive geometry where action choices are most consequential. Restricted predictor adaptation and a shared ordinal interface extend this alignment across complementary predictive geometries. D-JEPA further realizes the learned decision structure in JEPA-compatible future representations, enabling deployment through native latent-distance planning. Evaluations across latent control, manipulation, pretrained action-producing models, physical robots and autonomous driving demonstrate improved action selection, including 87.89% success on PushT, a 15.04-point average gain on RoboTwin, and a 17-point gain on physical robot tasks. These results establish decision-relevant relational structure as a direct bridge between predictive world modeling and effective control.

## 54. D-JEPA: Design-Recoverable JEPA Representation with Swappable Physics Decoders

**Keywords:** Scientific Machine Learning, Physics AI, Surrogate Modeling, Joint Embedding Predictive Architecture, Representation Learning, Disentangled Representation, Representation Collapse

[Main paper PDF](https://openreview.net/pdf?id=0zXWnFPtAW)

Joint-Embedding Predictive Architectures (JEPAs) provide a framework for learning compact representations without directly reconstructing
high-dimensional observations. However, in parameterized physical systems, learned representations can entangle geometry with operating conditions and task-specific physical responses, limiting their reuse across prediction tasks. We introduce D-JEPA (Design-recoverable JEPA), a geometry-centric JEPA that computes a compact representation from geometry alone and reuses it
across operating conditions and physical response spaces through lightweight physics-specific decoders. An explicit design-recoverability objective encourages the geometry latent to preserve information about the underlying design variables, enabling the representation to support design analysis and optimization. We further identify a case-level collapse failure mode in which target representations become nearly invariant across distinct geometries despite low reconstruction error, and mitigate it using case-level variation constraints and auxiliary target reconstruction. Across four 3D aerodynamic, hydrodynamic, and structural benchmarks, D-JEPA maintains or improves
full-field prediction accuracy while achieving near-perfect linear recoverability of design parameters. The frozen geometry representation can be reused at held-out operating conditions and transferred to a structural response task with fewer trainable parameters. Finally, the
representation supports differentiable design optimization, with designs validated using high-fidelity CFD, preserving the predicted ranking
of candidate designs. These results demonstrate that separating a reusable geometry representation from physics-specific prediction provides apractical representation for scientific surrogate modeling and design.

## 55. DA-WAM: Decision-Aligned Future Latents for Driving World Models

**Keywords:** autonomous driving, world models, trajectory planning, action-conditioned prediction, joint-embedding predictive architecture, representation learning

[Main paper PDF](https://openreview.net/pdf?id=ngwmV0yz3Y)

World models for autonomous driving should anticipate the consequences that matter for driving decisions rather than reconstruct every detail of future scenes. However, predictive representations alone are not guaranteed to distinguish candidate actions that lead to different planning outcomes. We propose DA-WAM, a decision-aligned world action model that couples a Joint-Embedding Predictive Architecture (JEPA) with candidate-level trajectory scoring. During joint training, the JEPA objective grounds future representations in observed scene dynamics, while the planning objectives encourage these representations to capture distinctions relevant to safety and utility. An action-conditioned predictor generates a distinct future latent for each candidate trajectory, and a multi-head trajectory scorer uses the corresponding latent to estimate planning factors and overall utility. In addition, safety-critical post-training with hard negatives further improves discrimination between geometrically similar trajectories with different safety outcomes. DA-WAM achieves state-of-the-art performance among learned camera-based planners on NAVSIM-v1, NAVSIM-v2, and Bench2Drive. Ablation studies demonstrate the effectiveness of each component in driving decision-making.

## 56. DasWM: Disentangling Dynamic and Static Factors for Latent World Modeling

**Keywords:** World Models, Tokenization

[Main paper PDF](https://openreview.net/pdf?id=IeXR5GeFPs)

We introduce DasWM, a world model representation that softly disentangles dynamic, action-relevant factors from static ones, allowing the allocation of prediction capacity to the dynamic parts. Latent world models make visual planning efficient by encoding observations (e.g. pixels) into compact latent representations. However, not all encoded information needs to be subject to prediction. We show in this work that recently proposed JEPA-like latent world models fail when static visual factors are introduced. We identify the cause of this failure as static-dynamic entanglement in the representation. Our DasWM latent world model encodes each observation as a sequence of tokens, ordered with respect to their dynamic responsiveness. This leads to a representation where dynamic information lies in the early tokens, and static information in the latter ones, minimizing the entanglement. We evaluate DasWM on background-modified versions of several datasets and demonstrate clear improvements in planning, in addition to other benefits such as flexible budget planning at test-time.

## 57. Decision-weighted prediction redirects what a capacity-limited encoder retains

**Keywords:** representation learning, world models, model-based reinforcement learning, partial observability, JEPA, optimal control

[Main paper PDF](https://openreview.net/pdf?id=tfDLB7kbt8)

Capacity-limited predictive encoders are standard in model-based control: each compresses a controller's belief into a code too small to hold it, and no guarantee says the code keeps the directions the control cost depends on. The unweighted objective ranks belief directions by predictive energy, which the control cost does not enter. We prove, using standard spectral arguments, that one reweighting of the target redirects the same capacity onto the directions the cost weights most. The weight is a fixed matrix, the factor that makes prediction error measure control cost. That statement is read at an exact optimum with no tie in the cost's ranking, so our finitely trained runs illustrate it rather than test it. Such a factor exists exactly when the predictive map discards no decision-relevant direction; a counterexample shows the reweighting cannot be dropped. Two companion results drop encoder linearity, show decoder linearity cannot be dropped, and make the condition checkable in advance; every theorem is machine-checked in Lean. On synthetic linear-Gaussian systems the weighted target lowers decision-relevant error wherever the capacity constraint binds.

## 58. DELTA: Dual-stream Encoding with Latent Temporal Anticipation for Frozen Visual World Models

**Keywords:** world models, robotic manipulation, visual dynamics, representation learning, JEPA

[Main paper PDF](https://openreview.net/pdf?id=8D9IsNxnWW)

Frozen vision backbones such as V-JEPA 2.1 provide strong visual features for manipulation, but not an action-conditioned model of dynamics. Existing world models introduce that dynamics under different modeling assumptions. Predictors defined on frozen features take a short temporal window and regress the next embedding, so they maintain no state beyond that window and do not cast the prediction as an update of the observed frame. Predictors that retain a longer history instead advance an image code or a learned latent, and therefore depart from the frozen representation. We propose DELTA, a reconstruction-free world model on frozen V-JEPA 2.1 (ViT-B/384) features. A dual-stream latent carries state across time and is updated by an action-conditioned causal transition. A residual head writes the resulting short-horizon change onto the observed tokens. Actions enter only as conditioning. On manipulation demonstrations, under a shared feature-cache protocol, DELTA lowers multi-step open-loop, replan, and CEM feature-prediction error relative to these baselines.

## 59. Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation

**Keywords:** robot learning, world model

[Main paper PDF](https://openreview.net/pdf?id=WSCUqPbOC9)

Robotic imitation learning is often treated as reproducing demonstrated actions, but actions are inherently embodiment-specific.
When demonstrations come from humans or robots with different morphology, kinematics, or action spaces, this action-centric view requires shared action spaces, heuristic retargeting, or large-scale multi-embodiment co-training.
We instead view demonstrations as implicit specifications of future goals: the target agent should infer what state the demonstrator is trying to realize, rather than how the demonstrator executes it.
We propose Demo-JEPA, a cross-embodiment imitation framework that decouples demonstration intent from embodiment-specific execution.
Built on a JEPA-based world model, Demo-JEPA translates source visual demonstrations into target-compatible future latent trajectories in a shared predictive representation space.
The target agent then uses these latent trajectories as subgoals and realizes them through planning under its own learned forward dynamics.
Because Demo-JEPA avoids action-level correspondence and requires only visual demonstrations plus the target agent's own interaction experience, it supports flexible imitation across heterogeneous embodiments.
Experiments on RLBench and real-world manipulation tasks show that Demo-JEPA matches specialized in-domain planners and generalizes to unseen tasks and embodiment configurations where prior methods fail.

## 60. DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation

**Keywords:** Visual Perception; JEPA; Depth; Embodied Manipulation

[Main paper PDF](https://openreview.net/pdf?id=PJnDxPEjb8)

Predictive representations for robot manipulation should connect scene geometry with the state changes induced by actions. Our intuition is that understanding what an action will change starts with understanding where things are: complementary RGB and depth observations ground a common scene representation from which to infer those changes. Guided by this intuition, we introduce **DepState-JEPA**, a dual-stream RGB--Depth joint-embedding predictive architecture that connects spatial understanding with action-conditioned prediction through a shared latent state, **DepState**.
Built on V-JEPA~2.1, the framework uses depth both as a complementary observation stream and to ground both modalities in metric 3D space, aggregating shared information into DepState while retaining modality-private features for decoding.
Ray-conditioned readouts predict local features without target depth; after an action-conditioned transition, the same decoders predict future RGB and depth features using the predicted state and fixed initial private features.
Robot-state readouts provide recursive proprioceptive inputs; object-trajectory supervision and calibrated forward kinematics shape state learning through motion targets and joint--TCP consistency.
Comparisons show stronger RGB-encoder transfer after RGB-D adaptation, feature completion, conditioned visual forecasting, and manipulation success. Within-model ablations identify contributions from depth content, metric coordinates, and future-state matching, with additional control gains from FK regularization.

## 61. Detecting Temporal Concepts in Video Transformers via a No-False-Positives Test

**Keywords:** temporal representations, video transformers, mechanistic interpretability, sparse autoencoders, statistical testing, representation analysis

[Main paper PDF](https://openreview.net/pdf?id=0jT3rYKMXb)

Video models have the architecture to support encoding temporal aspects of the input, i.e. concepts that require more than one frame to define, like object movement. However, because motion and appearance change are entangled, a feature that appears to encode temporal concepts like object movement may instead encode non-temporal concepts like spatial presence at different positions whose activations merely correlate with motion. To resolve this, we introduce the No-False-Positives (NFP) test, a statistical test with a formal guarantee of statistical specificity for identifying features encoding temporal concepts. Using specially designed stimuli, we apply this test to representations produced by VideoMAE, V-JEPA2, and TimeSformer, and observe that temporal features exist in each model. We validate the test first by showing it yields no temporal features for the DINOv2 image-encoder. Then, using a synthetic representation space, we show that detection rate increases with a direction's projection onto the temporal subspace, and that Sparse Autoencoder features test-flagged as temporal project much more of their norm onto the temporal subspace than unflagged features. Interventions on temporal SAE features yield mixed results across models, suggesting that intervening on temporal features may not outperform a non-temporal feature baseline.

## 62. Devol-ONE: One Autoregressive Mixture of Transformers to Unify Vision-Language-Action and Latent World Modeling

**Keywords:** Vision-language-Action, World Model

[Main paper PDF](https://openreview.net/pdf?id=40IHLmcuK4)

Vision Language Action (VLA) models condition actions directly on current visual and language context, without an explicit account of how the scene evolves under candidate actions. World Action Models (WAM) attempt to address this limitation by predicting future states, but existing designs keep prediction and policy learning architecturally separate, connecting them only through the predicted output, whether through pixel space video generation or a latent forecasting module trained independently of the policy. We present Devol-ONE, a Mixture of Transformers architecture that unifies vision language understanding, latent world dynamics prediction, and action generation within a single autoregressive framework. Instead of encoding vision language tokens once and feeding them to the action expert, Devol-ONE runs autoregressive prediction jointly across a vision language stream and a V-JEPA pretrained dynamics stream, attending to the vision language key-value cache at every layer to forecast future latent states under language guidance. The action expert is in turn shaped continuously by semantic reasoning and predicted physical dynamics rather than by a fixed representation computed in advance. Extensive experiments are conducted on LIBERO, LIBERO-PLUS, RoboTwin2.0 along with real-world evaluation on Flexiv single-arm and dual-arm setups. Ablation studies show the effectiveness of dynamic stream prediction and layer-wise unified attention to validate our model architectural coherency.

## 63. DexForesight: Self-Distilled Foresight for Dexterous Vision-Language-Action Models

**Keywords:** Dexterous Manipulation, Vision-Language-Action Models, Self-Distillation, Foresight Learning, Predictive Representation Learning, JEPA

[Main paper PDF](https://openreview.net/pdf?id=Z9OV93HxGs)

Task-oriented dexterous manipulation requires coordinated arm–hand actions whose quality is determined by the physical and visual consequences that follow them. Demonstration trajectories therefore contain more supervision than the demonstrated actions alone: they also record how objects move, articulate, and appear after each interaction. We introduce DexForesight, a training framework built on a single observation: a demonstrated future can supervise a causal policy in two fundamentally different ways—a predicted future teaches the representation what interaction state to anticipate, while the realized future teaches the action generator how its current prediction should change. For representation learning, we adapt V-JEPA 2 to demonstration trajectories and design an action-conditioned latent predictor with structured arm–hand controls; its predicted future latent supervises learnable query tokens in the vision-language model (VLM) representation. For action generation, we execute the same policy under causal and privileged future context; their velocity difference defines a future-conditioned flow correction learned by a lightweight residual adapter. Future observations and simulator object states are used only during training and are removed at deployment. Across the 11 single-arm and bimanual tasks of DexJoCo, DexForesight improves the average success rate of the DexJoCo π0.5 baseline by 10.1 percentage points (62.6% vs. 52.5%). Both supervision paths improve the policy in isolation, and their combination performs best; combining physical and visual privileged future context also achieves the strongest average performance.

## 64. Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency

**Keywords:** world models; world model diagnostics; joint-embedding predictive architectures (JEPA); action-conditioned prediction; visual robustness

[Main paper PDF](https://openreview.net/pdf?id=NU3U8KWzFQ)

Joint-embedding predictive architectures (JEPAs) learn world models that predict in a compact latent space rather than in pixels, reducing the pressure to model nuisance appearance. Yet this provides no guarantee against visual perturbations: they can still alter the encoded representation and affect subsequent action-conditioned predictions. Bisimulation captures this requirement precisely: two observations should be treated as the same state only when their action-conditioned consequences agree. Guided by this criterion, we introduce Action-Conditioned Predictive Consistency (ACPC), a diagnostic that measures how far a clean history and a visually perturbed view of it diverge after being rolled forward under the same action sequence. We prove that this divergence bounds perturbation-induced changes in multi-step prediction error and planner cost, i.e., the change in predicted cost caused by a visual perturbation under the same action sequence. Building on pairwise ACPC, we define two complementary measures: Invariance Radius (IR) summarizes clean--perturbed rollout spread, while Separation Rate (SR) checks whether different states remain distinguishable after rollout. Experiments on four visual control tasks show that pairwise ACPC predicts perturbation-induced changes in prediction error and planner cost. On LeWM, the joint IR--SR screen transfers across tasks, and both IR and SR remain informative under blur and resize. PLDM exhibits similar diagnostic trends under a different architecture.

## 65. DiJEPA: Self-Supervised Learning via Diffusion in Latent Space

**Keywords:** JEPA, Self-Supervised Visual Learning, Diffusion Models, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=zejU11C6Hc)

Joint-Embedding Predictive Architectures (JEPAs) learn semantic representations by predicting the latent embeddings of the masked target view from the visible context.
Existing approaches use either direct regression in a continuous embedding space or token-softmax prediction over quantized targets.
While effective, direct regression does not explicitly model a target distribution, whereas token-based prediction performs distribution matching in a discrete space; both rely on carefully designed distribution regularization to stabilize training and improve representation quality.
We introduce DiJEPA, a JEPA-style framework that formulates visual representation learning as diffusion-based prediction over an online projection of the encoder's representation space.
DiJEPA jointly trains a Feature Auto-Encoder (FAE) with the encoder, mapping high-dimensional representations into low-dimensional continuous latents whose distribution is optimized throughout representation learning.
A diffusion predictor then reconstructs target-view latents from student-view representations through denoising, providing a distributional prediction objective in a continuous latent space.
On ImageNet-1K with a ViT-L backbone, DiJEPA achieves 83.24% top-1 linear probing accuracy under a non-distilled setting, competitive with 83.3% from DINOv3.
The jointly learned FAE latents can also be used for image generation, achieving 2.74 gFID without CFG in 80 epochs of latent diffusion training.
Our results establish diffusion-based prediction over evolving FAE latents as a new predictive objective alongside direct regression and distribution matching over discrete tokens for self-supervised visual learning.

## 66. DiPhy: Distilling Transferable Physical Knowledge for Physics-Aware Video Generation

**Keywords:** video generation, physical consistency, physics-informed generation

[Main paper PDF](https://openreview.net/pdf?id=hh9NHythnJ)

Recent generative video models have achieved impressive visual quality and increasingly realistic video synthesis, yet they still struggle to generate videos that obey plausible physical dynamics. Existing approaches typically incorporate physical information through textual descriptions, trajectory constraints, or additional conditioning signals, whereas how physical knowledge can be effectively mined and transferred to video generation has not yet been sufficiently investigated. Facing this challenge, we propose DiPhy, which distills transferable physical knowledge into a diffusion model for physically plausible video generation. Specifically, a JEPA-based teacher first mines physics-related cues from videos under semantic guidance. These cues are organized into a structured physical codebook that serves as a compact shared space for transferable physical knowledge, which is then distilled into a student module for text-only physical reasoning without video access. The inferred physical codes are subsequently injected into the diffusion backbone through a lightweight physical branch, providing explicit physical guidance during generation. Extensive experiments on physics-oriented video benchmarks demonstrate that our DiPhy improves physical consistency while preserving semantic alignment and overall video quality, with physical commonsense scores improving by approximately 9% and Joint performance by over 10% on VideoPhy2. Moreover, our DiPhy enables efficient video generation with relatively short inference time.

## 67. Disentangling the Geometries of Prediction and Planning in Latent World Models through Trajectory-Graph Control Calibration

**Keywords:** Latent world model; Disentanglement; Graph

[Main paper PDF](https://openreview.net/pdf?id=rLTNoi6Jhd)

Joint-Embedding Predictive Architectures (JEPAs) provide an efficient foundation for latent world models by predicting future representations rather than reconstructing pixels. However, Model Predictive Control (MPC) planners built on these models typically select action sequences by minimizing the terminal latent distance to the goal, which implicitly assumes that latent similarity measures the remaining cost to the goal. In contrast, goal-reaching cost can be directional, violating the symmetry imposed by latent-distance planning and potentially causing the planner to prematurely discard dynamically preferable action sequences. To address this limitation, we propose Trajectory-Graph Control Calibration (TGCC), a lightweight post-hoc method that disentangles the geometries of prediction and planning over the same frozen latent representations. Concretely, TGCC constructs a directed graph over offline trajectories and distills its temporal relations into a control geometry network. During planning, the network's graph-derived control score is combined with terminal latent similarity to rank candidate action sequences, thereby defining a planning geometry beyond the prediction geometry. Without retraining the world model, TGCC achieves superior planning performance across multiple datasets and latent world-model backbones, with higher success rates and fewer steps to success.

## 68. DO LATENT WORLD MODELS REALLY SELECT THE RIGHT ACTIONS?

**Keywords:** latent world model, planning, JEPA, model predictive control

[Main paper PDF](https://openreview.net/pdf?id=66VRiNq89U)

Latent world models have recently shown strong results in planning from images, particularly on navigation and manipulation tasks. They score candidate action sequences by the distance between their predicted embeddings and the embedding of a goal image. We find that on fixed candidate sets this score usually misses the best action sequence, and that on the manipulation tasks most models do no better than a random choice. On Push-T the released model's predictor causes this. If these scores misrank fixed candidates, why does planning still work so well? Part of the answer is that the same scores rank the planner's own candidates far above a random choice, with the best one on top in 18.1% of Push-T searches against 1.6%, and we show that wider search and more frequent replanning also contribute to this success. PointMaze success falls from 91% to 76% without replanning. On Push-T, a wider search raises success without replanning from 13% to 67%. Further analysis on PointMaze finds a successful action sequence among the planner's candidates in over 90% of episodes, yet the candidate the model scores highest succeeds in 63%. Our findings suggest that strong results in planning do not show that a latent world model selects the right actions.

## 69. Do-Causal-JEPA: Learning Interventional World Models with Graph Surgery Estimator

**Keywords:** invariant prediction, world models, causality

[Main paper PDF](https://openreview.net/pdf?id=x7TPKIQEEe)

Recent advances on Joint Predictive Embedding Architecture (JEPA) have shown significant progress in learning object-centric representations and the dynamics of these representations from images and videos. One prominent model is known as Causal-JEPA (C-JEPA) \citep{nam2026causaljepalearningworldmodels}, which learns the interaction dynamics of objects by masking different feature maps based on images from previous time frames to predict the next time frame's representation state. The model is shown to be able to learn an important notion called \textit{influence neighborhoods}, which are claimed to be the minimal predictor sets of each object in the image without causal sufficiency under mild assumptions. However, the relationship between influence neighborhoods and some classical causality concepts, such as invariant causal predictors, is not well-understood. In this work, we show that C-JEPA does not learn invariant causal predictors in a controlled environment in the presence of latent confounders. We propose an alternative training scheme to introduce an additional loss term that is based on graph surgery operations for learning object-level invariant predictors given a causal structure. Empirically, our proposed algorithm Do-CJEPA outperforms C-JEPA in learning the dynamics of the objects under mechanism shifts by having a smaller out-of-distribution test error gap and prediction errors in terms of mean squared error for both one-step prediction and rollout under shifted test environments.

## 70. Do-JEPA: From Masking to Intervention in Latent World Models

**Keywords:** world models, JEPA, paired interventions, action-effect learning, causal propagation, context invariance

[Main paper PDF](https://openreview.net/pdf?id=jA6DsjW60P)

Latent world models are trained to predict what happens next, so nothing in their
objective separates what an action caused from what merely co-occurred with it.
Object-masking models such as C-JEPA intervene on what the predictor can see; we
intervene on what physically happens. From one saved simulator state we run the
dynamics under an action $a$ and under a reference action $\anull$, and train the
model to predict the difference $\Delta z=z^{a}-z^{\anull}$ between the two latent
futures. The resulting objective, Do-JEPA, has an effect loss, a support loss
(where the action enters), a propagation loss (where its effect travels) and
invariance losses (what must not change). In a synthetic system with
object-aligned variables, support supervision finds the directly intervened object
in $99.95\%$ of test cases, where a sparse action mask sends the action to a
nuisance slot in every case, and response-onset supervision recovers the
ring-shaped propagation graph (edge AUROC $0.975$ vs.\ $0.624$). From pixels, the
effect loss beats a control trained on exactly the same data: it lowers latent
effect error by $28.4\%$ on an end-to-end LeWM model ($3/3$ seeds) and physical
effect error by $13.5\%$ when trained and tested on natural action sequences, and on three
independently generated CausalWorld benchmarks it lowers responsive effect error
by about $20\%$ under physics shifts and the latent context sensitivity of
predicted effects by $66\%$. Trained from scratch it costs factual accuracy;
fine-tuning an existing model with it removes this cost. Together, these results show 
that intervening on the world, rather than on what the model sees, helps latent world models
predict what their actions cause.

## 71. Does Latent Planning Survive Point Clouds? Action-Conditioned JEPA World Models for Geometric Observations and Goals

**Keywords:** world models, latent representation, robotics, control, point clouds

[Main paper PDF](https://openreview.net/pdf?id=Pt1DxECbW9)

Latent action world models let agents plan new behaviors at test time by predicting how actions change the environment, and joint-embedding predictive architectures (JEPAs) do so by forecasting future latent states rather than pixels. Yet nearly all such models see the world through a camera, even though robotic manipulation is fundamentally geometric: in robotics goals for manipulation are traditionally specified by target object poses, not by images of the object once placed. We ask whether latent planning survives a shift from appearance to geometry, on the observation side as well as on the goal specifications side. To answer this, we extend the stable-worldmodel evaluation platform with simulated LiDAR-style raycast point clouds as a new sensor modality, and adapt three JEPA designs to point clouds: a frozen-encoder model built on Utonia features, a distribution-prior model based on LeWM, and an action-sensitive model based on Delta-JEPA. We further introduce a goal-encoding mechanism that constructs the goal latent from the current latent and a 3D target pose, removing the need for goal images or goal point clouds. A comparative evaluation of the different anti-collapse mechanisms shows that point-cloud world models can match their image-based counterparts, demonstrating that the modality shift from appearance to geometry is achievable. All models are released as open weights with open-source training and inference code, to make world-model planning accessible for LiDAR-driven and pose-directed robotic tasks.

## 72. Does Surprise Measure Intuitive Physics? The Score Depends on How the Model Is Read

**Keywords:** intuitive physics, violation of expectation, evaluation methodology, video world models, latent-predictive models, V-JEPA, representation diagnostics, measurement validity

[Main paper PDF](https://openreview.net/pdf?id=KMwOmfu3bA)

Latent-predictive video models are said to acquire intuitive physics when they are more surprised by an impossible event than by a possible one (Garrido et al., 2025). That surprise is a single scalar, the difference in prediction error between two otherwise identical clips. The benchmark that defines that score chose the measure deliberately, naming one alternative protocol (Weihs et al., 2022) and reporting that the alternative had not yielded evidence of understanding (Bordes et al., 2025). Nothing has established what the difference contains. We decompose the squared form exactly into magnitude, direction and a selection term, and show it is not a fixed property of the model. We measure it on V-JEPA 2 (Assran et al., 2025) and V-JEPA 2.1 (Mur-Labadia et al., 2026). Both are publicly released latent-predictive encoders, and only V-JEPA 2.1 exposes intermediate depths to read at. Reading V-JEPA 2.1 at the four encoder depths its predictor was trained to read, with nothing attached on top, the reported accuracy spans 10.18 percentage points with the model, the clips and the readout all unchanged. Across the two encoders every term keeps its sign and none keeps its size, so the two standard normalisations disagree about which model is more direction-driven. A motion-only observer touching neither model shows that most or more of what the score detects is available from movement alone. We then move the score using a regulariser carrying no physics. An untrained random projection preserves accuracy at 88.39% against the frozen encoder's 89.55%. Training a small network in its place, under the coefficients published with VICReg (Bardes et al., 2022), drives it to 46.57%, a point estimate below chance whose 95% confidence interval contains chance. Raising one of those three coefficients recovers 94.62%. A violation-of-expectation score is not readable as physics evidence until six quantities are reported beside it. We specify those six and show what each one catches.

## 73. DroneWAM: Efficient World Action Model for Drone Visual Navigation

**Keywords:** World Action Model, UAV Navigation, Visual Navigation

[Main paper PDF](https://openreview.net/pdf?id=btjxiX4YmM)

World-action models give visual navigation agents a way to anticipate how candidate actions will change future observations and to act from the predicted consequences. 
For drones, this capability must operate under tight accuracy and efficiency constraints. We present DroneWAM, an efficient world-action model for drone visual navigation. DroneWAM adopts a JEPA-based architecture to model future states directly in representation space, avoiding the cost of explicit future image generation. A pretrained Resampler further compresses dense encoder features into fewer latent tokens, reducing the computation repeated at each imagined step. We also introduce adaptive rollout, where a preference-trained Gate adaptively allocates prediction depth according to the current scene. To support learning under richer aerial motion, we construct DroneNav-6D, a simulated visual navigation dataset with synchronized RGB observations, 6-DoF flight trajectories, control commands, and randomized wind disturbances. On DroneNav-6D, DroneWAM achieves the best trajectory accuracy among the compared methods.
Adaptive rollout further reduces the average prediction depth from 8 to 4.58 while improving trajectory accuracy, demonstrating that predictive computation can be allocated more effectively across scenes.

## 74. DSReg: Provably Recovering Individual World Latents without Reconstruction

**Keywords:** Representation learning, world model

[Main paper PDF](https://openreview.net/pdf?id=sS9rVZOFyx)

Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervision, or distributional asymmetries such as non-Gaussianity. Methods without these anchors, including joint-embedding predictive architectures (JEPAs), identify the latent state only up to a linear transformation, so individual latents remain mixed. We close this gap: individual world latents can be provably recovered with no reconstruction, no decoder, and no labels. The key condition is Structural Diversity: different latents leave distinct dependency footprints on observations, just as no two snowflakes are alike. Building on the linear identifiability that LeJEPA provides, we prove that under Structural Diversity and a standard faithfulness condition, DSReg (Dependency-Sparsity Regularization) recovers individual world latents up to signed permutation. It applies post hoc to any linearly identified representation, reusing trained checkpoints at no loss over joint training, and establishes the first fully identifiable JEPA that recovers every world latent. Moreover, as a condition on dependency footprints, Structural Diversity is strictly weaker than all structural conditions of prior identifiable latent variable models. Across synthetic regimes, world model probes, learned visual encoders, and external renderers, DSReg preserves dense prediction while improving individual-latent recovery and downstream use with scales.

## 75. DSSF: Robust Latent State Construction for JEPA-Based Visual Planning

**Keywords:** JEPA, Latent World Model, Out-of-Distribution Generalization

[Main paper PDF](https://openreview.net/pdf?id=TTYWvkU5jV)

Latent world models based on the Joint-Embedding Predictive Architecture provide an efficient approach to dynamics modeling for visual planning by predicting future representations rather than reconstructing pixels. However, latent prediction primarily optimizes the predictability of visual information and does not guarantee that the retained factors are relevant to control. Consequently, task-irrelevant backgrounds and visual distractors may be encoded into the latent state, perturbing state prediction and goal matching when previously unseen visual distractors occur at test time. We propose DSSF, a two-stage latent-state construction method for improving planning robustness under unseen visual distractors. In the first stage, learnable prototypes model the feature-space support of non-distractor visual factors and filter out local factors that are not supported by the training distribution. In the second stage, DSSF sparsely selects information relevant to action-conditioned dynamics from the retained factors to construct a compact latent state. In this way, DSSF separately models whether a visual factor is supported by the training distribution and whether it is relevant to control, thereby suppressing both unseen distractors and in-distribution yet control-irrelevant information. We evaluate unseen distractor instances and cross-family distractors to systematically assess planning robustness under increasingly severe shifts in distractor appearance and count.  Across multiple continuous-control tasks, DSSF better preserves clean-setting planning performance and consistently outperforms strong baselines under unseen distractors and cross-family distractor-appearance shifts, indicating that its robustness does not rely on memorizing the appearances of training distractors.

## 76. DT-JEPA: Learning to Predict Future Representations for Decision-Making

**Keywords:** Reinforcement Learning, Decision Transformer, Joint-Embedding Predictive Architectures, World Models

[Main paper PDF](https://openreview.net/pdf?id=EuV5fhaJkc)

Decision Transformer (DT) has demonstrated strong performance in various offline reinforcement learning (RL) tasks by conditioning action generation on expected future returns and historical trajectories. However, treating expected future returns as the condition provides an incomplete description of the future, as trajectories with different state transitions and behaviors may share similar returns. Moreover, expected future returns inherently depend on task-specific reward functions, which makes the policy learning reliant on reward-labeled datasets and restricts its scalability to tasks with similar but unseen rewards. Recently, Joint Embedding Predictive Architectures (JEPA) has emerged as a promising paradigm of self-supervised learning-based world models, which learns predictive representations of future dynamics in latent space rather than reconstructing future states in the original space. Inspired by JEPA, we propose DT-JEPA, an offline pretraining and online finetuning framework that learns general knowledge from reward-free offline trajectories and achieve excellent adaptation to the unseen tasks. Instead of predicting a single deterministic future embedding, we design a novel probabilistic predictor to model the
conditional distribution of future representations in the latent space, thereby
capturing both predictive information and uncertainty about future
dynamics. The predicted future representation is then utilized to guide DT's action generation. To generalize to tasks with unseen reward objectives, we further develop a critic-guided fine-tuning mechanism to efficiently adapt the pretrained policy to unseen reward functions with limited online interactions. Theoretically, we show that 1) the JEPA objective seeks to maximize a variational lower bound on the mutual information between historical representations and future trajectories; and 2) predictive future-conditioned policy learning admits a finite-sample performance bound with an $\mathcal{O}(N^{-1/4})$ estimation term. Experiments on D4RL benchmarks demonstrate that DT-JEPA achieves efficient adaptation across varying offline RL tasks, outperforming traditional DT-based and other offline RL methods.

## 77. Earth-JEPA：Toward efficient and transferable Earth-system latent representation learning

**Keywords:** representation learning, self-supervised learning, earth system modeling, foundation models

[Main paper PDF](https://openreview.net/pdf?id=CTH0mXU2lj)

Deep learning for Earth system forecasting has advanced rapidly, mostly through end-to-end supervision on reanalysis data for individual tasks. This training paradigm tends to be less efficient on spatiotemporally smooth fields, while making cross-task adaptation relatively expensive. To overcome these challenges, we introduce Earth-JEPA (E-JEPA), a reconstruction-free, multi-resolution, modality-wise Joint-Embedding Predictive Architecture for efficient and transferable Earth-system prediction. Modality-specific branches encode satellite observations, atmospheric reanalysis and geographic fields into a multi-resolution latent state. A latent-pyramid predictor with Scale-Specific Attention forecasts future representations, each supervised by its corresponding exponential moving average (EMA) target through a State-Transition Loss. On WeatherBench2, Earth-JEPA achieves 17.8% higher 24-hour U850 anomaly correlation coefficient (ACC) than a leading large-scale supervised weather forecaster using only about 12.8% of their estimated training compute. Experiments on SEVIR and our proposed EarthCastBench benchmark demonstrate transferability across time-intervals and sensors, robustness to missing reanalysis, and strong performance on dense tasks, e.g., precipitation nowcasting, and forecasting of surface and atmospheric variables. These results suggest a promising direction for efficient and transferable Earth-system latent representation learning. Code and data will be released upon publication.

## 78. EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos

**Keywords:** Dexterous Manipulation, JEPA, Egocentric Video

[Main paper PDF](https://openreview.net/pdf?id=KTnr4gJFoS)

Egocentric human videos offer a scalable alternative to costly robot demonstrations, yet transferring their manipulation priors to robot control remains challenging. The commonly adopted retargeting-based approaches convert human wrist and finger poses into embodiment-specific action commands through hand-crafted geometric mappings. However, such mappings require meticulous recalibration across different embodiments and risk propagating hand-tracking errors into downstream robot control pipelines. To this end, we propose EgoJEPA, a three-stage framework that learns embodiment-agnostic representations from egocentric human videos without rule-based human-to-robot retargeting: 1) Human-action pre-training learns effect-aware latent actions through JEPA-style visual prediction conditioned on hand-motion differences; 2) Latent-action-based world modeling jointly predicts future visual dynamics and latent actions, which decouples human prior pre-training from robot-specific control parameterizations; 3) Embodiment-specific tuning adapts the pretrained model to diverse robots through lightweight action adapters. Experiments on five real-world manipulation tasks across three robot embodiments demonstrate the effectiveness and efficiency of EgoJEPA. It achieves a 74% average success rate under the out-of-domain evaluation, compared with 65% for the retargeting baseline, while reducing cumulative cross-embodiment wall-clock cost by 47.2%, from 743.2 to 392.7 hours.

## 79. EMR-JEPA: Future-Focused and Policy-Responsive Learning for Clinical Forecasting

**Keywords:** irregularly sampled time series, self-supervised learning, joint-embedding predictive architecture (JEPA), electronic health records, domain generalization

[Main paper PDF](https://openreview.net/pdf?id=8hn0ChnllS)

Clinical monitoring requires predicting a patient's future from sparse, irregular measurements collected under hospital-specific acquisition policies. We introduce EMR-JEPA, which learns patient-state representations by predicting future latent states rather than raw measurements. We first examine the masking policy: progressively shifting a matched masking budget from the past to the future increases mean out-of-domain frozen-probe AUROC from 0.6273 to 0.6502 across six-hour AKI and sepsis prediction on MIMIC-III, HiRID, and eICU. We then study the representation on which prediction operates. Fixed-count patching groups 16 consecutive measurements into adaptive-duration patient states, preserving finer resolution in densely observed periods. Because these states are defined by measurement count, their number and timing within the forecast horizon are unknown at prediction time and reflect the hospital's acquisition pattern; EMR-JEPA therefore predicts both alongside the states' latent content. Fixed-count patching alone matches fixed-duration patching in mean out-of-domain AUROC (0.650 for both), whereas adding count and time prediction raises it to 0.681 with one weighting shared across hospitals and tasks, and produces the clearest separation between local and long-range attention heads. Fine-tuned on a held-out hospital, EMR-JEPA attains the best average rank among self-supervised baselines for both sepsis and AKI, with the largest margin when target labels are scarce.

## 80. Enterprise-JEPA: Learning Latent Tool-Use Dynamics for Efficient Agent Planning

**Keywords:** world models, joint-embedding predictive architectures, LLM agents, model-based planning, efficient inference

[Main paper PDF](https://openreview.net/pdf?id=PQw4BecKzn)

Enterprise workflows require tool-using agents to coordinate actions across applications, maintain state over long horizons, and avoid costly execution errors. World models can improve planning by predicting the consequences of candidate tool actions, but existing LLM-based approaches rely on autoregressive generation of imagined observations, making repeated planning computationally expensive. We introduce \emph{Enterprise-JEPA}, the first action-conditioned latent world model for enterprise tool-using environments. Given the task context, interaction history, and a candidate action, Enterprise-JEPA predicts the latent representation of the resulting tool observation and decodes seven interpretable operational signals: action type, execution status, error, progress, side effects, information sufficiency, and task completion. A two-stage training procedure first learns latent dynamics from unlabeled trajectories and then fits operational-state heads using annotated transitions. Scaling unlabeled pretraining improves structured next-state prediction and surpasses a similarly sized LLM-based world model. Enterprise-JEPA also delivers strong downstream performance. With beam search, it consistently outperforms a no-world-model baseline across all five benchmarks, while its latent rollout mechanism is substantially faster than an LLM-based world model. These results demonstrate that latent world modeling enables more effective and efficient planning for enterprise tool-using agents, improving decision quality while reducing inference latency. Code is available at https://anonymous.4open.science/r/enterprise_jepa-8421.

## 81. Entropy--Contraction Coupling in Softmax-Routed Mixture Systems: Theory and Applications

**Keywords:** Mixture-of-Experts (MoE), Joint Embedding Predictive Architectures (JEPA), diffusion model classifier-free guidance, hierarchical reinforcement learning with options, Entropy-Aware Spectral Regularization (EASR)

[Main paper PDF](https://openreview.net/pdf?id=ivqFr1rHRX)

We establish a general theoretical connection between the routing entropy
of a softmax-gated mixture system and its global Lipschitz (contraction)
constant. For any operator of the form
$\mathcal{T}(z) = \sum_{k=1}^{K} \pi_k(z)\, F_k(z)$,
where $\pi(z) = \softmax(g(z))$ and each component $F_k$ has Lipschitz
constant $c_k$, we prove that
\[
  L_{\mathcal{T}} \;\leq\; c_{\min}
  \;+\; (c_{\max} - c_{\min})\,\frac{e^{H(\pi)}}{K},
\]
where $H(\pi)$ is the Shannon entropy of the routing distribution.
This \emph{Entropy--Contraction Coupling} (ECC) theorem reveals that
routing specialization -- a decrease in $H(\pi)$ -- automatically tightens
the contraction bound, independently of the learning algorithm, loss
function, or data distribution.
We instantiate ECC across four settings: (i) Mixture-of-Experts (MoE)
language models, where ECC explains training instability and suggests
entropy-scheduled spectral constraints; (ii) Joint Embedding Predictive
Architectures (JEPA), where ECC certifies stability for recursive latent
predictors; (iii) diffusion model classifier-free guidance, where ECC
characterizes score-mixture stability; and (iv) hierarchical reinforcement
learning with options, where ECC gives Bellman-contraction guarantees under
option switching.
We propose \emph{Entropy-Aware Spectral Regularization} (EASR), a
practical training technique derived from ECC, and validate it empirically
on MoE language model training and JEPA representation learning.

## 82. EquiJEPA: Learning Action Representations for Effect Prediction and Action Generation

**Keywords:** JEPA, World Model, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=kL6yVNKC2j)

An action representation should describe how an action changes the world and help an agent choose actions that produce a desired change. We introduce EquiJEPA, an inverse-dynamics Joint Embedding Predictive Architecture that learns this bidirectional connection in latent space. A state-blind effect head predicts latent changes from actions alone, encouraging transitions induced by the same action to concentrate around a shared prototype. Each transition consists of this prototype and a residual capturing state-dependent departures, including contact and collision. The prototypes provide concrete operations in latent space: an effect can be transferred to a new state, combined with another effect, and decoded into an action through the inverse head. Across simulated environments, we evaluate these operations through physical execution, including cross-state reuse and action combinations absent from training. EquiJEPA connects action-conditioned prediction with effect-conditioned action generation, providing an explicit action representation for reuse and compositional generalization.

## 83. ErrandVLN: A Benchmark for Intent-Driven Long-Horizon Continuous Vision-and-Language Navigation

**Keywords:** Vision-and-Language Navigation;Benchmark;Embodied AI

[Main paper PDF](https://openreview.net/pdf?id=ZxSqNLKyhH)

Existing continuous vision-and-language navigation (VLN) benchmarks primarily
evaluate single-goal route following, whereas everyday household requests may
require agents to visit multiple semantic landmarks in a prescribed order. This
mismatch leaves **intent-driven, multi-stage navigation**
insufficiently characterized. We introduce **ErrandVLN**, a benchmark
that pairs continuous trajectories with diverse role-conditioned requests,
allowing the same ordered landmark requirements to be expressed across varied
activity contexts. Constructed on InteriorGS environments in NVIDIA Isaac Sim
through an automated semantic-geometric pipeline, ErrandVLN comprises 913
scenes, 65,134 unique physical trajectories, and 502,233 instructions, with
evaluation splits for unseen scenes, novel trajectory compositions, and unseen
instruction styles. To address compounding errors over ordered stages, we
propose **VLN-JEPA**: a continuous trajectory proposer (TP-Flow)
generates candidate motions, an action-conditioned latent world model
(NaviLat) predicts future latent states under these candidate motions without
decoding future observations, and a compact 2.35B VLM controller uses these
predictions together with the instruction and observation history to generate
the next executable action. On ErrandVLN Test Scene-Unseen, VLN-JEPA achieves superior performance across multi-stage 
milestone completion (20.5\% GCR, 16.1\% GC-SPL, 29.2\% OSR) and competitive 
task success (12.6\% SR), while substantially reducing physical collisions by 
40\% compared with DualVLN. On a single NVIDIA RTX 4090,
it achieves 94\,ms per policy-inference step (10.7 FPS) and 5.3 FPS in complete
closed-loop execution.

## 84. EV-JEPA: Elastic V-JEPA for Any Device and Cross-Device Inference

**Keywords:** JEPA, video representations, distributed neural networks, elastic networks, nested networks, slimmable networks

[Main paper PDF](https://openreview.net/pdf?id=nDx8xoL0jB)

Foundation models like V-JEPA are increasingly deployed across a heterogeneous edge–cloud continuum spanning smart glasses, phones, robots, and servers. Yet, they are typically trained as rigid, fixed-capacity networks bound to one device, supporting neither reconfigurable compute budgets nor collaborative execution. Existing approaches address only one axis at a time: slimmable and NAS-based methods provide width elasticity but assume single-device inference, whereas split-computing methods enable cross-device collaboration only for fixed partitions and static capacities. We introduce Elastic V-JEPA (EV-JEPA), a single model trained once and deployable everywhere along the continuum. Its width is reconfigurable, and it is natively partitionable across heterogeneous devices. 
 At its core is Transition-Aware Triplet Training (T3): at every step, a pair of widths is trained both standalone and as endpoints of a hybrid configuration that transitions between them in a split layer, so that the same weights serve the execution of single-width and cross-width. Across various benchmarks, EV-JEPA falls within 1\% of independently trained baselines while improving over previous elastic training approaches by up to 11\%. Cross-device hybrid execution recovers to within 2\% of the highest-capacity standalone model and supports many-to-one, any-to-any, and variable-split configurations. 
 Finally, we show that the elastic principle extends beyond the backbone to an elastic token compression mechanism that exposes controllable trade-offs among on-device computation, latency, and accuracy.

## 85. EventCone-WM: Counterfactual Event Cones for Reliable Action-Conditioned Latent Planning

**Keywords:** World Models; Latent Planning

[Main paper PDF](https://openreview.net/pdf?id=EhGzm436a4)

Action-conditioned world models can predict plausible futures while propagating an action's effects to entities it cannot physically reach. We introduce EventCone-WM, which contrasts candidate and matched-control latent rollouts, decodes entity-event relations, and propagates them into a finite-horizon event cone. Outside-cone invariance, inside-cone effect separation, paired-action ranking, and a planning penalty discourage unsupported changes while preserving goal-relevant interactions. The evaluation spans three manipulation environments under visual, physical, and occlusion shifts, jointly examining closed-loop success, cone false-positive rate (FPR), collisions, and latency. EventCone-WM is shown at 75.9% Physics-OOD success versus 57.8% for JEPA-WM; across the full comparison, cone FPR is 11.1% versus 24.5%, collision rate is 8.7% versus 14.9%, and per-action planning latency is 83.6 versus 68.4 ms. These results demonstrate that EventCone-WM substantially reduces physically implausible interactions with only a modest computational overhead, maintaining real-time viability for closed-loop control.

## 86. EVEWorld: Physical Evolution Supervision for Embodied World Models

**Keywords:** World Models; Embodied AI;Video Generation

[Main paper PDF](https://openreview.net/pdf?id=DQRKuAr4cO)

Embodied world models enable scalable simulation of embodied interactions for robot learning. However, existing models are prone to Model Laziness, as they focus on visual fidelity at the expense of physical reasoning and lack process-level supervision over the temporal dynamics of manipulated objects. In this work, we propose EVEWorld, a physical evolution-supervision framework for physically consistent target evolution. EVEWorld consists of two components: Instance-Guided Restoration (IGR) and Temporal Instance Alignment (TIA). First, IGR promotes instance consistency through restoration supervision. Second, TIA promotes cross-frame consistency by aligning target instances across adjacent frames. We further introduce the Model Laziness Rate (MLR), a metric that measures persistent violations of instance consistency in generated trajectories. Extensive experiments on DreamGenBench, EWMBench, and PBench demonstrate the effectiveness of EVEWorld, notably achieving an 87.5% reduction in MLR compared with GigaWorld-0. On the WorldArena 2.0 Track 1 leaderboard, our model ranks 6th in JEPA Similarity and 17th overall, which further validates the performance of our evolution supervision strategy. Source code is available at an anonymous link: https://anonymous.4open.science/r/EVEWorld-release-C8B4.

## 87. Exploring Temporal Context-Aware Physical Grounding in Latent World Models

**Keywords:** world model, joint‑embedding predictive architecture, physical state grounding

[Main paper PDF](https://openreview.net/pdf?id=IiBRfLm6Vy)

Learning latent dynamics is fundamental to building action-conditioned world models for planning. Among existing families, Joint Embedding Predictive Architectures (JEPAs) offer a natural framework by modeling transitions directly in latent space rather than at the pixel level. However, two issues remain in JEPA-based world models: (i) physical grounding lacks explicit aggregation of temporal context and (ii) action planning always overly relies on generic sampling distributions. To this end, we propose $\mathcal{G}$-JEPA, which incorporates temporal context into physical grounding for latent world models and couples the learned models with prior-guided action planning. Specifically, during learning, we incorporate a shared causal temporal module that aggregates temporal context within observation and prediction sequences under physical state supervision, grounding both in task-relevant physical states. When planning, we further introduce action inference through stepwise conditioning of a generative action distribution on the current and goal latent representations together with their evolving discrepancy, yielding anchored proposals that guide model-based online refinement. Together, physical state supervision guides temporal representation learning, while the action prior guides search through the learned world model. Experiments demonstrate improved planning performance on manipulation tasks, including tasks with increasing temporal separation between initial and goal observations. Code will be made publicly available.

## 88. Extracting Behavior from Frozen Latent World Models: Experience-Anchored Proposals with Offline Verifier Alignment

**Keywords:** latent world models, model-based planning, offline reinforcement learning, JEPA, flow matching, cross-entropy method, goal-conditioned control

[Main paper PDF](https://openreview.net/pdf?id=91bWZP39CG)

Planning in frozen latent world models is usually performed with the
cross-entropy method (CEM). CEM is memoryless: every replan starts a new
Gaussian search that uses none of the experience the model was trained
on. Planning is therefore slow, 2.1s per replan in our setup, and
uneven, from 67\% to 91\% success across four suites.
We replace this search with a proposer that learns from the model's
experience. A generative proposer is behavior-cloned from the corpus.
At plan time it generates candidates and the model selects among them
by imagined latent distance to the goal. We then improve the proposer
by offline reinforcement learning with this imagined distance as the
reward, and analytic relative-position constraints can be added at plan
time without retraining. We recommend a rectified-flow proposer, the
LeWM Action Proposer (LeAP), improved by World-model
Advantage-weighted Verifier Regression (WAVR), which needs no
trust-region term.
With 256 candidates, a replan takes 24ms and $1/35$ of CEM's model
evaluations, about 90 times faster per planning call. On Cube, TwoRoom
and PushT, whose corpora contain directed or expert behavior, the
behavior-cloned proposer alone reaches 99.9\%, 98.0\% and 96.2\%,
against 67.0\%, 88.8\% and 91.4\% for CEM. On Reacher, whose corpus is
random behavior, WAVR raises success from 76.1\% to 97.3\%, against
84.3\% for CEM. With a keep-out region added on Cube at plan time, the
planner reaches the goal without entering it in 91.6\% of episodes,
against 55.9\% for CEM.

## 89. Fast LeWorldModel

**Keywords:** latent world model, action prefix prediction

[Main paper PDF](https://openreview.net/pdf?id=y66MjOTBw3)

Joint-Embedding Predictive Architectures (JEPAs), including recent LeWorldModel (LeWM), have become a promising foundation for reconstruction-free visual world models. For visual planning, however, LeWM evaluates candidate action sequences by repeatedly applying a local one-step latent transition model. This autoregressive rollout makes planning computationally expensive and causes accumulated latent prediction errors as the horizon grows. We propose We propose Fast LeWorld-Model (Fast-LeWM), a fast latent world model that replaces repeated local rollout with action-prefix prediction. Given the current latent state and a candidate action sequence, Fast-LeWM encodes its prefixes and predicts the future latents reached after executing those prefixes in parallel. By making action prefixes the basic prediction unit, Fast-LeWM directly models action effects accumulated over different horizons. This prefix-level supervision forces Training these multi-horizon predictions jointly encourages the model to learn how states continuously evolve under different action prefixes, rather than only fitting one-step state transitions. During planning, the predictor uses the prefix from the encoded action sequence to evaluate the corresponding future latent directly, without explicitly rolling through each intermediate imagined state. Across multiple tasks, Fast-LeWM improves average success over LeWM while substantially reducing planning time. It also achieves lower open-loop latent prediction loss, with errors growing considerably more slowly as the rollout horizon increases.

## 90. Feasible Actions, Misleading Rollouts: Diagnosing Latent World Model Planning

**Keywords:** Visual world models; Model-based planning; Model predictive control; Goal-conditioned control; Planning evaluation

[Main paper PDF](https://openreview.net/pdf?id=HHiFzgMMJm)

Prediction error, goal-cost disagreement, and actuator imprecision require different evidence in latent world-model planning. We study frozen planners by executing fixed action banks and comparing predicted cost, actual-outcome cost, and physical error. On ten V-JEPA2-AC/RoboCasa sources and ten LeWM/PushT tasks, predicted selection incurs mean range-normalized actual-cost regrets of 19.2\% and 6.5\%, respectively, while outperforming within-bank uniform selection. Seven LeWM banks select the actual-cost minimum; the distinct banks do not support a model ranking. We then test intermediate known-state feedback in DINO-WM. After a common actuator finish, feedback reduces composite object error relative to native planning, endpoint-only correction, and first-patch consistency control by 0.132, 0.090, and 0.098 on 32 generated tasks. Coarse-success non-inferiority remains unestablished. A finite-history analysis characterizes the learned state-error paths omitted from a shared comparison bound, without guaranteeing smaller realized errors. Separately, a 16-task LeWM terminal-constraint test does not confirm an object benefit. Together, the results show why candidate-level cost regret, physical outcomes, and actuator precision must be evaluated separately.

## 91. Filter Before Adapting Latent World Models

**Keywords:** latent world models, JEPA, test-time adaptation, Bayesian filtering, Kalman filter

[Main paper PDF](https://openreview.net/pdf?id=aTIl9ouw7W)

Test-time adaptation helps latent world models remain effective under deployment shift. However, direct adaptation treats every prediction--observation mismatch as a learning signal, even when the discrepancy arises from a transiently unreliable observation. Such erroneous updates can persist after the observation recovers, degrading subsequent prediction and planning. We formulate this problem as latent residual attribution, which seeks to recover the clean-target prediction-side residual from an observed discrepancy that also contains observation-side error. We introduce BayesJEPA, which estimates prediction-side and observation-side uncertainty and uses their relative reliability to filter the residual before adapting the predictor. Under second-moment assumptions, this uncertainty-weighted rule is optimal among linear attribution rules; under Gaussian uncertainty, it becomes the posterior mean with a Kalman-style gain and induces the posterior-optimal estimate of the corresponding clean-target adaptation gradient. On PointMaze, BayesJEPA improves recovery of the clean-target residual, reduces harmful updates and parameter drift under transient visual corruption, and preserves useful adaptation under persistent dynamics shifts. Under mixed dynamics and observation shifts, it further improves planning over direct adaptation. Together, our theoretical and empirical results establish filtering before adapting as a principled and effective approach to robust test-time adaptation of latent world models.

## 92. FlexiWorld: Learning and Planning via Flexible Action Chunks Across Multiple Time Scales

**Keywords:** joint-embedding predictive architectures, multi-horizon learning, long-horizon control

[Main paper PDF](https://openreview.net/pdf?id=qoepaU1QMf)

Latent world models predict future states for goal-directed planning using action chunks spanning multiple primitive steps. Existing methods typically use fixed-length chunks and either omit goal-conditioned action generation or limit their supervision to short goal spans. We introduce FlexiWorld, a JEPA-based world model that combines mixed-span goal supervision with variable-length action chunks to improve long-horizon control. During training, we sample varying goal spans and randomly partition the actions into variable-length chunks. We jointly train the world model with a causal action encoder that embeds variable-length chunks and an autoregressive actor that generates primitive actions sequentially. Student Forcing reduces exposure bias by training on generated action prefixes. For planning, Actor-Residual Cross-Entropy Method (ARCEM) combines action-residual search with within-chunk autoregressive feedback and chunk-boundary latent prediction. Across four benchmarks and goal distances, FlexiWorld with ARCEM achieves 89.29% mean success, compared with 83.98% for the strongest baseline. PushT ablations show improved direct control from mixed-span supervision, variable-length chunks, and Student Forcing. Without retraining, FlexiWorld supports different planning chunk lengths: longer chunks accelerate ARCEM by approximately 1.3× on average while maintaining comparable average success.

## 93. Flow-JEPA: Robust Latent Dynamics for JEPA World Models via Flow Matching

**Keywords:** World Models, Joint-Embedding Predictive Architectures, Flow Matching

[Main paper PDF](https://openreview.net/pdf?id=O7wBqVHiqt)

Joint-Embedding Predictive Architectures (JEPAs) provide a powerful framework for latent world modeling and planning in a reconstruction-free manner. Although numerous JEPA-based approaches have been proposed to mitigate representation collapse, our experiments on localized, out-of-distribution visual noise reveal that performance degradation remains pronounced and unresolved. We propose Flow-JEPA (F-JEPA), a flow-based latent dynamics model that jointly generates a sequence of future latent states conditioned on the current observation and actions. A Gaussian distribution serves as the flow source, exposing the vector field to perturbed latent trajectories as it learns to transport them toward clean future representations. This formulation retains the reconstruction-free JEPA framework while switching from pointwise transition regression to stochastic trajectory-level prediction. F-JEPA raises mean success from $86$\% to $92$\% under clean observations and from $67$\% to $86$\% under noisy conditions. Further evaluations over varying perturbation severity and inference settings show that the performance advantage persists across a broad range of conditions. These results suggest that conditional flow matching provides a promising alternative to deterministic autoregressive prediction as a dynamics formulation in JEPA world models.

## 94. From World States to Videos: V-JEPA for Driving Scene Generation

**Keywords:** V-JEPA, video generation, world-state prediction, driving-scene generation, predictive representation learning, latent video diffusion

[Main paper PDF](https://openreview.net/pdf?id=NtZ1RXkwQU)

Predicting a driving video is not only a problem of extending pixels: the generator must decide how traffic, road geometry, and camera motion evolve after the last observed frame. We ask whether a learned world state can make that evolution explicit. A compact Transformer predicts a future-oriented V-JEPA state from observed video, and a latent-video generator uses the state to synthesize the future. Neither future images nor motion metadata are available at inference. Across 130 unseen nuScenes scenes, predicted states improve a fixed semantic–geometric–motion measure by 6.88% over context-only generation in every seed, retaining more than 95% of the benefit of a teacher state extracted from the logged future. A matched predictive pathway built on VideoMAE uses the same predictor and generator budgets, yet predicted V-JEPA states perform 4.24% better. The gain spans all evaluator components and aggregation rules. Motion readouts explain why this is plausible: V-JEPA exposes temporal dynamics more clearly than VideoMAE on two scene cohorts. Oracle-conditioning experiments then show that the generator uses this information and degrades when state and scene no longer correspond. Together, these results support a context-to-state-to-video path in which predicted world states guide future-video synthesis.

## 95. Frozen in a Frame: The Velocity Blind Spot in JEPA World Models

**Keywords:** world models, joint-embedding predictive architecture, identifiability, self-supervised representation learning, video prediction, latent dynamics, velocity estimation, model-based planning, recurrent state-space models

[Main paper PDF](https://openreview.net/pdf?id=XgB7jpGAnn)

Joint-embedding predictive architectures for world modeling train an encoder so that a predictor can map a current frame embedding and an action to the embedding of the next frame. The target for this prediction always comes from a single rendered frame. We show that this choice has a structural blind spot. Every renderer without motion blur is instantaneous: it draws a scene from its configuration alone and leaves no trace of how fast that configuration is changing. So a single-frame embedding is a deterministic function of configuration alone, and it carries no information about velocity. This holds for the optimal predictor under any encoder, however large, including the official released LeWM weights. We confirm this on official checkpoints across four real benchmarks, PushT, Reacher, Cube, and TwoRoom, where every linear velocity probe sits at or below its own chance floor while position probes reach $R^2 \approx 0.95$. We then introduce RateIdent, a three-stage diagnostic protocol, and TI-JEPA, a lightweight fix that splits the latent into a pose code and an explicit finite-difference motion code and predicts both. Across three physically grounded environments, TI-JEPA gives a statistically significant, seed-robust improvement on a stop-at-goal planning task over a matched-memory baseline, for example a 55% lower final distance on Pendulum ($p=3.2\times10^{-10}$) and 64% lower on CartPole ($p=5.1\times10^{-15}$). We reproduce the theory's central prediction at official ViT-Tiny plus AdaLN-transformer scale on two environments, then push the same recipe onto real dm_control Reacher photographs trained entirely from scratch, where TI-JEPA's kill-experiment branch separation exceeds the memory-having baseline's by roughly $38\times$, the largest margin in the paper. We also compare directly against a recurrent RSSM-style predictor at the same footprint. Its opaque hidden state matches or beats TI-JEPA's raw rollout accuracy on two of three environments, but it cannot be probed for pose and motion separately the way TI-JEPA's explicit split can, and it loses outright on the environment with the most coupled dynamics. Together, a checkable formal argument and six evaluated environments show that single-frame targets are the wrong object to predict when velocity matters, and that a small, interpretable structural change fixes it without any privileged supervision.

## 96. Gaze World Model

**Keywords:** World Prediction Model for Gaze, Gaze shift detection

[Main paper PDF](https://openreview.net/pdf?id=qn2fIgVLER)

Human gaze provides a social cue between people and their surroundings, revealing where their visual attention is directed. Modeling this cue over time requires understanding where a person is looking in the observed scene and anticipating how their gaze will change as the scene unfolds. World models connect an understanding of the current environment with predictions of how it will evolve. Inspired by this perspective, we introduce the Gaze World Model (GWM), which unifies observed gaze understanding and future forecasting through latent scene prediction. Given a video clip and the person’s head box, GWM uses V-JEPA 2.1 and a temporal trunk to encode scene context and person-specific cues. From this representation, it estimates gaze locations and detects gaze shifts in the observed clip. It further forecasts future gaze locations and shifts using latent scene features predicted by the world predictor. To evaluate both current gaze understanding and future forecasting, we augment VideoAttentionTarget and ChildPlay with gaze-shift annotations, complementing spatial localization with event-level evaluation of person-involving target transitions. GWM achieves state-of-the-art performance on observed gaze-target estimation and shift detection on the evaluated benchmarks, and outperforms the compared baselines on future gaze localization and shift forecasting.

## 97. Generative Uncertainty as a Self-supervised Signal for Semantic Similarity Learning

**Keywords:** similarity learning, generative uncertainty

[Main paper PDF](https://openreview.net/pdf?id=yFWwAW9HzX)

Evaluating semantic similarity between videos is a fundamental challenge in computer vision, essential for tasks ranging from out-of-distribution (OOD) detection to video retrieval. However, defining and labeling video similarity is notoriously difficult and expensive due to the complex spatio-temporal nature. In this paper, we propose a novel self-supervised approach that leverages generative uncertainty from text-to-video (T2V) diffusion models to learn semantic similarity without human annotations. Our method is based on the observation that T2V models produce consistent outputs for familiar concepts but exhibit high variance and uncertainty when prompted with specialized concepts. We utilize this behavior to identify stable semantic features within existing pretrained representations, such as VideoMAE and V-JEPA. Specifically, we learn a mask over these embeddings using purely generated data, encouraging the model to retain features that remain consistent across generations of general concepts while discarding those associated with generative noise or uncertainty. Experimental results across three key tasks demonstrate that our learned feature subspaces consistently outperform original pretrained features and baseline feature selection methods.

## 98. Geometry Is Not Enough: Symplectic Structure and Noise Robustness in JEPA World Models for Beam Dynamics

**Keywords:** Joint-Embedding Predictive Architectures; symplectic structure preservation; learned surrogates; beam dynamics; particle accelerators

[Main paper PDF](https://openreview.net/pdf?id=CfWJV4futd)

Joint-Embedding Predictive Architectures (JEPAs) learn dynamics in latent space and promise
cheaper, noise-robust learning-based surrogates for physical simulation.
Without a reconstruction loss anchoring the representation, however, the encoder and predictor are free to settle on latents that are mutually consistent with little knowledge about the system dynamics.
But whether enforcing that structure in latent space improves performance remains poorly understood.
We address this by studying JEPAs on a system whose latent dynamics have a known target: longitudinal beam dynamics, whose one-turn map is a symplectic Hamiltonian flow, and use that structure as a reference for the learned latent.
Our contributions are threefold: we examine whether enforcing symplectic structure on the latent predictor restores the geometry of the true one-turn map and improves accuracy, benchmark JEPA against reconstruction-based and pixel-space surrogates in error and cost, and assess its robustness to noise and distribution shift.
On $23{,}101$ BLonD simulations of the FNAL Recycler, we find that symplectic predictors restore the geometry of the one-turn map but only direct map parameterisations improve accuracy, and that JEPA trains $2.1\times$--$2.5\times$ faster, and filters input noise, though reconstruction retains the lowest error.
Our findings align with prior work on transfer-operator and latent Hamiltonian learning and point to encoder objectives and training regimes that would make JEPA a reliable surrogate for complex physical dynamics.

## 99. GLAM: TRAINING A LATENT WORLD MODEL OVER GLOBAL SPATIOTEMPORAL MEMORY FOR ACTIVE EXPLORATION AND NAVIGATION

**Keywords:** world model, embodied ai, navigation, cogtive-map

[Main paper PDF](https://openreview.net/pdf?id=9AdP14hXLB)

Active exploration and semantic navigation require an embodied agent to build memory from partial observations, predict how the evolution of observed spatial memory may support future motion, and convert that prediction into actionable plans. We present GLAM, a goal-conditioned latent world model trained over global spatiotemporal memory, and GLAM NAV, the complete navigation system built around it. Given historical map tokens, a navigation goal, and the current robot pose, GLAM jointly predicts future map representations and robot-centric waypoint latents, allowing future spatial context and navigation intent to be inferred in a shared representation space. The model follows a JEPA-like latent prediction paradigm, operates directly on map-level latent tokens rather than RGB reconstruction, and uses a pretrained waypoint encoder–decoder to supervise and decode navigation plans within GLAM NAV. Training data are collected in Habitat over HM3D v0.2 by sampling oracle-guided ObjectNav trajectories and their map transitions. On the full HM3D-Semantics v0.2 ObjectNav benchmark, GLAM NAV achieves a state-of-the-art success rate of 82.30% with 34.00% success weighted by path length.

## 100. GRPO-JEPA: Mitigating Semantic Drift in GRPO via Joint Embedding Predictive Architecture

**Keywords:** large language models, joint-embedding predictive architecture, GRPO, reinforcement learning, representation learning, semantic drift, RL post-training

[Main paper PDF](https://openreview.net/pdf?id=yi8a39AfOh)

Group Relative Policy Optimization (GRPO) is a standard method for RL post-training of large language models, yet its objective stays in the output space: neither the policy gradient nor the token-level KL term observes representation-space dynamics. This blind spot lets semantic drift occur while the loss stays low. We present GRPO-JEPA, which brings the Joint-Embedding Predictive Architecture (JEPA) into LLM RL post-training as explicit representation-space supervision: an advantage-weighted InfoNCE signal turns GRPO's group-sampled completions into multi-view data, propagating scalar reward signals into representation-space alignment. This JEPA supervision signal enters training in two ways: (i) Method A (direct regularization) adds it to the GRPO objective, and (ii) Method B (soft modulation) converts it into a dynamic controller of the KL coefficient. Across four benchmarks (Spider, GSM8K, HellaSwag, and Yelp) and five models from four families (Qwen, OLMo, SmolLM, and Gemma), GRPO-JEPA improves on standard GRPO on all $20$ model--dataset pairs: average gains are $5.9$ points for Method A and $4.6$ for Method B. It also surpasses recent GRPO variants (SAPO, BNPO, and DAPO) on every benchmark for Method A and on average for Method B. Representation-space predictive consistency offers a usable JEPA supervision signal for RL post-training.

## 101. GSJEPA: Self-Supervised Approach to Learning Gaussian Splat Representations Using Joint Embedding Predictive Architecture

**Keywords:** Self-supervised Learning, Gaussian Splatting, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=RchUozeXVJ)

We introduce a self-supervised representation learning framework for 3D objects represented as Gaussian Splats based on Joint Embedding Predictive Architectures (JEPA). GS-JEPA represents individual Gaussian primitives as nodes in a local graph and learns their representations through latent prediction, explicitly modeling geometric and appearance-aware relationships between primitives. To isolate the effect of relational modeling, we additionally consider a point-based formulation that treats Gaussian primitives as an unordered set and serves as a baseline. Both formulations learn representations directly from Gaussian splat objects without relying on reconstruction objectives. Across classification and segmentation benchmarks, predictive learning outperforms the reconstruction-based Gaussian Masked Autoencoder. Notably, despite being pretrained exclusively on synthetic objects, the proposed JEPA-based approaches generalize effectively to real reconstructed Gaussian splat data. On MACGS classification, the point-based and graph-based approaches achieve $95.76\%$ and $94.60\%$ accuracy, respectively. On ShapeNetPart segmentation, the graph-based model achieves an mIoU of $85.15\%$, demonstrating the potential benefits of explicit relational modeling. These results establish JEPA-based predictive learning as an effective approach for transferable Gaussian splat representations and highlight relational modeling as a promising direction for 3D Gaussian representation learning.

## 102. H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning

**Keywords:** World Model, JEPA, Planning, SSL, Hierarchical world models

[Main paper PDF](https://openreview.net/pdf?id=HfeFkcLX32)

Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with multiple horizons in one shared latent space. We introduce H-JEPA, an end-to-end recipe for training a hierarchy of action-conditioned JEPAs in which each level predicts farther ahead in its own learned latent space. Planning proceeds top-down: the top level optimizes progress toward the goal, and each level's predictions become subgoals for the planner below it. When factors in the data evolve at separated timescales, higher levels discard fast, unpredictable detail and retain slower task-relevant state. Across four simulated navigation and manipulation environments, hierarchical planning improves over a flat JEPA; on Visual AntMaze, a three-level hierarchy raises success from 18% to 73% at matched compute. Ablations attribute these gains to both temporal decomposition and higher-level goal representations. With inverse-dynamics supervision, the approach extends to diverse real-robot videos from DROID, where hierarchy improves offline planning fidelity at lower planner compute.

## 103. Hamiltonian JEPA: Action-Conditioned World Models with an Inherited Isotropic Control State

**Keywords:** world models, vla, robotics

[Main paper PDF](https://openreview.net/pdf?id=96zH0yxuo7)

Planning from pixels needs more than a latent space that is stable and predictable.
The state the planner scores must also be organized by how actions move the
system. Joint-embedding predictive architectures (JEPAs) avoid pixel reconstruc-
tion by predicting future representations, but existing action-conditioned JEPAs
ask one embedding to serve both perception and control. We introduce H-JEPA,
which separates the two. A wide perceptual code is regularized toward a well-
scaled isotropic geometry with a Bures-Wasserstein prior, and a fixed orthonor-
mal slice of that code is the control state, which inherits the code’s covariance
without any objective of its own. The state evolves under phase-conditioned dis-
sipative port-Hamiltonian dynamics whose input port has orthonormal columns.
Port-inverse consistency (PIC) reads the executed action back through the trans-
pose of that port. We show that this readout is exactly the rollout error projected
onto the port directions, so PIC is a parameter-free reweighting of prediction error
and not an auxiliary action decoder. Untying the readout from the port breaks this
identity and loses half of the gain. H-JEPA matches or exceeds reconstruction-free
baselines, including the action-decoding Delta-JEPA, on four pixel-based control
benchmarks after at most 10 training epochs, and its largest gain is on OGB-Cube
(91.9 against 79.3 percent). Ablations on PushT and OGB-Cube separate the con-
tributions of the structured predictor, PIC, the prediction horizon, the state rank,
and the anti-collapse prior.

## 104. Hamiltonian JEPA: Symplectic Latent Dynamics for World Models

**Keywords:** world models, joint-embedding predictive architecture, JEPA, Hamiltonian dynamics, physics-informed learning, self-supervised representation learning, and symplectic integration.

[Main paper PDF](https://openreview.net/pdf?id=Z7JKlRfoZ1)

Joint-embedding predictive architectures (JEPAs) learn world models directly in latent space, but unconstrained autoregressive predictors may contract the latent distribution over long rollouts. We introduce Hamiltonian JEPA (LeHami), which replaces the standard predictor with an action-conditioned Hamiltonian flow over a structured latent state $(\mathbf{q}, \mathbf{p})$ integrated using an exactly symplectic leapfrog step. This construction preserves phase-space volume at every rollout step and rules out uniform contraction, asymptotically stable fixed points, and merging of distinct latent states, independently of the learned parameters or action sequence. We obtain the momentum-like component from temporal derivatives of the learned position-like representation, providing an explicit second-order state for prediction and control. On conservative and actuated visual pendulum environments, LeHami substantially improves long-horizon velocity prediction over an unconstrained JEPA world model and empirically maintains constant latent volume where the baseline contracts. The learned flow also supports accurate integration at unseen sub-frame step sizes and numerical time reversal. These results show how geometric structure can provide inference-time guarantees that are complementary to representation regularization in latent world models.
Code for LeHami is available at https://anonymous.4open.science/r/hamiltonian-jepa-7F08.

## 105. HEART-JEPA: LEARNING CROSS-VIEW REPRESEN- TATIONS FOR CARDIAC MRI WITH JOINT-EMBEDDING PREDICTIVE ARCHITECTURES

**Keywords:** Cardiac magnetic resonance imaging; Self-supervised learning; Cross-view representation learning; Joint-embedding predictive architecture; Masked latent prediction; Ventricular function estimation.

[Main paper PDF](https://openreview.net/pdf?id=OeZxEjBA6G)

Cine cardiac magnetic resonance imaging (CMR) captures the same heart from
complementary anatomical views. Learning representations that transfer between
these views is a central challenge for reusable cardiac prediction. We introduce
HEART-JEPA, a cross-view joint-embedding predictive architecture that predicts
masked latent features across anatomical planes without spatially matched patches.
Pretrained on 39,992 UK Biobank participants, HEART-JEPA achieves a crossview structural-transfer R2 of 0.48 in 15,935 participants absent from pretraining,
without target-view refitting or recalibration. Matched ablation studies show substantial gains over same-view pretraining and stronger cardiac phenotype prediction
and structural and functional transfer than cross-view contrastive learning. In a
separate ventricular-function benchmark, supervised linear probes fitted to concatenated frozen features from all three views achieve the lowest mean LVEF MAE
among the seven evaluated models (3.19 percentage points), with competitive
RVEF performance. These findings establish cross-view latent prediction as an
effective approach to cardiac representation learning and motivate its extension to
videos acquired from complementary, spatially unaligned views

## 106. HEPA: A Self-Supervised Horizon-Conditioned Event Predictive Architecture for Time Series

**Keywords:** time series, self-supervised learning, joint-embedding predictive architecture, event prediction, representation learning, label efficiency, transfer learning, predictive maintenance

[Main paper PDF](https://openreview.net/pdf?id=eSOioRqbC1)

Critical events in multivariate time series, from turbine failures to cardiac arrhythmias, demand
accurate prediction, yet labeled data is scarce because such events are rare and costly to annotate.
We introduce HEPA (Horizon-conditioned Event Predictive Architecture), built on two key principles.
First, a causal Transformer encoder is pretrained via a Joint-Embedding Predictive Architecture
(JEPA): a horizon-conditioned predictor learns to forecast future representations rather than future
values, encouraging the encoder to capture predictable temporal dynamics from unlabeled data alone.
Second, we freeze the encoder and finetune only the predictor toward the target event, producing a
monotonic survival cumulative distribution function (CDF) over horizons. With fixed architecture and
optimiser hyperparameters across all benchmarks, HEPA handles water contamination, cyberattack
detection, volatility regimes, and eight further event types across 11 domains, matching or
exceeding leading time-series architectures including PatchTST, iTransformer, MAE, and Chronos-2 on
at least 10 of 14 benchmarks each, with an order of magnitude fewer tuned parameters and, on
lifecycle datasets, an order of magnitude less labeled data.

## 107. How Far Can Latent World Models Imagine Ahead? Probing the Capabilities and Limits of Latent Planning

**Keywords:** World-models, Latent world models, video self-supervised learning, Model predictive control, JEPA, Planning, Vision-language-action models.

[Main paper PDF](https://openreview.net/pdf?id=u8OFXbfqS1)

World models offer a promising way to help robots understand how the physical world evolves and plan complex behaviours through imagination. Yet existing studies mainly demonstrate what these models can accomplish, leaving unclear when their predictions remain useful for planning and where they fail. We study this question using action-conditioned predictors built on five frozen self-supervised visual backbones: V-JEPA 2, V-JEPA 2.1, VideoMAEv2, VideoPrism, and DINOv2. We use frozen backbones to test representations intended to transfer across environments. We evaluate these models on diverse Meta-World manipulation tasks and real-robot interactions from BridgeData V2. We find that a world model guides action selection reliably only when the goal lies within, or slightly beyond, the trajectory it imagines during planning. With five-step rollouts, the length the predictor was trained on, the world model ranks actions reliably only for targets five to ten control steps ahead, whereas task goals lie 16 to 53 steps away. Neither an 81-fold larger predictor nor longer-rollout training extends this range; the encoder affects both range and closed-loop success, with V-JEPA 2.1 performing most consistently. More fundamentally, the limit persists under perfect prediction: using the real simulator, success falls from 92\% to 41\% as the target moves from five to twenty steps ahead of a five-step rollout (Figure 1). Planning therefore requires either longer imagined trajectories or closer subgoals. For distant goals, pure imagination succeeds in 23\% of episodes, planning with feedback (MPC) raises success to 30\%, imagining as far as the goal to 47\%, and nearby expert subgoals to 76\%. Used within its plannable range, a world model can also improve a vision-language-action (VLA) policy: choosing among eight actions the VLA proposes raises its success from 65\% to 77\% across 16 different tasks.

## 108. How Latent Transition Geometry Matters for Planning in World Models

**Keywords:** World Models, JEPA, Transition Geometry, Planning, Curvature Regularization

[Main paper PDF](https://openreview.net/pdf?id=FNjhZqkTMK)

World models support planning by predicting how the environment will evolve under candidate actions. In latent world models, the model is typically trained for one-step prediction, while planning typically requires repeatedly composing the learned transitions to compare candidate futures over a multi-step horizon. However, one-step latent predictive accuracy does not automatically translate to planning success. This raises a question: *what geometric properties of the learned one-step transition are useful for multi-step planning?* We study this question through an action-conditioned *transition-field* view of latent dynamics, using curvature regularization as a controlled geometric intervention. Across four continuous-control tasks, appropriately tuned regularization improves planning, while excessive regularization can sometimes be detrimental. To understand this observation, we decompose the transition field into an affine component and a residual non-affine component. We find that the curvature intervention reduces the field's sensitivity to action primarily by contracting its non-affine component. These sensitivity reductions propagate through the rollout, blurring the distinction among candidate futures and, in turn, altering the planner's decisions. Together, these results suggest that useful latent dynamics should retain sufficient action-induced predictive differences through multi-step propagation to keep candidate futures distinguishable to the planner.

## 109. How Many Futures Are Enough? Redundancy-Aware Effective Multimodality for End-to-End Autonomous Driving

**Keywords:** End-to-End Autonomous Driving, Multimodal Planning, Effective Multimodality, Trajectory Redundancy, Action-Conditioned Predictive Representations, Latent World Models, Joint-Embedding Predictive Architectures, Multimodal Decision Making

[Main paper PDF](https://openreview.net/pdf?id=KlfVWfhiKc)

Multimodal end-to-end planners can generate multiple plausible trajectories for the same driving scene, yet a larger set of candidates does not necessarily represent a larger set of distinct futures. Numerically different trajectories may repeatedly describe closely related driving decisions and induce similar future evolution, resulting in multimodal redundancy. We introduce effective multimodality to distinguish the nominal number of generated trajectories from the effective future structure represented by the candidate set.

We propose AMC-Drive (Action-conditioned Multimodal Consolidation for Driving), which uses a frozen action-conditioned predictive model to establish candidate-level relations beyond trajectory geometry. AMC-Drive reshapes redundant candidate structure through effective-multimodality calibration and topology-aware redundancy correction, while a cross-mode guard preserves distinct decision modes. The physical output cardinality remains unchanged throughout this process.

On NAVSIM v1, AMC-Drive achieves 93.9 PDMS, establishing a new state of the art among JEPA-based world-model planners. It further reaches 89.2 EPDMS on NAVSIM v2 and obtains a 0.4308 HD-Score on HUGSIM without HUGSIM-specific fine-tuning.

AMC further yields consistent gains across proposal-based, diffusion-based, and flow-matching planners, and transfers to robotic manipulation, demonstrating the broader applicability of redundancy-aware effective multimodality across multimodal decision systems.

## 110. I Act Therefore I Am: When Is JEPA's Action-Conditioning Enough to Learn Causal Mechanisms?

**Keywords:** Joint-embedding predictive architectures, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=IhJYd4Lt0M)

Recent empirical and theoretical advances suggest that joint-embedding predictive architectures (JEPAs) may learn promising representations for action-conditioned prediction of future representations. However, accurate prediction does not, in general, necessarily imply recovery of the underlying causal states that give rise to the observed dynamics. This work investigates when and how JEPAs can recover the underlying causal states from observations. We first introduce a latent variable model, in which high-dimensional observations are generated from latent causal states whose dynamics are governed by action-conditioned transition mechanisms. Based on this formulation, we develop a general information-theoretic objective that combines conditional likelihood maximization for learning transition dynamics with entropy maximization for preserving latent state information. We then establish identifiability conditions under which representations learned by this general objective recover the underlying latent causal states up to component-wise invertible transformations and permutation. One key condition for such identifiability is sufficient action-induced variation in the transition mechanisms. Guided by this finding, we instantiate the general objective with an action-modulated Gaussian additive-noise model, yielding action-modulated JEPA (A-JEPA). Experiments on synthetic environments verify the theoretical findings under the identifiability conditions and robustness to moderate violations, while visual benchmarks demonstrate improved state recovery and transfer to unseen transition mechanisms.

## 111. Innovation SIGReg: Regularizing Transition Residuals for JEPA World Models

**Keywords:** joint-embedding predictive architectures (JEPA), world models, self-supervised representation learning, transition innovations, Gaussian regularization, temporal representation learning, representation learning for planning

[Main paper PDF](https://openreview.net/pdf?id=FPiMD6rQNk)

Gaussian regularization helps joint-embedding predictive architectures
(JEPAs) resist collapse, or loss of distinctions between inputs. Yet the
marginal embedding distribution pooled over trajectories need not be
Gaussian, so enforcing this target can compete with linear state decoding.
\emph{Innovation SIGReg} applies Sketched Isotropic Gaussian Regularization
to persistence-adjusted transition residuals, with a weighted raw-embedding
anchor to constrain location and scale. Linear--Gaussian dynamics motivate
the target: true transition noise can remain Gaussian while state
distributions change, although learned residuals need not recover that
noise. On Reacher, a robot-arm benchmark, mean linear angle-decoding
$R^2$ at temporal stride 64 rises from $0.537\pm0.092$ to
$0.787\pm0.125$ across ten runs per method, and the weakest-coordinate
score rises from $0.217$ to $0.669$. Normalization alone and rescaled
temporal differences do not reproduce these gains at the tested settings.
On Two-Room navigation, unguarded residual regularization produces both
strong and poor planners. An anchor guard improves mean success over
marginal SIGReg by $4.00$ percentage points in a prespecified first-cohort
comparison and by $5.67$ points in an exploratory second-cohort comparison;
fixed and scheduled anchor increases perform comparably in the first.
Detaching current-batch statistics yields $97.50\pm1.00\%$ success
versus $76.00\pm17.39\%$ with differentiable statistics, although three
runs per configuration leave reliability unresolved. A separate Reacher
ablation reverses this comparison: detachment reduces $R^2$ from
$0.421$ to $0.010$, while detached running averages perform best.
These findings show that both the regularization target and the handling
of its statistics matter for downstream decoding and planning.

## 112. Intention First: Latent State Planning with Coupled JEPAs for Visual Navigation

**Keywords:** Image Goal Navigation, World Models, Joint Embedding Predictive Architecture, Latent State Planning, Embodied AI

[Main paper PDF](https://openreview.net/pdf?id=8RcfgtmexP)

Visual navigation requires goal directed planning informed by predictions of environment dynamics. Representative navigation world model methods propose complete action candidates before predicting consequences for selection or search updates. For each candidate, predictions primarily evaluate proposed actions rather than guide its stepwise construction. To this end, we propose InJepa, an intention first planning paradigm centered on latent states. A goal conditioned JEPA proposes latent intentions, and an action conditioned JEPA continually predicts future latent states. Both operate in a shared latent space to align their predictive representations. Within each candidate, predicted consequences feed into the next intention proposal and action inference, forming a closed loop of intention, action, and consequence. This extends the world model's role beyond evaluation to leading candidate construction through latent intentions. We evaluate InJepa through closed loop image goal navigation in Habitat MP3D. The results show effective multistep navigation through intention guided action generation and consequence feedback. Experiments across encoders further support applicability across visual representations. These findings support latent intentions as the central planning object and show that world models can directly guide plan construction through coordinated reasoning about intentions and consequences.

## 113. Invariant Imagination: Learning What Should Not Change the Future in JEPA World Models

**Keywords:** Joint-Embedding Predictive Architecture, World Models, Predictive Robustness, Future-Anchored Learning, Latent Prediction

[Main paper PDF](https://openreview.net/pdf?id=HoCpCXKSOt)

Joint-Embedding Predictive Architectures (JEPAs) support latent prediction
and visual planning, yet strong clean performance does not guarantee
reliable predictions under degraded observations.
We characterize this vulnerability through the predictive brittleness gap,
defined as the increase in prediction error when clean and degraded
contexts are evaluated against the same clean target.
We introduce **FAPI** (Future-Anchored Predictive Invariance),
an adaptation framework that transforms observation-derived contexts
while preserving clean target representations as shared predictive anchors.
This asymmetric design encourages predictive stability without an
explicit pairwise consistency loss or changes to the prediction architecture.
We evaluate **FAPI** on LeWorldModel and Sub-JEPA across PushT,
OGB-Cube, TwoRoom, and DMC under Gaussian noise, patch masking,
and incomplete history.
Under Gaussian noise, \texttt{FAPI+LeWM} improves mean planning success
from 49.5% to 61.5% and reduces the mean brittleness gap by 24.6%;
**FAPI+Sub-JEPA** improves success from 40.0% to 57.0%
with a 43.1% gap reduction.
Both models also improve mean clean success and planning under
patch and history masking.
Extensions to V-JEPA on Something-Something-v2 and I-JEPA on ImageNet
yield lower prediction error and stronger clean--corrupt consistency,
supporting the applicability of future anchoring across
action-conditioned, video, and image prediction settings.

## 114. Investigating Priors for Informed Latent Planning in World Models

**Keywords:** World Models, Latent Planning, Robot control, Generative Modeling, Flow Matching

[Main paper PDF](https://openreview.net/pdf?id=CKXbFR0Ny8)

World models leveraging the Joint Embedding Predictive Architecture (JEPA) are trained to reach goals zero-shot through latent planning. Most work starts from an uninformed Gaussian prior for planning, while a few recent works show the advantage of learned priors. However, the effectiveness of different priors is not thoroughly studied. In this work, we investigate three priors learned by different policy heads, i.e., a deterministic head (Behavior Cloning), a Gaussian one, and a generative one (Flow Matching). We evaluate these priors on success rate together with planning latency across four world model backbones and six robot environments. Our results show that learned priors can improve the success rate by a large margin, e.g., by $40.5$ percentage points in the Cube environment. Moreover, learned priors exhibit computational efficiency, reducing planning time per action sequence by a factor of $2$ to $15$ across all environments, highlighting their practical utility. We show that while no single prior dominates in the short-horizon setting, Flow Matching learns a more robust prior most capable of challenging long-horizon planning tasks. Based on our findings, we distill guidance on choosing between priors, and other algorithm settings such as replanning cadence, to inform the design of future latent planning systems for real-world applications.

## 115. IsoAlign: Isoform-Aware DNA-Protein Alignment via Joint-Embedding Predictive Architectures

**Keywords:** genomic foundation models; joint embedding predictive architecture; multimodal learning; alternative splicing; representation learning

[Main paper PDF](https://openreview.net/pdf?id=q6oLJGwXnF)

Genomic foundation models (GFMs) have emerged as a powerful paradigm for learning DNA sequence representations, yet existing self-supervised pretraining strategies overlook alternative splicing and underperform compared to specialized models. To address this gap, we introduce IsoAlign, a multimodal framework that grounds genomic pretraining in isoform-aware DNA-protein alignment to learn biologically meaningful representations. IsoAlign aligns transcripts to their corresponding protein isoforms, capturing both coding sequences and broader regulatory contexts, using two Joint-Embedding Predictive Architectures (JEPA): DNA-Protein JEPA (DP-JEPA), which predicts protein representations from DNA using contrastive alignment, and Isoform-Masked JEPA (IM-JEPA), which models relationships among alternative isoforms of the same gene through masked protein prediction. We evaluate the learned DNA representations of these architectures across a multi-metric evaluation suite spanning tasks, including the prediction of pathogenicity, fitness, gene expression, and TF binding. Our results demonstrate that isoform-aware cross-modal alignment using JEPA significantly improves functional representations and downstream performance, establishing a promising direction for GFM pretraining.

## 116. JACT: Learning to Act Through Frozen JEPA Dynamics

**Keywords:** jepa

[Main paper PDF](https://openreview.net/pdf?id=iPKGg1MCr3)

Visual world models can guide control through online planning, but repeated pre- diction and search add deployment cost. We propose JACT (JEPA-guided Action- Consequence Training), which moves the use of predictive dynamics into offline policy training. A direct policy acts recursively inside a frozen joint-embedding predictive architecture (JEPA), conditions subsequent decisions on predicted con- sequences, and learns to align the resulting trajectory with observed future em- beddings. Gradients pass through the fixed dynamics into the actor, while local supervision anchors its actions. Deployment uses only the encoder and policy, with no predictive rollout, search, or retrieval. Across 11 visual control settings, JACT combines broad task coverage with efficient direct execution. It achieves 97.25% average success on the four-task comparison, the highest among the listed methods with complete coverage. Controlled ablations and repeated actor training support the value of recursive consequence supervision, while identifying task- dependent limits. JACT offers a simple route from pretrained JEPA dynamics to direct visual control.

## 117. JELI: Joint Modeling of Latent and Input-Space Evidence for Time Series Anomaly Detection

**Keywords:** Time Series Anomaly Detection, Self-supervised Learning, Attention, Transformer

[Main paper PDF](https://openreview.net/pdf?id=d453wM2zWV)

Time-series anomaly detection is a crucial task, commonly formulated as learning characteristic temporal patterns from normal observations and identifying abnormal deviations. Prior work has broadly explored time-series anomaly detection in two spaces, with input-space approaches detecting anomalies through discrepancies between inputs and their reconstructions, while latent-space approaches identify deviations from normal patterns in learned representations. However, the two approaches have largely evolved as separate research directions, even though they can serve complementary roles in anomaly detection. In this paper, we propose **JELI** (**J**oint **E**vidence from **L**atent and **I**nput Spaces), a unified framework that integrates contextual anomaly evidence from both spaces for time-series anomaly detection. Specifically, we first train a JEPA-based backbone to learn contextual representations from surrounding input context and predict target representations at arbitrary temporal positions, forming a normal representation space. Second, we finetune the pretrained backbone for contextual reconstruction with an attention-masking bottleneck that prevents each target from attending to its own representation while preserving alignment with the pretraining objective. Lastly, to bridge the two sources of anomaly evidence, we design a joint-distribution-based scoring method that explicitly accounts for their dependence. Through extensive experiments, we demonstrate that our framework substantially outperforms prior state-of-the-art baselines on the time-series anomaly detection benchmarks.

## 118. JEP-VGP: Learning Vision Graph Prompts via Joint-Embedding Prediction of Prompt Residuals

**Keywords:** Vision Graph Neural Networks, Vision Graph Prompting, Parameter-Efficient Fine-Tuning, Joint-Embedding Prediction, Prompt Residual Prediction, Type-Guided Prompt Learning

[Main paper PDF](https://openreview.net/pdf?id=VoTVlzImoc)

Vision Graph Neural Networks (ViGs) model irregular semantic relationships in images through dynamic visual graphs, while vision graph prompting enables parameter-efficient adaptation by introducing low-rank Graph, Edge, and Node Prompts with a frozen backbone. However, existing methods mainly rely on image-level classification supervision, providing limited contextual constraints on prompt-induced node representation changes and underutilizing cross-region dependencies in visual graphs. To address this issue, we propose JEP-VGP, a vision graph prompt learning framework inspired by the Joint-Embedding Predictive Architecture (JEPA), which takes prompt residuals as prediction targets to provide explicit contextual guidance. Specifically, we introduce Prompt-Residual Embedding Prediction (PREP), which extracts prompt-induced representation changes by comparing prompted and matched-reference representations under the same configuration, and predicts target residuals from contextual residuals through a lightweight predictor with a slowly updated prompt teacher. This transforms cross-region dependencies into fine-grained supervision for prompt adaptation. Furthermore, we develop Type-Guided Prompt Learning (TGPL) to impose type-specific residual prediction constraints on different prompt pathways through cyclic mode selection and type-dependent weighting, while preserving joint prompt optimization in classification learning. During training, the ViG backbone remains frozen, and only lightweight adaptation components are optimized; auxiliary components are removed during inference without introducing additional inference-time auxiliary computation. Experiments on 10 visual classification benchmarks show that JEP-VGP improves the average accuracy of VGP by 1.5 percentage points under the same experimental settings.

## 119. JEPA LEARNS WHAT THE MASK LEAVES UNRECOVERABLE

**Keywords:** self-supervised learning, I-JEPA, V-JEPA, masking, masked image modeling, self-distillation, representation learning, video representation learning, compressed sensing

[Main paper PDF](https://openreview.net/pdf?id=Afr68jI5JI)

Joint-embedding predictive architectures are unusually sensitive to how the input is masked: block masks work, scattered masks do not, and the explanations are empirical. We give a measurement account. A mask is a linear measurement, and in a compactly supported wavelet basis every atom whose support lies inside the hidden region falls in the measurement's null space and leaves no trace in the data. The JEPA loss asks only that the encoded context suffice for the target, so a target that a low-level prior can recover admits a shortcut, one the moving-average target encoder can make self-consistent. What removes the shortcut is the coarse-scale content the mask leaves unrecoverable, provided enough context stays within reach of each target. We score that content before training and test the account's distinctive predictions in 151 pre-training runs. On ImageNet-100, strip masks match blocks in area and contiguity yet are recoverable, and they land at 40.3% linear top-1, beside random masks at 40.8%, against 64.3% for blocks; within one geometry family, the placements that leave the least unrecoverable content lose 6.5 points to those that leave the most, over five seed pairs; pixel targets span 7 points where latent targets span 25; and against a frozen target the gap between random and block masks, 19 points on the same kind of GPU, closes to 1.5, so the geometry acts through the target the encoder produces for itself. On UCF101 the masking ratio decides which condition, content or reach, binds; removing whole frames, unrecoverable in space but recoverable from neighbouring frames, is worst at both ratios; and on V-JEPA's own masks, batching them intact instead of truncated changes little (36.0% against 35.1%), whereas making 100 target tokens inside the blocks visible lifts them to 48.7% and hiding 100 context tokens outside the blocks does not (33.7%).

## 120. JEPA-Anything: Learning Predictive Models across Different Worlds

**Keywords:** World Models; Joint-Embedding Predictive Architectures; Predictive Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=OidXUN3er9)

World models learn internal states for predicting how an underlying system changes. Cells, molecules, physical fields, control environments, and clinical trajectories differ in observation geometry, yet require predictions of hidden, intervened, or future states from available context. Joint-embedding predictive architectures (JEPAs) provide a natural framework for this problem, but their single target-prediction pathway does not explicitly organize predictive target coordinates. We therefore introduce \method, a framework that separates domain-specific observations and context--target construction from a shared predictive-state interface. Within this interface, we further propose \emph{orthogonal predictive factorization} (OPF), which assigns target coordinates to separately parameterized factor-specific output heads and synthesizes them into a complete state for readout, intervention, planning, and multi-step rollout. Across a broad set of visual, biological, clinical, control, physical-field, weather, and molecular settings, domains retain their own encoders and observation geometries while using the same predictive core contract. Matched experiments show improvements in terminal readout, intervention prediction, and out-of-distribution or recursive forecasting; geometric analyses support well-conditioned synthesis, and factor interventions indicate functional use of the learned coordinate blocks. These results support a shared factorized predictive principle for heterogeneous worlds while preserving the structures needed for prediction, interaction, and analysis.

## 121. JEPA-Bisim: Learning Robust Visual Representations for Planning with Joint-Embedding Predictive World Models

**Keywords:** Joint-Embedding Predictive Architectures (JEPA), world models, bisimulation, invariant representation learning

[Main paper PDF](https://openreview.net/pdf?id=ZnG7TNmdNY)

World models learned from high-dimensional visual observations allow agents to make decisions and plan directly in latent space, avoiding pixel-level reconstruction. However, recent latent predictive architectures (JEPAs), including the DINO world model (DINO-WM), display a degradation in test time robustness due to their sensitivity to ``slow features". These include visual variations such as background changes and distractors that are irrelevant to the task being solved. We address this limitation by augmenting the predictive objective with a bisimulation encoder that enforces control-relevant state equivalence, mapping states with similar transition dynamics to nearby latent states while limiting contributions from slow features. We evaluate our model on a navigation task (PointMaze) and on a manipulation task (PushT) under different test-time background changes and visual distractors. Across all benchmarks, our model consistently improves robustness to slow features while operating in a reduced latent space, up to $10\times$ smaller than that of DINO-WM. Moreover, our model is agnostic to the choice of pretrained visual encoder and maintains robustness when paired with DINOv2, SimDINOv2, and iBOT features.

## 122. JEPA-DIT: FROM-SCRATCH PREDICTIVE WORLD-MODEL PRETRAINING FOR MANIPULATION

**Keywords:** JEPA; DIT; WORLD MODEL; PRETRAINING; Embodied AI

[Main paper PDF](https://openreview.net/pdf?id=dgiqOf1NtQ)

World-action models—transformers that jointly denoise future video and
actions—represent the world almost exclusively in the latent of a reconstruction
VAE inherited from a video-generation prior. That is a liability for control: a re-
construction objective must preserve every pixel-level nuisance a decoder has to
repaint, whereas a policy needs only the scene’s controllable structure. A policy-
free diagnostic makes the cost concrete—under domain randomisation the recon-
struction latent moves nearly twice as far from its clean distribution as a predictive
(JEPA) latent (ρ= 2.05 vs. 1.16), while a cross-task control shows both register
a change of task equally: invariance, not collapse. The field keeps the VAE any-
way, because a JEPA latent has no generative prior to build a world model on.
We present JEPA-DiT, to our knowledge the first world-action model whose dif-
fusion transformer is pretrained from random initialisation in a JEPA latent, car-
ried unchanged from egocentric pretraining through teleoperation mid-training to
downstream manipulation, and delta-JEPA, which makes the two representations
complementary rather than competing by having the predictive stream carry the
temporal difference from the present observation. Training from scratch proves to
be not the price of a predictive latent but the reason it works: in a width-matched
ablation the from-scratch stream develops a language pathway at 25×the floor
uniform attention would give while a warm-started run reaches 2.1×, barely above
chance, and passes that deficit downstream. Across all 50 RoboTwin 2.0 tasks with
randomisation held out of training, JEPA-DiT reaches 84.5% clean and 59.5% out
of distribution—the best OOD score and best clean/OOD average among world-
action models on this protocol. Each representation alone falls short of the pair:
with a mature prior but no predictive stream the model scores 1.9% under the shift,
with a predictive stream but no prior 11.9%.

## 123. JEPA-DNA: Grounding Genomic Foundation Models through Joint-Embedding Predictive Architectures

**Keywords:** Joint-Embedding Predictive Architecture, JEPA, genomic representation learning

[Main paper PDF](https://openreview.net/pdf?id=maQnnAp3hR)

Genomic Foundation Models (GFMs) typically rely on Masked Language Modeling
(MLM) or Next-Token Prediction (NTP) to learn the "Laws of Nature". While
effective at capturing local syntax, these generative paradigms prioritize token-level
reconstruction over high-level functional context. We introduce JEPA-DNA,
a model-agnostic continual training framework that integrates a Joint-Embedding
Predictive Architecture (JEPA) with traditional generative objectives. By supervising
global sequence embeddings in a latent space, JEPA-DNA forces models to
predict the functional representations of masked genomic segments, shifting the
learning signal from token recovery to semantic alignment. We evaluate JEPA-DNA
on 17 diverse genomic benchmark tasks, demonstrating consistent gains in
linear probing and zero-shot performance regardless of the underlying GFM architecture
or generative objective, and establishing a new state-of-the-art for GFMs
under the linear-probing protocol. Through extensive ablation studies, we further
characterize the synergistic interplay between generative and latent objectives. Our
code is provided in the supplementary material.

## 124. JEPA-Guided Soft Grouping for Step-Level Credit Assignment in Long-Horizon LLM Agents

**Keywords:** reinforcement learning, credit assignment, LLM agents, long-horizon decision making, predictive representation learning, joint-embedding predictive architecture (JEPA), soft grouping

[Main paper PDF](https://openreview.net/pdf?id=325vOXyVFx)

Long-horizon LLM agents trained with outcome rewards face a central credit-assignment challenge: final success or failure does not reveal which intermediate decisions contributed to the outcome. Step-level grouping provides finer-grained supervision by comparing the subsequent returns of intermediate steps across trajectories, making group construction central to effective credit assignment. However, constructing groups through exact observation text matching excludes comparisons between states that share task-relevant context, such as holding the same object for the same goal, but differ in their descriptions of the surroundings. We introduce JEPA-guided soft grouping to recover such comparisons in a learned feature space while retaining the original exact text groups. A task-conditioned JEPA state encoder is trained through future-latent prediction, and current-state feature similarity is used to retrieve neighbors from other trajectories of the same task, forming soft comparison sets. Differences between each step’s observed discounted return and those of its neighbors yield supplementary step-level credit. Because feature similarity alone does not guarantee reliable comparisons, a selective gate controls the admission of this credit and a bounded residual limits its magnitude, while preserving the original episode-level and exact step-level advantages. On ALFWorld with Qwen2.5-1.5B-Instruct, our method achieves 92.97% success—the highest among the configurations in our main comparison—versus 87.76% for the reproduced exact-grouping baseline (+5.21 percentage points). These results support supplementing exact text grouping with learned feature space comparisons for step-level credit assignment.

## 125. JEPA-MUSIC: Self-Supervised Predictive Subspace Learning for Multiple Signal Classification

**Keywords:** DoA estimation, Multiple Signal Classification, Self-Supervised Learning

[Main paper PDF](https://openreview.net/pdf?id=z4t76QBuhO)

Direction-of-arrival (DoA) estimation is fundamental to modern wireless communication and sensing systems. While the classical multiple signal classification (MUSIC) algorithm offers high angular resolution and clear interpretability, its performance degrades under limited snapshots, low signal-to-noise ratios (SNRs), and coherent sources due to empirical covariance breakdown. Conversely, data-driven methods mitigate such degradation but typically demand large DoA-labeled datasets and yield less transparent inference. To bridge this divide, we propose JEPA-MUSIC, a model-based self-supervised learning framework that integrates representation learning with subspace-based MUSIC inference. Specifically, JEPA-MUSIC constructs paired observations from the same signal scene and employs a tailored joint-embedding predictive architecture (JEPA) to learn to recover a structured, MUSIC-compatible covariance without requiring ground-truth DoA labels. During inference, this recovered covariance directly feeds into standard MUSIC for spatial-spectrum search, preserving its rigorous model-based interpretability. Extensive evaluations across diverse sensing conditions demonstrate that JEPA-MUSIC substantially outperforms classical MUSIC in challenging regimes and matches or surpasses strong data-driven baselines, while achieving higher subspace fidelity, lower tail failure rates, and superior sample efficiency.

## 126. JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts

**Keywords:** world model, test-time training

[Main paper PDF](https://openreview.net/pdf?id=MrNqktueaq)

World models enable agents to plan by predicting future states of the environment, but their predictions can become unreliable when test-time dynamics differ from those seen during training. We present JEPA-TTT, which adapts the latent dynamics predictor of a pretrained action-conditioned Joint-Embedding Predictive Architecture world model throughout test time. Self-supervised updates accumulate across episodes, while the visual encoder and reward head remain fixed, preserving the pretrained representation and task objective. Planning requires neither a goal image nor online environment reward. JEPA-TTT uses dense replay, which forms prediction windows at every temporal offset, retains them in a growing buffer, and samples minibatches from that buffer for predictor updates. Across eight dynamics shifts in four continuous-control environments, JEPA-TTT improves planning on every shift. After 500 test-time episodes, it reduces autoregressive latent prediction error by 83% on average and improves planning performance by 153% over the frozen JEPA world model. These results show that persistent self-supervised test-time training can adapt a pretrained latent world model under changed dynamics.

## 127. JEPA-UQ: Benchmarking Uncertainty in Latent World Model Rollouts

**Keywords:** Joint-Embedding Predictive Architecture; Latent World Models; Uncertainty Quantification; Rollout Uncertainty; Predictive Reliability; Autonomous Driving

[Main paper PDF](https://openreview.net/pdf?id=PekBRA0p57)

Latent world model rollouts need uncertainty estimates tied to future prediction error. JEPA-UQ defines a measurement protocol that specifies prediction-time information, target loss, horizon, output meaning, and statistical unit. We study one frozen visual encoder and two variance-based predictive systems on 14 nuScenes logs outside the project's recorded history. Both systems show a positive scoreloss association at H1-H5, with weaker correlations at longer horizons. At H1 and H2, AUROC intervals lie above chance. Overall, score rankings carry information about continuous rollout loss across all five horizons. Interval evidence for thresholded failure events is concentrated at H1 and H2.

## 128. JEPA-VA: JEPA Is a Good Visual Action Verifier for Generalizable Robot Policies

**Keywords:** Robot Learning, Policy Generalization, Visual Consequence Verification, Imitation Learning, World Models

[Main paper PDF](https://openreview.net/pdf?id=gI3baMfvCU)

Vision-language-action (VLA) policies are commonly trained to align predicted actions with demonstrations, while world-action models (WAMs) jointly predict future video and action; neither explicitly checks whether an action produces its intended visual consequence. We study this complementary training signal: does a policy's proposed action lead to the expected visual change? We introduce \method, a JEPA visual verifier that evaluates proposed action chunks through their predicted feature changes relative to demonstrated transitions. Conditioned on the current observation and an action chunk, the verifier predicts the feature change at the end of the chunk. During policy training, a change-weighted cosine objective aligns the predicted change direction with the demonstrated one, sending a consequence-consistency gradient through the verifier's action input back to the policy. The verifier is not needed at deployment and adds no inference cost. Verifier-guided policy learning raises LIBERO-Plus success from 62.68% to 71.73% and clean-to-randomized RoboTwin success from 12.00% to 17.80%, suggesting that JEPA-VA helps policies learn more generalizable robot manipulation.

## 129. JEPA-x: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics

**Keywords:** JEPA, physical grounding, world model

[Main paper PDF](https://openreview.net/pdf?id=G8WCdaDci4)

Latent world models plan by predicting the outcomes of candidate actions in a learned representation space. In self-predictive models, however, the encoder and predictor are optimized jointly and can co-adapt to latent transitions that are easy to predict in the training distribution but weakly constrained by the physical evolution of the scene. We introduce the cross-predictive JEPA (JEPA-x), which grounds latent dynamics in privileged physical trajectories. JEPA-x treats visual observations and physical states as corresponding views of the same action-conditioned trajectory, advances both through a shared predictor, and matches each prediction to the future representations of both modalities. This encourages the action-conditioned predictor to learn a common transition rule across the two views. Privileged physical state is used only during training, leaving a visual-only model at deployment. Empirical results show that JEPA-x reduces the rollout drift of a newly fitted predictor from 0.361 to 0.104 and increases mean control success from 53.6% to 78.2% on a multi-task suite spanning six evaluation subfamilies. We additionally show that direct full-state regression improves position decodability without improving forecastability or control, indicating that the benefit comes from shaping latent dynamics rather than merely encoding physical variables.

## 130. JEPACast: Precipitation Nowcasting in a Decodable and Predictable Latent Space

**Keywords:** Precipitation Nowcasting, Joint-Embedding Predictive Architecture, Generative Modeling

[Main paper PDF](https://openreview.net/pdf?id=LF98y8bmMU)

Generative models have become a dominant approach to probabilistic radar-based precipitation nowcasting, yet the latent space where they generate has barely been examined. Most models rely on reconstruction-trained autoencoders, while advances focus on increasingly specialized generators without changing the representation. A simple decomposition of forecast error motivates two fundamental requirements for a forecasting latent space: *decodability* and *predictability*. We find that representations from a V-JEPA encoder trained on radar data remain strongly decodable while achieving higher predictability of future dynamics than widely used reconstruction-based representations. Building on this, we introduce **JEPACast**, which adapts the representation autoencoder paradigm to generative nowcasting by combining the V-JEPA encoder with a latent flow transformer and a ViT decoder. On SEVIR and MeteoNet, JEPACast outperforms various baselines on key forecast metrics, with larger gains for intense precipitation and longer lead times. These results highlight latent representation design as an important direction for generative precipitation nowcasting.

## 131. JEPath: a world model for first-person navigation

**Keywords:** World Models, Latent Planning, JEPA, Representation Learning, First-person Navigation

[Main paper PDF](https://openreview.net/pdf?id=1k87vKEY9U)

JEPA world models combined with test-time trajectory optimization have recently achieved strong results on tasks conditioned on a single goal image. However, most of these results assume fully observable environments, and their adaptation to first-person navigation raises specific challenges. In this study, we introduce PADoom, a benchmark built on ViZDoom where the same environments and trajectories can be observed either from a fully observable top-down view or from a first-person view. We show that perceptual aliasing, where different locations produce nearly identical observations, requires combining visual and spatial information, and that the spatial signal must avoid absolute position encoding to generalize across maps. Based on these findings, we propose JEPath, a new JEPA world model that jointly predicts future visual features and ego-motion from observations and actions. Unlike models that predict absolute position, JEPath predicts motion and integrates it along candidate paths. The planner scores paths by distance to the goal rather than visual similarity, resolving perceptual aliasing while still relying on vision to handle navigation-relevant scene structure such as obstacles. On PADoom, JEPath outperforms recent world models and goal-conditioned policies for first-person navigation. It also generalizes substantially better to unseen maps, where competing methods experience a pronounced performance drop. The benchmark and models will be released upon acceptance.

## 132. Joint Driver, Vehicle, and Road Modeling for Forecasting and Driver Monitoring

**Keywords:** joint forecasting, driver monitoring, human-centered driving, multimodal representation learning, on-vehicle deployment

[Main paper PDF](https://openreview.net/pdf?id=tN4FNZO748)

Predicting how drivers, vehicles, and road scenes interact and evolve together is central to driver monitoring. Prior work models in-cabin activity or traffic-conditioned driver motion in isolation, motivating joint driver, vehicle, and road modeling with real-time on-vehicle evaluation. We introduce TriDrive, to our knowledge the first unified framework that jointly forecasts driver kinematics, vehicle dynamics, and road demands through an automation-conditioned transition model. Modality-specific encoders (an anchored kinematic representation of the driver, causal CAN-bus dynamics, and frozen V-JEPA 2 road latents with structured road margins) are connected by directed residual connections through which driver and road context refine vehicle forecasts. We evaluate TriDrive on three downstream tasks. On the public AIDE benchmark, its kinematic encoder recipe sets a new full-set state of the art (SOTA) among published baselines (48.05 versus 71.47 All-MPJPE). On 197.2 hours of naturalistic BATON driving, directed connections and road margins raise assistance-engaged PR-AUC by 0.084 for steering onset and 0.286 for time-to-collision drops. For real-time use, we distill the road encoders and run TriDrive on a comma four with an external 8 GB GPU, where a lightweight current-state warning probe updates at 5 Hz with 177 ms p95 latency while the joint model forecasts concurrently. The probe is above an openpilot-based baseline on human-labeled manual-driving warnings (AUROC 0.725 versus 0.563), and in a paired on-road study 14 drivers rate its warnings as more appropriate (+1.79) and timely (+2.67) than those of openpilot's driver-monitoring system.

## 133. JOINT-EMBEDDING PREDICTIVE LEARNING CLOSES THE UNIMODAL–MULTIMODAL GAP IN ECG PRE- TRAINING

**Keywords:** Self Supervised Representation, JEPA, Foundation Model, 12 LeadECG

[Main paper PDF](https://openreview.net/pdf?id=gaUSLsn6k5)

In time series representation learning, pairing signals with free-text descriptions typically outperforms signal-only pretraining; in ECG, where most recordings carry a written interpretive report, the gap is read as evidence that language supplies information the waveform lacks. Whether it survives a controlled comparison is unknown: published comparisons vary the pretraining corpus, the evaluation protocol and whether baselines are retrained at all. We fix all three, retraining six published methods from their official code on 1.21 million recordings and probing every model with the same frozen linear probe on PTB-XL and SPH. Under these controls, joint-embedding predictive learning (JEPA) largely closes the gap: it comes within 0.005 macro-AUROC of the strongest multimodal model on PTB-XL and scores 0.007 above it on SPH, the two being equivalent under two one-sided tests with a 0.02 margin. Reconstruction, discrete-target and contrastive
baselines trail behind. Adding reports gives no gain with all labels, but adds 0.015 and 0.045 with 10% of them. Language buys label efficiency rather than a higher ceiling: signal-only latent prediction reaches the same performance without ever seeing a report, and whether text earns its cost elsewhere in time series needs the same controls applied.

## 134. Juno: Taming Predictive Latents for Vision-Language-Action Models

**Keywords:** Jepa, vla, world model

[Main paper PDF](https://openreview.net/pdf?id=GZdwmSCjJs)

Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision–language–action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts.
We introduce **_Juno_**, a unified framework built around one action-conditioned JEPA that serves as a control-aligned representation backbone, a predictive teacher, and an adaptable dynamics model. During **pretraining**, we train it on embodiment-matched trajectories and use a dynamic CLS loss to transfer motion-weighted patch dynamics to a compact global state. During **policy learning**, we fuse current-frame JEPA patches into VLA perception and use a decoupled reasoning branch with separate transformation parameters to distill future latent states for action generation. During **deployment**, we adapt the world model on all observed transitions, including failed rollouts, freeze the adapted teacher, and re-align the policy on verified executions using LoRA adapters and a trainable action head, without expert corrections or task rewards.
On SimplerEnv, **_Juno_** raises average success from $60.9\%$ to $68.5\%$ over Qwen3GR00T, the strongest baseline, and test-time adaptation further reaches $72.7\%$; on a real robot, it retains $70\%$–$75\%$ success under background, height, and object shifts where the base policy collapses to $0\%$.

## 135. K-JEPA: From Point to Distributional Prediction by Kernelized Joint-Embedding Predictive Architectures

**Keywords:** JEPA, Kernel Methods, Predictive Reliability, Self-Supervised Learning, Responsible AI

[Main paper PDF](https://openreview.net/pdf?id=GMRGQIf7n4)

Joint-Embedding Predictive Architectures (JEPA) learn representations by predicting latent target features from a visible context. Although effective, standard JEPA objectives treat prediction as a point-estimation problem: the population-optimal predictor recovers a single point summary of the conditional target distribution.
When a visible context $x_c$ admits multiple plausible masked or future targets, this point estimate retains insufficient distributional information to identify the underlying conditional target distribution.
We propose K-JEPA, a novel, simple, kernelized extension that applies a characteristic-kernel transformation to JEPA latent targets while preserving the 
architecture and prediction setup. 
Rather than predicting only the latent target $z_t$, K-JEPA predicts its kernel representation $\phi(z_t)$.
We prove this changes the population target from a point summary of the latent target distribution to its conditional kernel mean embedding, which uniquely identifies the corresponding conditional target distribution when the kernel is characteristic.
Empirically, we evaluate this distributional behavior in controlled
settings and introduce a systematic target-retrieval comparison for direct evaluation of JEPA target prediction across heterogeneous formulations and modalities. 
We complement this evaluation with probabilistic scoring, calibration, selective prediction, prediction-set efficiency, and downstream transfer analyses. Our results characterize when K-JEPA improves target prediction and how these changes relate to downstream performance and reliability. 
Code is made available to the reviewers during the discussion process.

## 136. KEEPING JEPA WORLD MODELS PLANNABLE WHEN LITTLE OF THE FRAME MOVES

**Keywords:** world models, JEPA, model-based planning, representation collapse, inverse dynamics, language-conditioned planning, benchmark

[Main paper PDF](https://openreview.net/pdf?id=VcTDzyB84c)

Specifying a goal in language rather than as a goal frame is a natural interface for planning with a latent world model, but testing it needs scenes in which language must discriminate between several objects. We build SLIM, a pushing benchmark with several small objects and paired visual and language goals on identical scenes. On SLIM a LeWM world model that solves PushT succeeds on under 1% of trials, although a scripted controller with simulator state solves every tier. Probes locate the failure in the encoder: its latent is nearly action-insensitive, neither pusher nor object positions can be decoded from it, and rollouts are no better than copying the current latent forward. One inverse-dynamics auxiliary loss, applied to encoder latents and to predicted latents through a shared head discarded at test time, restores every probe and raises success from 0.003 to 0.35 (0.16 on the hard pushing tier, where a goal-agnostic policy scores zero), and improves PushT at twice the trained horizon. Controls attribute the repair to the gradient into the encoder, and a response sweep shows that the vanilla model plans once enough of the frame responds to actions. A cheap action-sensitivity probe, computable without environment access, acts as an empirical necessary condition: all configurations below its threshold failed to plan. On the repaired latent, a small language-goal head plans from sentences without retraining the world model: it reaches 0.84 on navigation (visual-goal oracle 1.00), follows the named zone when it is swapped with a decoy, and degrades gracefully to unseen nouns, while choosing which object to push from language remains open.

## 137. KerJEPA: Kernel Discrepancies for Euclidean Self-Supervised Learning

**Keywords:** self-supervised learning, representation learning, Joint-embedding architectures, kernel methods, distribution matching

[Main paper PDF](https://openreview.net/pdf?id=Uk0slRKkH1)

Breakthroughs in self-supervised Joint-Embedding Predictive Architectures (JEPAs) have established that regularizing Euclidean representations toward isotropic Gaussian priors yields provable gains in training stability and downstream generalization. We introduce a new, flexible family of Euclidean joint embedding self-supervised learning algorithms with kernel-based regularizers. One instance of this family corresponds to the SIGReg Epps-Pulley regularizer which approximates a sliced maximum mean discrepancy (MMD) with a Gaussian prior and Gaussian kernel. By expanding the class of viable kernels and priors and computing the closed-form high-dimensional limit of sliced discrepancies, we develop alternative methods with improved training stability and design flexibility and leverage those techniques to train strong vision learners at scale.

## 138. La-JEPA: Compact Robot Policies with Latent World Modeling

**Keywords:** JEPA, Robotics, World Action Models

[Main paper PDF](https://openreview.net/pdf?id=bnXZ71rCNk)

World-action models commonly adapt pretrained video generators, and vision-language-action models build on pretrained vision-language backbones; both tie policy architecture and inference cost to large transformers designed for generation rather than control. While the knowledge accumulated through large-scale pretraining is certainly useful, it remains unclear how much generation-oriented architectural choices affect control performance, and whether the trade-off required to access this pretraining is worth it. In this work, we introduce **Latent Action JEPA (La-JEPA)**, a compact world-action model whose policy transformer is trained from scratch in the feature space of a pretrained V-JEPA 2.1 encoder, so that its architecture and capacity can be chosen for control. Following Fast-WAM, La-JEPA learns to predict future features jointly with actions during training and generates only actions at inference. **Among policies without embodied pretraining, La-JEPA achieves state-of-the-art clean and randomized success on RoboTwin 2.0 and is equivalent to the state of the art on LIBERO-Plus, while using far fewer parameters than the strongest competing policies.** It runs substantially faster than Fast-WAM at comparable performance and outperforms the closest JEPA-based methods, LeapBot-WA and JEPA-WAM, on LIBERO-Plus and RoboTwin 2.0 without their pretrained policy backbones. On four real-robot tasks, including contact-heavy pushing and long-horizon multistep manipulation, its average success is comparable to $\pi_{0.5}$, outperforming non-embodied-pretrained baselines. Through a design study of the choices behind La-JEPA, we show that JEPA features outperform video VAE latents, most clearly out of distribution, and that training-time future prediction choices significantly impact the policy even when future prediction is skipped at inference. These results establish a compact, efficient foundation for JEPA-based world-action modeling: without a generative pretrained policy backbone, La-JEPA is comparable to or better than far larger policies built on video and language generation models, suggesting that robot foundation models may benefit from architectures designed for control rather than inherited from generation.

## 139. LaFree World Model: Label-Free Pretraining for Action-Conditioned JEPA World Models

**Keywords:** self-supervised learning, world models, latent actions, joint-embedding predictive architectures, label-efficient learning, vector quantization, model-based planning

[Main paper PDF](https://openreview.net/pdf?id=cCw8Ca0yEx)

Learning world models from observation sequences could reduce dependence on synchronized action labels, but learning to explain observed transitions does not necessarily yield dynamics that support downstream control.
We introduce LaFreeWM, an end-to-end action-conditioned JEPA world model that learns dynamics using discrete latent actions inferred from consecutive observations.
A quantized action interface, together with latent transition objectives, couples action discovery and representation learning without action annotations.
A small action-labeled subset subsequently adapts the pretrained world model to the environment's control inputs for planning.
Across control benchmarks, LaFreeWM improves planning with limited action supervision while retaining a compact efficient planner.
Ablations show the benefit of end to end training and reveal a prediction--planning mismatch: removing quantization substantially lowers held-out latent prediction error while degrading downstream planning.
The results demonstrate the value of label-free pretraining for counterfactual planning with action-conditioned world models and highlight the importance of evaluating inferred-action representations through the control they enable.

## 140. LaLa-World: Scaling Latent World Models with Natural Language Actions

**Keywords:** Latent World Models, Language-Conditioned World Models, Model-Based Planning, Policy Fine-Tuning

[Main paper PDF](https://openreview.net/pdf?id=Y5bMFgPFlM)

This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models.
We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning.
To this end, we introduce **LaLa-World**, a **La**nguage-conditioned **La**tent **World** model that learns from simulation and robot trajectories together with broader image and video data.
Two designs make this work.
First, we describe both numerical actions and visual changes in language, enabling joint training of a single future predictor across heterogeneous datasets.
Second, we build the predictor on a language model, allowing it to interpret language conditions while predicting future latent states.
The resulting predictor achieves higher average MPC planning performance than existing LWMs trained separately for each domain or task.
Adding image and video data further improves average planning performance and robustness to action phrasing.
In a matched comparison with an RAEv2-based video generation model baseline, LaLa-World reaches comparable planning performance with $6\times$ less training cost and $13.9\times$ faster planning.
Beyond planning, the pretrained LaLa-World serves as an initialization for LaLa-Policy, which jointly predicts actions and future visual representations.
LaLa-Policy performs competitively with Cosmos Policy on LIBERO and RoboCasa, with up to $5.5\times$ faster inference.

## 141. Laminar: Querying Biology at Any Scale with Tissue Embedding Fields

**Keywords:** Foundation Models, AI for Science, Spatial Data, Omics data, Biology, Biomedical data, JEPA, transfomers, geometric deep learning, spatial omics

[Main paper PDF](https://openreview.net/pdf?id=pPaLAz7poc)

Biology is organized at nested spatial scales, from molecules to cells to multicellular neighborhoods, whose functions emerge from multi-scale organizations rather than any single cell. Imaging-based spatial transcriptomics (iST) captures all of these scales in a single experiment, measuring up to billions of individual transcripts, each with its gene identity and sub-micrometer position. To handle this volume, existing foundation models pool transcripts into predefined units such as cells, patches, or bins before learning, which fixes the representation to a single spatial scale and discards the molecular geometry within each unit. We introduce *tissue embedding fields*, a representation that assigns contextual embeddings on a shared unit hypersphere to every measured transcript. A region of any size or shape, from a single cell to a whole section, can then be represented by summing and normalizing the embeddings of the transcripts it contains, without re-encoding the tissue. The spatial unit of analysis is therefore chosen at query time rather than fixed during training. To compute such fields at billion-transcript scale, we introduce Laminar, a local-to-global encoder whose cost grows linearly with transcript count. A graph neural network exchanges short-range molecular information over local transcript graphs while a quadtree spatial Transformer propagates information to progressively larger tissue tiles. Each transcript then retrieves this multi-scale context through cross-attention, yielding its final embedding. We train Laminar using a joint-embedding predictive architecture, where a context encoder processes spatially- and gene-masked tissue, while a predictor matches multi-scale regional representations of the complete tissue.
A single Laminar encoder pretrained on 632 public human iST sections, evaluated frozen on eight transfer tasks spanning cell, niche, and tissue scales, achieves the best scores on tissue-scale tasks while remaining competitive with fixed-scale foundation models at cell scale, with an overall best mean rank. Laminar shows that biological representations need not be tied to predefined spatial units; a unified representation enables reasoning across the hierarchy of tissue organization.

## 142. Language-Reasoning JEPA: Searching Imagined Futures over Language

**Keywords:** World Models, Language Models, JEPA

[Main paper PDF](https://openreview.net/pdf?id=6RT0D5VDJc)

A language model reasons by generating text about the future with the same likelihood readout that chooses its actions, and it has no separate mechanism for imagining what an action would do. Action-conditioned joint-embedding predictive architectures (JEPAs) supply such a mechanism in robotic control, and we study whether the same construction supports reasoning over language. We read a sentence as a partial observation of a controlled process and a derivation step as an intervention, whose observed consequence is the supervision a JEPA is trained to predict. Transition prediction determines the dynamics of the latent space but leaves its metric free, so we add a goal-conditioned energy head that we train only by ranking outcomes the environment has executed, and we plan by model-predictive control over imagined latent trajectories. We call the model Language-Reasoning JEPA (LR-JEPA) and evaluate it in two synthetic environments rendered entirely in language, where every policy selects its next step from the same menu of admissible actions and we measure overshoot, the number of executed actions relative to the shortest solution. On chain-structured deduction, language models trained on the same trajectories are optimal inside the trained lengths and reach overshoot $1.69$ to $1.91$ beyond them, where a random policy reaches $2.01$. The same ranking head on the frozen language model reaches $1.03$ at search depth one and falls to the random level by depth four, because a language model cannot roll its state forward and appending the true consequences of imagined steps to its context does not restore search reliably, while LR-JEPA improves from $1.31$ to $1.09$ over those depths. On dependency graphs the search degrades with depth, which we trace to the drift of imagined trajectories.

## 143. Latent evolving World Action Model

**Keywords:** Robotic Manipulation, World Action Models, Visuomotor Policy Learning, Predictive Representations, Direct Preference Optimization

[Main paper PDF](https://openreview.net/pdf?id=ltSAJVmHWF)

World Action Models (WAMs) jointly model action generation and environment dynamics and are mostly built on pretrained Video Diffusion Models (VDMs). In VDM-based WAMs, observations are first encoded by a VAE, and the resulting compressed latents are then processed by large video diffusion backbones to extract effective features for action generation.  However, this paradigm ties WAM performance and training cost to large-scale video generation pretraining, limiting WAM efficiency and scalability. In this paper, we theoretically and empirically investigate how visual representations affect action generation in WAMs. Our results show that predictive embeddings from Joint-Embedding Predictive Architecture (JEPA) encoders better support action generation than compressed VAE latents, with I-JEPA performing best in our encoder comparison. Based on these findings, we propose LeWAM, which conditions action generation on JEPA embeddings and models environment evolution by predicting future embeddings in the same space, without relying on a video diffusion backbone. We further find that imitation learning matches demonstrated actions but does not distinguish better actions from worse ones, even though small action deviations can greatly affect task success. To address this limitation without additional environment interaction or the human oversight required for resets and safety, we introduce Demonstration-Guided DPO (DemoDPO), an offline preference refinement stage that derives preference supervision directly from demonstrations. With only 0.4B trainable parameters, LeWAM achieves an average success rate of 92.28\% on RoboTwin 2.0, comparable to that of state-of-the-art VLAs and WAMs, and maintains practical effectiveness on real-world manipulation tasks.

## 144. Latent Goal Prediction from Language for Model-Based Planning

**Keywords:** world models, hierarchical planning, subgoal prediction, language-conditioned planning, joint-embedding predictive architecture

[Main paper PDF](https://openreview.net/pdf?id=3CsEiuXGJe)

Joint-Embedding Predictive Architectures (JEPAs) enable agents to plan in latent space by imagining the outcomes of candidate actions, yet task specification remains a bottleneck. Visual targets provide precise
local gradients but poor distant guidance, while language is flexible yet limited by noisy cross-modal alignment or dependence on distinct large generative models. We introduce LAGO (Latent Goal Prediction from Language), a hierarchical world model in which a single predictor both forecasts action-conditioned dynamics and grounds language instructions as sequences of intermediate latent subgoals, training both modes with a single regression objective over a shared latent space. At each planning step, LAGO predicts a sequence of latent subgoals from a language instruction and optimizes an action sequence using a soft-minimum alignment cost that rewards subgoal proximity without enforcing a rigid path. Subgoals are repredicted as the agent's state evolves, turning a single long-horizon instruction into a sequence of locally tractable objectives. Across environments spanning navigation and manipulation, LAGO outperforms flat and hierarchical image-goal planners, with the largest gains on long-horizon navigation with curved, hazard-constrained paths, where it more than doubles the success rate of a goal-conditioned behavior cloning policy trained on the same demonstrations. Grounding language in the world model's own latent space also outperforms vision-language reward models, including one that plans with ground-truth dynamics.

## 145. Latent JEPA: Abstract Future Prediction for Latent Reasoning in Chemistry

**Keywords:** AI for chemistry, Joint-Embedding Predictive Architecture

[Main paper PDF](https://openreview.net/pdf?id=BTzVQ2fXK1)

Large language models offer a promising foundation for chemical reasoning,
bringing together chemical knowledge and multistep problem solving.
Chemical intuition can provide an initial sense of plausible outcomes
before the details of a solution are fully worked out.
Inspired by how such expectations complement explicit analysis, we study
how continuous latent thoughts can be trained to anticipate informative
aspects of future solutions without verbalizing every intermediate step. We introduce
Latent JEPA, a framework that combines autoregressive learning with
joint-embedding prediction of one or more future views.  For chemical
reasoning, we develop textual and molecular prediction objectives that
connect latent thoughts to both subsequent reasoning and molecular outcomes.
Experiments on ChemCoTBench show gains in molecular
optimization and on several editing and reaction metrics. Representation
analyses show that future prediction makes latent thoughts more informative
about molecular outcomes and strengthens their correspondence with chemical
structure. These findings support abstract future prediction as a learning
principle for connecting continuous latent reasoning with scientific outcomes.

## 146. Latent Metrics for Planning with World Models

**Keywords:** World Models, Joint-Embedding Predictive Architectures (JEPA), Robot Learning, Planning

[Main paper PDF](https://openreview.net/pdf?id=shrZrxHBY2)

Joint-Embedding Predictive Architectures (JEPAs) enable visual planning by predicting the future outcomes of candidate actions directly in latent space. However, existing JEPA planners typically evaluate candidate actions using Euclidean distance between the predicted outcome and the goal. This treats all latent directions equally, despite differences in their sensitivity to actions and in the model's prediction accuracy along them. We introduce Latent Metrics for Planning with World Models (LENS). LENS identifies the \emph{action-response fidelity} of different latent directions from the action-conditioned dynamics already learned by a pretrained world model, while keeping both the encoder and predictor frozen. Specifically, LENS derives action-response fidelity from the consistency of action-conditioned variation between real and predicted futures together with the accuracy of the corresponding future predictions, and uses this fidelity to determine the relative influence of different latent directions in planning. Directions with higher action-response fidelity receive greater relative weight in the planning metric. The resulting metric is used both to evaluate predicted futures and to guide sampling-based search, without retraining the world model. Across four benchmarks, LENS improves average success rate from 85.8\% to 95.8\%. With candidate actions and world-model predictions fixed, it increases the average Spearman correlation between model rankings and real outcomes from 0.540 to 0.696. These results show that the action-conditioned dynamics already learned by a world model can provide not only a basis for predicting the future, but also a basis for determining the relative role of different latent directions in planning.

## 147. Latent Prediction Helps Physical Representations Only When It Predicts the Future

**Keywords:** self-supervised learning, JEPA, latent prediction, vMAE, pixel reconstruction, physical simulation, representation learning

[Main paper PDF](https://openreview.net/pdf?id=27HPPxb5wt)

Joint-embedding predictive architectures (JEPAs), which predict in a learned latent space, are reported to learn better representations of physical systems than masked autoencoders, which reconstruct pixels. Previous studies, however, change the space of the prediction target together with its time horizon, the architecture and the training pipeline making it difficult to determine which factor contributes to improved representations. With this motivation, we separate prediction space from prediction horizon. We train ViT-S encoders on three physical simulations from The Well. These encoders are identical except for their objectives. We train on four distinct objectives, varying whether they predict (a) pixels or latent representations and (b) the current eight-frame clip or the next eight-frame clip. Across all encoder layers, we probe representations for regime parameters and for pooled and token-level physical quantities at current and future times. We find that regime probes and future-time probes favour representations trained on the Latent-Future objective, suggesting that latent prediction helps physical representations only when paired with future prediction. Probes for same-time physical quantities provide similar results for all models. We further analyse representations after adding noise to the inputs and find there is not one objective that produces representations more robust to noising. This paper analyses how prediction space and prediction horizon affect learned representations while holding the other training components fixed.

## 148. Latent Prediction Yields Cross-Subject Alignable Representations in Sensory-Evoked fMRI

**Keywords:** self-supervised learning, fMRI, neural decoding, cross-subject alignment

[Main paper PDF](https://openreview.net/pdf?id=iohlEQGDm5)

Decoding sensory-evoked functional magnetic resonance imaging (fMRI) data is a central analytical tool in cognitive neuroscience. Here we ask whether self-supervised learning (SSL), which has been scarcely explored in this domain, can yield representations that support strong downstream performance. To do so, we adapt a joint embedding predictive architecture (JEPA) to train participant-specific encoders on brain data alone. The encoders never see the stimulus images or any representation derived from them. Applied to the Natural Scenes Dataset (NSD), we evaluate our learned brain embeddings on the downstream tasks of brain captioning and image reconstruction, as well as cross-participant generalization. Our self-supervised approach achieves competitive performance with parameter-rich supervised pipelines that are trained end-to-end with access to image and language data. We further find that encoders trained independently for different participants can be aligned fully unsupervised, using neither images nor stimuli shared between them. After alignment, a neural decoding head trained on one participant can be applied to another without fine-tuning and retains most of its within-subject performance on image reconstruction and brain captioning. By removing the need for images and shared stimuli, our approach is a step towards pooling fMRI data across participants and, eventually, across datasets.

## 149. Latent Weather Forecasting with Joint-Embedding Predictive Architectures

**Keywords:** Joint-Embedding Predictive Architecture, JEPA, weather forecasting, ERA5, latent prediction, self-supervised learning, medium-range forecasting, Vision Transformer, autoregressive rollout, anomaly correlation

[Main paper PDF](https://openreview.net/pdf?id=GMr8A6r8el)

We investigate Joint-Embedding Predictive Architectures (JEPAs), a self-supervised approach that predicts in embedding space rather than pixel space, as a basis for data-driven weather prediction. We train JEPA-WX on 39 years of ERA5 reanalysis at 5.6° resolution for 12 upper-air variables at three pressure levels. The architecture combines a Vision-Transformer context encoder, an exponential-moving-average (EMA) target encoder, a Transformer predictor with free-running rollout training, and a lightweight convolutional decoder. Training uses three terms: a latent prediction loss, a Slicing Univariate Test regularizer against representation collapse, and an auxiliary reconstruction loss that we find essential for downstream decoding. We show that (i) JEPA-WX outperforms persistence at all evaluated lead times on all 12 variables, with a day-1 anomaly correlation (ACC) of 0.94 on Z500; (ii) JEPA-WX is competitive with a pixel-space U-Net at short leads and outperforms it at day 14 on 8 of 12 variables; and (iii) RMSE grows by 3.2× from day 1 to day 14 for JEPA-WX versus 7.6× for the U-Net, suggesting that the latent bottleneck acts as an implicit regularizer against autoregressive error accumulation. Code, checkpoints and evaluation scripts are released.

## 150. Latent World Models Need to Also See the Details: Keyframe-Aware Visual Alignment

**Keywords:** keyframe-aware visual alignment, joint embedding predictive architecture, latent world models

[Main paper PDF](https://openreview.net/pdf?id=RYRKeKdA5j)

Latent world models built on the Joint Embedding Predictive Architecture (JEPA), such as LeWorldModel, learn environment dynamics entirely in latent space and avoid the cost of pixel-level reconstruction. This purely latent paradigm, however, has two fundamental limitations. In fine-grained manipulation, the target object typically occupies only a tiny fraction of the frame, and the encoder's information bottleneck can suppress visual details critical to success. Moreover, the absence of any decoder that maps latents back to an observable space makes the long-horizon accuracy of latent rollouts unverifiable, allowing an overconfident yet physically implausible plan to pass unnoticed. We introduce **KAVA** (Keyframe-Aware Visual Alignment), a hybrid framework that augments a JEPA next-embedding objective with a temporal-saliency key-frame selector---combining the JEPA-loss gradient norm with an action-perturbation uncertainty score---and applies a pixel-level reconstruction loss only to a small subset of information-dense frames per trajectory. The reconstruction gradient is stopped at the predictor, preserving the latent signal the JEPA objective is designed to learn, and the decoder simultaneously serves as an online probe for the consistency of imagined rollouts. Across four image-based control benchmarks, KAVA achieves the best planning success rate among four representative latent world-model baselines. Selective, saliency-driven observation supervision is therefore a promising recipe for retaining the efficiency of reconstruction-free world models without sacrificing visual fidelity or rollout verifiability.

## 151. Latent-Action-Guided Video-Language Feature Learning for Surgical Instrument–Tissue Interaction Recognition

**Keywords:** Surgical action recognition, Video representation learning, Vision-language learning

[Main paper PDF](https://openreview.net/pdf?id=e84SGSPW8T)

Recognizing instrument--tissue interactions is essential for
context-aware surgical AI. Vision-language models offer a natural way to
inject semantic structure into surgical representations by aligning video
features with textual action descriptions. However, pretrained encoders may
lack spatial coherence, while global semantic alignment does not ensure precise
spatial and temporal representations. By analyzing frame-to-frame feature
changes, we find that semantic alignment increases their dimensionality, but
larger increases do not necessarily improve recognition; encoders also differ
in how strongly dominant changes localize to interaction regions.
Motivated by these findings, we introduce LAViF, which compresses
frame-to-frame changes into latent actions and predicts next-frame features
during end-to-end video--language alignment. Without additional spatial or
motion annotations, LAViF improves the interaction grounding of leading
feature changes and temporal-direction sensitivity in our evaluated settings.
We further characterize how action capacity and prediction strength affect
recognition across encoders and triplet components. Using image encoders
without large-scale video pretraining, LAViF achieves competitive recognition
with faster inference and smaller INT4 accuracy drops than V-JEPA2/2.1,
supporting its deployment potential.

## 152. Latent-Predictive Universal Horizon Models for Long Horizon Zero-Shot RL

**Keywords:** Offline reinforcement learning, zero-shot reinforcement learning, successor measure, goal-conditioned reinforcement learning

[Main paper PDF](https://openreview.net/pdf?id=CYxmQV30gg)

While behavior foundation models (BFMs) have achieved impressive zero-shot performance on various human locomotion tasks, these methods struggle on tasks that require longer horizon reasoning. Recent work has explored using geometric horizon models (GHMs) for planning on top of pre-trained BFMs to achieve longer horizon tasks; however, such methods require significant test-time compute, operate in raw observation space, and require a complex two-stage training process. In this work, we instead explore training horizon models in latent space and as an auxiliary loss \textit{during} BFM training. In particular, we propose a novel latent-predictive Universal Horizon Model,  which we learn jointly with a latent-predictive BFM with both models shaping the state- and task-encoding spaces. We demonstrate that this auxiliary representation learning objective is theoretically compatible with the primary TD-JEPA objective, with respect to the learned state and task encodings, and we demonstrate empirically that it can be beneficial for downstream zero-shot performance. Finally, we show that this UHM model can be used to perform model-based updates in the zero-shot RL setting, allowing us to stably train a latent-predictive BFM at discounts as high as $\gamma=0.999$.

## 153. LEAP: Latent Encoder Alignment for Physics Rewards in Video Generation

**Keywords:** reward feedback learning, latent reward model, text-to-video generation, video generation model, reinforcement learning, computer vision

[Main paper PDF](https://openreview.net/pdf?id=KJxKpYhlT4)

Reward Feedback Learning is a powerful paradigm for generative modeling, yet its extension to Text-to-Video (T2V) generation is hindered by intractable computational overhead and the scarcity of differentiable reward signals. Although mapping rewards to the latent space reduces computational burdens, existing latent rewards rely heavily on human preference datasets, inherently lacking the rich physical and structural priors of foundational models. In this work, we introduce a novel framework that constructs a latent physics reward by extracting and leveraging priors from a latent world model. We overcome two fundamental hurdles to achieve this integration: 1) developing an alignment mechanism {with a lightweight Aligner} to connect the generative VAE latent space with the target prior embedding space, and 2) adapting the feedback learning algorithm to stably incorporate these latent priors during training. Our method is the first to demonstrate the viability of projecting T2V latent representations into the V-JEPA 2 vision embedding space for enforcing physical plausibility in generated videos. Empirical results on the VideoPhy and VideoPhy2 datasets validate that our lightweight Aligner helps latent reward substantially improves the physical realism and temporal consistency of generated videos, while training within 12.9GB, where backpropagating the same reward through pixel space would require hundreds of GB.

## 154. Learn and Pin: A Transferable JEPA-Style Visual Token Compressor for Frozen VLM Hosts

**Keywords:** visual token compression, vision-language models, JEPA, self-supervised learning

[Main paper PDF](https://openreview.net/pdf?id=CYvu746zb0)

In vision--language models, the image dominates the input: LLaVA-1.5 renders one
image as $576$ tokens, far more than a typical prompt, so most image compute is
spent inside the language model. Existing visual token compressors either
hand-specify the pre-designed method or learn it with task supervision tied to one host. 
None learns label-free model inside a frozen encoder and transfers it, unmodified, to a new host. In this paper, we train a small compressor inside a \emph{frozen} vision encoder without captions. 
It uses a \emph{JEPA-style} predictive term and a \emph{distributional pin}. The pin is a kernel two-sample
statistic that keeps the distribution of the compressed tokens close to the
encoder's own. The compressor then
runs frozen in the encoder's forward pass and is evaluated zero-shot.
We do not quote published numbers. We re-run all competitors, both published
methods and training-free anchors, in one setting. They are matched on token count, or on total cost for decoder-side pruners. 
At $K{=}144$ (a quarter of the tokens) on the LLaVA\,+\,SmolLM2-135M parameter host, the proposed method leads the field by $+9.02\pm1.23$ CIDEr zero-shot and $+11.08\pm2.76$ one-shot at $43.3\%$ of the uncompressed analytic cost.
The compressor transfers unchanged into LLaVA-1.5-7B. It retains
$92$--$97\%$ of the uncompressed ceiling on five of six in-context tasks and
$94$--$99\%$ on five standard benchmarks, at $31\%$ of the analytic cost. It
also transfers to an unseen Q-Former bridge at $96.6\%$ retention, $+5.02$ over
the strongest competitor. On CLIP retrieval, it retains $99.5\%$ of recall at
$K{=}98$ and leads \tome{} by $+0.72$.

## 155. Learning Editable Predictive States for Ocean World Modeling

**Keywords:** World models; Predictive state representations; State perturbations; Joint-embedding predictive architectures; Ocean forecasting

[Main paper PDF](https://openreview.net/pdf?id=PGMj7nN0Lf)

Accurately modeling the coupled evolution of the ocean carbon--physics system and its accompanying events is a long-standing challenge in climate science. Conventional data-driven methods often rely on the regression capacity of neural networks to map past surface fields to future ones without a state into which a physical change could be written, or model individual events in isolation, neglecting the information that sparse event records carry about the continuous fields. In this paper, we propose the State-Perturbation Joint-Embedding Predictive Architecture (SP-JEPA), a world model that represents the environment by a compact state and advances this state autonomously. Central to our method is a basis-anchored state: each frame combines the coefficients of a fixed spatial basis with a learned residual representation, so that a perturbation written into the coefficients changes the decoded field exactly by the prescribed pattern, and a single predictor propagates both the natural and the perturbed futures without reading future observations. Historical fields and source-grounded event observations jointly initialize this state, from which future fields and events are read out. We evaluate natural prediction on three decades of global monthly surface carbon--physics fields with six event families, and response prediction in a controlled transport--exchange environment that provides the true future before and after each perturbation. On the validation splits, SP-JEPA reaches a normalized root mean squared error of 0.131, level with the best field forecaster and 18\% below the best compared latent world model, and fusing historical events lowers event-prediction error by 9--11\% against absent or mismatched event inputs without increasing field error. On mechanisms unseen during training, its rollout reproduces the mean response of each pulse and reaches a response skill of 0.575 and a latent counterfactual skill of 0.206, whereas compared latent world models score below zero.

## 156. Learning from Next-Frame Prediction: Towards Unified and Scalable Visual World Modeling

**Keywords:** Video Representation Learning; Joint Embedding Predictive Architectures; Generative Pretraining; Self-supervised learning

[Main paper PDF](https://openreview.net/pdf?id=914TgLn2iS)

Video provides a natural source of supervision: what happens next serves as a learning signal for visual world modeling. Yet masked video pretraining focuses on recovering missing content from surrounding context rather than predicting the future from the past. Autoregressive methods instead predict forward one token at a time, but have yet to match joint-embedding methods in representation quality. This gap motivates us to revisit the granularity and space of future prediction. In this work, we introduce VANE, a self-supervised visual pretraining framework built on next-frame prediction in embedding space. A causal encoder summarizes past observations for a state predictor that infers the representation of the entire next frame, making temporal evolution the primary learning signal. To retain fine-grained spatial detail alongside semantic content, a lightweight auxiliary generative decoder reconstructs future-frame patches conditioned on the predicted representations. To unify visual modeling across images and videos, we construct a local-to-global crop sequence for still images, allowing the same encoder to predict newly revealed regions from earlier crops under the same objective. Experiments show that VANE improves with model and data scaling, achieving SOTA on most anticipation, recognition, and dense perception benchmarks among unified encoders. Especially on EPIC-KITCHENS-100 action anticipation, it surpasses V-JEPA~2.1 by 7.1 points in mean-class recall@5. These results demonstrate that next-frame prediction in embedding space is effective and scalable for visual world modeling.

## 157. Learning from the Past: Experience Replay Strengthens Joint-Embedding Predictive Learning in Language Models

**Keywords:** Large language models, JEPA, Continual Learning, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=JTTUWxqEfs)

Large language models (LLMs) excel at token-level generation but may learn undesirable abstract semantics and lack comprehensive perception. LLM-JEPA mitigates this by aligning different views of the same underlying knowledge via a joint-embedding predictive architecture (JEPA). However, strong alignment does not necessarily lead to accurate, stable predictions. To address this, we propose ER-JEPA, which adds an episodic replay path to LLM-JEPA. ER-JEPA stores training pairs in a memory. At each step, it stores and retrieves relevant data to provide additional supervision. This enables learning from both the current batch and stored training pairs, providing additional supervision for token prediction and representation alignment. Experiments across multiple datasets (NL-RX, GSM8K, Spider,and NQ-Open) demonstrate that ER-JEPA consistently outperforms LLM-JEPA.

## 158. Learning Graph Representations via Predictive Language Supervision

**Keywords:** Graph Language Model, Latent Predictive Learning, Zero-shot, Graph Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=RSbbxTffpR)

Graph--language pretraining typically relies on autoregressive token prediction or graph--text alignment. Token prediction ties supervision to a particular \emph{linguistic realization}, while alignment may suppress information that is unnecessary for matching but useful for downstream graph tasks. We introduce \textbf{GL-JEPA}, which uses a frozen Text Encoder to define a continuous target for each description and a Predictor to reconstruct this target from graph states. Predicting the full description latent reduces dependence on surface form while encouraging graph states to capture description information that may otherwise be suppressed by alignment. For downstream adaptation, query conditioning allows the Predictor to extract task-relevant information from frozen graph representations. Compared with token prediction, GL-JEPA improves by 25.2--43.8 percentage points the rate at which two valid descriptions both outrank a negative. In a controlled diagnostic, latent prediction achieves 95.6\% probe accuracy on a target-relevant factor, versus 12.7\% for alignment with easy negatives. GL-JEPA also outperforms direct alignment on node-, link-, and graph-level tasks and supports query-conditioned graph question answering across nine tasks with a frozen Graph Encoder.

## 159. Learning Physical Dynamics through Relational Prediction

**Keywords:** Physical Prediction, Relational Learning, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=yTZyqOQkUS)

Predicting physical trajectories in unfamiliar configurations requires reusing local interactions. Trajectory supervision evaluates their combined effect on motion, so fitting training trajectories need not capture how individual relations evolve. We introduce **HORME**, which trains the same pair features for motion computation and prediction of relational evolution. To supervise this evolution during recursive prediction, we propose Reference-Anchored Joint-Embedding Predictive Architecture (RA-JEPA). It matches predicted and observed feature changes pair by pair in a shared space, retaining initial features as a fixed reference. The forecasts condition physical pair features, allowing trajectory errors to train the predictor. Computing displacement further requires resolving when acceleration acts within each step. To capture timing effects missed by sparse acceleration samples, we propose Temporal Response Decomposition (TRD), separating displacement contributions from mean acceleration and its timing. A readout shared across integration stages corrects the timing-dependent component while preserving the current step's velocity update. HORME achieves the lowest trajectory root mean square error (RMSE) among compared methods on I-PHYRE and gravitational N-body, including unseen games, larger systems, and extended horizons.

## 160. Learning to Drive from the Future, Planning Trajectories in One Forward Pass

**Keywords:** Autonomous Driving, World–Action Models, Visual Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=SNIGyRYB8i)

World--action models (WAMs) enrich autonomous-driving policies with future-state supervision, yet it remains unclear which visual representations best support joint future-state and action learning and how to retain the benefits of future supervision in a single-pass planner.
We introduce JEWAM, a Joint-Embedding World--Action Model for joint future-state and action learning, and use this framework to evaluate different visual representations.
Comparisons of features from ViT, MAE, CroCo v2, DINOv3, and V-JEPA under a shared interface show that representation choice substantially affects planning.
V-JEPA's predictive video features achieve the strongest planning results among the evaluated representations, motivating their adoption in the final model.
We further show that future-state supervision improves action learning while its benefits are retained with single-pass, action-only inference.
Direct full-horizon prediction outperforms the tested iterative variants at lower inference cost, supporting effective world--action learning without future rollout or iterative denoising at deployment.
Using only front-view camera observations, JEWAM achieves 90.98 EPDMS on NAVSIM v2 NavTest and 39.86 on NavHard.

## 161. Learning to Ignore What Matters: JEPAs in Stochastic Worlds

**Keywords:** world models, joint-embedding predictive architectures, JEPA, self-supervised learning, stochastic dynamics, model-based reinforcement learning, planning

[Main paper PDF](https://openreview.net/pdf?id=Iv3LeM0evU)

Joint-embedding predictive architectures (JEPAs) learn world models by predicting future representations rather than reconstructing observations. We show that this objective does not protect the information needed for control. We identify two failure mechanisms for jointly trained JEPAs in stochastic environments: the representation can discard the state that decisions depend on, and the predictor can lose decision-relevant features even when the representation keeps them. We test both by training agents entirely inside a JEPA world model and inside a generative world model with the same data and compute, then evaluating them in the real environment. The JEPA supports far weaker control: agents trained inside it survive up to 50 times less often and fail to learn multi-step behavior in Craftax. These failures are not caused by collapse, and rollouts that look correct can still teach agents to exploit errors in predicted rewards and terminations. Low latent prediction error and non-collapsed representations coexist with poor closed-loop performance, so neither is sufficient for control.

## 162. Learning Visuomotor Policies from JEPA Latent Transition Models

**Keywords:** Visuomotor Policy; Robot Policy; JEPA

[Main paper PDF](https://openreview.net/pdf?id=NHSEeACa16)

Video pretraining offers more than visual representations: predictive models also learn how visual states evolve. The success of recent generative world-action models (WAMs) suggests that pretrained transition models can themselves provide a transferable foundation for policy learning. We ask whether this principle extends to latent transition models learned through joint-embedding predictive architectures (JEPAs): beyond transferring the visual encoder, can a predictor that consumes robot actions be repurposed into a visuomotor policy that produces them? We introduce LTM-Policy, which adapts the latent transition model through two complementary routes. A policy route employs learnable action queries to generate robot actions, while a world route retains action-conditioned prediction of future representations from demonstrated transitions. At deployment, the resulting policy generates actions without pixel reconstruction, future-video rollout, or model-predictive search. Controlled experiments show that pretrained transition priors remain beneficial after repurposing the model for action generation. Retaining future-latent prediction during adaptation provides an additional 5.4-point benefit, and the transfer advantage persists in low-data regimes with limited robot demonstrations. Across the four LIBERO suites, LTM-Policy achieves 97.4% average success using only a single forward pass at deployment, without pixel reconstruction or future-video rollout. We further evaluate the method on LIBERO-Plus and real-world manipulation.

## 163. Learning What to Share: Latent Representations for FedRL with Observation Distractors

**Keywords:** Federated reinforcement learning, Latent world models, observation distractors, Proximal policy optimization (PPO)

[Main paper PDF](https://openreview.net/pdf?id=v3M1kQvLMS)

Federated reinforcement learning lets agents in different environments learn a
shared policy by averaging updates without exchanging trajectories. This setting
becomes harder when each observation contains task-irrelevant signals: the policy
must learn from returns which coordinates matter, and each client learns that lesson
from a different noise realisation. We study whether the federation should share
a learned representation rather than raw-observation policies. We formalise the
setting as a federated exogenous block MDP, then train federated PPO with an
encoder whose gradient is routed through the value loss, with or without a self￾supervised objective. The objectives include a JEPA-style multi-step predictor, a
behavioural metric, and a multi-step inverse model. A linear–Gaussian analysis
shows why a noise-free representation is common across clients and why policy￾gradient learning on raw observations pays a fixed-step-size penalty that grows
with the number of distractors. On six MuJoCo tasks with clients that differ in
physical parameters, the critic-trained encoder outperforms FedAvg, FedProx, and
FedKL baselines under 64 appended Gaussian distractors. The gain is largely due
to gradient routing rather than model width. Self-supervised objectives help on
some tasks and hurt on others. For the predictive agent, the gain grows with the
number of i.i.d. distractors, but its size changes with temporal correlation: it is
reduced on several tasks at ρ = 0.99 and remains positive on most. Federation
improves the critic-trained encoder on all four tasks with a single-agent comparison,
although it is not the source of the basic advantage.

## 164. Learning World Models with Joint-Embedding Prediction for Single- and Multi-Agent Reinforcement Learning

**Keywords:** jepa, world model, marl, multi-agent, physical-models, single-agent, reinforcement-learning, latent space, model based reinforcement learning

[Main paper PDF](https://openreview.net/pdf?id=czkLf6XIa2)

World models improve sample efficiency by training policies on imagined trajectories, but their usefulness depends on learning representations that capture the information needed for future control. 
We study whether self-supervised joint-embedding prediction (JEPA) can provide this learning signal in both single- and multi-agent reinforcement learning. 
We introduce MA-JEPA a stochastic world model that replaces observation reconstruction with prediction of target representations, enabling model-based multi-agent reinforcement learning with centralized training and decentralized execution.
A categorical latent state and a causal Transformer are trained with posterior, action-conditioned dynamics, and masked spatial prediction objectives and are then used for actor-critic learning from imagination in the latent space. For multi-agent control, we add a training-only joint predictor that conditions on joint local states and the actions to predict each agent's next local observation representation. 
These predictions are passed through the same local posterior used during real interaction with a centralized critic that is used only for value learning, with execution remaining decentralized. 
Our experiments show that this architecture performs strongly on SMAC, matching or exceeding the strongest reported comparator median on three of six evaluated maps.

## 165. LeCompass: Task-Level Execution through State-Indexed Interfaces

**Keywords:** World Models; Joint-Embedding Predictive Architectures; Task-Level Execution; Model-Based Planning; Test-Time Search

[Main paper PDF](https://openreview.net/pdf?id=3cbewEIfpL)

Action-conditioned joint-embedding predictive architectures (JEPAs) offer a foundation for predictive decision-making by modeling the consequences of actions in representation space. Yet evaluating local reachability in latent space does not by itself provide a task-level execution interface: intermediate targets must be generated, local inference has finite budgets, and execution requires spatial feedback and persistent interaction state. We introduce LeCompass, a state-indexed execution framework built around a frozen LeWorldModel (LeWM). A proposer supplies intermediate latent targets, while CompassFlow searches the source space of a learned trajectory prior to obtain effective action candidates under limited predictive-evaluation budgets. Patch-token readouts provide spatial feedback, while observation-based memory supports phase transitions and bounded recovery. State-indexed targets support cross-episode context–goal composition. On 1,000 official TEST full-episode Cube trials, the complete LeCompass execution system achieves 86.9% native 4-cm reach. Separate matched analyses show that predictive ranking raises success from 4.7% to 44.9% on TEST PushT and from 33.8% to 77.7% on TEST TwoRoom, whereas Cube retains 86.4% native reach without predictive ranking. These results demonstrate task-level execution with task-dependent roles for latent target proposal, predictive search, and observation-grounded control.

## 166. LeDreamer: Bridging the Understanding of Representation Collapse Between JEPA and Sample-Efficient World Models

**Keywords:** World Models, Model-Based Reinforcement Learning, Representation Collapse, Joint Embedding Predictive Architecture (JEPA), Sample-Efficient World Models (SEWM), Self-Supervised Learning, Discrete Representations, Sample-Efficient Reinforcement Learning, Decoder-Free, Atari 100k

[Main paper PDF](https://openreview.net/pdf?id=ZwKRzEKmkr)

Joint Embedding Predictive Architectures (JEPAs) efficiently learn representations without pixel-level reconstruction, with recent methods seeking to replace stabilization heuristics such as stop-gradient with the minimization of well-defined objectives. Although the Sketched Isotropic Gaussian Regularizer (SIGReg) prevents representation collapse in continuous JEPAs, its direct application does not account for the factorized structure of discrete categorical latents used by sample-efficient architectures such as DreamerV3. In these latents, shifts applied to the logits of each categorical distribution do not change the resulting probabilities, but can still affect the regularization objective. We introduce LeDreamer, a decoder-free transformer-based world model that addresses this mismatch by applying SIGReg per distribution to pre-sampling categorical logits. We prove that applying SIGReg to the flattened representation, formed by concatenating the logits of all categorical distributions, admits zero-information solutions whose regularization cost decreases as $\mathcal{O}(1/K)$ with the number of categorical distributions $K$, whereas applying SIGReg independently to each distribution assigns every such solution a positive cost independent of $K$. Empirically, per-distribution SIGReg prevents marginal representation collapse where flattened regularization fails. We further find that preventing marginal collapse is insufficient for control: in this setting, retaining stop-gradient remains necessary to learn sufficiently action-sensitive dynamics and achieve competitive agent returns. To systematically evaluate these effects, we introduce Atari-5-100k, a statistically selected five-game ablation suite derived from results for 32 recent sample-efficient world models. Across the complete 26-game Atari 100k benchmark, LeDreamer recovers 79.7\% of the interquartile mean score of DreamerV3 while training 2.12 times faster, performing on par with recent decoder-free alternatives while training between 2.0 and 3.8 times faster than evaluated decoder-enabled architectures.

## 167. LeGramJEPA: Negative-Free Multimodal Graph Foundation Models in Latent Space with Volumetric Alignment and SIGReg

**Keywords:** Graph Learning, MultiModal, SIGReg, JEPA, Information Maximization, Text-Attributed Graphs

[Main paper PDF](https://openreview.net/pdf?id=KAU2j8VAsa)

Self-supervised learning on text-attributed graphs enables graph foundation models that transfer to out-of-distribution graphs without labels. The standard approach aligns a graph encoder and a text encoder with a contrastive objective, pulling positive graph-text pairs together and pushing mismatched pairs apart. This depends on large numbers of negative pairs, and extending it beyond two modalities requires a pairwise alignment term for each pair of modalities, so the number of terms grows quadratically. We present LeGramJEPA, a latent-space approach to multimodal graph self-supervised learning that uses no negatives and whose alignment cost grows linearly in the number of modalities. LeGramJEPA replaces the contrastive term with a volumetric alignment objective and constrains each encoder’s output distribution toward an isotropic Gaussian with SIGReg to prevent embedding collapse. The volume term couples all modalities in a single quantity per anchor, reducing the number of alignment terms from quadratic to linear in modalities compared to cross-modal methods. Pretraining with LeGramJEPA is competitive with contrastive baselines on zero-shot node classification and improves over them on link prediction. Under a three-modality (graph, text, image) training and transfer scheme, LeGramJEPA consistently outperforms its contrastive counterpart across modality pairs

## 168. LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics

**Keywords:** self-supervised learning, video pretraining

[Main paper PDF](https://openreview.net/pdf?id=p6BV8mTYj3)

Video carries the temporal structure of the physical world, yet learning representations from it remains computationally expensive. Current self-supervised methods either prevent representation collapse through architectural asymmetries (an exponential-moving-average target encoder, a stop-gradient, and a predictor), or avoid it by reconstructing masked content in pixel space with a dedicated decoder. We introduce LeVJEPA, the first extension of LeJEPA to video. A single encoder is trained with an invariance loss between global and local views of a clip, while collapse is prevented by SIGReg with provable guarantees. Thus, neither architectural asymmetries nor pixel reconstruction is needed. This formulation has two properties that we study in this paper. First, the pretraining cost depends only on the number of tokens the encoder observes. Dropping tokens uniformly at random reduces this number and, at the same time, improves downstream accuracy. At matched epochs on identical data, LeVJEPA matches or outperforms V-JEPA~2 across ViT-S/B/L with $5.6$ to $20.8\times$ less pretraining compute. At matched FLOPs, it exceeds the strongest video baseline by $7.6$ points on ImageNet-1K while remaining competitive on motion-centric benchmarks. Second, since no target encoder or predictor is involved, the encoder can be trained with block-causal attention without loss in accuracy, so that the representation of each frame depends only on past frames. Finally, compared to DINOv2 trained on frames of the same videos with matched compute, LeVJEPA remains within $3.1$ points on ImageNet-1K while nearly doubling the accuracy of DINOv2 on Something-Something-v2. These results suggest that, once its computational overhead is removed, video is a viable substrate for general-purpose visual pretraining.

## 169. LeWAM: End-to-End World and Action Modeling with JEPAs

**Keywords:** JEPA; Visual Control; World Action Model

[Main paper PDF](https://openreview.net/pdf?id=aOc1yAaYmW)

Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction. However, existing JEPAs typically learn representations and dynamics independently of downstream control objectives, complicating the pipeline and leaving unexplored how world- and action- learning benefit each other. We introduce LeWAM, an end-to-end JEPA for control with: (1) a joint training objective over next latent state prediction and action flow matching, and (2) an isotropic Gaussian constraint on the latent state, enabling a single model to support direct policy execution and efficient planning by evaluating sampled actions with its learned latent dynamics. Compared with prior JEPAs in visual planning, LeWAM improves success rate from 26.8% to 85.5% on contact-rich tasks and from 10.9% to 46.2% on long-horizon tasks, and plans 32.3x faster. On behavior cloning tasks in simulation and physical robots, LeWAM is also competitive with established methods. Interpretability analyses show that LeWAM learns control-relevant representations and action distributions effectively guiding test-time planning and control.

## 170. LeWM++: Repairing the Planning Interface of Latent World Models

**Keywords:** JEPA, Latent World Models, Long-Horizon Planning, Planning Interface, Hierarchical Planning, Goal-Conditioned Planning

[Main paper PDF](https://openreview.net/pdf?id=RIpEtbedmF)

Latent world models enable visual control without reconstructing pixels, yet remain unreliable over long horizons. We identify three planning mismatches that worsen with goal offset: target mismatch between a distant goal and a short reliable rollout; search mismatch between sparse effective action sequences and uninformed sampling; and cost mismatch between goal-reaching semantics and restrictive terminal-only cost. Addressing these failures requires a planning interface that effectively translates latent representations into actions. We introduce LeWorldModel++ (LeWM++), a planning-interface framework built on a frozen latent world model. LeWM++ comprises three complementary components guided by a central principle: preserving global intent through the final goal while using a local target to drive short-horizon planning. LatentPathFlow generates a temporally aligned latent path and uses its endpoint as the local target; a final-goal-conditioned Action Chunk Prior guides CEM search with temporally coherent action-chunk proposals; and Min-over-Horizon scores each rollout by its closest approach to the local target. On the LeWM Control Suite, LeWM++ achieves the highest average success at all four evaluated goal offsets; as goal distance increases, its lead over LeWM grows from 12.0 to 32.3 percentage points. Across eight visual OGBench datasets, LeWM++ achieves 50.62% average success, exceeding the model-based planning method Latent Diffusion Planning (LDP) by 34.2 percentage points. On two real-robot tasks, LeWM++ outperforms goal-conditioned Diffusion Policy by 18.9 percentage points, demonstrating its control effectiveness under the hardware protocol. These results show that effective latent planning depends not only on predictive dynamics, but also on aligning the planner's target, proposal, and cost.

## 171. LIFT-JEPA: Task-Aware Joint-Embedding Supervision via Target Interventions for Spatiotemporal Forecasting

**Keywords:** joint-embedding predictive architectures, self-supervised representation learning, task-aware supervision, spatiotemporal forecasting, radar precipitation nowcasting

[Main paper PDF](https://openreview.net/pdf?id=Frtg5fWc75)

In spatiotemporal forecasting where task-critical phenomena are sparse, prediction losses applied in observation space allow pixel-wise errors in task-critical regions to be directly reweighted. By contrast, joint-embedding predictive learning applies the loss in representation space; because latent units lack an explicit correspondence to task semantics expressed in observation space, observation-space task weights cannot be directly applied to the representation-matching loss.
To this end, we introduce LIFT-JEPA (\textbf{L}atent \textbf{I}mportance \textbf{F}rom \textbf{T}arget Interventions for Joint-Embedding Prediction). Given a future observation, LIFT-JEPA constructs an intervened counterpart by removing task-critical structures and encodes both using the same target encoder. The resulting representation differences are used to estimate the task relevance of individual representation units and reweight their matching losses, thereby translating task priorities specified in observation space into representation-space supervision.
We evaluate LIFT-JEPA across precipitation nowcasting and urban traffic flow prediction using three forecasting backbones with distinct inductive biases. Compared with Vanilla JEPA and alternative task-weighting strategies, LIFT-JEPA consistently improves task-relevant forecasting performance across both domains, from intensity-defined targets in radar nowcasting to temporal-drift targets in traffic flow prediction. These results demonstrate that LIFT-JEPA can translate task semantics ranging from spatial intensity structures to temporal drift into effective representation-space supervision.

## 172. LocaLeJEPA: Maximum Entropy Representations under Geometric Priors

**Keywords:** JEPA; Self-Supervised Learning; Geometric Deep Learning; Entropy-Maximization;

[Main paper PDF](https://openreview.net/pdf?id=X4kZhguynv)

Joint-Embedding Predictive Architectures (JEPA) offer a compelling approach to self-supervised learning, but are typically prone to representation collapse. LeJEPA resolves this by introducing a provably robust distribution-matching objective that drives the embedding towards an isotropic Gaussian. However, this approach is fundamentally tied to Euclidean assumptions. Therefore, it is incompatible with the incorporation of domain-specific geometric priors, such as the use of non-Euclidean embedding geometries, e.g., equivariant CNNs or hyperbolic ViTs. We thus introduce LocaLeJEPA, a framework motivated by a manifold-theoretic reformulation of LeJEPA’s entropy-maximization property. The accompanying LocaLeReg, a novel locally Euclidean distribution-matching regularizer, enables a robust, practical implementation of the LocaLeJEPA framework. We then perform extensive experiments on models trained on ImageNet-1k. LocaLeJEPA outperforms LeJEPA not only when paired with hyperbolic ViT-S/8 and equivariant ResNet-50 backbones, but even with an ordinary Euclidean ViT-S/8, both in terms of linear and kNN classification performance on ImageNet and on a series of downstream tasks tested. Overall, we view the LocaLeJEPA formalism as a principled approach to the JEPA paradigm that better respects intrinsic data geometry while also accommodating generalizations to exotic embedding geometries.

## 173. LocalProp: Neuro-Localized Memory-Efficient Backpropagation

**Keywords:** neural network optimization, efficient learning, neural network training

[Main paper PDF](https://openreview.net/pdf?id=X5gp1Cy51A)

The current deep learning training paradigm employs end-to-end backpropagation, regardless of the training stage, i.e. pre-training or fine-tuning. However, backpropagating through the entire model is neither biologically plausible nor memory efficient, since learning inside the brain is highly localized. Therefore, we propose LocalProp, a training procedure that locally updates the weights of a model. Our neuro-localized weight updates follow the "pre-training then fine-tuning" paradigm, where the pre-training is based on I-JEPA. After locally updating the  weights, a pruning operation is performed, followed by a short final fine-tuning phase. Pruning helps by sending the learning signal from higher blocks to lower blocks. We perform experiments on several datasets, including large-scale benchmarks such as ImageNet, and empirically show that LocalProp reaches good performance at a fraction of GPU peak memory. By varying the number of jointly optimized blocks, we identify gradient-propagation span as a practical control over the accuracy-memory trade-off. We publicly release our code at https://see.supplementary.

## 174. Locating Memory In Predictive World Models: Interventional Diagnosis Beyond Probing

**Keywords:** interpretability, probing, world models, latent dynamics, causal intervention, JEPA, memory, recurrent neural networks

[Main paper PDF](https://openreview.net/pdf?id=CdxFd9WDU6)

Linear probing is the default instrument for asking what a learned representation encodes, but it cannot say how a model retains that information. We exhibit three world models — a stateless Joint Embedding Predictive Architecture (JEPA), a GRU and an LSTM — that reach identical probe accuracy (1.000) on the same delayed working-memory task while implementing mechanistically incompatible forms of memory. To separate them we introduce nested interventional diagnostics: stable retention (SR) asks whether information about a past causal event survives a latent rollout; an interventional causal separation test, with a 2x2 extension that toggles recurrent state, asks where the memory resides; and the causal-subspace Lyapunov factor lambda_v(t) asks how the predictor sustains it. Three findings follow. Memory locus is a property of the trained model rather than of the architecture class: GRU and LSTM seeds trained identically span from near-pure state-based to predominantly dynamical solutions, a spread invisible to probe accuracy. A stateless predictor sustains memory by selective subspace preservation: at a prediction horizon of K = 5 it contracts sampled latent distances on average (kappa ~ 0.36) while amplifying the causal direction 6.48x relative to a typical direction, a condition strictly weaker than the global norm preservation that unitary and orthogonal recurrent parameterisations enforce. And a controlled ablation that redistributes a trained encoder's causal weight across an orthonormal basis, holding predictor, task and training protocol fixed, drives stable retention from 0.458 to 0.107 and causal-subspace amplification from 14.2 to 4.3: encoder geometry causally gates whether dynamical memory is available at all.

## 175. Loop LeWorldModel: Reliable Recursion for Depth Reuse and Temporal Rollout in Latent World Models

**Keywords:** World Models; Looped Transformers; Post-Training; Joint-Embedding Predictive Architectures; Self-Correction

[Main paper PDF](https://openreview.net/pdf?id=qMigUOhEAK)

Visual world models based on joint embedding predictive architectures (JEPAs) support planning by predicting action consequences before execution. In real-world deployment, compact and reliable end-to-end world models are increasingly needed under limited computational and memory budgets. Recursive layer sharing offers a natural way to reduce model size. However, naively looping pretrained layers across depth erases depth-specific computations, and recursively feeding predicted states back often accumulates errors and destabilize imagined trajectories. To address these two issues, we propose Loop LeWorldModel, a loop-based adaptation of pretrained visual world models. Specifically, we utilize depth-specific low-rank adapters to preserve distinct transformations at each loop. Additionally, we design a training-free self-correction gate to suppress abnormal prediction steps using recent motion statistics. Extensive experiments on various visual-control tasks demonstrate that Loop LeWorldModel can significantly improve planning success with fewer parameters and less accumulated errors than the original model. All source codes will be released online.

## 176. Low-Dimensional Decision Spaces for Latent World-Model Planning

**Keywords:** Visual Planning, World Models, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=1s8WwVeI6e)

Latent world models can make visual planning more efficient by predicting in representation space rather than pixel space. However, conventional methods
still predict a separate high-dimensional latent trajectory for every candidate
action sequence, even though much visual information is shared across
candidates. We study the variation among candidate outcomes for a fixed
context, goal, and planning horizon, and refer to it as the *decision
space*. Our analysis shows that a small number of directions
captures most candidate variation while preserving much of the
candidate-ranking signal used for action selection. Based on this finding, we
introduce the Low-Dimensional Decision World Model (LDD-WM). LDD-WM performs one
shared, action-free visual rollout and uses an action-conditioned component to
update a compact $r$-dimensional state for each candidate. The model is trained
from physical-cost ordering and avoids reconstructing a separate full latent trajectory
for every candidate. Across six datasets, LDD-WM consistently outperforms
conventional full-latent reconstruction world models while requiring less
computation and lower latency at inference. On MetaWorld Reach-Wall, LDD-WM
improves success from $29.9\%$ to $64.6\%$ over JEPA-WM while reducing
inference computation by a factor of $150$ and running $71\times$ faster.
These results support decision-space modeling as an efficient alternative to
full-latent prediction for visual planning.

## 177. Lower Loss by Forgetting: How Trainable Targets Suppress Information in JEPA World Models

**Keywords:** self-supervised learning, joint-embedding predictive architectures, world models, representation learning, latent-space planning

[Main paper PDF](https://openreview.net/pdf?id=jUDCutOLmH)

Joint-embedding predictive architectures (JEPAs) learn world models by predicting future representations and can reduce prediction error by suppressing information already present in their representations. We identify gradients through the learned prediction target as a mechanism for this suppression. Our gradient decomposition shows that, with an optimal
predictor and a linear encoder aligned with independent factors, the target contribution attenuates each factor at a rate proportional to its innovation variance. A quadratic covariance penalty yields a closed-form retention threshold and links retained variance to each factor's weight in the linear model's planning distance. Controlled experiments with initially decodable synthetic signals support the predicted ordering, with higher-innovation signals losing decodability earlier. In a simulated pushing task, a model acquires and subsequently suppresses information about block position. A state variable can also remain decodable while having little influence on the latent distance used for planning. 
On the Cube manipulation task from OGBench, weaker regularisation reduces normalised prediction error by $3.4\times$ while lowering contact-related decodability and planning success. Paired head interventions improve Cube planning, but their benefits depend on the task. These findings identify a mechanism by which predictive training can impair a representation for control, and motivate evaluating information retention and its influence on planning distance alongside prediction accuracy.

## 178. LpWM: A Case for Sparse Representations in World Models

**Keywords:** JEPA, Sparsity, World Models, Planning, Self-Supervised Learning, Information Maximization

[Main paper PDF](https://openreview.net/pdf?id=4SAQxyCPrC)

Joint-embedding predictive architectures (JEPAs) learn latent dynamics for planning and avoid representation collapse by matching features to maximum-entropy distributions such as isotropic Gaussians, yielding dense representations. However, it is unclear if dense representations are the most favorable geometry for modeling dynamics. In this work, we ask whether a different geometry such as sparse representations can make action-conditioned latent dynamics easier to model, and what dynamical structure emerges from such representations. We first show that nonlinear Lipschitz dynamics can be approximated arbitrarily well by action-conditioned linear dynamics in a sufficiently high-dimensional one-hot latent space, with rollout error vanishing as the dimension grows. This motivates distributed sparse representations as a practical relaxation of one-hot sparsity. We introduce LpWorldModel (LpWM), a JEPA model regularized with Rectified Distribution Matching Regularization (RDMReg) to match encoder features to a Rectified Generalized Gaussian distribution, yielding non-negative sparse codes. Empirically, sparsity lowers the predictor complexity required for successful planning: on PushT, sparse LpWM outperforms dense LeWM by up to 57\% in planning success at intermediate predictor capacities. This advantage also extends beyond Gaussian distribution matching, with LpWM outperforming dense VICReg representations across multiple predictor families. We further find and provide proven guarantee that the learned sparse representations on piecewise-affine dynamics are mode-factored, with support encoding discrete dynamical regimes and feature magnitudes capturing continuous within-regime state. Together, these results suggest that sparse representations reduce the predictor complexity for control while revealing interpretable structure.

## 179. LRC-JEPA: Disentangling Dynamics and Residual Context for Efficient World Models

**Keywords:** world model, representation learning, vision encoder, vision transformer, JEPA, model-based control

[Main paper PDF](https://openreview.net/pdf?id=3zhvqj1Gl9)

Compact JEPA world models enable efficient latent-space planning, but low-dimensional representation trained under reward-free self-supervision must encode both action-conditioned dynamics and predictable visual context. This competition can entangle controllable state with high-rank nuisance appearance and degrade planning as scenes become more complex. We introduce LRC-JEPA, a lightweight end-to-end world model that routes information into a compact predictive latent $\mathbf{z}$ and learned-query residual-context embeddings $\mathbf{u}$. Only $\mathbf{z}$ is propagated by the dynamics model and used for planning, while $\mathbf{u}$ captures temporally persistent information for cross-attention reconstruction; a differentiable residual connection encourages the latent to retain complementary dynamic content. Under explicit assumptions, we show that the resulting representation is sufficient, minimal, nuisance-invariant, and disentangled. Across four simulated control environments, LRC-JEPA improves average planning success over a parameter-matched JEPA baseline by 9 percentage points and matches or exceeds substantially larger pretrained models. On the real-world Bridge-v2 set, its 5.5M-parameter active encoder outperforms DINO-WM (22.1M) and V-JEPA2 (303.9M) encoders while also enabling faster planning. Physical-state probes, reconstruction interventions, and ablations confirm the effectiveness of LRC-JEPA's representation disentanglement.

## 180. LS-JEPA: Learning Long Short-Term  Dynamics for Fast Latent Planning

**Keywords:** World Model, JEPA, long short-term

[Main paper PDF](https://openreview.net/pdf?id=1XJs03cwyl)

Joint-Embedding Predictive Architecture (JEPA) offers a promising route to model-based control by predicting future latent dynamics. Current approaches mainly adopt one-step prediction objectives, which fail to capture the long-term latent transitions for action recovery. In this work, we introduce LS-JEPA, an end-to-end latent world model that jointly learns forward and inverse dynamics across Long Short-term temporal scales. Specifically, LS-JEPA combines one-step prediction with fixed-horizon autoregressive rollout, while an endpoint-conditioned action decoder reconstructs both individual actions and multi-step action sequences from latent displacements. These complementary objectives encourage predictive, action-relevant representations and directly connect latent transitions to control. Furthermore, the learned one-step and multi-step inverse mappings can be naturally used for fast latent planning during the inference time. We propose a Test-Time Replanning (TTR) strategy in which a goal-directed action sequence is decoded and then a one-step correction from a fresh observation is applied to refine the action. Extensive experiments are conducted to validate our proposed approach. The results show that LS-JEPA achieves the state-of-the-art results with 96.00%, 100.00%, 99.67%, and 100.00% on Push-T, OGBench-Cube, Reacher, and Two-Room, respectively, yielding a macro-average of 98.92% with only 11 ms of planning time per decision. These results suggest that jointly learning Long Short-Term forward and inverse dynamics with our proposed TTR strategy enjoys both the accuracy and efficiency for latent planning. Code is available at https://anonymous.4open.science/r/LS-JEPA-E034/.

## 181. MacJEPA: Missingness-Robust Audio-Visual Recognition from Untrimmed Egocentric Videos

**Keywords:** audio-visual recognition, missing-modality robustness, untrimmed egocentric videos, Joint-Embedding Predictive Architectures, multimodal learning

[Main paper PDF](https://openreview.net/pdf?id=V0D9Az1N95)

Audio-visual models improve egocentric action recognition by exploiting
complementary cues, yet typically assume that both streams remain available at
inference. Existing missing-modality methods operate on trimmed, single-event
clips in which a stream is entirely present or absent, whereas real sensors fail and recover within long, untrimmed observations. We redefine egocentric modality
missingness as temporally localized sensor outages within untrimmed, multi-event
observations, with whole-clip absence as the limiting case. We introduce
MacJEPA, a missing-modality-robust Masked-context query JEPA that recognizes visual actions and acoustic events from
supplied interval queries over audio-visual context. Window-local modality dropout simulates these sensor outages during training. MacJEPA further repurposes masking in JEPA from a self-supervised pretext into a supervised robustness objective, aligning masked and clean latent representations of both multimodal content tokens and the
task-conditioned queries. All objectives are optimized jointly with recognition in a single stage, requiring no test-time adaptation. Across Epic-Kitchens-100 and Epic-Sounds, a single checkpoint
remains competitive under complete input and consistently surpasses published
missing-modality baselines when either the dominant or auxiliary stream is
removed. MacJEPA thus unifies strong full-input recognition with temporal
missing-modality robustness in a single model operating on untrimmed multi-event
videos.

## 182. ManiJEPA: Manifold-Aware JEPA World Models via Directional Contraction

**Keywords:** World Models, Long-horizon Planning

[Main paper PDF](https://openreview.net/pdf?id=ydmjm7miuG)

Joint-embedding predictive architectures learn world models by predicting future representations from current ones, enabling planning directly from pixels. But when the predictor is rolled out autoregressively at planning time, small errors compound exponentially, making long-horizon control unreliable. Existing fixes either leave the exponential form unchanged or force the predictor's Jacobian to uniformly contract, bounding error at the cost of destroying the sensitivity to early actions that planning requires. We show that this tension has a principled resolution: constrain only the directions that the training data cannot identify. Because encoder latents from reachable observations lie on a low-dimensional manifold, the predictor's behavior normal to the manifold is never observed by the teacher-forced loss and can be regularized at no bias cost, while the tangent directions that carry dynamics and control signal are preserved. ManiJEPA estimates the local tangent space of the latent manifold via local PCA on neighboring latents, decomposes the predictor Jacobian into tangent and normal blocks, and imposes three hinge penalties: normal contraction, a tangent shell that preserves on-manifold gain, and a leak term that blocks error from flowing back into the tangent space. An explicit feasibility condition coupling these penalties guarantees at most linear rather than exponential error growth, and a control-authority lower bound ensures early actions retain influence over the plan. On PushT, TwoRoom, OGBench-Cube, and LIBERO-Goal, ManiJEPA matches baselines at short horizons and substantially outperforms them at long horizons, with ablations confirming that each directional component is necessary.

## 183. Marginal normality does not constrain time: a prescribed Gaussian path law for JEPA world models

**Keywords:** world models, joint-embedding predictive architectures (JEPA), self-supervised learning, representation learning, temporal dynamics, optimal experimental design, visual planning

[Main paper PDF](https://openreview.net/pdf?id=03pJ3i4TMn)

SIGReg, the anti-collapse regulariser of the LeWM world model, constrains the latent marginal at each time step and says nothing about how consecutive steps relate: a latent that is constant along every trajectory attains the global minimum of both training terms, and the identifiability theory for this objective assumes exactly the cross-time structure it never enforces (Klindt et al., 2026). We close the gap with **T-SIGReg** (temporal SIGReg), which prescribes the joint law of a trajectory window, $\mathcal{N}(0, R_{\rho,h} \otimes I_d)$, with the profile $R_{\rho,h}$ measured from the observation stream before training, and enforces it with the characteristic-function test SIGReg already uses, pointed at a *separable sketch* $q \otimes v$ that keeps the cross-time signal a full-sphere draw averages away, at cost $O((h{+}1)d)$. Which measure supplies $q$ is an experimental-design variable: the temporally optimal design gives up the spatial law, and mixing the marginal directions back in restores it at a cost linear in the mixing weight. On four pixel-based control suites under a paired protocol, prescribing the measured path law raises planning success on TwoRooms from 63.7 to 100.0, improves Reacher and Cube by more than twice the largest retraining threshold we measured, and on Push-T recovers the loss an AR(1) prior incurs against the control; prescribing no cross-time structure at all falls below the control in all four suites.

## 184. MedJEPA: Latent Cross-Modal Prediction for Medical Vision-Language Reasoning under Missing Images

**Keywords:** JEPA, Missing Modality, Reasoning

[Main paper PDF](https://openreview.net/pdf?id=vAuRWaRTQT)

Vision Language Models (VLMs) have become effective tools for reasoning over medical images, yet their multimodal reasoning pathways typically assume that the image is available at inference. In many real-world clinical scenarios, images may be unavailable because they are not transmitted across clinical workflows, are withheld due to privacy or data-sharing constraints, are corrupted during transmission, or have not yet been acquired. Existing missing-modality methods rely on prompt adaptation, retrieval, or modality reconstruction, but these strategies either work around the missing input or attempt to recreate the observation itself, rather than directly recovering the latent visual representation that the downstream VLM was trained to reason over. To overcome these limitations, we propose \textsc{MedJEPA}, a latent cross-modal prediction framework inspired by the Joint-Embedding Predictive Architecture (JEPA). Given only the clinical text and the corresponding question, \textsc{MedJEPA} predicts the patch-level visual representations that a frozen medical VLM would extract from the missing image, without synthesizing pixels.The predictor is trained with a JEPA-style masked latent objective in CLIP feature space, using the frozen image representation as a stop-gradient target. A masking curriculum spans partial to complete visual absence, with patch annealing progressively removing real visual tokens and iterative self-refinement improving the latent prediction from previous estimates. At inference time, the predicted visual tokens are projected through the frozen multimodal projector of the VLM and injected into its visual stream. A confidence-gated cascade then progressively evaluates sparse and dense visual-token injection, reverting to text-only reasoning when the predicted visual signal fails to improve the model’s confidence. Across PMC-VQA and ScienceQA, \textit{MedJEPA} consistently improves image-absent accuracy, from 70.8\% to 73.4\% on PMC-VQA and from 68.8\% to 72.3\% on ScienceQA, yielding gains of 2.6 and 3.5 percentage points, respectively. Ablations confirm the benefits of latent prediction, anti-collapse regularization, and self-refinement. These results show that latent cross-modal prediction enables medical VLMs to reason more reliably when images are unavailable.

## 185. MemJEPA: Erasure-Trained Memory Lets Latent World-Model Planners See Through Occlusion

**Keywords:** world models, JEPA, latent planning, occlusion, recurrent memory, frozen encoders, model predictive control, partial observability, robot manipulation

[Main paper PDF](https://openreview.net/pdf?id=SrOV8zNnVl)

A latent world model can imagine the consequences of its actions in a learned state space, enabling model predictive control in robotics. However, an agent often loses sight of what it controls, such as when its arm moves out of the camera's frame. A windowed joint-embedding predictive architecture (JEPA) planner is then blind to the hidden actor, and adding memory trained only on visible clips does not help. We introduce Memory-Augmented JEPA (MemJEPA), which carries a recurrent belief through the planner's imagination and trains it with actor erasure: the actor is removed from the input clips but kept in the prediction targets. Theoretically, we show that a fixed-window latent planner cannot react to a hidden actor's motion that leaves no trace in its window, making memory of earlier frames necessary, and that erasure training against clean targets provides a learning signal for a useful carried state. Empirically, MemJEPA was tested on three image-based control tasks (reaching, pushing, navigation) with the frozen encoder of LeWorldModel (LeWM). MemJEPA raises average success under actor occlusion from 13% to ~75% against a memoryless twin trained on the same data with the same actor erasure, while matching or exceeding its performance with the actor in view. The hidden-view gains transfer, at a smaller size, to a DINO-WM backbone.

## 186. MEND: Measuring and Constraining Latent Dynamics in World Models

**Keywords:** world models; joint-embedding predictive architecture; long-horizon prediction; Lyapunov exponents; symplectic structure; representation collapse

[Main paper PDF](https://openreview.net/pdf?id=itoxkUzY2n)

World models used for planning and simulation must preserve dynamics under repeated prediction. In joint-embedding predictive architectures (JEPAs), one-step accuracy does not ensure this behavior. We formulate latent prediction as an approximate semi-conjugacy. In the linear-symplectic setting, this relates dimensional collapse to encoder rank and prediction drift to predictor spectrum. MEND measures frequency, instability, and contraction in latent trajectories and uses these measurements to constrain a new predictor while keeping the encoder frozen. An orbit-averaged log-determinant separates physical dissipation from least-squares attenuation. An autonomously iterated V-JEPA~2 predictor has at least 12 positive finite-time Lyapunov exponents and loses an oscillator signal within $15$ to $21$ steps, while the encoder retains it. On a real pendulum video, MEND constrains a conformal-symplectic predictor in a two-dimensional observable. It extends the open-loop horizon from 21 to 651 steps (0.6 to 18.4 periods), approximately 31 times, while following the observed decay. These results support video-based system identification and prediction of mechanical motion using frozen representations. Extending the constraints to action-conditioned world models could support longer-horizon planning and control.

## 187. Meta-Causal Predictive States: A World Model for High-Dimensional Event Sequences

**Keywords:** foundation models, event sequence, forecasting, jepa, discrete event sequences, time series, world models

[Main paper PDF](https://openreview.net/pdf?id=Yq5R7PEJEe)

While current temporal foundation models transfer across domains through a shared numerical observation space, high-cardinality discrete event streams, such as those in cloud systems or clinical care, describe system dynamics through symbols whose identities are local to each domain. This limits direct vocabulary sharing even when different systems exhibit similar predictive structures. To address this constraint, we propose a world model for high-dimensional discrete event sequences organized around meta-causal predictive states, which group equivalence classes of histories whose conditional future distributions coincide up to event relabeling. Our main hypothesis is that transferable event dynamics can be expressed through a shared predictive vocabulary, while context binds this vocabulary to local event identities. We realize this through a two-stage framework: (i) DES-JEPA, which learns discrete event representations from causal occurrence statistics using predictive teacher-student training, and (ii) DES-PFN, which learns in-context dynamics over the frozen representations and decodes event types, enabling autoregressive forecasting without target-task parameter updates. Pretrained on a mixture of six synthetic process families and evaluated on six diverse real-world domains, our analysis demonstrates that DES-PFN is competitive on low-cardinality datasets and, to our knowledge, the first method to successfully scale zero-shot forecasting to hundreds of event types.

## 188. Metro-WM: Long-Horizon Latent Planning with Realisable Sub-Goals

**Keywords:** world models, hierarchical planning, model-predictive control, joint-embedding predictive architectures

[Main paper PDF](https://openreview.net/pdf?id=ydh3XsRypN)

Model-predictive control with Joint-Embedding Predictive Architectures (JEPAs) provides a strong zero-shot goal-reaching planner, but it is only effective over short planning horizons. Hierarchical extensions attempt to bridge this gap by learning a macro planner to predict intermediate latent sub-goals to guide the micro planner. In this work, we demonstrate that unconstrained latent sub-goal prediction is fundamentally flawed. A rigorous evaluation reveals that a leading state-of-the-art macro planner routinely emits physically unrealisable sub-goals. To resolve this, we introduce Metro-WM, a hierarchical framework that issues sub-goals by retrieving genuine states from prior experience rather than generating ungrounded latent vectors. Specifically, Metro-WM constructs a graph whose vertices are observed frames from offline expert demonstrations or random-action trajectories, allowing frames from different episodes to be connected and stitched into routes to the goal. Planning over the full graph also makes the system highly robust to execution errors: if the micro planner drifts off course, Metro-WM instantly finds a new optimal path from the current state. Our experiments show that Metro-WM achieves superior long-horizon success rates of up to $37.33$ percentage points over the next best hierarchical approach while being up to $10.9\times$ faster, requiring both $13\text{--}56\times$ less offline compute and fewer tuned hyperparameters. Additional analysis reveals that Metro-WM finds shorter paths than the offline demonstrations, outperforms an oracle relying on the query's own demonstration, and maintains robust performance under extremely sparse dataset conditions.

## 189. MoJEPA: Joint-Embedding Predictive Learning for Dynamic Graphs with Discrete Morse Theory

**Keywords:** Dynamic Graph Representation Learning, Joint-Embedding Predictive Architecture, Discrete Morse Theory, Self-Supervised Learning, Temporal Link Prediction

[Main paper PDF](https://openreview.net/pdf?id=QVudSYUo68)

Self-supervised pretraining on dynamic graphs can reduce reliance on task-specific labels and support transfer across datasets. In joint-embedding predictive architectures (JEPAs), the learning task is jointly defined by what is masked and what context remains available for prediction. On dynamic graphs, these choices face two fundamental coupled challenges. First, masking interactions also removes relational evidence needed for prediction. Second, changing interactions limit the context available at each time, leaving useful relations observed at other times unavailable for prediction. To address these challenges, we design _MoJEPA_ which combines partial interaction masking with a shared Morse reference forest. We partially mask interactions so that the model can predict missing evidence from the relations that remain visible. To enrich this predictive context, we introduce _Morse reference context_, which leverages discrete Morse theory from low-dimensional topology to reduce the relations observed across a window to a sparse rooted forest. This allows the relations observed at other times to support information exchange at the target time. A relation observed at one time can subsequently support the exchange of node states at another, even when the corresponding interaction is absent. This combination allows prediction to use context beyond the interactions present at an individual time. Our experiments demonstrate that MoJEPA leads on all 9 within-dataset tasks and 15 of 18 transfer directions, with relative gains over the strongest external baseline up to 13.13\% and 12.27\% for within-dataset prediction and transfer respectively.

## 190. MoJEPA: Learning Transferable Motion Representations via Structured Dual-View Joint-Embedding Prediction

**Keywords:** Inertial Sensors; Human Activity Recognition; Cross-Domain Transfer; Joint-Embedding Predictive Learning; Self-Supervised Learning;

[Main paper PDF](https://openreview.net/pdf?id=Wbzn6I7Zw3)

A fundamental challenge in sensor-based Human Activity Recognition (HAR) is learning transferable motion representations from unlabeled inertial sensor signals for effective cross-domain adaptation. Existing self-supervised methods often rely on signal reconstruction or consistency across augmented views, which may capture low-level signal variations rather than the underlying physical structure of motion, limiting the transferability of the learned representations. To address this problem, Joint-Embedding Predictive Architectures (JEPAs) offer a framework for learning representations through latent-space prediction. Building on this framework, we propose MoJEPA, a dual-view joint-embedding predictive framework that learns transferable motion representations by explicitly modeling the underlying motion structure. MoJEPA introduces two structured masking views along the channel and temporal dimensions, guiding the model to predict masked latent representations from complementary motion cues. The channel view encourages the representation to capture cross-channel physical dependencies, while the temporal view captures temporal motion dynamics. Jointly optimizing these complementary objectives encourages representations that capture shared motion structure. Extensive experiments with pretraining on two large HAR datasets and evaluation across seven target datasets show that MoJEPA outperforms existing self-supervised baselines under frozen-encoder evaluation with few-shot and low-label adaptation.

## 191. Mol-JEPA: A multimodal Joint Embedding Predictive Architecture for Molecules

**Keywords:** Molecular Machine Learning, Foundation Model, World Model, Chemistry

[Main paper PDF](https://openreview.net/pdf?id=arRWIJAbQ0)

Despite recent advances in molecular foundation models, several limitations remain, such as chemically invalid augmentations, modality collapse, and incomplete representation of biochemical environments. To address these challenges, we present **Mol-JEPA**, a scalable framework for learning molecular world models. Rather than relying on suboptimal molecular perturbations, our model uses modality masking to exploit information from molecular structures, cellular phenotypes, binding affinities, ADMET profiles, quantum chemistry simulations and other drug discovery data. Across various benchmarks, we show that the representations learned by Mol-JEPA deliver strong performance, demonstrating the value of incorporating biochemical context through latent space prediction.

## 192. More Camera Frames, Better Driving? Within-Scene Information Scaling in Autonomous Driving

**Keywords:** End-to-End Autonomous Driving, Information Utilization, Model Capacity, Temporal Redundancy, Information Scaling

[Main paper PDF](https://openreview.net/pdf?id=clDpaFHaep)

Autonomous driving requires models to learn vehicle motion, agent interactions, and scene evolution from driving data. Existing scaling efforts focus on increasing model capacity and expanding driving data coverage, largely treating driving scenes as the unit of training information. However, how the information exposed within each scene should scale with model capacity remains underexplored. We study \emph{within-scene information scaling}, using temporal sampling frequency as a controlled probe to vary camera-frame density within fixed driving scenes. We formulate a minimal information--capacity model that captures the interaction among bounded driving-relevant information, increasing driving-irrelevant exposure, and finite model capacity. The model characterizes the capacity-dependent scaling behavior of within-scene information and predicts that the preferred temporal sampling frequency increases with model capacity under its assumptions. We conduct controlled frequency sweeps across compact end-to-end models, large vision-language-action (VLA) models, and world-action models on Waymo, nuScenes, and PAVE and in NAVSIM-based settings, with additional iteration-matched comparisons. AutoVLA and DriveVLA-W0 attain their lowest reported nuScenes trajectory errors at the highest tested frequency, yet further reductions above 4\,Hz are much smaller for DriveVLA-W0. Drive-JEPA achieves strong driving performance on NAVTEST already at 2\,Hz. These findings distinguish how much a model improves with denser temporal exposure from how well it already performs under sparse temporal exposure. They motivate evaluating driving performance alongside frequency-response curves and jointly developing model architectures, learning objectives, and within-scene data construction to utilize driving-relevant information that affects the driving decision while limiting the influence of driving-irrelevant exposure.

## 193. MORE: Learning Motion-Oriented Registers for Driving World Models and Planning

**Keywords:** Autonomous Driving, World Model

[Main paper PDF](https://openreview.net/pdf?id=WcveyOpJGj)

By predicting future states, latent world models provide rich self-supervision for end-to-end driving, but often inherit dense features from pretrained visual encoders as their world-state interface. This creates a mismatch: visual pretraining produces information-rich, spatially dense features, but their adaptation for motion-conditioned world modeling and planning is deferred to downstream training. The dense grid also makes future prediction more computationally expensive as visual resolution increases. We therefore argue that video pretraining should directly learn state representations suited to downstream world modeling and planning, rather than relying on downstream training to adapt inherited visual features. We propose ***MORE***, a V-JEPA framework that learns **M**otion-**O**riented **RE**gisters during video pretraining as a shared state interface for driving world models and planning. MORE injects temporally aligned ego motion into a small set of registers and uses them as the sole context for masked patch prediction, channeling dense patch-level supervision through a compact state bottleneck. A complementary blockwise register-masking objective further shapes predictive structure in the register space. During downstream training, the same register space defines the future states predicted by the world model and provides shared scene memory for trajectory generation and scoring. On NAVSIM-v2, MORE outperforms the state of the art by 1.6 in EPDMS, while achieving superior efficiency with only 1/10 the inference latency of DriveLaW. These results support learning the state interface for world modeling and planning directly during video pretraining.

## 194. Motion-Guided Contrastive Regularization for Latent World Models

**Keywords:** Latent world models, joint-embedding predictive architectures (JEPA), representation collapse, robotic manipulation

[Main paper PDF](https://openreview.net/pdf?id=obMtDauYJn)

JEPA-style world models learn action-conditioned latent dynamics without reconstructing observations, but distributional regularization alone does not ensure that their representations preserve information needed for control. We identify \emph{static collapse}, a failure mode in which the encoder preserves episode-specific static content while suppressing manipulation-relevant state changes. Because static content is temporally predictable yet diverse across episodes, this failure can persist despite regularizers such as SIGReg. A controlled study on OGBench-Cube shows that introducing randomized backgrounds substantially degrades planning performance while leaving the underlying manipulation task unchanged. To address this problem, we propose \emph{motion-guided contrastive regularization}. Our approach compares predicted latent transitions with transitions to candidate observations from the same episode, reducing the usefulness of static background identity for distinguishing action outcomes. Optical-flow similarities provide soft contrastive targets, allowing candidates with similar motion to receive similar supervision. Combined with latent prediction and SIGReg, our objective encourages representations to preserve within-episode state distinctions and similarities between related transitions. Our method improves planning success over LeWorldModel (LeWM) from 52\% to 78\% on OGBench-Cube with randomized backgrounds and from 14\% to 54\% on LIBERO-Object, while maintaining comparable performance on four other visual-control benchmarks.

## 195. Motion-JEPA: Physically Structured Residual Predictive Representation Learning for Autonomous Driving

**Keywords:** Joint-Embedding Predictive Architecture; Motion Prior; Latent Representation Learning; Vehicle Dynamics; Predictive World Modeling; Autonomous Driving

[Main paper PDF](https://openreview.net/pdf?id=PAg5AgdlUn)

Driving world models must predict and represent future scenes relevant to driving decisions. Changes in high-dimensional representations arise both from referenceframe changes caused by ego motion and from temporal evolution of the surrounding environment. When a model directly predicts the complete future, a predictor with limited capacity must fit both known geometric effects and unknown scene changes. This can impair future-scene prediction, produce representations that are less useful for driving decisions, and impose substantial computational costs. We propose MotionJEPA, a physically structured residual predictive representationlearning framework. It uses low-dimensional, interpretable ego-motion variables to construct a physical reference evolution for high-dimensional representations, and then learns the conditional residual not explained by that reference. The method combines explicit SE(2) motion transport, residual prediction around a physical reference, and static-dynamic diagnostics of residual sources. In 10,000 training steps on NAVSIM, model A3, which combines motion transport with an environment-residual predictor, reduces masked Smooth-L1 error by 7.76% relative to A1, which uses motion conditioning alone. A3 also achieves a 7.35% lower best validation Macro Smooth-L1 and a 7.69% lower overall test Smooth-L1 than A1. The additional validation metric, mean Intersection over Union (mIoU), also improves.

## 196. MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space

**Keywords:** JEPA, Latent World Model, Feature Collapse, Computer Vision, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=OhIFmmrsXg)

Joint Embedding Predictive Architectures (JEPAs) are a promising paradigm for learning task-agnostic latent world models without visual reconstruction. However, standard JEPA training exhibits a strong inductive bias towards slow features, causing feature suppression and the collapse of latent representation. While inverse dynamics provides temporal anti-collapse, it relies on action labels and offers little incentive to embed general, unlabeled dynamics. We introduce **D**ifference **I**mage and **S**ingle image embedding **Reg**ularization (DISReg), a novel regularizer that builds on an inverse-dynamics-style module that predicts temporal difference image embeddings without any pixel reconstruction loss, encouraging balanced static and dynamic feature learning. DISReg consists of a static term that shapes the distribution of the image embedding and encourages slow features, and a dynamic term, which, unlike direct regularization on the embedding, imposes no constraint on the image embedding's shape or distribution and instead only incentivizes that dynamic features be present. By integrating this regularizer into a standard JEPA, we establish our new architecture, MotionJEPA. Latent probing demonstrates that MotionJEPA produces more complete representations than other methods, and our trajectory analysis shows it maintains geometrically simple latent embeddings with low curvature. We further show that MotionJEPA improves downstream planning success under static-background distractors across four environments.

## 197. Multi-Scale Future Modeling for Latent World Models

**Keywords:** World Model, Latent World Model, JEPA

[Main paper PDF](https://openreview.net/pdf?id=yUpCWMAUcD)

Latent world models efficiently predict future world states in representation space, but most existing approaches model the future only at the timestep level, as a dense sequence of latent states. While this preserves fine-grained dynamics, it provides no explicit representation of future evolution over longer temporal intervals, potentially biasing forecasting toward local dynamics. We present MS-JEPA, a multi-scale latent forecasting framework that models future evolution at complementary temporal scales. The key idea is to represent the same future through both dense latent states and Future Abstractions: the former preserve fine-grained dynamics, while the latter summarize evolution over temporal intervals. A high-level predictor anticipates these abstractions from observed latents to guide dense forecasting. By explicitly modeling temporal structure across scales, our framework combines broader future context with fine-grained dynamics. Experiments across egocentric hand motion, whole-body motion, and physical-scene forecasting show consistent improvements over latent world modeling baselines, demonstrating the effectiveness and generality of our approach.

## 198. MV-JEPA: Post-Training Video Encoders for Cross-View Understanding

**Keywords:** self-supervised learning, representation learning, JEPA, multi-view learning, cross-view prediction, viewpoint robustness

[Main paper PDF](https://openreview.net/pdf?id=0oRl8hj8fQ)

JEPA-based video encoders learn strong representations for video and image understanding through prediction in latent space. However, their standard pretraining predicts features within individual images or video clips, without explicitly exploiting paired camera views of the same object or moment. Consequently, the learned representations may not reliably support matching across different camera viewpoints.
To solve this problem, we introduce multi-view predictive post-training to strengthen cross-view instance and temporal correspondence while retaining independent single-view inference. A shared encoder processes masked context views independently, and a training-time predictor jointly predicts latent tokens for masked context regions and a fully held-out view. We alternate cross-view prediction with single-view masked prediction on general image and video data to help retain the encoder’s pretrained capabilities. After only 9,000 post-training updates on a single GPU, MV-JEPA improves cross-view
instance retrieval and coarse cross-camera moment retrieval on various datasets, with further gains in zero-shot action-phase retrieval
and frozen-feature classification on AE2. Frozen-probe evaluations further indicate that post-training largely preserves motion recognition, image recognition, and dense semantic segmentation performance on the evaluated
benchmarks. Together, these results demonstrate that multi-view predictive post-training can strengthen instance and coarse temporal correspondence in JEPA video encoders without modifying the encoder architecture or single-view inference interface.

## 199. NDB-JEPA: Label-Efficient Grasp Detection from Frozen I-JEPA Features

**Keywords:** robotic grasp detection, object manipulation, grasp point detection, vision foundation models, JEPA, I-JEPA, self-supervised learning, label efficiency, robustness to distribution shift, robustness to out-of-distribution, vision transformers

[Main paper PDF](https://openreview.net/pdf?id=07om1gaWpv)

As robots become increasingly prevalent in real-world settings, their perception models must become label-efficient and robust to distributional shifts not represented in their labeled training data which poses a considerable challenge for end-to-end grasp detection models typically trained on limited or synthetic datasets. We introduce NDB-JEPA, a label-efficient grasp point detection perception model centered around I-JEPA.  Our proposed model takes advantage of the robust, generalized feature extraction of I-JEPA, a self-supervised joint-embedding predictive foundation model. Our model trains lightweight grasp heads on top of the frozen image patch outputs of a 632M-parameter I-JEPA encoder, predicting grasp confidence, orientation, and width per embedded patch. We ask whether these frozen features can replace end-to-end training for the grasping problem. On the Cornell Grasping Dataset, NDB-JEPA reaches 86.9\% Top-1 rectangle success, within 1.5 points of an end-to-end GR-ConvNet baseline, and among large pretrained encoders, I-JEPA features outperform MAE, supervised ViT, and DINOv2 alternatives. The frozen representation is also markedly more label-efficient and robust: with only 10\% of the training data, NDB-JEPA attains roughly 74\% success versus 40\% for GR-ConvNet trained from scratch, and it retains about 94\% of its clean accuracy under severe darkening while the end-to-end baseline collapses to 1.1\%. While end-to-end models retain a small edge in clean accuracy, our results indicate that frozen joint-embedding predictive representations offer a data-efficient, robust basis for grasp perception.

## 200. Nested Latent Representations for Size-Flexible End-to-End World Models

**Keywords:** nested representations, jepa, world models

[Main paper PDF](https://openreview.net/pdf?id=Sz1bw9EY03)

Latent world models for planning typically assume a fixed representation size. While recent work, such as SubJEPA, considered operating in subspaces of smaller dimensionality, they require additional task-specific tuning of the subspace granularity. In this work, we ask whether world models can learn representations that remains useful across multiple post-hoc embedding sizes. As an answer, we introduce ElasticJEPA which jointly trains a world model at multiple nested granularities. ElasticJEPA combines subspace regularization with prediction losses applied to the same prefixes used at inference. The novel prediction loss objective induces a coordinate-supervision profile that is naturally monotonically-ordered. ElasticJEPA also ensures that privileging prefixes are retained under truncation. With such a construction, a single trained model can be evaluated at multiple representation sizes with no need for retraining. Importantly, inference-time evaluation can also include widths not supervised during training. Across four environments, ElasticJEPA is competitive with prior methods at full width, retains most of its performance under substantial truncation, and degrades less than baselines truncated to the same size, most clearly at the smallest widths.

## 201. NestedWM: World Models with Nested Latent Representations

**Keywords:** World Model, Latent World Model, LeWorldModel, JEPA, Nested Representation, Matryoshka Representation

[Main paper PDF](https://openreview.net/pdf?id=tw9rh4fyrA)

Planning with world models requires repeated rollouts, yet conventional models are trained with a fixed latent size that determines the trade-off between representation capacity and planning cost.
We propose NestedWM, which learns nested latent representations that allow a single world model to predict and plan using leading prefixes of its predictive state at different budgets.
Each prefix contains either the leading dimensions of a latent vector or the leading tokens of an ordered latent-token sequence.
We jointly train an encoder and an action-conditioned predictor over sampled prefix budgets, using each selected prefix as both the predictor input and the target prediction space.
In a dimension-wise study with the architecture held fixed, a single encoder and predictor support planning across budgets, achieving high success with only a fraction of the full latent dimensions in most evaluated visual-control and synthetic tasks.
Further analyses show that leading prefixes preferentially retain planning-relevant information, while predictable distractors can consume limited representation budget.
We then turn this capability into computational savings with a token-wise instantiation that processes only the selected prefix tokens during rollout.
In controlled multi-token settings, a single model supports successful planning across multiple token budgets, with smaller prefixes reducing model-based cost-evaluation time.

## 202. Neural Voxel Dynamics: Learning Latent 3D Physics via Volumetric Feature Advection

**Keywords:** 3D, latent space, world models, JEPA, self-supervised, simulation, video generation

[Main paper PDF](https://openreview.net/pdf?id=uz2NwmDssT)

We present $\textit{Neural Voxel Dynamics}$, a self-supervised framework for learning 3D latent dynamics from monocular video. While generative video models now produce visually compelling motion, their predominantly 2D representations provide limited geometric structure for modeling and controlling physical interactions. 
Instead, we learn dynamics in a lifted volumetric latent space. Specifically, we unproject semantic Video Joint-Embedding Predictive Architecture (V-JEPA) features into a voxel grid using monocular depth priors, producing a geometrically grounded representation that retains rich video features. 
We then introduce $\textit{Volumetric Feature Advection}$, an action-conditioned transition model that predicts the evolution of these latent features directly in 3D. Unlike hybrid approaches that assume access to privileged physics-engine states or explicit simulation during training and/or inference, we learn only using video-derived supervision and actions, allowing a single latent dynamics model to represent heterogeneous material-dependent phenomena, unifying rigid-body and fluid dynamics. 
We evaluate across multiple datasets (synthetic and real) and unseen scenarios (e.g., unseen boundary conditions, OOD generalization), measuring both predictive fidelity and 3D geometric consistency. 
We further evaluate physical plausibility with Physics-IQ using videos decoded from predicted latent states and videos generated from predicted optical flow. 
Our results show that geometrically lifting pretrained video latent representations provides a scalable route toward dynamic world models that learn structured 3D physical dynamics without access to privileged simulator state.

## 203. NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings

**Keywords:** chronic neural recordings, neural decoding, brain-computer interfaces, self-supervised learning, representation learning, foundation models, transformer, electrophysiology, neuropixels

[Main paper PDF](https://openreview.net/pdf?id=lEfFuKX6oA)

Understanding how neural activity represents higher-order cognition and how these representations evolve over time has long been a central pursuit in neuroscience. However, current analytical tools cannot easily distinguish representational plasticity from recording instability in chronic neural recordings. Here, we introduce NeuroLens (Latent Embeddings of Neural Semantics), a self-supervised model based on the Joint-Embedding Predictive Architecture (JEPA) framework that learns denoised, semantically informative latents from chronic neural recordings. An adaptive encoder maps changing neural populations into a common latent space, while a temporal predictor learns structure that supports prediction of future latent states. By predicting in latent space, NeuroLens captures temporally predictable structure and reduces sensitivity to transient, recording-specific variability. Across chronic intracortical data in mice and humans, the learned representations improve decoding of decision-making and semantic task variables. Multi-day pretraining enables generalization to future sessions, rapid few-shot adaptation to unseen neural populations, and more stable decoding over time than state-of-the-art baselines. Together, these results establish NeuroLens as a new paradigm for studying how neural representations change during learning and over long timescales.

## 204. No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models

**Keywords:** joint-embedding predictive architectures, self-supervised representation learning, world models, contrastive learning, representation collapse, inverse dynamics, latent dynamics, model-based planning, visual control

[Main paper PDF](https://openreview.net/pdf?id=rM6SFNpHl2)

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting
future embeddings, but the objective admits a trivial solution of a constant
encoder, so every practical system adds an anti-collapse mechanism. LeWorldModel (LeWM)
prevents collapse with SIGReg, a regularizer that forces the latent
distribution to match an isotropic Gaussian: the representation is stabilized by
prescribing what it must look like, independently of the environment it models.
We argue that the anti-collapse pressure can instead come from the transition
data itself. Action-Contrastive Masked Transition Modeling (AC-MTM) keeps LeWM's forward
latent prediction objective and adds a training-only inverse-dynamics head
trained with Action-NCE: each latent transition must identify the action that
produced it among the other actions in the batch, a discrimination task that a
collapsed encoder provably fails. The inverse branch is discarded after
training, leaving test-time encoding, forward prediction, planning, and compute
identical to LeWM. On four standard pixel-control tasks under a matched
planning protocol, AC-MTM trains stably from scratch and matches or exceeds
SIGReg. On the harder multi-object OGBench Visual Scene task,
results suggest that SIGReg's prescribed geometry is a bottleneck:
AC-MTM reaches $80.0{\pm}2.0\%$ success rate versus $58.0{\pm}2.0\%$ for
SIGReg, improving by 20--24 points in each training seed. A random-policy run gives a 52\% baseline estimate. Contrastive inverse dynamics thus provides a distribution-free anti-collapse signal that requires no target
network, stop-gradient, pretrained encoder, or reconstruction objective, and we
characterize the action space and observability assumptions under which it
holds. We will release code and configuration files after review.

## 205. Noether World Models: An Exactly Conserved Family of Latent Invariants

**Keywords:** world models, latent dynamics, conservation laws, unitary operators, Cayley transform, graph Laplacian, object-centric representations, model-based planning, JEPA

[Main paper PDF](https://openreview.net/pdf?id=BpNDUNJzdj)

World models predict by rolling a learned latent transition forward over many steps. Current methods pursue conservation through a soft penalty, a symplectic integrator or an implicit projection, so each exact guarantee covers a small set of scalars fixed before training and paid for with an implicit update. We propose the Noether World Model (NWM), which assembles the generator as a graph Laplacian over object subspaces, $\mathbf{H}=\mathbf{L}\otimes I_m$, and advances the latent with a Cayley transform. The resulting unitary operator conserves a $2m^2$-dimensional family of quadratic invariants exactly at every value of its weights, and that family is exactly the set of quadratic forms with that property. Experiments on three physics datasets and three planning environments show that NWM holds the entire family at double precision whereas no baseline holds more than the norm, with $32\times$ fewer parameters than the strongest physics-structured baseline. Decoded quality in distribution separates the nine designs by only 1.3 dB, whereas under a zero-shot change of force law NWM leads the unconstrained transitions by 1.9 dB, so the family pays where the data leaves the training distribution. Exactness has a price, since the operator fixes every member of the family and most goals in a latent it did not shape lie off the reachable set. The same family can nonetheless enter the training objective of a world model whose predictor we do not replace, and it improves planning only where that predictor already drifts, a condition measurable before retraining.

## 206. Normalizing Flows are Capable World Models

**Keywords:** world models, normalizing flows, JEPA

[Main paper PDF](https://openreview.net/pdf?id=hrbXJ7zUf8)

World models predict how the world evolves in response to actions and have
developed along two main directions. Video world models, most of which are
built on diffusion models, generate future observations with impressive quality but
typically require large models and multiple denoising steps per prediction. Latent
world models instead predict and plan in a learned representation space. Those
based on Joint Embedding Predictive Architectures (JEPAs) learn this space jointly
with the predictor through a regression objective, but require an additional anti-
collapse mechanism, and their deterministic predictors cannot represent multiple
possible futures. To bridge these directions, we present Normalizing-Flow World
Model (NFWM), an autoregressive normalizing flow consisting of an invertible
encoder and a probabilistic predictor. Both components are trained jointly by
exact maximum likelihood, which trains the predictor to model a distribution
over future latent states and prevents representation collapse without an additional
anti-collapse mechanism. Since the encoder is invertible, NFWM can generate
future observations like a video world model, while predicting in a single step
and planning in its learned latent space like a latent world model. Although the
encoder preserves all information, its latent coordinates are still learned, so we can
shape them for planning with an auxiliary inverse-dynamics objective. Empirically,
NFWM achieves the highest average success on deterministic goal-conditioned
planning and outperforms JEPA-based world models in stochastic environments
and on robotic manipulation, while also supporting policy learning in imagination.
These results provide initial evidence that normalizing flows are capable world
models, establishing them as a promising direction for connecting video and latent
world models.

## 207. OCCAM: Object-Centric Causal World Model via Vision-Language Graph Grounding

**Keywords:** World Models, Causality, Vision-Language Models

[Main paper PDF](https://openreview.net/pdf?id=tC8M1HeYEc)

Latent world models trained via joint-embedding predictive architecture (JEPA) excel at planning from pixels, but their transition functions are monolithic, lacking explicit representations of objects and interaction dynamics necessary for controllable and explainable embodied planning and reasoning. To address this issue, we introduce Object Centric CAusal World Model (OCCAM), a framework that integrates language-grounded causal structures directly into the transition function. 
OCCAM first uses open-vocabulary segmentation and tracking to obtain object-level latent states without hand-labeled masks. Then, OCCAM queries a vision-language model over motion-salient frames to build a sparse causal graph, validated by an independent conditional mutual information estimator. By combining language-grounded object abstraction with verified causal graph discovery, OCCAM enforces sparse, explainable state updates that isolate task-irrelevant entities, mitigating the extensive data requirements in classical causal discovery.
We systematically evaluate OCCAM, analyzing dense, object-centric, and causal transition regimes across $12$ tasks of increasing visual and relational complexity. Experimental results demonstrate that OCCAM achieves a highly interpretable, object-centric latent space while preserving goal-conditioned planning accuracy. Crucially, on the complex multi-object LIBERO benchmark, OCCAM achieves superior downstream task control compared to dense and object-centric baselines, indicating that the structured causal reasoning is essential for reliable control as scene complexity scales.

## 208. OISE: Objective-Induced Splits in Encoders

**Keywords:** frozen vision encoders, representation comparison, self-supervised learning, masked image modeling, training objectives, label-free group discovery, partition agreement, Adjusted Rand Index

[Main paper PDF](https://openreview.net/pdf?id=9GyYhjLGuG)

What a frozen vision encoder splits images on first depends on whether its training objective matches a whole-image target or predicts hidden content. We examine this relationship in 21 frozen vision encoders, comprising 15 core models spanning objectives and architectures and six language-supervised variants spanning scale, pretraining data, a convolutional backbone, and a VLM tower. A fixed clustering procedure induces a binary partition within each class without group labels. We compare assignments on the same images using the Adjusted Rand Index (ARI), whose chance expectation is zero. On UrbanCars, 19 of the 21 encoders have self-consistency of 0.56–0.93 across discovery draws. Eight self-supervised cross-view encoders produce similar partitions (ARI 0.56–0.81). Label- and language-supervised models occupy an intermediate position, agreeing with the cross-view models at 0.37 on average. MAE, data2vec, I-JEPA, and the hybrid DINOv2 have low agreement with whole-image models (0.07) and with one another (0.06). The exception is MAE–data2vec (0.32 on UrbanCars and at most 0.08 elsewhere). Within the original four-dataset analysis, the three latent-prediction models (data2vec, I-JEPA, and DINOv2) are jointly isolated only on UrbanCars, where partitions are most stable. Matched training reproduces the ResNet-18 ordering with the same images, epochs, and batch size. Controlled interventions link partition selection to cross-view augmentation and show that relative variance can shift the partition among stably expressed factors. Finally, label-free partition agreement predicts cross-encoder group-transfer gains, although the gains are limited to a few worst-group accuracy points.

## 209. On the Demand-Supply Geometry of Representation Collapse

**Keywords:** World Models; Joint-Embedding Predictive Architectures; Representation Collapse; Two-Sided Regularization; Numerical Stabilit

[Main paper PDF](https://openreview.net/pdf?id=feMFdRSPF4)

Preventing representation collapse remains a central challenge in Joint-Embedding Predictive Architectures (JEPAs). Endpoint-only constraints cannot fully prevent or repair collapse when intermediate representations lose sample distinctions. We introduce SADL (Supply And Demand Loss), an adaptive one-sided bridge that matches endpoint demand to the available capacity of the representation path. SADL compares demand from the output objective and realized endpoint geometry with the weaker of encoder excitation and cross-endpoint transmission capacity, applying a correction only when demand exceeds supply. It works with different output regularization functions without auxiliary networks, learned gates, or a separate schedule. In single-task and jointly trained four-task LeWorldModel (LeWM) and INTACT experiments, the collapse rate falls from 50% to 0% in a ten-seed collapse test. After only 1 epoch of training with SADL, encoder effective rank increases by 3.4–6.4× and latent prediction error decreases by 20–303× relative to the corresponding endpoint-only baselines. Under multiple regularization functions, INTACT also achieves over 95% mean search-free control success. Across four image datasets, each with multiple paired seeds, SADL delivers consistent seed-wise improvements in accuracy and stability at representative checkpoints, with its largest gains emerging early in training. These findings indicate that demand–supply matching along the representation path is a general principle for faster and more stable representation learning across control and image classification.

## 210. On the Representation of World Action Models

**Keywords:** World Model, Representation Learning, Embodied Intelligence

[Main paper PDF](https://openreview.net/pdf?id=9vz1VBE0WT)

World action models (WAMs) use visual prediction to learn intermediate
representations (e.g., global or dense semantics, geometry, and spatiotemporal
dynamics) for robot action prediction. Learning these representations depends on which visual features are used as inputs/outputs and how these features are predicted. In this paper, we conduct comprehensive analyses on how these two choices shape
intermediate representations and thus help action prediction.
Our study yields two key findings:1) V-JEPA 2.1 features (which are good at spatiotemporal dynamics) outperform Wan VAE
(pixel reconstruction), DINOv3 (dense semantics), and SigLIP-2
(global semantics) features for robot action prediction. 2) using frame-wise autoregression for visual feature prediction performs better than diffusion, i.e., shaping the intermediate representations better for action prediction.
On RoboTwin 2.0, our representation recipe
(V-JEPA 2.1 + frame-wise autoregression) achieves an average success rate of 85.9%, compared with 38.0% for the baseline
recipe (Wan VAE + diffusion), without additional robot pretraining.
This advantage persists after additional pre-training on 3,300 hours robot data, with success rates of
91.5% (our recipe) and 75.1% (baseline recipe).
We hope these findings provide helpful guidances for developing more effective
representation recipes for WAMs.

## 211. Parallelizable Probabilistic Latent Reasoning for Diverse Reasoning Trajectories

**Keywords:** Autoregressive Language Model; Language Model; Continuous Chain-of-Thought; Joint-Embedding Predictive Architecture

[Main paper PDF](https://openreview.net/pdf?id=CtluWEsiX7)

Language models relying on verbalized Chain-of-Thought (CoT) are constrained to token-by-token generation in the language space, where many tokens serve textual coherence rather than core reasoning. This entangles genuine differences in logical trajectories with superficial variations in verbalization. Moving reasoning into a compact, continuous latent space offers a promising alternative for efficiently representing and exploring diverse reasoning trajectories. However, current latent models remain largely deterministic, capturing only a single reasoning trajectory rather than modeling a distribution over multiple valid alternatives. While stochastic approaches parameterize distributions over latent reasoning steps, they frequently suffer from unstable optimization and limited empirical performance. Furthermore, their reliance on autoregressive latent prediction during training precludes effective parallelization, leading to prohibitively long training times. To overcome these bottlenecks, we propose Probabilistic Latent Reasoning Models (PLRM), a parallelizable variational framework for probabilistic latent reasoning. PLRM adopts a JEPA-style objective in which the posterior infers latent distributions in parallel from observed reasoning trajectories, while the prior learns to predict the subsequent latent distribution via teacher forcing. To model heterogeneous reasoning processes, we introduce a discrete strategy variable together with a mixture-based prior, allowing the model to preserve the Gaussian-mixture structure induced by multiple distinct reasoning trajectories rather than collapsing them into a single Gaussian. Across diverse benchmarks, PLRM achieves performance competitive with deterministic latent reasoning models on single-trajectory datasets while enabling efficient training and consistently outperforming competing stochastic baselines on multi-trajectory datasets.

## 212. PARM-WM: Persistent Action–Response Memory for Long-Horizon Visual World Models

**Keywords:** World Models, Long-Horizon, Bounded Action–Response Memory

[Main paper PDF](https://openreview.net/pdf?id=XPQKF7j7kI)

Long-horizon visual prediction must retain how a scene responds to earlier actions as real observations leave the rolling context. We introduce PARM-WM, a world model with Persistent Action–Response Memory (PARM). An observable response encoder combines visual feature changes with aligned actions to form a compact state. A zero-preserving, low-rank residual then reads this state throughout the rollout. A validation-selected latent interpolation combines the response branch with a JEPA continuation using one mixing weight across sources. We evaluate the complete predictor against seven action-conditioned baselines on three robotic trajectory sources, using seven observed frames to predict twenty future frames. PARM-WM achieves the best values on all four metrics for RoboMimic Lift, LIBERO New, and LanguageTable, reducing pixel MSE relative to JEPA-WM by 49.3%, 3.8%, and 12.1%, respectively. Globally Holm-corrected paired tests confirm improvements over every baseline on all four metrics on all three sources. These results establish persistent action–response memory as a useful interface for sustained visual forecasting.

## 213. Partner as Task: Belief-conditioned Successor Features for Zero-shot Coordination

**Keywords:** Zero-shot coordination, Multi-agent, Reinforcement Learning.

[Main paper PDF](https://openreview.net/pdf?id=R5na7mjMe5)

Zero-shot coordination (ZSC) requires cooperation with partners unseen during training. We view each partner as a task: the reward remains fixed, but the partner changes the ego-agent's effective dynamics and hence how it should act. Learning these dynamics is difficult when the partner policy is unobserved, and reward is sparse. We introduce belief-conditioned successor features (BSFs), which summarize discounted future features conditioned on a belief over the partner's latent type. The belief is inferred from interaction history and augments the state. We show that the value of a belief-independent policy is linear in the belief, connecting belief inference to task conditioning in standard successor features. We approximate BSFs in MA-JEPA, an on-policy self-play (SP) algorithm that combines a learned history encoder with a temporal difference latent prediction objective. This objective provides reward-free supervision for long-term predictive representations. Across Overcooked and SMAC, MA-JEPA outperforms self-play, population-based, and agent-modeling baselines, with the largest cross-play gains over the strongest baseline under sparse rewards ($77\%$) and RGB observations ($32\%$).

## 214. PDE-JEPA: Predictive Representation Learning of Latent Dynamics modeling for Parametric PDEs

**Keywords:** parametric pde, jepa latent space, geometry aligned, physical structured latent predictor

[Main paper PDF](https://openreview.net/pdf?id=8KdcFtg3bv)

Physical trajectories contain more than snapshots of a system: they also reveal how its states evolve under governing conditions. However, representation learning for parametric partial differential equations (PDEs) has largely relied on reconstruction-based objectives that emphasize recovering observed physical fields. In this paper, we investigate predictive representation pretraining as an alternative to reconstruction-based learning. We find that predictive representations preserve rich physical information, yet this advantage alone does not ensure accurate field evolution. Based on these observations, we introduce PDE-JEPA for parametric PDE dynamics. Specifically, we first train an encoder using a masked-latent prediction to capture the underlying regularities of PDE dynamics. To explicitly adapt the pretrained representation toward a more dynamics-aligned state space, we then introduce a geometry projector that aligns latent trajectory geometry with the evolution geometry of physical fields. Finally, building on this geometry-aligned latent space, we further develop a physics-structured latent predictor that decomposes the dynamics into parameter-independent evolution and parameter-dependent response components. 
Extensive experiments on nine widely used PDE benchmarks demonstrate that our framework outperforms existing state-of-the-art methods by an average of 33.4\% in-distribution, while achieving an average improvement of 51.4\% when extrapolating to unseen governing parameters. Our implementation will be released.

## 215. PersJEPA: Interpretable Language Model Personalization through Sparse Residual Prediction

**Keywords:** Large language models, personalization, joint-embedding predictive architectures, sparse autoencoders, activation steering, mechanistic interpretability

[Main paper PDF](https://openreview.net/pdf?id=ffblZbohRZ)

Language models can personalize their answers when given a user's profile or past interactions, but repeatedly supplying this information consumes context and computation. Learning personalized parameters can reduce this dependence on prompting, yet offers limited visibility into how user preferences affect the model's responses. Activation steering has attracted growing interest as a way to personalize models through interventions in hidden states without updating their parameters, yet it faces three key challenges: (1) fixed adjustments overlook how user preferences interact with each request, (2) steering confined to the initial decoding step leaves later steps without further intervention, and (3) accurate prediction of hidden representation changes does not reliably translate into personalized responses. To address these challenges, we introduce PersJEPA, a framework for interpretable personalization of frozen language models through sparse prediction conditioned on user information. Inspired by JEPA, we formulate predictive residual learning, using paired generic and personalized representations to learn how user context changes the model's hidden states. We design sparse residual decoding so that each request activates a small set of learned features whose directions are combined into a personalization residual. User conditioning determines which features contribute and how they adjust the model's representations. We further develop generation-aligned steering, applying the decoded residual throughout generation and optimizing the predictor for the likelihood of personalized responses through the frozen model while retaining residual supervision. The language model remains frozen throughout training, and inference requires no profile text in the prompt. Experiments demonstrate substantial improvements in controlled persona generation across multiple language models and gains on real user personalization benchmarks. Analyses of the learned features reveal how their contributions vary across user groups, providing a concrete basis for interpreting the learned personalization interventions. Our implementation is fully open-sourced.

## 216. PhyLatent: Learning Dynamics-Relevant Representations for JEPA World Models

**Keywords:** JEPA, World Models, Dynamics-Relevant Representation Learning, Representation Collapse, Latent Dynamics, Model Predictive Control, Visual Planning

[Main paper PDF](https://openreview.net/pdf?id=x9mOt7HBI6)

We propose PhyLatent, a dynamics-relevant training objective for JointEmbedding Predictive Architecture (JEPA) world models. Our key observation is
that preventing global latent collapse does not necessarily ensure that the learned
representation preserves physically meaningful state and action relationships. We
identify three failure modes: sensitivity to appearance changes that leave the physical state unchanged, insufficient separation of distinct physical states, and insufficient separation of different action-conditioned futures. We refer to these as Physical Invariance Collapse, Physical Distinguishability Collapse, and Counterfactual
Dynamics Collapse, respectively. PhyLatent targets these failures through three
coordinated training pathways, implemented with physical state grounding, future
representation alignment, static visual invariance, counterfactual branch separation, and latent denoising. On OGBench-Cube, PhyLatent reduces the three collapse rates by 43.9%, 27.9%, and 47.1%, respectively, while improving MPC
success by 12.0 percentage points (17.2% relative). Across four visual-control
tasks, average planning success increases by 6.62 percentage points (8.3% relative). These results show that global non-collapse alone is insufficient for learning
a reliable JEPA world-model state space, and that explicitly preserving dynamics relevant structure can improve closed-loop planning.

## 217. PhyMem: Retrieved Predictive Memories for Physically Plausible Video Generation

**Keywords:** video generation, video diffusion models, world models, physical plausibility, retrieval-augmented generation, memory-augmented generation, predictive video representations

[Main paper PDF](https://openreview.net/pdf?id=ugQBs0hXdx)

Text-to-video diffusion models can synthesize visually compelling clips, yet they remain unreliable when prompts require coherent motion, causal interactions, or physically plausible temporal evolution.
A key limitation is that text specifies what should happen but provides little evidence about how the scene should physically unfold.
We study whether predictive video representations retrieved from real videos can provide external guidance for physically plausible generation with a frozen Transformer-based latent video diffusion backbone.
We introduce PhyMem, a plug-in memory framework that (i) retrieves prompt-relevant reference clips, (ii) instantiates world-model memories with predictive representations extracted by a frozen V-JEPA2 encoder, (iii) compresses the resulting spatiotemporal tokens into compact memory tokens, and (iv) injects them into the self-attention layers of a frozen video diffusion backbone through a lightweight trainable memory module, without finetuning the backbone.
Training updates only a lightweight memory interface, with $33.9$M trainable parameters and approximately $0.8$K training videos, while the video diffusion backbone, text encoder, and generator VAE remain frozen.
Across physics-focused evaluations, PhyMem improves physical plausibility and physical commonsense under matched inference settings while largely preserving semantic adherence.
Diagnostic ablations further indicate that the gains depend on representation source, retrieval relevance, and retrieval budget: V-JEPA2 memory outperforms native VAE memory, prompt-relevant references are more effective than shuffled ones, and retrieval performance peaks at an intermediate budget.
These results suggest that retrieved predictive memories offer a parameter-efficient route toward improving physical plausibility in video generation.

## 218. PL-JEPA: Joint Predictive and Generative Learning for Structure-Based Drug Discovery

**Keywords:** Protein–ligand representation learning; joint-embedding predictive architecture; structure-based drug design; virtual screening; molecular generation; equivariant diffusion models; target fishing

[Main paper PDF](https://openreview.net/pdf?id=gr8PMrnaoO)

Structure-based drug discovery is typically formulated as two separate tasks. Virtual screening ranks existing molecules for a protein pocket, whereas structure-based molecular generation constructs new molecules conditioned on that pocket. Although both tasks are governed by the molecular constraints imposed by the same binding pocket, they are commonly modeled separately. We introduce PL-JEPA, a protein-ligand joint embedding predictive architecture that represents these shared constraints as a binding embedding in ligand representation space. The binding embedding provides a common interface for molecular recognition and realization. It can be directly matched with ligand representations for virtual screening or used to condition an equivariant diffusion decoder for 3D molecular generation. PL-JEPA progressively learns this shared interface through predictive alignment, representation-conditioned generation, and joint predictive and generative training, making the binding embedding both searchable and realizable. A single checkpoint supports virtual screening, 3D molecular generation, and target fishing. On DUD-E and LIT-PCBA, PL-JEPA improves BEDROC$_{80.5}$ over DrugCLIP by 36.2\% and 84.3\%, reaching 68.80 and 11.48, respectively. On CrossDocked2020, it achieves a median Vina Dock score of -8.23 kcal/mol and a diversity of 0.78. On CASF-2016, it improves target fishing Acc@5 from 62.59 to 65.96. Ablation studies show that the three-stage training progressively establishes and integrates the searchable and realizable properties of the binding embedding.

## 219. PlanJEPA: Learning Control-Structured Representations for Latent Planning

**Keywords:** World Model, Latent World Model, JEPA

[Main paper PDF](https://openreview.net/pdf?id=e0NaCz8nSB)

Learning representations that support planning is essential for latent world models. However, existing representation-learning objectives focus on latent-state prediction or action recoverability and do not constrain the complexity of the control relation between actions and latent transitions, so an accurate predictor can still operate over a latent space with highly nonlinear control relations. Consequently, accurate latent prediction does not necessarily lead to successful planning, since goal costs, candidate-trajectory ranking, and gradient-based action optimization all depend on the control structure exposed by the latent space. We introduce PlanJEPA, which learns control-structured representations with a multi-horizon linear action objective. By requiring actions to be predicted through a shared linear map of current and future latent states across multiple temporal horizons, PlanJEPA encourages the encoder to organize control-relevant variations directly in the representation. We prove that the imposed linear action relation forces nontrivial control errors to induce nontrivial latent goal errors and improves the local conditioning of goal-directed planning objectives. Empirically, PlanJEPA better organizes control-relevant state changes in latent space and consistently outperforms strong latent world model baselines across closed-form control, learned policies, cross-entropy method search, and gradient-based planning.

## 220. Planning Before and After Feedback: Allocating Five Complete Planner Calls with Frozen Visual World Models

**Keywords:** visual world models, model predictive control, cross-entropy method, feedback replanning, planning budget allocation, robotic manipulation

[Main paper PDF](https://openreview.net/pdf?id=9THJe46wZt)

Planning with a frozen visual world model poses a temporal allocation problem: given $K=5$ complete planner calls, how many calls $r$ should be spent on independent search before acting, and how many should be reserved to replan from fresh observations? We compare precommitted schedules while fixing the model, scorer, call count, and logical function evaluations within each panel. On Wall, a disjoint pilot selects $r=3$; relative to the all-initial-search schedule $r=5$, the registered endpoint changes by $-34.7$ (two-way 95% sensitivity interval $[-45.0,-24.5]$), with a descriptive success change of $+31.6$ percentage points. PointMaze provides a boundary: both registered intervals for selected $r=1$ versus $r=5$ include zero. A matched Wall sham replaces fresh post-execution observations with cached imagined latents while holding later call slots and horizon work fixed; real minus sham is $-23.9$ (two-way 95% sensitivity interval $[-31.9,-16.4]$), supporting fresh-observation conditioning relative to that control. The Wall direction recurs in targeted iCEM-component, DecentCEM-style, and one-checkpoint JEPA-WM adaptations. PushT repeats the fixed $r=4$ versus $r=5$ direction in a prospective train-split policy confirmation and a retrospective validation-split replication, although equal-call restart controls do not establish a task-general feedback mechanism. Planner-call timing is therefore a measurable, task-dependent controller choice under the tested protocols, not a universal replanning rule.

## 221. PowerJEPA: From Tail-Aware Alignment to the Downstream Utility of Global Spectral Structure

**Keywords:** Representation learning, JEPA, Tail-aware alignment, Spectral geometry

[Main paper PDF](https://openreview.net/pdf?id=DvKUPN9lm6)

Learning general-purpose embeddings requires preserving semantic correspondences while retaining variation useful across downstream tasks. Despite LeJEPA’s success in visual representation learning, its direct extension to general-purpose text embeddings yields limited downstream performance in our experiments. Empirical analysis identifies insufficient alignment of difficult positive pairs as a key limitation. Motivated by this finding, we introduce PowerJEPA, combining tail-aware power-mean alignment, selective hard-negative discrimination, and Sketched Isotropic Gaussian Regularization (SIGReg) to shape local and global embedding geometry. Experiments across text (MS MARCO and NLI) and image (ImageNet) modalities demonstrate its effectiveness. We further examine how the global representational capacity shaped by SIGReg, measured by effective dimension, relates to downstream performance. Spectral interventions on frozen text representations show that retrieval is more sensitive to truncation than clustering and reranking, while larger effective dimension does not consistently improve performance. Theory further shows that spectra with identical effective dimension can have different regularized effective degrees of freedom. We therefore combine effective dimension with spectral curvature into a capacity–shape description for assessing downstream utility. A calibrated predictor using both descriptors achieves a Spearman correlation of 0.97 with mean MTEB scores. These results connect geometric representation learning with calibrated diagnostics of downstream transfer.

## 222. Predict-Then-Adapt: Cross-Plane Joint-Embedding for Test-Time Medical Segmentation

**Keywords:** Medical Image Segmentation, Joint-Embedding Predictive Architecture, Test-Time Adaptation, Domain Shift

[Main paper PDF](https://openreview.net/pdf?id=WhRpXMEjTr)

Test-time medical image segmentation adapts source-trained models to unlabeled target volumes under distribution shifts. Existing methods mainly derive adaptation signals from model predictions or individual slices, leaving the intrinsic three-dimensional structure of test volumes underexploited. In particular, orthogonal views observe the same anatomy with exact voxel-wise correspondence, providing natural within-volume supervision. However, a representation that is predictable across views may not remain compatible with the source-trained segmentation task. We propose \textbf{CP-JEPA}, a \textbf{C}ross-\textbf{P}lane \textbf{J}oint-\textbf{E}mbedding \textbf{P}redictive \textbf{A}daptation framework following a \textbf{predict-then-adapt} principle. CP-JEPA models cross-plane prediction and task-space translation as two complementary stages. It first predicts masked target-view representations from geometrically corresponding orthogonal views, constructing a JEPA-style objective within each test volume. It then compares the cross-plane prediction with a capacity-matched axial control to isolate geometry-specific counterfactual evidence and translates this evidence into bounded, source-anchored segmentation corrections. CP-JEPA supports both single- and continual-volume adaptation by resetting volume-specific predictive states while selectively retaining reliable task-space evidence across cases. We evaluate CP-JEPA on multi-organ MRI segmentation under single- and continual-volume deployment, with and without labeled target-development data used only for configuration. Across DINOv3- and U-Net-based backbones, CP-JEPA achieves the strongest macro-average performance in three of four evaluation settings and ranks second in the remaining setting, outperforming the strongest TTA baselines by approximately $1.0$ Dice point on average.

## 223. Predicting Semantic Latents for Robust and Efficient World-Action Models

**Keywords:** Robotics, World-Action Model, Video Generative Model

[Main paper PDF](https://openreview.net/pdf?id=t8jFwDcd7c)

World-Action Models (WAMs) adapt pretrained video generative models for robot control by jointly predicting future pixel observations and actions. We argue that robot manipulation requires reasoning about high-level scene structure and object dynamics, but does not require pixel-level fidelity, which can be sensitive to nuisance factors like lighting. Rather than predicting future pixels and actions, we train our model to predict future semantic latents (e.g., frozen DINO, SigLIP, or V-JEPA encodings of future frames) and future actions. We refer to our approach as Semantic Latent Action Prediction (SLAP). Importantly, we find that video diffusion backbones can be efficiently post-trained to directly regress (in a single forward pass) future semantic latents, eliminating the need for expensive iterative video denoising. Semantic targets improves robustness to environmental perturbations (like lighting or even end-effector initial position) and requires far less robot data for post-training. We ablate several design choices and find that intermediate layers of the pretrained video transformer provide better features for control compared to the final layers, motivating an early-readout design that further improves efficiency and performance. On standard simulation benchmarks like LIBERO and RoboTwin, SLAP remains competitive with strong VLA and WAM baselines that train on 50× more robot-data. On the perturbation-heavy LIBERO-Plus benchmark, SLAP substantially outperforms pixel-level prediction. Finally, we show that SLAP can be deployed for real-world robot manipulation with as little as 30 demonstrations. SLAP is 1.9× faster than Fast-WAM, 2.2× faster than Flex-π Joint, and 19× faster than LingBot-VA, while remaining comparable in speed to $\pi_{0.5}$.

## 224. Predicting the Predictable: Feature Suppression in Joint-Embedding Predictive Architectures

**Keywords:** self-supervised learning, joint-embedding predictive architectures, feature suppression, shortcut learning, representation collapse, isotropic regularization

[Main paper PDF](https://openreview.net/pdf?id=2hxylt8J0e)

Self-supervised methods that train an encoder to map different augmented views of an image to similar embeddings must prevent the trivial solution in which all embeddings become identical. Recent work does so by constraining the embedding distribution itself: LeJEPA requires embeddings to follow an isotropic Gaussian and proves that this distribution minimizes worst-case downstream risk. However, we observe that fixing the distribution turns the prediction objective into a competition for a bounded variance budget. We find that this competition orders directions by the fraction of their variance that is stable across views—an intraclass correlation—rather than by how easily a feature is learned. Whichever feature ranks higher occupies the budget and suppresses the other. Because the constraint fixes each direction’s variance rather than which feature fills it, numerical rank does not drop even as effective rank, which measures how evenly variance is used, does. In contrast, I-JEPA, which predicts masked representations rather than comparing views, is unaffected by a competing feature that substantially degrades LeJEPA. To address this, we propose a penalty that removes variance stable across views of an image but not shared with other images, leaving the isotropy constraint intact. Empirically, we show that it reduces feature suppression and improves downstream performance.

## 225. Predictive Self-Supervised Learning Provably Identifies Stochastic Signals under Nuisance

**Keywords:** Non-generative latent variable model, JEPA, Nonlinear ICA, Causal representation learning

[Main paper PDF](https://openreview.net/pdf?id=fvSJrQqZun)

Self-supervised learning (SSL) by predicting in latent space, without generating
the input data itself, learns highly abstract, useful representations. Intuitively,
this success is often attributed to its ability to discard nuisance information that
is irrelevant to prediction. However, this poses a conundrum: both stochastic
variation in a prediction-relevant latent signal and true nuisance make observations
partly unpredictable; how could they be distinguished? Surprisingly, we prove that
common SSL methods can achieve exactly this, by implicitly instantiating a latent-
variable model with stochastic dynamics and observation-private nuisance. We
trace their ability to recover the stochastic signal to two complementary principles:
Predictive mutual information maximization ensures that representations retain the
information needed for prediction, while latent distribution matching constrains
how this information is encoded, thereby making the retained signal identifiable.
We confirm this identifiability result in simulations for Gaussian predictors, which
recover the true signal up to an affine transformation even in dynamic, nuisance-
laden environments.

## 226. Preserving Unstable Modes Through Inverse Dynamics in JEPA World Models

**Keywords:** joint-embedding predictive architectures (JEPAs), world models, inverse dynamics, feedback stabilization

[Main paper PDF](https://openreview.net/pdf?id=ei8NxUoCD5)

Robotic systems often exhibit unstable modes, along which small perturbations and disturbances can cause unbounded growth unless corrected through feedback. Controlling such systems from high-dimensional visual observations requires representations that preserve these modes. Joint-embedding predictive architectures (JEPAs) provide a natural framework for learning representations and their dynamics from visual data. However, we demonstrate that next step prediction combined with anti-collapse regularization provides no such guarantee: the training loss can be minimized while controllable unstable modes are collapsed, making stabilization from the learned representation impossible. To circumvent this, we augment predictive world-model training with an action reconstruction objective (i.e., an inverse dynamics loss) that encourages control-aware representations, namely, visual representations that preserve crucial features for control. We prove that exact action reconstruction makes the encoder injective on the finite-horizon reachable subspace, hence, no state direction produced by an action sequence within $H$ steps can be discarded. Moreover, as $H$ grows, the dominant eigenspace of the finite-horizon controllability Gramian reveals the controllable unstable subspace. Despite our theory considering linear systems, experiments on nonlinear visual control tasks (CartPole, Walker2D, and PointMaze) validate our findings and show the benefits of control-aware representation learning.

## 227. Pretraining Strategies and Scaling for ECG Foundation Models: A Systematic Study

**Keywords:** ECG, foundation model, scaling analysis, representation learning

[Main paper PDF](https://openreview.net/pdf?id=sijfRmQcmw)

Specialized foundation models are beginning to emerge in various medical subdomains, but pretraining methodologies and parametric scaling with the size of the pretraining dataset are rarely assessed systematically and in a like-for-like manner. This work focuses on foundation models for electrocardiography (ECG) data, one of the most widely captured physiological time series world-wide. We present a comprehensive assessment of pretraining methodologies, covering five different contrastive and non-contrastive self-supervised learning objectives for ECG foundation models, and investigate their scaling behavior with pretraining dataset sizes up to 11M input samples, exclusively from publicly available sources. Pretraining strategy has a meaningful and consistent impact on downstream performance, with contrastive predictive coding (slightly ahead of JEPA) yielding the strongest overall downstream performance across diverse clinical tasks. Scaling pretraining data continues to yield meaningful improvements up to 11M samples for most objectives and translates into improved downstream performance. We also compare model architectures across all pretraining methodologies and find evidence for a clear superiority of structured state space sequence (S4) models compared to transformers and CNN models. We hypothesize that the strong inductive biases of S4 models, rather than pretraining scale alone, are the primary driver of effective ECG representation learning, with important implications for future foundation model development in this and potentially other physiological signal domains.

## 228. PRISM: Probing Physical Consequence Signals In World Model Predictions

**Keywords:** JEPA

[Main paper PDF](https://openreview.net/pdf?id=piThXl52G9)

Action-conditioned world models predict the consequence of each candidate action, yet standard planners reduce each prediction to a single feature distance to a goal image. This scalar readout couples task progress with obstacle safety in one number, and the progress signal dominates: consequence information that the model faithfully predicts is lost in the aggregation. We expose this readout bottleneck through a controlled comparison. A frozen text-image projection, aligned once on robot data without collision labels, reads named object relations from the same predictions. Where feature-distance planning fails on obstacle-dense pick-and-place sequences, this relational readout achieves 71.7%, revealing that the learned representations already encode physical consequences. Three isolating interventions confirm the information is per-candidate and prediction-dependent: shuffling action-score pairings eliminates every gain, reading from current observations instead of predictions yields only partial benefit, and goal-image contrast rules out directional matching. This is a representation-level finding: the consequence information exists regardless of how downstream planning uses it. PRISM exploits this by decoupling direction from selection: geometry handles progress toward the goal, and two sequential consequence gates read VLM-written relations from each candidate’s predicted scene, filtering harmful candidates before geometry picks among survivors. On 450 transport trials, consequence gating raises completion from 62.2% to 86.7% and cuts obstacle displacement by 63%, lifting safe completion from 33.3% to 55.6%. The mechanism transfers to pick-and-place sequences and to a real Franka arm without retraining

## 229. Procedural Planning with JEPA World Model

**Keywords:** World Model, Procedural Planning, JEPA

[Main paper PDF](https://openreview.net/pdf?id=v2pJ8dMPM3)

In this work, we introduce JEPA-Pro, a Joint-Embedding Predictive Architecture (JEPA)-based world model trained end-to-end for procedural planning, whose unit of prediction is a procedural step and in which text is used only to define actions and goals. World models predict how the state of the world changes under an action, which makes them a natural fit for model-based planning. Current world models, however, predict at a fixed temporal granularity which suits low-level control but is misaligned with the unit of decision in procedural tasks such as assembling furniture or cleaning a house. The challenge in procedural planning is twofold: (1) steps have variable duration ("wash the floor" may take seconds or minutes), and (2) they are rarely contiguous, since people often performs unrelated actions in between. To address this, our model is composed of two core components: an action-conditioned causal predictor trained jointly with the state encoder, and a learned cost function that estimates how far a predicted state is from the goal. At inference time, JEPA-Pro produces plans by test-time search over candidate action sequences in latent space, selecting the sequence whose predicted trajectory minimizes the cost, without generating pixels nor text. We evaluate JEPA-Pro on world modeling, procedural understanding and procedural planning benchmarks. We establish a new state-of-the-art on WorldPrediction-WM ($71.8\%$) and on EgoPlan-Bench ($58.7\%$). On ENACT, the world model in zero-shot outperforms 23 of 30 VLM baseline, and all caption-free baselines on WorldPrediction-PP ($41.6\%$) using up to two order of magnitude less parameters. We show that finetuning the cost with few trajectories enables the world model to adapt to unseen tasks while naturally enabling test-time scaling during planning, outperforming zero-shot VLM policies on ALFRED and BEHAVIOR-1K.

## 230. Projector-JEPA: A Gated DeltaNet Two-Expert Residual Projector Bridging Video-LLMs to World-Dynamics Understanding

**Keywords:** video-llm, projector, gated deltanet

[Main paper PDF](https://openreview.net/pdf?id=up0Xp7sa3S)

Recent Video-LLMs have made rapid progress by combining powerful vision encoders with large language models. However, most models rely on a projector that simply maps frame-level visual features into the LLM input space, without explicitly modeling local changes between frames or long-range state transitions. This limitation can become a bottleneck in video understanding tasks that require temporal structure, such as motion reasoning, event ordering, and state change recognition. We propose Projector-JEPA, a two-expert residual projector that improves world-dynamics understanding in Video-LLMs by explicitly modeling local motion and global state transitions, while keeping the vision encoder, base projector, and LLM frozen. Projector-JEPA augments the output of the base projector with two Gated DeltaNet-based residual experts. The Local Expert processes a temporal sequence at each spatial position, while the State Expert processes spatially pooled frame summaries; both retain recurrent history. To supervise these complementary spatial granularities, we introduce JEPA-inspired auxiliary objectives that combine a local correspondence loss with a masked state reconstruction loss. We evaluate Projector-JEPA on seven Video-LLMs from the PLM, VideoLLaMA3, and InternVL3 families across five video understanding benchmarks. Projector-JEPA consistently improves performance across all models and benchmarks, with larger gains on tasks involving state changes, memory, and motion direction. These results suggest that the projector in Video-LLMs should be viewed not merely as a modality alignment module, but as a key component for conveying dynamic visual information to the LLM.

## 231. ProteinJEPA: Latent prediction improves protein language model pretraining

**Keywords:** protein language model, Bioinformatics, self-supervised learning, representation learning, NLP, JEPA, MLM, continued pretraining

[Main paper PDF](https://openreview.net/pdf?id=Y5mutDGK8R)

Protein language models are trained primarily with masked language modeling
(MLM), which predicts masked amino-acid identities. Joint-embedding predictive
architectures (JEPA) instead predict latent representations, but have not been
applied to proteins. 

ProteinJEPA supplements MLM with a cosine
loss for predicting the half-depth hidden states of a teacher given the unmasked sequence. On 19 tasks,
with ESM2 at 35M and 150M parameters and three pretraining seeds, MLM+JEPA
outperforms compute-matched and step-matched MLM-only continued training in 78 and 76 of 114 comparisons (14 losses, 22
ties). 

The median compute-matched gain is
$+0.0106$ on structure- and homology-sensitive tasks versus $+0.0041$
elsewhere, led by SCOPe-40 retrieval and remote homology with improvements of 6.1 percentage points in Recall@1 and 2.7 points in accuracy, respectively. Gains on these tasks increase with model size from 8M to 150M. Against the off-the-shelf checkpoint,
MLM+JEPA wins 81 of 114 comparisons (median $+0.0068$) without improving MLM loss.
 In random initialization the gain is smaller and replicates inconsistently across seeds ($p{=}0.059$). The same recipe improves the
causal ProGen3 model, beating a compute-matched next-token-prediction control
on 12 of 16 tasks. Ablations show that cosine loss beats mean squared error, while adding
shallower targets removes most of the task gain. 

JEPA-only
training collapses downstream performance: latent prediction complements MLM rather than replacing it.

Code: https://anonymous.4open.science/r/protJepa-FF24

## 232. PRP: Diagnosing State Readability Beyond Prediction Error in JEPA World Models

**Keywords:** world models, joint-embedding predictive architectures, representation probing, state readability, rollout evaluation, test-time adaptation

[Main paper PDF](https://openreview.net/pdf?id=g9q1X0ykvD)

World models predict environmental changes from observations and actions to support planning. Latent world models predict learned representations, typically evaluated through aggregate error. We introduce Paired Rollout Probing (PRP), a state-specific evaluation protocol combining three paired representation paths, fixed observation-trained probes, and persistence baselines. Comparing observed and predicted representations measures state readability through probe accuracy at each horizon; comparison with the initial representation measures decoding gains beyond initialization. Two Meta-World-trained models maintain high position readability over 15 rollout steps, whereas a DROID-trained V-JEPA 2-AC model evaluated on Meta-World shows sharp decay within two predictions. In the shifted checkpoint, matched observation restarts improve next-step object decoding by 22 percentage points, with the benefit fading over the next two to three steps. One-step adaptation lowers prediction error while the displayed adapted readout remains below frozen-latent persistence over steps 2–8. PRP thus adds a physical-state criterion to rollout evaluation: whether prediction and adaptation improve access to the required quantities beyond retaining the initial observation.

## 233. Q-JEPA: Predicting Question-Relevant Visual Representations

**Keywords:** multimodal large language models, visual question answering, visual focusing, V-JEPA

[Main paper PDF](https://openreview.net/pdf?id=FjfYoKYLoy)

Acquiring visual representations that capture question-relevant regions is central to visual understanding. Existing approaches obtain such representations through explicit image manipulation, attention-guided visual selection, or autoregressive latent generation, requiring additional visual processing or intermediate generation within the language model. As the transition from a full image to a question-relevant local view can be considered as a zoom-in prediction in video, we propose Q-JEPA, which draws on V-JEPA’s video-pretrained spatiotemporal representations and predictive priors to infer question-relevant target-view representations directly from the full-image context. These representations are predicted independently of the LLM’s generation process, providing an effective and flexible visual interface with the potential to reduce inference overhead. Specifically, Q-JEPA introduces a Question-Guided Predictor that builds on the pretrained predictor with global cross-attention module to incorporate the full question context and focus cross-attention module to further associate target-view features with object- and relation-bearing contents in the question, thereby guiding prediction toward the relevant visual evidence.  In addition, a three-stage training strategy progressively enables the predictor with the ability to produce question-relevant visual representations and subsequently aligns these representations with a downstream LLM for visual understanding. Evaluations show that Q-JEPA achieves 64.10% on GQA and 79.03% on PhysObjects, outperforming Qwen2.5-VL-7B by 3.72 and 19.58 percentage points, respectively, while reducing image inference latency by 22.2%.

## 234. Q-PhysJEPA: Query-Conditioned Physical Abstraction for JEPA World Models

**Keywords:** JEPA, World Model

[Main paper PDF](https://openreview.net/pdf?id=CiSKLLStye)

Embodied world models should preserve the physical evidence needed for the task at hand, yet accurate latent prediction and physical-property decoding do not by themselves establish decision relevance. We introduce Q-PhysJEPA, a query-conditioned joint-embedding predictive architecture that incorporates task queries before low-dimensional history compression, rather than only during candidate evaluation. The model aggregates visual, proprioceptive, and action histories into shared evidence slots, reweights these slots through query-conditioned gating, and compresses them into a task-dependent representation. It then predicts future observation representations for candidate control settings and estimates their utilities from the predicted futures. Future prediction, utility regression, and candidate ranking are jointly trained using observed executions. We examine query-relative physical content through property readouts, candidate-future predictions, and utility estimates under matched query switches and physical interventions. On ManiSkill manipulation tests with physical parameters outside the training ranges, Q-PhysJEPA achieves 56.29\% top-1 candidate-selection accuracy, averaged equally across four task objectives, compared with 46.83\% for a query-independent representation baseline, an improvement of 9.46 percentage points. Controlled analyses further suggest that greater query-dependent physical selectivity does not necessarily translate into better decisions. These findings support task-conditioned history compression while highlighting the distinction between accessible physical information and its usefulness for candidate selection. Codes are available at \href{https://anonymous.4open.science/r/Q-PhysJEPA-30A7}{\faGithub}.

## 235. Qantara: Bridge-Flow Training for Multi-Paradigm JEPA Inference

**Keywords:** JEPA, world models, visuomotor control, flow matching, Brownian bridge, goal-conditioned planning, behaviour cloning, inverse dynamics

[Main paper PDF](https://openreview.net/pdf?id=MFFYUUwGjs)

Joint-Embedding Predictive Architectures (JEPAs) underpin a growing family of latent world models for control from raw pixels. Published JEPA world models for pixel-based control (PLDM, DINO-WM, LeWM, V-JEPA-2-AC) each commit at training time to a single inference paradigm, trajectory optimisation in a learned dynamics model, so a checkpoint trained to plan cannot be read off as a policy without retraining. Deferring that choice to inference would let the constraints that bind at deployment, per-step latency and whether a goal observation can be supplied, pick the path. We present Qantara, an end-to-end JEPA of about 21M parameters whose joint training objective pairs a Brownian-bridge interpolant between consecutive clean latents on the state axis with noise-to-data flow matching on the action axis. One checkpoint serves three inference paradigms without retraining: latent planning, behaviour-cloning action sampling, and a video-inverse composition that predicts the next latent without action conditioning, then recovers the action bridging the two. Training samples the two noise levels along the edges of the (action-noise, state-noise) square, one edge per inference dispatch, so each path is trained where it is queried. Replacing that sampler with uniform sampling over the square at matched compute drops Push-T planning from 90.1 to 53.3 success rate (SR). On the LeWM control suite at a matched 10-epoch budget, Qantara averages 91.2 SR over the four environments and reaches 93.7 on OGBench-Cube, +7.7 over DINO-WM and +17.0 over LeWM, each measured against the stronger of that baseline's published score and our retrain of it. From the same weights the two goal-blind paths, which receive no goal image, reach 82.1-83.2 SR on Push-T and 70.8-72.8 on Cube at roughly 15-65x lower inference cost, and fall to near-noise on Reacher, whose released training corpus comes from a random policy.

## 236. R-JEPA: A Relational World Model That Predicts Before It Observes

**Keywords:** relational world models, joint-embedding predictive architectures, few-shot relational reasoning, latent prediction, negative sampling, knowledge editing, link prediction

[Main paper PDF](https://openreview.net/pdf?id=OAxT23jFH0)

Relational reasoning from a few examples is usually studied by naming the shared relation or scoring candidate answers, while joint embedding predictive architectures (JEPA) hold that predicting a target without negatives is the better objective. These views obscure what a relation does to a state, when that operation can stay fixed, and when predicting the state beats choosing among candidates. We argue that relational reasoning is better understood as an inference cycle in latent space, where a relation induced from example pairs predicts an unobserved state that is reused as the next input and checked against later observations. Based on this view, we propose R-JEPA, a relation reader and a transition operator that returns a state, trained by latent prediction or classification or used without learned parameters. Across knowledge graphs and systems described to language models, the predicted state follows edits of the knowledge, composes over grounded steps and ranks facts missing from a 2019Wikidata snapshot as well as the true relation does. How consistently roles form directions, measured across seven language models, decides whether the transition must be learned, and latent prediction needs no negatives, while classification with one negative per query trails it by up to 0.13. These results suggest that relational reasoning should be evaluated by prediction before observation, and that latent prediction pays where classification cannot see enough negatives.

## 237. Reachability, Not Resemblance: Learning the Planning Geometry of Latent World Models

**Keywords:** world models, latent planning, model predictive control, quasimetric learning, temporal distance, goal-conditioned reinforcement learning, long-horizon planning, JEPA

[Main paper PDF](https://openreview.net/pdf?id=SS5iIxcZqA)

World models (WMs) let an agent act by imagining the consequences of candidate actions. Latent WMs roll candidate action sequences forward in latent space and keep the one whose predicted final latent lies nearest the goal, so the distance behind “nearest”, the planning geometry, is what planning optimizes. Current models, LeWorldModel (LeWM) among them, use a plain Euclidean norm in an encoder trained only to predict and to avoid collapse, a geometry with no reason to reflect temporal reachability, and whether the mismatch matters has never been measured. Here we show that the mismatch is benign for near goals and dominant for far ones, and that it can be repaired without retraining: Geometry for World Models (GeoWM), a head with $0.6\%$ of the parameters fitted to the frozen encoder so that consecutive states lie within one unit and random pairs far apart, approximates temporal distance and, read as the terminal cost, restores long-horizon planning at no added planning cost. On four benchmarks the head matches or exceeds the baseline at the standard goal offset and separates from it as the goal recedes, raising success from $16\%$ to $38\%$ on Push-T and from $38\%$ to $94\%$ on Two-Room at four times that offset. The gain is in the cost, not the representation, and the head transfers unchanged to a WM of another family. The planning geometry is thus the lever for long-horizon planning, the one component prior work has held fixed while improving the rollout and the search around it. More broadly, what a planner is asked to measure matters more than the machinery around it: plan by reachability, not resemblance.

## 238. Recoverable but Not Preserved: Hidden Forgetting in Continual Self-Supervised Medical Pretraining

**Keywords:** continual learning, self-supervised learning, representation learning, catastrophic forgetting, foundation models, stability-plasticity, domain shift, medical imaging

[Main paper PDF](https://openreview.net/pdf?id=V1QrGvrUmU)

Continual self-supervised pretraining is a natural strategy for keeping medical foundation encoders current, yet its standard evaluation protocol, fine-tuning the updated encoder on a source task, can itself recover degraded representations and thereby obscure underlying forgetting. Continuing CheXWorld, a JEPA-style chest-radiograph ViT, on RSNA Pneumonia leaves NIH ChestX-ray14 fine-tuning performance nearly unchanged (79.6--80.1 mAUROC), while a frozen linear probe on the same checkpoints loses 1.6 points. These trends diverge consistently across three training seeds and individual pathologies: Nodule, Pneumothorax, and Emphysema lose 3.5--4.2 probe points that fine-tuning largely recovers. This degradation occurs even though RSNA images are drawn from NIH and grows to 12.5 points after a single PadChest hop. We then ask what mechanisms preserve frozen representational accessibility. Prediction surprise, used to gate a fast/slow EMA dual memory, is a valid \emph{plasticity} signal, tracking which samples induce larger representation changes ($\rho=0.51$), but per-sample target arbitration retains no more than a constant gate matched to its mean. More broadly, methods whose targets track the learner single, dual, gated, or rate-modulated converge to similar retention (77.8--78.2 mAUROC), whereas methods that explicitly constrain the learner toward the pre-update model retain up to 80.0 mAUROC in single-seed comparisons; EWC exhibits the same trend as regularization strength increases. Finally, changing only the probe early-stopping rule shifts the estimated retention by 2.4 points. Together, these results distinguish recoverability from preservation and plasticity from vulnerability, and motivate a reporting protocol for evaluating continually updated encoders.

## 239. Representation Geometry Matters for Planning with JEPA World Models

**Keywords:** world model, representation learning

[Main paper PDF](https://openreview.net/pdf?id=4HVGSrk9Pm)

Joint-embedding predictive world models support planning through latent predictions, but unconstrained joint training can collapse distinct observations to identical embeddings.
Two prominent strategies for avoiding collapse are to inherit pretrained features, as in DINO-WM, or to learn representations end-to-end with anti-collapse regularization, as in LeWorldModel (LeWM).
Yet avoiding collapse does not ensure that latent distances distinguish outcomes in ways that matter for the task.
In object manipulation, for example, success depends on the object's position and orientation relative to the goal.
Such task-relevant state information can remain accurately decodable while barely influencing latent distance. The resulting planning cost may fail to reflect how close a predicted outcome is to the task goal.
In this paper, we propose SCALE (State-CAlibrated Latent Embeddings), a method that correlates sampled pairwise latent distances with distances in task-relevant state space.
Added to LeWM's existing objective, SCALE preserves its architecture, requires privileged state only during training, and adds no planning-time computation.
We show that SCALE improves planning success over LeWM across manipulation and navigation tasks with multiple solvers and provide a comprehensive analysis of how SCALE reshapes representation geometry to support planning.

## 240. Representation Selection in Capacity-Limited LeJEPA

**Keywords:** self-supervised learning; LeJEPA; representation learning; latent variable recovery

[Main paper PDF](https://openreview.net/pdf?id=UIZpTlKNek)

Self-supervised Joint-Embedding Predictive Architectures (JEPAs) learn from correlated observations of the same system. Existing LeJEPA theory shows that, when the representation dimension matches the number of latent variables and all latent variables evolve at the same rate, the training objective can linearly recover the latent variables. In practical models, however, the representation dimension is often smaller, and there is still no complete theory of how limited representation capacity is allocated. We study latent variable selection in LeJEPA under limited representation capacity and analyze how its distributional constraint affects this selection. We show that, when latent variables evolve at different rates, the model ranks both the latent variables and nonlinear functions of them. As a result, functions of higher order of slower latent variables can replace faster latent variables in the learned representation. LeJEPA's distributional constraint can rule out simple polynomial solutions of higher order, but it can still allow multiple representation coordinates to depend on the same slow latent variable. This source reuse can leave predictable information about the next representation outside the selected span. Based on this analysis, we introduce an additional conditional mean constraint to reduce this information loss. Under the Gaussian model, the two constraints yield linear invariant structure, and alignment selects the leading linear subspace when the cutoff is strict. Our experiments support the predicted selection boundary and the effect of the proposed correction.

## 241. Representational Collapse and Spectral Recovery in Koopman-Structured Time-Series JEPAs

**Keywords:** Joint-embedding predictive architectures (JEPA), Self-supervised representation learning, Koopman operator theory, Delay embeddings, Time-series dynamical systems

[Main paper PDF](https://openreview.net/pdf?id=EyN56DCrQx)

Joint-embedding predictive architectures (JEPAs) are an effective framework for self-supervised learning on sequential data, but their latent representations remain difficult to interpret, particularly when a dynamical system generates the data. We study predictive self-supervised learning through Koopman operator theory and delay embeddings. Extending prior analyses of the eigenvalue-one case, we show that, under standard assumptions, training a linear latent predictor amounts to learning a finite-dimensional approximation to a Koopman-invariant subspace. Absent variance and covariance constraints on the latent space, both unconstrained and norm-preserving predictors converge toward degenerate representations rather than well-organized ones; this collapse, rather than the loss of oscillatory structure, is the dominant failure mode of predictive self-supervised learning on dynamical data. Standard variance-covariance regularization suffices to prevent it, and a Koopman-structured predictor adds interpretability: its learned rotation angles can be compared directly against the spectral content of the underlying system. We relate context length, latent dimension, and prediction horizon to observability, spectral capacity, and predictability. On synthetic dynamical systems, the learned representations recover the true oscillation frequencies, including combination frequencies not explicitly targeted by the model, while exhibiting the collapse and capacity trade-offs predicted by our analysis.

## 242. RESETTLE: Robotic Recovery through Disagreement-Triggered Retrieval and Efficient Corrective Control

**Keywords:** Robot Policy Recovery, Vision-Language-Action Models, World-Action Models, Uncertainty-Aware Control, Retrieval-Guided Control

[Main paper PDF](https://openreview.net/pdf?id=9OPjnVXWHy)

Reliable robotic manipulation requires timely intervention to correct emerging deviations and restore progress after execution errors. However, recovery methods based on repeated vision-language reasoning or iterative online optimization can incur substantial latency, delaying intervention. To address these challenges, we introduce RESETTLE (Robotic recovery through disagreement-Triggered retrieval and Efficient Corrective Control), a model-agnostic framework that provides computationally efficient recovery at the action-execution interface of frozen robot policies. RESETTLE triggers recovery when two action proposals independently sampled under identical conditioning persistently disagree. It retrieves a same-task demonstration reference using an adapted V-JEPA encoder and combines a state-servo prior with a guarded visual residual to execute one corrective action without online trajectory optimization or additional vision-language reasoning, then returns control to the base policy. Across six base policies in simulation, RESETTLE achieves up to 8.70\%, 6.28\%, and 6.83\% absolute success-rate gains on LIBERO-Plus, Meta-World, and RoboCasa Tabletop, respectively, with further improvements on four real-world tasks using two policies. In QwenPI-based comparisons, its monitoring-and-recovery computation latency is 74.04\%--93.57\% lower than VoLoAgent's monitoring-and-planning latency for grasp and place tool calls. It also raises Harness VLA's LIBERO-Pro Swap success from 42\% to 50\%, demonstrating compatibility with high-level agentic planning.

## 243. Rethinking the Representation Space for World-Action Models: Pixels, VAE Latents, or Semantic Representations?

**Keywords:** world-action model, robotic control

[Main paper PDF](https://openreview.net/pdf?id=vZofYkQXj7)

World-action models (WAMs) built on video generation models learn interaction dynamics that map observations to robot actions. Because video generators can produce implausible or hallucinated futures under perturbation, many recent WAMs add auxiliary supervision on other representations to improve robustness under distribution shift. These additions increase post-training cost and introduce trade-offs among loss weights, while leaving open where generalization comes from. We instead ask a more basic question: in which representation space should a WAM predict the future? Within a shared framework and without auxiliary objectives, we compare models that predict the future in pixels (Pixel-WAM), VAE latents (VAE-WAM), or semantic features from frozen pretrained encoders (RAE-WAM). Across six fusion designs, hidden-state fusion transfers video pretraining most effectively. Following this, the V-JEPA RAE-WAM reaches 55.2% success from scratch, compared with 45.7% for the DINOv2 RAE-WAM, 45.4% for VAE-WAM, and 37.2% for Pixel-WAM on LIBERO-Plus. The same representation ordering holds in clean simulated bimanual manipulation, and on a real dual-arm platform the V-JEPA RAE-WAM outperforms π0.5 and DreamZero. Our results point to a simple principle for building world-action models: rather than reconstructing pixels or relying on auxiliary supervision, predict the future in a pretrained semantic space whose structure already reflects how scenes evolve under action.

## 244. Reweight, Do Not Re-calibrate: Reusing the Same Encoder-Predictor Pair (World Model) When the Policy or Query Changes

**Keywords:** conformal prediction, uncertainty quantification, distribution shift, covariate shift, density ratio estimation, world models, robot learning, off-policy evaluation, calibration

[Main paper PDF](https://openreview.net/pdf?id=g08iJmKcRc)

A world model calibrated under one policy is queried under another once a planner selects actions from its predictions. We ask whether the same frozen encoder-predictor can be reused under a changed policy or a changed query law without re-calibration on target labels. Conformal off-policy prediction marginalizes the action and predicts a return, which makes the importance weight a function of the outcome and forces an outcome model, rejection subsampling, or a trajectory product. We condition on the action and predict the next state, which makes the weight measurable before the outcome and removes all three; the reduction holds at one step, and the occupancy factor returns over a horizon. With a planner enacting the new policy on RoboCasa, exact propensity weighting of the source calibration set reaches 0.913 coverage with no new observations, against 0.910 after recalibrating on 75 labelled target episodes per task (model seed 271828, temperature 3); recalibration re-collects 300 labelled episodes under each new policy, while the weighted construction reuses one 600-episode source set across all nine target policies. We prove that the target-to-source likelihood ratio is measurable before the outcome and factors into state-occupancy and action-propensity ratios, and combine weighted conformal prediction with the exact or an estimated ratio. Under a query change, coverage at nominal 0.90 moves from 0.902 to 0.550 and to 0.909 with learned weights on 192 Franka transitions, and from 0.734 to 0.903 on 5,100 FurnitureBench episodes, matching oracle weighting; with V-JEPA-2-AC in place of DINOv2 on the Franka data, 0.561 and 0.917. Under the planner-enacted policy change, coverage moves from 0.750 to 0.912 with each radius finite, a paired gain of 16.2 points [8.5, 23.7], replicating on two further model seeds at 0.690 to 0.877 and 0.735 to 0.892. For a learned ratio, the exact convex dual of the classifier-regret constraint within each quantile bin of the posterior gives coverage lower bounds of 0.863 and 0.802 on the two query-change corpora, against observed 0.909 and 0.903. Finite-support identities of the argument are machine-checked in Lean 4.

## 245. RiJEPA: Rule-Informed Neuro-Symbolic Joint-Embedding Predictive Architecture

**Keywords:** Joint-Embedding Predictive Architectures, Neuro-Symbolic Learning, Rule-Informed Representation Learning, Energy-Based Model, Self-Supervised Learning

[Main paper PDF](https://openreview.net/pdf?id=ruRMMWmXgV)

Modern Joint-Embedding Predictive Architectures (JEPAs) learn powerful representations from data but lack explicit mechanisms for incorporating symbolic knowledge, while traditional rule systems are interpretable but rely on rigid discrete representations and combinatorial search. We introduce \textbf{RiJEPA}, a Rule-Informed Neuro-Symbolic JEPA that connects symbolic reasoning and predictive representation learning in both directions. In the \emph{rules-for-JEPA} direction, RiJEPA combines Energy-Based Constraints (EBC) with a multi-modal dual-encoder architecture to align continuous observations and symbolic rules in a shared latent space, shaping valid rules into low-energy basins while repelling contradictory or invalid rules. In the reverse \emph{JEPA-for-rules} direction, the resulting differentiable rule-energy landscape replaces discrete rule search with gradient-guided exploration, supporting joint rule generation, forward inference, abductive reasoning, and marginal-predictive translation. On a controlled simulation, RiJEPA preserves near-zero energy for valid rules while increasing the energy of invalid OOD rules by approximately $85\times$ relative to a classic JEPA. On the UCI Heart Disease case study, RiJEPA organizes patient representations around symbolic diagnostic poles, enabling prediction by latent-space proximity without training a downstream classifier and supporting generative rule reasoning. Together, these results establish a bidirectional neuro-symbolic principle: symbolic rules can shape predictive representations, while the resulting representations provide a continuous, differentiable space for reasoning over and discovering rules.

## 246. RoboCTR: Cross-Modal Trajectory Rewarding for World Model-Based Robotic Planning

**Keywords:** Embodied AI

[Main paper PDF](https://openreview.net/pdf?id=ctxuGW19TT)

Action-conditioned world models require a planning score that evaluates predicted trajectories with respect to the task goal. We propose RoboCTR, a Cross-Modal Trajectory Reward (CTR) interface that scores a latent rollout against the available text, goal-image, and demonstration-video goals. Stage I learns a goal-conditioned per-step critic; Stage II freezes this critic and uses its gradients to shape the V-JEPA2 predictor; receding-horizon MPC then reuses the same critic to rank candidate action sequences. We further introduce RoboTrain, an eight-task simulation collection with keyframe-aligned subtask instructions and positive and negative trajectory segments. On seven RoboTwin2 tasks, RoboCTR achieves 84.3\% macro success versus 79.7\% for $\pi$0, a gain of 4.6 percentage points, with the largest gains on Pick Dual Bottles and Place Object in Basket. Additional ablations examine the training stages, reward interface, goal modalities, task decomposition, and guidance weight. We also present qualitative demonstrations on a physical manipulator.

## 247. RoboJEPA: Scaling Robotic Latent World Models

**Keywords:** world models, scaling laws, robotics, planning

[Main paper PDF](https://openreview.net/pdf?id=talcM0NCjb)

Latent world models have shown a remarkable ability to predict future states and to plan in the real world. In practice, however, we lack a principled way to estimate how their capabilities scale with model size, data, and compute, an open problem that slows progress in the field. In this work we present RoboJEPA, a world model based on the Joint Embedding Predictive Architecture (JEPA) and trained on a large-scale dataset spanning 12 robotic embodiments. We show that RoboJEPA's imagination error, the error of its latent rollouts, follows a second-order power law in compute, allowing us to predict model quality well beyond the scale at which the law is fit. We further show that downstream robotic planning performance improves predictably with compute, and that imagination error is strongly correlated with it, making it a reliable proxy for real-robot evaluation. Finally, we demonstrate that latent world models can be deployed zero-shot as robotic agents, planning toward a single goal image to solve tasks requiring  long-horizon planning on real hardware. We will release all model checkpoints together with our training and robot deployment code. To our knowledge, this is the first work to establish scaling laws for multi-embodiment robotic world models trained on real robot data, and RoboJEPA, at 8B parameters, is the largest JEPA predictor model trained to date.

## 248. ROBOLEAK: CLAIM-CONDITIONED OVERLAP AUDITING FOR EMBODIED AI BENCHMARKS

**Keywords:** Embodied AI, Robot Learning, Dataset Overlap, Benchmark Contamination, Train–Test Leakage, Benchmark Auditing, Generalization Evaluation, Data Deduplication

[Main paper PDF](https://openreview.net/pdf?id=R79WM5NLWK)

Robot-learning benchmarks often reuse objects, scenes, and skills across training and evaluation to probe transfer under controlled changes. Yet a benchmark score alone does not reveal which aspects of the evaluated behavior are novel relative to the training collection. We introduce ROBOLEAK, a claim-conditioned auditing framework that first records cross-boundary relations at five levels—stored files,
decoded observations, near-duplicate views, object and scene structure, and task semantics—and then applies a declared evaluation contract specifying which observed relations violate the benchmark’s intended novelty. Auditing LIBERO with ROBOLEAK shows that all seven Goal-task object models already appear in the training suites, while no scene composition is repeated; under a strict novelty rule
a single familiar task is excluded, and this one exclusion raises SmolVLA’s score from 76% to 80%, leaves X-VLA unchanged at 100%, and slightly lowers VLA-JEPA’s score. The same cleaning moves different models in opposite directions because it removes a task each model finds differently hard. A complementary controlled exposure study finds no consistent average gain from exact-task demon-
strations, while revealing substantial seed-level variation under a fixed training budget. ROBOLEAK turns a benchmark score into an answerable question: what was shared, what was required to be new, and which tasks does the number average over?

## 249. S$^2$-JEPA: Self-Sparsifying Representations in Joint-Embedding Predictive Architectures

**Keywords:** Joint-Embedding Predictive Architectures, Sparse Representation Learning, Self-Supervised Learning, Adaptive Optimization

[Main paper PDF](https://openreview.net/pdf?id=xf3A7EBait)

Rectified LpJEPA enables direct control over representation sparsity in joint-embedding predictive architectures (JEPA), yet its performance degrades as representations approach extreme sparsity. We show that much of this degradation is an optimization cost rather than a limit of the sparse code, as aggressive sparsity shrinks gradients and limits early formation of informative features. We therefore introduce S$^2$-JEPA, a self-sparsifying JEPA that paces sparsification from loss curvature and corrects optimization strength from code density, adapting both throughout learning without labels or reference runs. At $\sim 96\%$ sparsity, reference-free S$^2$-JEPA improves frozen encoder and sparse projector accuracy over fixed-sparse training by up to $14.4$ and $14.5$ points, and exceeds its non-sparse counterpart on CIFAR-100 and STL-10, while retaining $97.2\%$ of non-sparse accuracy on ImageNet-100. Its gains over fixed-sparse training hold across ResNet and ViT backbones and four optimizers. Pretrained on CIFAR-100, S$^2$-JEPA improves mean transfer accuracy across five datasets by $8.7$ points over fixed-sparse training, matching non-sparse transfer, and outperforms dense JEPA codes in nearest-neighbor retrieval with $12\times$ less storage.

## 250. S-JEPA : Soft Clustering Anchors for Self-Supervised Speech Representation Learning

**Keywords:** JEPA, Representation Learning, Speech

[Main paper PDF](https://openreview.net/pdf?id=z6BHyA5Xtw)

Self-supervised speech encoders are predominantly trained by predicting discrete hard cluster IDs at masked positions, a recipe that collapses acoustic ambiguity at category boundaries and requires interrupting training to re-cluster the entire corpus between iterations. We introduce S-JEPA, a JEPA-style encoder-predictor pair trained to match the soft posteriors of a Gaussian Mixture Model at masked
positions via KL divergence. Training runs as one continuous optimization trajectory in two phases: a fixed GMM over MFCC features, then an online GMM over encoder features, with the input layer selected adaptively from a label-free signal, so the re-cluster step runs online rather than offline and the choice of which transformer layer to cluster on is no longer hand-tuned. Under the SUPERB protocol, S-JEPA achieves the lowest WER among evaluated SSL methods below 90M parameters and matches HuBERT-Base on emotion recognition at roughly half its parameter count, with no offline re-clustering and no pretrained teacher. Pre-training data differs across the compared methods, so this is a comparison at matched parameter count rather than matched data or compute. An analysis of the predictor’s per-frame entropy on held-out speech reveals a bimodal distribution with a substantial minority of frames near the entropy of a perfect two-cluster tie, showing that the objective retains inter-cluster mass on frames where a hard target would have to discard it.

## 251. SE-JEPA: Learning Representations of Structured Event Sequences via Latent Prediction

**Keywords:** Self-Supervised Learning, Structured Event Sequences, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=ZKk5oRN4qm)

Structured event data contains within-event field dependencies and cross-event contextual relationships that can provide 
complementary information for representation learning. A key challenge is to integrate information from related events into field-level predictive learning. We propose the Structured-Event Joint-Embedding Predictive Architecture (SE-JEPA), a self-supervised framework that combines local field modeling with cross-event context through masked-field latent prediction. SE-JEPA constructs within-event representations using field-specific encodings and retrieves field-aligned context through same-field cross-event attention. An event-level residual auxiliary objective further uses pooled event representations to learn context-induced corrections to local predictions. The two mechanisms optimize a shared encoder and predictor using latent targets supplied by an exponential moving-average teacher. Experiments on four public structured-event benchmarks covering diverse downstream tasks demonstrate the effectiveness of SE-JEPA under frozen linear evaluation and full fine-tuning.

## 252. See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space

**Keywords:** embodied navigation, navigation foundation model, representation learning, pretrained visual encoders, multi-level feature fusion, latent dynamics, world models, long-horizon planning

[Main paper PDF](https://openreview.net/pdf?id=DqQf4Zia2s)

What visual representation should a navigation policy act on? A central idea of representation learning is that the task’s own error should shape the representation. Navigation policies built on vision foundation models largely set this idea aside: the encoders’ pretraining objectives decide much of what the vision-language backbone sees. We present RepresentNav, a navigation foundation model built on a self-constructed representation space: a visual representation constructed by the policy’s own objectives out of the internal structure of vision foundation models. RepresentNav builds this space with Representation Residuals, a compact three-layer transformer that attends over features spanning the full depth of multiple complementary vision foundation models, so that the policy learns to see what it needs for navigation. In the same space it dreams what it wants: before every action a latent chain-of-thought predicts the representation of the scene a moment ahead. The dream is trained end-to-end with the policy as a joint-embedding predictive architecture (JEPA), with a next-representation prediction loss and a regularizer on its targets. RepresentNav sets a new state of the art on VLNVerse, VLN-CE R2R, EVT-Bench, and two point-goal benchmarks, and its gains carry over to a physical robot amid clutter and moving people. On the VLNVerse fine-grained benchmark, RepresentNav achieves a success rate of 83.80%, outperforming the previous state of the art by 20.05 percentage points, and on EVT-Bench distracted tracking it reaches 85.5% with a single camera (+10.1). Analysis shows where they come from. With the same encoders, the self-constructed space clearly outperforms concatenating their outputs and learns to weight their layers unevenly, and a dream in it cuts collisions by a quarter. A single dreamed latent decodes into the depth, semantics, and 3D occupancy of the scene a moment ahead, more accurately than pretrained encoders applied to the real future frame, although occupancy is never supervised, and the rollout tracks the robot’s own motion over the next second: the dream emerges as a compact latent world model.

## 253. Self-Supervised Encoders Learn a Task Prior in Their Spectrum That Isotropy Erases

**Keywords:** self-supervised learning, representation learning, isotropy, JEPA, spectral regularization, linear probing, ridge regression, Bayesian prior, spectral bias, label efficiency, few-shot transfer, pre-registration

[Main paper PDF](https://openreview.net/pdf?id=VVxJGbOtKq)

Self-supervised objectives increasingly push representations toward an isotropic Gaussian, which LeJEPA proves optimal for worst-case linear probes. We show that once tasks come from a distribution, a representation's spectrum is a label-free prior over them, and isotropy is the uniform prior. A one-penalty ridge probe on spectrum $s$ is generalised ridge on the latents with per-direction penalty $\lambda/s_i$, and is the Bayes (Wiener) estimator iff $s\propto p$, the prior's variances, for any sample size, dimension and design that excites every direction (Lindley–Smith read from the representation's side), and a power-law prior recovers the spectral-bias learning-curve rate. Theorem A prices a spectrum in labels, and Theorem B shows that a $C$-class task's prior has rank $C-1$, so isotropy flattens exactly the directions that carry the task. Under a protocol on 23 encoders and 15 vision and text tasks (169 cells), isotropy costs a median 21 accuracy points at 200 labels (range 0.5–64), and recovering the discarded prior takes a median 500 labels, a price predicted ($\rho=0.89$) by the cost of detecting the weakest task direction, found post hoc on 20 cells, then replicated on the other 149. The prior comes back without labels. Averaged over other tasks, it recovers a median 89% of the oracle gain, and training toward a non-flat spectral target instead of isotropy raises 200-label accuracy from 60% to 80%, with the isotropy-trained encoder still worse even given the oracle prior. A supervised control pays the same price, so the effect is a property of linear probing itself.

## 254. Self-Supervised Learning of Task-Agnostic Representations for Physical Dynamics

**Keywords:** Foundation Models, Dynamical Systems, PDE, Self-supervised, Latent representations, JEPA

[Main paper PDF](https://openreview.net/pdf?id=SfmcXkC3Zh)

Foundation models for spatio-temporal physical systems seek representations that generalize across systems, parameters, and operating conditions. We explore a self-supervised route to this goal, decoupling representation learning from task-specific prediction to capture reusable properties of physical dynamics.
We study masked reconstruction in physical space and JEPA-style prediction in latent space, and introduce regime fingerprinting to capture trajectory-level properties of the dynamics: an early partial observation must identify a broader view of the same trajectory, thereby encouraging the preservation of information that persists across time.
The learned representations provide explicit, compact conditioning signals for downstream models and support efficient in-context adaptation to previously unseen physical systems. Experiments on heterogeneous 2D and 3D spatio-temporal dynamics across multiple downstream tasks show strong performance in few-shot settings, together with computationally efficient cross-physics generalization.

## 255. Semigroup-JEPA: Latent Dynamics Consistency for Zero-Shot Physics Generalization

**Keywords:** Physics-Conditioned World Models, Zero-Shot Physics Generalization, Long-Horizon Prediction, JEPA, Robot Learning, Out-of-Distribution Dynamics

[Main paper PDF](https://openreview.net/pdf?id=E2hTmSfYZG)

Joint-Embedding Predictive Architecture (JEPA) world models learn a compact latent representation of the world that supports prediction and planning, but their capability to learn physics and generate physically realistic dynamics remains hitherto untested. In this work, we introduce SemiGroup-JEPA (SG-JEPA), which extends the LeWorldModel framework by supplying the parameter governing the physics to the temporal model via action-conditioning and jointly training an encoder and predictor through an autoregressive latent rollout. To evaluate the model's ability to generalize out of distribution, we design dynamical tasks under different gravitational fields that, despite obeying the same physical law, exhibit qualitatively different dynamics, ranging from floating motion in weak gravitational fields to rapid bouncing in strong ones. In contrast to DINO-WM, SG-JEPA reduces open-loop prediction error by up to $2\times$ on two-dimensional datasets, and increases control success rate up to $2.5\times$ for three-dimensional robotic datasets, for which we train independent diffusion policies. To explain this advantage, we develop a linear feature model that separates local law-conditioned error from its recursive amplification under rollout. Guided by this model, we find that back-propagating the multi-step rollout loss into the representation trains the encoder to keep the features that the predictor can carry forward, and that those are the features the dynamics depend on, so most of the gain comes from the encoder learning better features rather than from the predictor learning better dynamics.

## 256. ShiftWM: World Models that Move What They Saw

**Keywords:** world models, feature forecasting, action-conditioned prediction, DINOv2, robot learning

[Main paper PDF](https://openreview.net/pdf?id=xsYoBJWWJo)

World models let an agent evaluate actions before executing them, and forecasting in the patch-feature space of a frozen visual foundation model keeps them compact. Current latent world models, such as DINO-WM and V-JEPA 2-AC, regenerate the whole feature grid at every future step and feed their predictions back as inputs. Yet in manipulation and surgical scenes most content persists and only moves, so regeneration corrupts the static background and lets errors compound. We introduce ShiftWM, a latent world model that forecasts by moving what it has already seen: for every future step it predicts an action-conditioned soft transport of nearby observed patch features, learned without flow supervision, a gate between moved and kept features and a correction for new content, and it decodes all horizons in parallel. As an output head, it also attaches to open-source world models. On held-out real-robot video from DROID, Language-Table and the bimanual IWS tasks, and on seven surgical tasks from Open-H, ShiftWM has the lowest error of all matched output heads, 7.6% below a direct predictor on DROID; as a plug-in, it lowers the error of the 1.3B-parameter V-JEPA 2-AC by 15.7%.

## 257. SiamJEPA: On the Role of Siamese Student Encoders in JEPA

**Keywords:** JEPA, self supervised learning

[Main paper PDF](https://openreview.net/pdf?id=rnGKOcquJa)

Joint Embedding Predictive Architectures (JEPAs) have emerged as a promising framework for self-supervised representation learning by predicting latent embeddings of masked regions rather than reconstructing pixels. Existing JEPA methods typically employ a single student encoder, leaving the role of Siamese student encoders largely unexplored. In this paper, we propose Siamese JEPA (SiamJEPA), a JEPA framework with masked Siamese student encoders and an exponential moving average (EMA) teacher, which can also be viewed as a JEPA formulation of the brain-inspired representation learning model PhiNet. We further introduce Random Shuffle Teacher (RST), which removes spatial correspondence in teacher targets to encourage semantic patch representations, and develop an RST-based semantic-to-spatial curriculum. Experiments on ImageNet show that Siamese student encoders effectively regularize the JEPA objective, improving representation separability and accelerating early-stage learning. Moreover, under RST, stronger Siamese regularization substantially increases class-discriminative information in individual patch tokens, suggesting that the semantic bias arises from the interaction between RST and the Siamese objective rather than from shuffling alone. SiamJEPA consistently outperforms comparable single-encoder JEPA variants under limited training budgets. With RST-based curriculum learning and a ViT-Base backbone, SiamJEPA achieves 73.3\% linear-probing accuracy after 450 epochs using a substantially simpler masking strategy, compared with 72.9\% for I-JEPA after 600 epochs. Under I-JEPA's linear-probing protocol, the same checkpoint achieves 74.2\%, outperforming I-JEPA (72.9\%) and DSeq-JEPA (73.5\%). These results demonstrate that Siamese student encoders provide an effective inductive bias for predictive representation learning and can be further enhanced through semantic-to-spatial curriculum learning.

## 258. Slice Selection Matters: Structured and Adaptive Directions for Sliced Latent Regularization

**Keywords:** sliced latent regularization, representation learning, self-supervised learning, autoencoders, JEPA, Gaussianity, sliced Wasserstein, Epps--Pulley, adaptive slice directions

[Main paper PDF](https://openreview.net/pdf?id=RuJtQpHao5)

Sliced latent regularization typically uses random projections to pursue Gaussian-target matching, but these directions can conceal discrepancies along directions populated by the encoder. We investigate deterministic rotation and propose a simple radial-adaptive augmentation to better fulfill the regularization objective. For $D$-dimensional latents, we append $K$ normalized minibatch vectors to $D$ random or rotating base directions, selecting vectors whose lengths are unusually small or large relative to the isotropic Gaussian target. Recomputed at each training step, this construction requires no additional learned parameters or inner optimization and supports both sliced Wasserstein-$2$ and Epps--Pulley losses. Across autoencoding and JEPA-style self-supervision on MNIST and ImageNet-100, matched-budget controls replace the $K$ adaptive directions with $K$ random directions, separating augmentation from base schedule and slice count. Over ten matched seeds, radial-adaptive augmentation lowers mean held-out latent-direction Kolmogorov--Smirnov discrepancy in all 16 comparisons spanning datasets, objectives, losses, and base schedules. Additional evaluation with disjoint samples preserves these mean improvements. Deterministic rotation alone has no universal advantage, whereas adaptation benefits both base schedules. A residual directional gap remains, so improved projected agreement does not establish complete Gaussian matching. We therefore recommend radial-adaptive augmentation as a simple complement to sliced Gaussian regularization when improved target matching is the goal, together with evaluation using both random and latent directions.

## 259. Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models

**Keywords:** Visual World Models; Representation Learning; Joint-Embedding Predictive Architectures; Object-Centric Representation Learning.

[Main paper PDF](https://openreview.net/pdf?id=pP6eBCqjLf)

As a prototypical latent world model, Joint-Embedding Predictive Architectures (JEPAs) provide strong semantic representations. However, dense patch representations expose a redundant interface to downstream predictors, which must implicitly infer spatial organization and temporal correspondence, presenting three challenges. First, object information is distributed across patches, forcing each downstream predictor to redundantly recover object structure that could otherwise be reused across tasks before modeling interactions. Second, the lack of explicit entity correspondence across time makes historical transitions expensive, restricting the predictor's flexibility in utilizing context. Third, limited by the lack of explicit transport structure, existing JEPA models typically use pointwise $\ell_1/\ell_2$ distances, which are insensitive to spatial displacement when predicted and goal supports are largely disjoint. We propose the Slot-based Joint-Embedding Predictive Architecture (Slot-JEPA), which decomposes dense representations into stable semantic slots and time-varying spatial masks. Pretrained once and frozen downstream, this decomposition exposes a reusable object-structured interface. Building on it, our Transition Memory Predictor (TMP) stores visual transitions as compact masks and retrieves useful context using statistics of corresponding slots. Its two branches separate slot-specific dynamics from shared cross-slot dynamics. We further use Unbalanced Optimal Transport (UOT) to supervise mask prediction and evaluate candidate plans by transporting mass between aligned predicted and goal masks, providing a signal better aligned with spatial progress. Across seven visual-understanding benchmarks, the slot-reconstructed features remain transferable. Slot-JEPA also improves goal-conditioned planning across six planar environments and four robotic arm planning tasks on the REALM-JEPA benchmark.

## 260. Solver-JEPA: A Joint-Embedding Predictive Architecture for Visual Problem Solving

**Keywords:** joint-embedding predictive architecture; Visual Problem Solving

[Main paper PDF](https://openreview.net/pdf?id=Qtydq74fhU)

Visual problem solving requires transforming visually presented problems into structured solutions under global constraints and objectives. While methods learn to generate solution images or reasoning trajectories, visual problem solving still lacks a representation-learning objective designed to organize the information required for solution construction. Such learning is challenging because the visually observed structure and the underlying decision structure are not equivalent: small local differences can induce discontinuous changes in global feasibility or optimality, while a final solution image reveals only one successful endpoint and leaves the consequences and interactions of alternative decisions unspecified. We introduce **Solver-JEPA**, a solver-supervised joint-embedding predictive architecture that turns each problem into a family of decision-conditioned prediction tasks. During training, partial commitments specify tentative local decisions, and task solvers provide targets describing their consequences for problem structure, global feasibility, attainable solution quality, and compatible complete solutions. Predicting these targets in representation space encourages the visual encoder to preserve solution-relevant local-to-global dependencies. A separately trained decoder reuses the frozen representation to construct complete solution images without solver access at inference. Across four visual problem solving tasks, Solver-JEPA improves strict solution accuracy by up to **11.6** percentage points and provides **15**--**150 times**  faster inference than generation-based baselines. Controlled ablations show that joint-embedding alignment and composite-commitment supervision improve the readability of complete solutions from the learned representations.

## 261. SPACE: Sparse Predictive Attractor via Counterfactual Eviction for Streaming Video Memory

**Keywords:** Streaming Video Memory; Predictive Representation Learning; Long-Horizon Video Understanding; Attractor Dynamics;

[Main paper PDF](https://openreview.net/pdf?id=cs4d8TMUS7)

Fixed-capacity streaming video memory requires repeated eviction decisions whose effects accumulate over time. Yet existing policies are evaluated primarily in terms of retained information or downstream accuracy, leaving how repeated updates alter the futures supported by memory largely unexamined. We define a memory's predictive state as the future representations supported by its retained history and formulate eviction as counterfactual control over transitions in this space. We introduce SPACE (Sparse Predictive Attractor via Counterfactual Eviction), which uses a frozen multi-horizon JEPA to predict the future representations induced by alternative eviction actions. Counterfactual utility identifies future-useful alternatives, while slow predictive-basin geometry determines when to correct avoidable drift and when to adapt to sustained predictive change, without online parameter updates. We further introduce MABS-Bench, which evaluates future-task sufficiency, within-regime predictive stability, transition responsiveness, and perturbation recovery under matched causal streams and memory budgets. Across multiple video datasets, SPACE yields consistent improvements in dataset-native task performance while reducing predictive-state drift.

## 262. Sparse-TD-JEPA: Improving Zero-Shot Reinforcement Learning With Sparse Latent Task Representations

**Keywords:** Zero-Shot Reinforcement Learning

[Main paper PDF](https://openreview.net/pdf?id=s0c6BSrswA)

Successor-feature-based zero-shot reinforcement learning methods pre-train a task encoder and successor-feature predictor on offline, reward-free data, then recover a policy at test time by solving a closed-form linear regression over a small labeled dataset. We find that the success rate of this method can be improved by a property that has received little attention: when the task encoder is dense, the predicted reward surface is less concentrated near the goal, producing a weaker gradient for the policy to follow. We address this by introducing a sparsity learning objective into the task encoder that concentrates reward-predictive structure into a smaller effective subspace of the task encoder's latent space. The sparsity penalty is applied during training and requires no change to the closed-form inference procedure at test time. We instantiate this idea as Sparse-TD-JEPA, a direct extension of the recently published TD-JEPA framework, a Temporal Difference (TD) reinforcement framework for the Joint-Embedding Predictive Architecture (JEPA). We evaluate our method across various standard zero-shot performance benchmarks covering various robot manipulation, locomotion, and exploratory navigation tasks. Our method does not only achieve consistent better zero-shot performance than the baseline framework, it achieved the best performance of all established zero-shot baselines tested in most cases.

## 263. SparseWAM: Driving World-Action Models are Worth 16 Register Tokens

**Keywords:** End-to-End Autonomous Driving; World-Action Model; Register Latent; Mixture-of-Transformers

[Main paper PDF](https://openreview.net/pdf?id=6ISCyimm6T)

World Action Models (WAMs) transfer scene-dynamics priors to planning by jointly forecasting future scenes and ego trajectories. However, WAMs built on video generators must generate dense future videos at inference, incurring prohibitive latency, while efficient variants discard the world branch at deployment and thus forgo test-time imagination. Even when dense video latents are replaced with patch-level DINO or JEPA features, these representations still involve long token sequences and encode decision-irrelevant information. We therefore propose SparseWAM, which forecasts in a sparse register space of only 16 tokens per frame, compressed from frozen DINOv2 features and shaped by joint planning-and-scoring pretraining to concentrate decision-relevant information. Within this space, SparseWAM employs a modality-decoupled Mixture-of-Transformers with a causal attention mask that lets action tokens condition on imagined future registers, retaining explicit imagine-then-act reasoning at deployment. Its compactness further enables low-cost multimodal sampling. As a result, our SparseWAM achieves 92.1 PDMS on NAVSIM v1, 89.8 EPDMS on NAVSIM v2, and 40.1 on NavHard at only 260 ms latency, roughly 1/3 that of DriveVA, demonstrating the efficiency of the sparse register space. Code will be released upon acceptance.

## 264. Spectral Unit Tests for Predictive Representation Models: A Fault Atlas and Its Scope Conditions

**Keywords:** self-supervised learning, representation learning, JEPA, model diagnostics, spectral analysis, evaluation, failure detection

[Main paper PDF](https://openreview.net/pdf?id=bJHuhRxqDt)

Predictive representation models are trained and monitored through one scalar loss, which can hide
a predictor that loses to the unconditional mean of its targets in some directions. We audit the
residual spectrally: whitening its second moment against the target covariance makes any generalized
eigenvalue above one a certificate of regret against the mean; a covariance ceiling attributes that
regret to the predictor, not to irreducible noise. A LayerNorm-aware rank bound predicts the
unit-eigenvalue plateau a normalized affine head forces; five public checkpoints saturate it, and
excising it makes the spectrum interpretable. On the official I-JEPA head the scalar and the spectrum
disagree: its NMSE is below that of a ridge head refit on the audit data, yet its plateau-excluded
regret mass is 2.2 times that of the ridge head, a gap that official-loss refits narrow
by only 4-10%. A calibrated gate fires at full power on a five percent
rise in scalar error for rank, bias and noise faults, and reaches faults confined to low-variance
directions, which no calibrated NMSE gate reaches on this source budget. NMSE-matched injected faults
leave distinct spectral signatures consistent with the theory's bounds, and rules fit on one
checkpoint transfer blind to two others under conditions we state and measure. The audit also caught
the HuggingFace I-JEPA export carrying the online encoder rather than the EMA target.

## 265. Spectral-Target Physical Latent Structuring for JEPA-Style World Models

**Keywords:** LeWorldModel; Physical  representation laziness;  Fourier auxiliary head

[Main paper PDF](https://openreview.net/pdf?id=Dm7YQ9buR6)

Latent world models have become increasingly popular as a method to predict and plan in latent space rather than pixel space. Recent architectures, such as LeWorldModel (LeWM), jointly train the encoder and predictor using regularization techniques like SIGReg to prevent representation collapse. Even with such regularization preventing representation collapse, we identify a new world model failure mode of physical representation laziness, particularly noted in highly dynamic environments. For these lazy cases, the learned latent states do not collapse but nonetheless fail to represent key physical properties, causing ubiquitous downstream planning failure. To resolve this issue, we propose training-time auxiliary supervision with a lightweight "Fourier auxiliary head", which enforces physically-informed structuring of the latent space with no additional inference-time cost and can be generalized to any environment. Experimentally, we show that the auxiliary head substantially improves planning success rates in dynamic environments where the baseline LeWM exhibits physical representation laziness. It also leads to modest improvements in other environments, even when the baseline does not exhibit physical representation laziness. We further observe superior planning performance being accompanied by higher latent space correlations with key physical properties, indicating both the ability of our method to physically structure latent states and the potential planning-side benefit to the learned representation being physically structured. Finally, we ablate across various training data amounts, showing that in low-data regimes, auxiliary supervision is particularly impactful in increasing success rate. These findings support the use of our Fourier auxiliary head method to improve both overall success rate and data efficiency, while avoiding representation laziness in latent world models.

## 266. SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation Pretraining

**Keywords:** Earth observation, foundation models, hyperspectral imagery, multimodal learning, self-supervised learning, representation learning

[Main paper PDF](https://openreview.net/pdf?id=vvRwX9PlGE)

Earth observation (EO) foundation models (FMs) are increasingly trained on multisensor data, spanning multispectral imagery (MSI), synthetic aperture radar (SAR), and derived geospatial layers, but hyperspectral imagery (HSI) remains underrepresented. Conversely, most existing hyperspectral FMs are trained on HSI alone, leaving joint pretraining and fusion of HSI with co-located EO sensors underexplored. We introduce SpectralEarth-FM, a hierarchical transformer for multisensor EO input with heterogeneous spectral dimensionality. The architecture combines spectral tokenization for HSI, sensor-specific encoders, a cross-sensor fusion module, and a shared encoder. To pretrain SpectralEarth-FM, we curate SpectralEarth-MM, a multimodal dataset that co-locates HSI from three spaceborne sensors (EnMAP, EMIT, DESIS) with Sentinel-2, Landsat-8/9 optical imagery, Landsat land surface temperature, and Sentinel-1 SAR. It comprises approximately 2M globally distributed locations, 25M georeferenced patches, and over 40TB of data. Pretraining uses a Joint-Embedding Predictive Architecture (JEPA)-style objective that matches representations between global views and single-sensor local views from the same location. We evaluate SpectralEarth-FM on hyperspectral downstream tasks and standard EO benchmarks following the PANGAEA protocol, achieving results that are competitive with state-of-the-art models.

## 267. SphereJEPA: Learning Spherical Video Representations From Perspective Video via $360\degree$ Self-Supervision

**Keywords:** self-supervised learning, joint-embedding predictive architecture, video representation learning, 360° video, spherical representations, out-of-view prediction, point tracking

[Main paper PDF](https://openreview.net/pdf?id=FRp5VHW5K6)

We introduce SphereJEPA, a joint-embedding predictive architecture that learns to
predict features for every direction around the camera from ordinary
perspective video. Its context and target come from different projections of
the same scene. The context encoder reads the perspective video, an EMA target
encoder reads the panorama, and both write onto tokens indexed by direction on
a gravity-aligned sphere. Unlike a standard JEPA, whose predictor is discarded
after pre-training, SphereJEPA keeps its predictor, because its output is the
representation of what lies out of view. Training crops are rendered from the
panorama, so the data needs no posed or calibrated capture, and the model never
receives camera parameters. Inference is a single forward pass through a
113M-parameter encoder and predictor. The predicted features identify unseen
scenes and their orientation, and agree with what the camera later observes.
With frozen features and an analytical readout, SphereJEPA roughly halves the
TAPVid360 mean angular error of every method not trained on the benchmark,
without using point labels.
representation whose spatial support extends beyond the current image, while
fine-grained transfer depends on the complete training construction.

## 268. SPLICE: Latent Diffusion over JEPA Embeddings for Conformal Time-Series Inpainting

**Keywords:** self-supervised representation learning, time-series imputation, uncertainty quantification, conformal prediction, energy systems, joint-embedding predictive architectures (JEPA), flow matching

[Main paper PDF](https://openreview.net/pdf?id=IIeFblS1gb)

Long gaps in time series are difficult to reconstruct reliably, and in power systems
imputed load values inform dispatch and planning. Existing generative imputers
are accurate but provide no finite-sample reliability guarantees under changing
conditions. We introduce SPLICE (Self-supervised Predictive Latent Inpainting
with Conformal Envelopes), which couples a JEPA encoder, a conditional latent
bridge, an hourly-conditioned decoder, and Adaptive Conformal Inference (ACI).
Controlled ablations indicate that long-horizon fidelity is driven more by the pre-
dictive representation than by generative complexity: under a matched bridge and
decoder, JEPA outperforms reconstructive VAE and contrastive TS2Vec encoders,
and once the representation is fixed a 5-step flow sampler matches or improves
on a 50-step DDIM sampler at a 5−10× speedup. The same ordering is recovered 
on twelve hydrological catchments. Across thirteen load datasets at 91-day
gaps, SPLICE attains the lowest mean Load-only MSE (0.056), winning 9 of 12
non-degenerate datasets against seven established baselines, and the best mean
CRPS (0.182, 7.8% below the strongest competitor), while ACI holds 93–95%
empirical coverage where static calibration under-covers by up to 7.5 percentage
points. A pooled JEPA encoder transfers to four held-out datasets with only bridge
and decoder adaptation.

## 269. SplitJEPA: Learning Invariant and Variant Latent Worlds without Reconstruction

**Keywords:** JEPA, Representation Learning

[Main paper PDF](https://openreview.net/pdf?id=iyVXG91BzC)

Understanding a dynamical world calls for more than a latent state that summarizes its observations: the state should also be organized into the factors that stay shared across related observations and the factors that vary between them. For example, a robot pushing a cube to a goal should take the same action when the camera shifts or the lights dim, since nothing in the scene has moved. Existing approaches to this decomposition commonly obtain it through reconstruction, so the latent variables must first explain the entire observational world before their organization can be trusted. Joint embedding predictive architectures (JEPAs) model the latent state directly and never reconstruct, yet no existing result recovers the invariant and variant parts of the state they learn. How to learn the invariant-variant structure of the latent world without paying for its reconstruction therefore remains open. To close this gap, we introduce SplitJEPA, a JEPA that jointly recovers the latent state and its invariant and variant organization directly in representation space, without any reconstruction. We prove that, under stationary Gaussian predictive dynamics and a full-rank variation condition, \modelname identifies the invariant and variant subspaces up to independent block-wise isometries, without introducing an observation decoder. Since the guarantee needs no decoder, the result extends reconstruction-free latent recovery to invariant-variant block identification.  Experiments on synthetic nonlinear systems and robotic manipulation tasks support the theoretical results and show their practical value for both robustness and efficiency.

## 270. ST-JEPA: JEPA-Enhanced Temporal Scene–Trajectory Representation Learning for End-to-End Autonomous Driving

**Keywords:** End-to-End Autonomous Driving; Joint-Embedding Predictive Architecture (JEPA)

[Main paper PDF](https://openreview.net/pdf?id=PcLf36bZTY)

End-to-end autonomous driving requires compact representations that preserve planning-relevant spatial and temporal context. A common design in recent ViT-based E2E planners is to introduce trajectory queries only after visual feature extraction, which limits the interaction between planning intent and visual representation learning during encoding. Meanwhile, in compact-token variants, scene tokens receive only auxiliary supervision without direct self-supervision on their latent representations. To address these limitations, we present **ST-JEPA**, a temporal scene--trajectory representation learning framework with two key designs: scene--trajectory encoding and JEPA-enhanced representation learning. First, ST-JEPA injects camera-aware scene tokens and ego-conditioned trajectory tokens directly into the visual encoder, enabling them to interact with image patches throughout feature extraction. Interleaved temporal global-register attention further aggregates cross-frame context and propagates the updated representations through subsequent backbone blocks. Second, ST-JEPA incorporates joint-embedding predictive learning through two complementary mechanisms. An online scene--trajectory JEPA objective predicts compact scene and
trajectory representations from masked observations, using targets
produced by an EMA teacher from unmasked inputs. This training-only objective provides latent self-supervision directly at the compact planning bottleneck. In parallel, we adapt JEPA pretraining to driving videos and integrate the resulting spatiotemporal latent features into the encoder by projecting them into the token space and fusing them with the native scene representation. ST-JEPA achieves state-of-the-art performance on NAVSIM-v1, NAVSIM-v2, and the closed-loop HUGSIM benchmark, with systematic ablations validating the effectiveness of the proposed scene--trajectory encoding, temporal interaction, and JEPA-based representation learning. The code will be made available upon publication.

## 271. Stack-JEPA: Molecular Graph Distillation for 3D Spatial Transcriptomics

**Keywords:** Joint Embedding Predictive Architecture, Spatial Transcriptomics, Graph Reconstruction, 3D modelling, Alignment

[Main paper PDF](https://openreview.net/pdf?id=e0x5V8iofk)

Spatial transcriptomics (ST) observes isolated two-dimensional sections, cutting
anatomy and molecular neighborhoods at one arbitrary plane. Three-dimensional
(3D) ST lifts that limit, but profiling a section by ST costs far more than imaging
it by histology, so volumes are built by imaging every section with hematoxylin
and eosin (H&E), profiling a sparse subset, and imputing the rest. Existing imputers
are supervised and count-space: they regress the raw counts of one fixed
gene panel from paired sections, so the objective is dominated by dropout entries,
a new panel forces a refit, and accuracy is capped by an inter-section alignment
computed once before the model runs. We introduce STACK-JEPA, a masked
molecular graph-distillation framework for learning molecularly informed representations
throughout a serial histology stack. On a profiled section, a frozen
molecular teacher defines both per-location latent states and their local molecular
relations. A stack student is trained to recover the held-out section’s molecular
representation and relation graph from a profiled context section, the target H&E
image, in-plane coordinates, and tissue depth. Frozen TERRA and UNI2-h encoders
feed a transformer with 3D rotary position embeddings, while node- and
relation-level distillation transfer molecular structure without placing the genepanel
dimension in the backbone. After pretraining, the backbone is frozen and
only a lightweight panel-specific count decoder is fitted. The same learned descriptors
can replace raw expression in partial fused Gromov-Wasserstein transport,
including when the target section has no measured transcriptome. Across
multipe tasks, imputation on public 3D ST benchmarks and alignment under the
PASTE2 subslice protocol, STACK-JEPA outperforms the supervised and generative
state of the art, on imputation in both per-cell and per-gene correlation, and it
aligns sections for which no transcriptome was measured, which expression-based
aligners cannot handle at all.

## 272. STAIRCASE POLICY: Streaming Inference for World-Action Models with Large Action Chunks

**Keywords:** World Action Models; Model Efficiency; Action Chunk

[Main paper PDF](https://openreview.net/pdf?id=zrg4OHauXt)

World-Action Models (WAMs) improve robotic manipulation by conditioning action generation on predicted future observations, but future prediction adds further inference overhead to already expensive iterative action generation. Action chunking can amortize this cost over multiple actions, yet performance degrades over long execution horizons because later actions remain conditioned on stale observations. We introduce STAIRCASE POLICY, a streaming inference and training framework that turns a flow-matching VLA into a JEPA-style WAM and partitions a large action chunk into sub-chunks at staggered denoising stages. Near-term actions are executed as soon as they become available, while later actions continue to be refined. At each sub-chunk boundary, the future latent is re-predicted from the latest observation and used to update all unexecuted actions, enabling long-horizon execution without repeated full policy inference. The resulting future-prediction error can further serve as a signal for adaptive chunking. S-WAM achieves 97.7% on LIBERO and 87.9% on LIBERO-Plus, and improves performance across multiple policy backbones and real-robot tasks. It reaches 292.7 executed actions per second, 3.62× the throughput of conventional execution at comparable accuracy, while reducing time-to-first-action from 123.6 to 73.3 ms. With additional inference optimizations, throughput further increases to 642.9 actions per second.

## 273. State Before Pixels: Large-scale Text-to-Video Generation in Representation Space

**Keywords:** Text-to-Video Generation, Video Representations, Riemannian Flow Matching, Multimodal Generation

[Main paper PDF](https://openreview.net/pdf?id=fgf0qKhzVI)

Video representations learned by vision foundation models encode scene semantics and dynamics as spatiotemporal world states beyond pixel appearance. While representation autoencoders have shown promise for image generation, representation-space video generation remains largely underexplored, with their higher dimensionality posing additional challenges. In this paper, we demonstrate that native video representations can serve as effective modeling targets for large-scale, open-domain text-to-video generation. Our approach, **WorldFlow**, separates world-state modeling from visual rendering: a text-conditioned flow model first generates latent world states directly in native V-JEPA space, and a second-stage flow model then renders these states into high-quality videos in VAE space. This design retains the learned semantic structure of pretrained video representations as the basis for generation, while allowing fine visual details to be synthesized in a space designed for reconstruction. To enable effective diffusion-transformer denoising in this high-dimensional representation space, we systematically study its geometry and prediction parameterization. We find that by conducting Riemannian Flow Matching on the native representation manifold with *v*-prediction, high-dimensional video representations can be effectively modeled without introducing additional compression. Extensive experiments demonstrate that WorldFlow achieves high-quality text-to-video generation. Beyond RGB, the same generated world states can be readily rendered into well-aligned multimodal outputs such as depth, segmentation, human pose, *etc*. These results demonstrate the feasibility of generating unified world states containing appearance, semantics, geometry, and dynamics within a shared representation.

## 274. Steering Physics in Video World Models

**Keywords:** Video World Models, Latent-Space Steering, Physical Control, World Model Interpretability, V-JEPA, Robot Control

[Main paper PDF](https://openreview.net/pdf?id=7RvZXo8a2W)

Video world models learn representations that support prediction and planning, and a growing body of work finds that these representations capture physics and dynamics. For example, velocity and acceleration can be read from the representations of V-JEPA 2. However, knowing that a quantity is encoded does not tell us where it is represented, and without that we cannot steer it. In this work, our goal is to edit the representation so that the decoded video carries out a requested physical instruction, such as making a ball move faster. Using simulation datasets, we investigate velocity and acceleration, both linear and angular. We first observe that translation and rotation trace very distinct shapes in the latent space, and that rotation splits along two axes. This structure motivates two steering writers, an additive writer that steers translation, and an orientation field that steers rotation. Measured from the motion in the decoded video, the additive writer controls both the direction and the speed of translation, with direction errors below $10^\circ$ and speed correlations of $0.750$ in 2D and $0.861$ in 3D. For rotation, the orientation field sets how fast the object spins, and the requested and decoded spin rates correlate at $\rho=0.942$, holding at $0.945$ when the object's appearance changes. The same field, fitted only on objects spinning at a constant rate, also makes objects speed up or slow down their spin, with no refitting. Finally, we use an edited representation to steer a simulated robot arm, which strikes a ball within $2\%$ of the requested speed on all 200 test commands. Together, these results show that a video model's latent space can serve as a two-way interface to physics, in which physical quantities can be measured, set, and used as goals to plan actions in the real world.

## 275. STOCK-JEPA: Prior-Anchored Latent Revision Representation Learning in Equity Markets

**Keywords:** Financial representation learning, Joint-embedding predictive architectures, Structured financial priors

[Main paper PDF](https://openreview.net/pdf?id=v9REGSFVbf)

Learning effective representations helps characterize the structure and dynamics of equity markets from financial data with a low signal-to-noise ratio. Black-box deep models can capture complex patterns but may overfit sample noise and lack explicit economic structure. Meanwhile, classic linear financial models provide interpretable references, but their oversimplified assumptions leave non-linear signals uncaptured. To combine the strengths of these two directions, we propose Stock-JEPA, a joint-embedding predictive framework that learns predictable incremental revisions relative to a point-in-time financial prior. First, we leverage a low-complexity financial model to produce fixed statistics summarizing multi-horizon return and risk. A prior projector then maps these statistics into the target encoder's latent space as an anchor. Second, we design a context-conditioned revision predictor to estimate the future representation's predictable displacement from the anchor. Separate losses update the two branches: the anchor learns from prior statistics, while the revision captures additional predictable information from historical context. Third, we freeze all representation modules and train a downstream readout, evaluating its forecasts through cross-sectional ranking and portfolio performance. Theoretically, we prove that optimal revision reduces the prior anchor's expected squared error for the same future representation by exactly $\mathbb{E}[\lVert\boldsymbol{\Delta}\rVert_2^2]$. This nonnegative gain is the expected squared magnitude of the additional signal predictable from historical context. Experimentally, Stock-JEPA outperforms 13 strong baselines across large-scale China and U.S. equity universes on 5 key evaluation metrics. Ablation studies and representation analysis further demonstrate the value of the learned revisions for representation learning in equity markets.

## 276. Structuring Spatial Audio Representations via Invariance-Equivariance Learning

**Keywords:** self-supervised learning, spatial audio, equivariance, invariance, joint-embedding predictive architectures, sound event localization and detection, ambisonics, captioning

[Main paper PDF](https://openreview.net/pdf?id=rSi7JMrteU)

A spatial audio representation must jointly capture scene semantics to recognize what is sounding and scene geometry to understand where sound events occur. Self-supervised objectives often favor semantic invariance, treating direction as a nuisance, making spatial geometry difficult to preserve. We propose a framework for structuring spatial audio representations through invariance--equivariance learning, using geometric transformations as a training signal. In first-order ambisonics (FOA), rotating a sound field is a matrix operation, providing rotated views and their relative rotations without labels. We train encoders to remain stable under spectral nuisances while predicting how their representations change under rotation. Within this framework, we compare representations explicitly partitioned into invariant and equivariant subspaces with an unsplit predictive latent. The latter, built on seq-JEPA, is to our knowledge the first joint-embedding predictive architecture (JEPA) for spatial audio that learns invariance and equivariance jointly. We show that this latent representation organizes direction as an ordered spherical map while preserving linearly separable sound classes without an architectural split. When frozen, it achieves a lower SELD score on real recordings than supervised baselines and improves spatial audio captioning and retrieval, with the largest gains in spatial accuracy. These results demonstrate a path toward robust, general-purpose spatial audio representations that jointly encode what is present and where it occurs in space.

## 277. Supervise What Decides Success: Criterion-Aligned Auxiliary Losses for Latent World-Model Planning

**Keywords:** world model, robotic manipulation, planning, representation learning, jepa

[Main paper PDF](https://openreview.net/pdf?id=pzrLWhVHqu)

Latent world models plan by scoring candidate action sequences with distances in latent space. However, task success is judged by physical quantities, hereafter the success-criterion quantities. In all four latent world models we examine, the end-effector position is encoded in the latent state with an error larger than the success criterion allows. Such a latent state cannot separate successful candidates from failing ones. We propose an auxiliary loss that uses success-criterion quantities as training targets, whereas existing latent world models take them only as inputs. During training, a linear head on the encoder and predictor outputs regresses the success-criterion quantities, and the regression error is added to the training loss. The head is discarded after training, so the model, its cost, and its inputs at inference are unchanged. This loss alone improves the success rate on PushT and cube by 3.5% and 3.4% (absolute), and both improvements are statistically significant. A success criterion thus specifies what a world model must retain in its latent state, and we show that it can serve directly as a training target.

## 278. Support-Aware Shielding Restores Safety for Predictive World-Model Control under Shift

**Keywords:** World Model, JEPA, Out of Distribution, Deep Learning Theory

[Main paper PDF](https://openreview.net/pdf?id=U1nlpXh9rY)

A predictive world model is supposed to let an operator ask ``what if'' before committing to a change, and that promise rests entirely on the model knowing when it is wrong. We study what becomes of the promise when the world moves. Working in a setting where every planning decision can be replayed against a full-information oracle, we find a pattern that repeats across every model we train: the planners that do best are the planners that are most dangerous. The models that extract the most benefit under familiar conditions are precisely the ones that breach the operator's safety constraints once a crowd forms, and the uncertainty intervals a shield would have to trust quietly stop covering the truth exactly when they are needed. This failure is invisible from forecasting accuracy alone: models that are nearly indistinguishable on held-out prediction error behave entirely differently once their forecasts are allowed to drive actions. We then show that the remedy is not a better forecaster. It is a planner that keeps asking whether it still recognises the world. A controller that re-plans as it goes, replays its own model against what it has just observed, checks whether its forecast has wandered outside the region its training data covered, and declines to act when either test fails, recovers nearly all of the lost safety while surrendering only a small and bounded share of the achievable benefit. We prove two statements that explain the exchange - one tying how reliably shifted situations are recognised to how often constraints can be breached, one showing that the cost of declining to act is paid in proportion to how often it is declined - and we machine-check both. The lesson we draw is that safety under distribution shift is more cheaply bought with an online admission of ignorance than with a more confident model.

## 279. Sync When It Counts: A Modality-Conditional Framework for Robust Audio-Visual Deepfake Detection

**Keywords:** audio-visual deepfakes, joint embedding predictive architecture, contrastive learning, self-supervised

[Main paper PDF](https://openreview.net/pdf?id=TXofhwr1Y2)

Current audio-visual forgery detectors primarily exploit cross-modal alignment, assuming a continuous synchronization between facial movements and the acoustic speech signal. While effective on curated benchmarks, this rigid paradigm catastrophically fails under real-world conditions. When a single modality is missing or degraded, state-of-the-art alignment models (e.g., AVH-Align) collapse to near-random performance. This reveals the vulnerability that enforcing cross-modal correlation effectively blinds the model to the rich, independent forensic signals within each surviving modality. To address this, we propose a modality-conditional, self-supervised framework that completely decouples unimodal representation learning from cross-modal synchronization. Our architecture pairs a contrastive audio-visual alignment module with independent visual and audio Joint-Embedding Predictive Architecture (JEPA) streams trained entirely without manipulation labels. During inference, a deterministic routing gate evaluates the input across two tiers. To prevent modality collapse, it routes inputs with missing modalities directly to the independent JEPA streams. For standard audio-visual inputs, it halts false-positive drift by explicitly dropping natural silences (e.g., authentic pauses or nods) from the synchronization calculation. Our method achieves state-of-the-art in-domain performance on AV-Deepfake1M++ (0.8525 AUC, 0.9434 AP). Crucially, the unimodal JEPA pathways retain robust detection capabilities under severe modality degradation (0.739 audio-only AUC and 0.673 visual-only AUC), whereas prior baselines fail entirely. Furthermore, in zero-shot cross-dataset evaluation on InDeepFake, our approach achieves 0.764 AUC, outperforming several supervised in-domain models. These findings demonstrate that substituting rigid alignment with conditional, context-aware routing is crucial for resilient deepfake detection in real-world scenarios.

## 280. Takens-JEPA: Scientific Inference Across Sampling Intervals

**Keywords:** self-supervised learning, joint-embedding predictive architecture, representation learning, physical dynamics, dynamical systems, Takens embedding theorem, delay coordinates, temporal sampling rate, distribution shift, scientific machine learning, parameter estimation

[Main paper PDF](https://openreview.net/pdf?id=Kw6jhQEhHX)

Physical processes are often recorded at different time intervals, and a model trained at one interval can become unreliable when that interval changes. We ask whether a self-supervised representation can support scientific inference when the sampling interval at deployment differs from that used for downstream training. Takens’ embedding theorem suggests an answer: histories that end at the same mo- ment describe the same underlying state even when their samples are spaced differ- ently. Takens-JEPA turns this correspondence into an auxiliary ranking objective for a joint-embedding predictive architecture, drawing together histories that share an endpoint and separating them from histories with other endpoints. It needs no new data, since the extra histories are subsampled from stored trajectories, and adds no inference cost. On Active Matter, Rayleigh-Bénard convection, and Shear Flow from The Well, we fit parameter-estimation and endpoint-state reconstruc- tion heads to frozen representations at one interval and evaluate them unchanged at coarser, partly unseen intervals. On Active Matter, Takens-JEPA roughly halves the predictive baseline’s parameter-estimation error at every shifted interval and cuts endpoint-state error by a third; on Shear Flow it lowers parameter-estimation error under shift by up to 62% at the cost of a small loss at the training interval; gains on Rayleigh-Bénard are smaller. A control that applies the predictive objec- tive at several intervals recovers part of this gain: Takens-JEPA is more accurate at the training interval and the nearest unseen interval, matches the control at the coarsest interval, and uses about one-third less training compute.

## 281. Temporal Context Needs the Right Target: Projected Latent Prediction for End-to-End Driving

**Keywords:** End-to-End Autonomous Driving, Latent World Models, Temporal Fusion, Joint-Embedding Predictive Architecture, Representation Learning, Trajectory Planning

[Main paper PDF](https://openreview.net/pdf?id=DtLHOnuCB7)

Temporal context is essential for motion-aware driving, yet we find that naively introducing temporally fused features into a reconstruction-based latent world model can degrade planning performance.
We attribute this failure to a representation--objective mismatch: the predicted latent encodes temporal history and action-conditioned evolution, whereas its supervision target remains a single-frame visual latent whose exact coordinates contain factors unnecessary for planning.
To address this mismatch, we propose Temporal-JEPA LAW.
Our method first introduces Latent World-Model Temporal Fusion (LWM-TF), which causally aggregates each LAW latent token over time while preserving its spatial identity and maintaining $O(NK^2)$ attention complexity.
It then replaces raw latent reconstruction with normalized projected alignment, allowing the world model to match prediction-relevant structure without reproducing every visual-latent coordinate.
Following LeWorldModel, a sketched isotropic Gaussian regularizer (SIGReg) prevents collapse in the unnormalized embedding space.
Controlled experiments reveal the central effect of this design: temporal fusion alone improves average planning L2 from 0.61m to 0.53m, whereas coupling temporal prediction with raw mean-squared error degrades it to 0.66m.
Projected alignment mitigates this negative transfer, achieving 0.51m average L2 and reducing the average collision rate from 0.30\% to 0.09\%.
These results show that temporal information and predictive supervision must be designed jointly: LWM-TF supplies motion evidence, while JEPA provides a planning-compatible target for latent future prediction.

## 282. TEMPORAL HYPERGRAPH JOINT- EMBEDDING PREDICTIVE ARCHITECTURE FOR MULTI-AGENT PATH FINDING

**Keywords:** Multi Agent, Graph Neural network

[Main paper PDF](https://openreview.net/pdf?id=DPyXxPRhXw)

Multi-Agent Path Finding (MAPF) becomes difficult in dense environments where
multiple agents must coordinate through shared aisles, intersections, and
bottlenecks. Existing learned methods typically predict actions from the
current interaction state, while pairwise representations can lose information
about conflicts involving several agents. We introduce \textbf{TH-JEPA}, a
Temporal Hypergraph Joint-Embedding Predictive Architecture that models MAPF
as the evolution of higher-order agent-resource interactions. TH-JEPA first
constructs a dynamic conflict hypergraph from anticipated shared-resource
usage, with persistent resource nodes preserving conflict identity over time.
Training proceeds in two stages: masked temporal pretraining learns the
structure of conflict evolution without actions, followed by
action-conditioned post-training that predicts future agent and resource
representations over multiple horizons. To prevent collapse in the shared
latent space, we introduce \textbf{Conflict-Spectral Dispersion
Regularization (CSDR)}, which preserves variation over the conflict
hypergraph while discouraging redundant latent directions. At inference,
candidate joint-action sequences are rolled forward in latent space and
evaluated using receding-horizon planning. We further establish that pairwise
projection cannot, in general, preserve higher-order conflict structure and
derive sufficient conditions under which CSDR prevents structural collapse.
Experiments across dense and out-of-distribution MAPF settings show improved
scaling to larger agent populations, stronger performance under
higher-cardinality conflicts, and accurate multi-horizon prediction.

## 283. Temporally Centered SIGReg Improves LeWorldModel Representations for Robot Policy Learning

**Keywords:** World Model, JEPA, Robot Learning

[Main paper PDF](https://openreview.net/pdf?id=TYL8K0NiiK)

Recent work on LeWorldModel (LeWM) has shown that the Sketched Isotropic Gaussian Regularizer (SIGReg) enables stable end-to-end world model learning from pixels by regularizing the latent representation toward an isotropic Gaussian. While effective for latent-space planning, the representations learned by Raw LeWM are poorly suited for downstream robot policy learning. In this paper, through Monte Carlo analysis, we show that the Raw LeWM objective biases variance allocation toward the temporally persistent component, thereby suppressing the variance of the temporally centered residual. Consistent with this analysis, trained Raw LeWM representations exhibit suppressed residual variation and reduced ecodability of robot state and dynamics, particularly gripper dynamics, which are crucial for robotic manipulation. To address this issue, we apply SIGReg to $\textbf{temporally centered residuals}$ rather than to the whole latent representation. This simple change decouples persistent and residual variance allocation while retaining an effective anti-collapse property. On the LIBERO benchmark, our method improves downstream policy success on the Goal suite by 1.66× and raises the average success rate across all suites from 63.6\% to 83.8\%. Without external pretraining, it also outperforms both Diffusion Policy trained from scratch and the pretrained OpenVLA baseline. These results associate the variance-allocation bias of Raw LeWM with the downstream policy gap, and show that decoupling persistent and residual variation yields representations better suited for downstream robot policy learning.

## 284. TEX-MEX: Similarity-Guided Temporal Contrastive Learning for Time Series

**Keywords:** self-supervised learning, foundation models, timeseries, biosignals

[Main paper PDF](https://openreview.net/pdf?id=p7koKDjwwr)

Contrastive learning for time series depends on deciding which pairs of inputs should be treated as similar and dissimilar. Because few augmentations reliably preserve meaning in time series, prior methods have relied on two disjoint notions of similarity between windows: structural similarity, which relates windows with similar morphology, and temporal similarity, which relates windows that occur close together in time. We introduce TEX-MEX, to our knowledge the first approach to unify the two into a single relationship. Given a random batch of windows drawn across the dataset, TEX-MEX uses the encoder to identify which windows are structurally similar or dissimilar to each other. It then pulls each window toward the temporally shifted versions of similar windows and pushes it away from those of dissimilar ones, learning what typically accompanies similar windows in time. Across PPG, EEG, ECG, accelerometry, and continuous glucose monitoring, TEX-MEX broadly achieves state-of-the-art performance against contrastive, reconstructive, JEPA-based, and modality-specific approaches, establishing it as a strong general SSL objective. We further train a 560K-parameter PPG foundation model that achieves state-of-the-art performance across a broad range of downstream benchmarks while being roughly 50× smaller than the next-best unimodally pretrained PPG foundation model in our evaluation. We will release this foundation model open-source and open-weight to the community to support future work and practical applications.

## 285. The JEPA Paradox in Language: The Geometry of Linguistic Alternatives

**Keywords:** Joint-Embedding Predictive Architecture (JEPA), Self-Supervised Learning, Language Representation Learning, Predictive Representation Learning, Representation Collapse, Conditional Uncertainty, Latent Prediction, Masked Language Modeling

[Main paper PDF](https://openreview.net/pdf?id=h1Ue2cjTbM)

Joint-Embedding Predictive Architectures (JEPAs) are effective for images, video, and audio, yet deterministic JEPA-style latent prediction has not become a standard objective for text encoders. We argue that this gap reflects a mismatch between squared-error latent prediction and the conditional structure of language. The key requirement is conditional concentration: given a context and target location, the target representation should lie near a single meaningful point. Local image prediction often satisfies this through spatial continuity, whereas masked text can admit multiple valid token or span completions whose representations need not share a coherent center. We formalize this mismatch through three conditions --- predictability, non-collapse, and low conditional variance --- and show how their failure creates centroid degeneracy and collapse pressure in text. Matched I-JEPA and T-JEPA experiments reveal the predicted sequence: mutual-information saturation and elevated target variance precede train--validation instability, effective-rank degeneration, cosine collapse, and poor downstream transfer. The same pattern appears across five independent data seeds, indicating that it is not a sampling artifact. These results do not rule out predictive learning for language; they show that text-compatible JEPA objectives must preserve multiple plausible completions rather than compress them into a single latent point.

## 286. The Predictability Bias of Joint-Embedding Predictive Learning in Medical Imaging

**Keywords:** self-supervised learning, representation learning, joint-embedding predictive architectures, medical imaging, predictability bias

[Main paper PDF](https://openreview.net/pdf?id=caB774AxZP)

Joint-embedding predictive architectures (JEPAs) learn by predicting teacher representations of masked regions from visible context. Point prediction summarizes the conditional target distribution and cannot reproduce variation that the context does not resolve. We call this constraint predictability bias. In computed tomography (CT), recurrent anatomy is predictable from context, whereas the sporadic, localized pathology that determines clinical interpretation often is not. We introduce TAP-JEPA, a ViT-B/3D trained on 113,611 CT volumes that is competitive with state-of-the-art encoders (COLIPRI, Merlin, VoxelFM) in scan-level classification. We then audit the learned predictive pathway by replaying the exact masking, teacher, and predictor computations used during training. Prediction lowers the mean Skill (prevalence-normalized average precision) from 0.388 to 0.271 for pathology, but only from 0.921 to 0.873 for anatomy. Along the teacher direction, separating pathology from matched control regions in the same organ, prediction moves pathology 34.7% toward the controls and controls 13.6% toward pathology, with larger shifts farther from visible context. Replacing visible matched-control representations increases surrounding-target prediction loss more than fully replacing pathology representations across four pathology categories. Downstream, removing all final-layer pathology tokens reduces the decision margin by at most 0.45% in four of seven scan-level probes. Together, these results show that contextual predictability is not a sufficient proxy for clinical relevance in medical representation learning. Training objectives should therefore retain diagnostic features regardless of their predictability from surrounding anatomy.

## 287. The TIME Machine: On The Power of Motion for Efficient Perception

**Keywords:** computer vision, self-supervised learning, point tracking, machine learning, efficiency, foundation models, motion understanding, temporal understanding, sim2real

[Main paper PDF](https://openreview.net/pdf?id=WVdlWWl5Ks)

Video representation learning has seen tremendous progress in recent years. This has been driven by many factors, including the scale of training and the success of self-supervised models trained on next-frame prediction. While these factors have pushed the boundaries of what video models can do, they also introduce their own set of limitations. First, scaling video models can reach prohibitive costs, with recent models needing hundreds of years of video to be trained. Second, learning to predict the next frame (or embedding of the frame) naturally focuses on spatial information and as a result, video models still struggle with temporal understanding.  In this paper we propose a novel approach that uses motion as a modality to alleviate both of these core issues. Given the motion in a video in the form of point tracks, we mask some of the tracks and use a masked autoencoder to reconstruct the missing tracks. This allows us to learn a representation in a self-supervised manner which we call TIME (Temporally-Informed Motion Embedding), and is focused on capturing temporal information. Also, as motion is inherently appearance-invariant, TIME needs far fewer examples to generalize well. As a result, without bells and whistles, on temporal tasks TIME performs on par with state-of-the-art models, using up to 4 orders of magnitude less training data. For general tasks, TIME can be used in combination with existing representations, and we observe that it leads to a significant improvement for V-JEPA 2, RVM and VideoMAE on standard benchmarks such as SSV2, EgoExo4D and Diving48. These results point to a new promising video paradigm for both more temporally-aware as well as more scalable models.

## 288. TIDE: Selective State Exposure for Low-Budget Robot Transfer from Passive Video

**Keywords:** world models and rl, TIDE

[Main paper PDF](https://openreview.net/pdf?id=SFwxl48Jtl)

A low-budget manipulation controller benefits from interaction phase, while direct coordinates for the camera motion and edit boundary that produced a video observation need not be action inputs. Transfer Interface with Differentiated Exposure (TIDE) makes this distinction architectural: action-free pretraining learns persistent slot variables, vector-quantized temporal state, egomotion, and a cut-reset gate, while a frozen export map admits only slots and temporal tokens to the grounded policy. A same-backbone intervention tests this partition by fitting a separate action head for each visible coordinate set. With 100 grounded CALVIN episodes and 100 episodes per RLBench single-task head, heads that jointly receive egomotion and cut coordinates attain success lower by 0.119 and 0.125; withholding the temporal token costs 0.180 and 0.158. A matched-GPU-budget retrain without the two acquisition branches also attains success lower by 0.085 and 0.103. TIDE reaches $0.516 \pm 0.029$ strict five-instruction-chain success on CALVIN and $0.579 \pm 0.028$ mean success on RLBench, exceeding a compute-, width-, and head-matched action-free V-JEPA transfer by $+0.096 [0.071,0.124]$ and $+0.087 [0.061,0.115]$. The advantage persists with one shared RLBench policy and across 8 ManiSkill2 tasks; Voltron requires $3.5\times [2.9,4.2]$ as much grounded interaction to reach the same two-suite target. These results establish policy visibility as a separate design axis from predictive representation in the 25--100-episode regime.

## 289. TIDE: The Reachability–Learnability Gap in Temporal Intent Control

**Keywords:** World Models, JEPA

[Main paper PDF](https://openreview.net/pdf?id=pou0kSXFwb)

Visual world models support goal-directed control through learned latent representations used for direct execution or decision-time search, yet search may
succeed when direct execution fails. This discrepancy raises three questions:
What behaviors can a frozen system execute? Which can finite-budget search
discover? And which can a shared model recover without online search? Focusing on goal-conditioned visual control with frozen, action-conditioned jointembedding predictive world models, we introduce TIDE, a controlled empirical framework that equips each frozen representation with a standardized intentconditioned execution head and varies only the temporal structure of bounded intent corrections. Specifically, we compare SINGLE one-shot corrections, SHARED
corrections reused across execution calls, and DYNAMIC call-specific corrections
to study how temporal intervention structure affects reachability, searchability,
and learnability. In a matched intervention evaluation based on Push-T, DYNAMIC
call-specific corrections uncover more validated successful behaviors. Across four
control tasks (Push-T, Cube, Reacher, and TwoRoom) and two frozen backbones
(LeWM and Fast-LeWM), persistent SHARED corrections are more consistently
effective under matched finite search budgets. Validated SHARED interventions
can also be partially amortized into search-free control, although the gains remain
modest and offline learning signals alone do not reliably predict closed-loop improvement. These findings expose a control-interface gap in this class of frozen
visual world models: predictive latent representations do not by themselves ensure
that reachable behavior is readily searchable or learnable.

## 290. Time-JEPA: Grounding Video World Models with Physical Time Series

**Keywords:** time series, physical time series, time series supervision, video world model, JEPA

[Main paper PDF](https://openreview.net/pdf?id=VuBJN8ebTP)

Video world models learn how visual environments evolve by predicting miss-
ing or future content. However, physical-state information can provide useful
context for predicting how environments evolve. Prior work incorporates this in-
formation through different mechanisms: domain-specific physical laws can com-
plicate multi-domain training, while supervision on individual frames or frame
pairs gives limited attention to how physical state evolves over time. We intro-
duce Time-JEPA, which fine-tunes a video world model using low-dimensional,
temporally aligned physical time series as auxiliary supervision. Physical time
series connect video representations with physical state at corresponding tempo-
ral positions, encouraging the model to preserve how physical state evolves. In
multiple domains including autonomous driving, robot manipulation, and human
motion, Time-JEPA improves current-state decoding, multi-horizon future-state
prediction, and kinematic reconstruction over matched video-fine-tuned controls
across both condition and state-variable distribution shifts. Multi-domain training
provides aggregate gains over matched single-domain training in all three tasks.
External evaluations further suggest that time-series supervision improves sensi-
tivity to physical anomalies and the representation of physical interactions, includ-
ing in unseen scenarios. Aggregate gains on a second video backbone indicate that
the method can be applied to more backbones. These results suggest that physical
time series help video world models better understand the physical world.

## 291. Timescale Identification from $k$-Step Transition Operators: The Structural Entropy Spectrum

**Keywords:** structural entropy, Markov chains, timescale identification, metastability, spectral methods, world models

[Main paper PDF](https://openreview.net/pdf?id=nVZXNXJGIv)

Agents and world models discretise experience into a transition graph at one fixed step, yet behaviour has structure at several timescales. Which step should the graph be built at, and which timescales are present? Multiscale tools (Markov stability, the map equation at Markov time, implied timescales of Markov state models) sweep a time parameter but attach no significance statement to the scales they report. We make the step count k an argument of a clustering objective on the k-step operator P^k and calibrate it against a matched null: chains whose stationary flow matrix has identical margins and dwell (self-loop) mass. Our theory uses structural entropy (SE), a two-level code-length objective: the structural entropy spectrum SE(k), its null SE_null(k) and the calibrated spectrum ΔSE(k) = SE_null(k) − SE(k). We prove that the k-dependence factors through an exact identity, SI(k;C) = Σ_a F_aa(k) log2(1/V_a) (k-step module persistence × module code length), prove that when metastable blocks have stationary volume < 1/2 the metastable partition is the unique global optimizer of the idealized in-window operator, and sketch a Simon–Ando extension to nearly uncoupled chains on a window whose endpoints scale as 1/(1−λ) for the fast and slow eigenvalue clusters, so the optimal partition path coarsens through a planted hierarchy in order. On a 36-state three-level chain, the path recovers both planted levels in order at calibrated effect sizes up to 1.8 bits, although at this fixture's modest scale separation ΔSE(k) shows no plateaus; a single-scale expander control is featureless; the spectrum is estimable from a single trajectory. On latent transition graphs from a pixel-based JEPA world model, the one-step graph's calibrated effect falls below the preregistered 0.1-bit floor, while the spectrum peaks reproducibly at k* = 11–16 with 1.6–1.9 bits across five training seeds; a self-loop control shows that this structure survives removal of dwell but that the peak location is a dwell-inflated step count (two state changes). The calibration is not SE-specific: wrapped around the map equation it passes the planted-hierarchy, single-scale and structureless controls, and around Markov stability all but the expander control; both recover two balanced blocks, SE's boundary case, and the scale boundaries move with the objective. All decisive experiments were preregistered with pass/fail gates and are reported verbatim.

## 292. Touch-JEPA: Tactile Representation Learning from Hand-Object Video with Limited Tactile Supervision

**Keywords:** Self-Supervised Learning, Representation Learning, Tactile Estimation

[Main paper PDF](https://openreview.net/pdf?id=HtIEqMh6Co)

Understanding contact and tactile magnitude in hand-object interaction is a key step toward physically intelligent systems, yet learning such representations is limited by the cost and restricted coverage of tactile measurements. We present Touch-JEPA, a framework for learning tactile representations from hand-object videos with limited tactile supervision. 
We first introduce a self-supervised pretraining objective that learns from video alone without tactile supervision. Using video-derived hand geometry, Touch-JEPA predicts masked visual features at corresponding hand-surface locations from spatial and temporal context, encouraging the representation to capture latent contact dynamics. We then extend this formulation to joint representation learning, where masked prediction is applied to all videos while tactile supervision is available only for a labeled subset, grounding the shared representation in measured contact and magnitude. With self-supervised pretraining alone, simple supervised readouts on frozen Touch-JEPA features outperform supervised baselines in contact discrimination and tactile magnitude estimation across three human-hand benchmarks, and transfer to robotic hands without robot tactile training data. Joint learning with limited tactile supervision further improves contact and magnitude estimation on the human-hand benchmarks. Together, these results show that hand-object video can provide scalable self-supervision for tactile representation learning, while limited tactile measurements provide complementary physical grounding.

## 293. Towards \textit{Effective Theory} of LLMs: A Representation Learning Approach

**Keywords:** Mechanistic Interpretability, Science of LLMs, Effective Theory, Steering

[Main paper PDF](https://openreview.net/pdf?id=YPnOwLdaEi)

We propose Representational Effective Theory (RET), a framework for describing large language model computation in terms of learned macrostates rather than microscopic details. RET learns these macrostates from hidden-state trajectories using a BYOL/JEPA-style self-supervised objective, coarse-graining activations into macrovariables that preserve higher-level structure relevant for prediction and interpretation. We evaluate whether these macrovariables are practically relevant for interpretability: RET yields temporally consistent states that reveal ``mental-state'' trajectories of reasoning, capture high-level semantic structure, support early prediction of behavioral outcomes such as sycophancy and alignment faking, and provide causal handles for steering generations toward interpretable computational phases. Together, these results suggest that LLM computation admits useful effective descriptions via RET: high-level, dynamically meaningful variables that support interpretation, prediction, and intervention.

## 294. Towards All-Atom Protein World Models: Learning and Diagnosing Predictive Latent Representations

**Keywords:** protein representation learning, all-atom protein structure, joint-embedding predictive architectures, self-supervised learning, latent representations, protein world models

[Main paper PDF](https://openreview.net/pdf?id=ohiv4hh8dy)

All-atom protein models compress atomic structure into latent representations, often using reconstruction or generative objectives that require these latents to preserve precise coordinate information. Yet, residue properties depend on both local atomic environments and longer-range 3D interactions. Joint-Embedding Predictive Architectures (JEPAs) offer an alternative: predicting representations in latent space rather than reconstructing the raw input. In vision, this shifts learning away from pixel-level reconstruction toward higher-level features that transfer across tasks. We ask whether the same approach can help protein representations capture both residue-level information and broader structural context useful for protein structure and function tasks. Using the La-Proteina encoder, we train JEPA, JEPA+SIGReg and LeJEPA on masked protein structures and evaluate them with StructTokenBench. We study how masking, positional information, rotations and cropped views affect the learned representations. JEPA with 70% random masking scores higher than the Cα-conditioned La-Proteina baseline on 17 of 21 functional-site and flexibility scores. In JEPA+SIGReg, I-JEPA-style absolute positional embeddings create a strong residue-index shortcut. Relative positioning suppresses this direct shortcut and scores higher on 19 of 21 functional-site and flexibility outputs. LeJEPA reveals a different shortcut: its representations organise residues by chain length, motivating us to replace full-protein views with fixed-length crops. Evaluating all 12 encoder blocks shows that blocks 4-6 provide the highest score on 17 of 24 task/splits, while block 4 outperforms every final representation in our 18-model comparison on 22/24 task/splits. These results show the potential of latent prediction for all-atom protein representations while highlighting the importance of protein-specific representation design.

## 295. Tracking Is Not Permanence: What Video World Models Keep of a Hidden Object

**Keywords:** video world models, object permanence, self-supervised video pretraining, V-JEPA, masked prediction, intuitive physics, representation analysis

[Main paper PDF](https://openreview.net/pdf?id=JufUpEAiLN)

Video world models track objects they can see; we ask what they keep of objects they cannot. We hide an object from a frozen V-JEPA 2 predictor and compare its prediction for the hidden region with the encoder's representation of two worlds that differ only inside that region. Its decision keeps a stationary object in part and one carried inside a container not at all, and loses a moving one within 0.3 s, or 0.5 s under V-JEPA's own tube mask (ViT-H keeps it to 1.1 s at pretraining's 90% masking ratio); in projection a trace remains after the first tubelet, below the midpoint for a moving object and a closed box, at 14–60% of what a baseline copying the last view retains. The information is there: the encoder reads the object's presence at 1.00 and keeps a closed container's contents decodable for the 3.5 s of the window, while the predictor's output, read with the encoder's own probe, contains the ball in 2% of scenes once the box has been closed for half a second. On rendered scenes permanence is missing on the predictor's side, and training installs it cheaply, as a prior: three thousand predictor-only steps on synthetic containers take this belief from 0.05 to 1.00 against two matched controls. They also raise IntPhys-2019 from 84.2% to 93.3%, but so does a curriculum without containers, and which training habit the benchmark credits changes with its scoring rule: for these checkpoints, benchmark accuracy does not track the belief. Continued training with tube masks for 16k steps produces 1.1–1.6 s of moving-object carry-over on egocentric and internet-style video, so the deficit is not intrinsic to latent prediction; what persists changes with the masks and the data. VideoMAE's pixel reconstruction keeps almost nothing, and Cosmos's next-token prediction keeps a stationary hidden object but not one carried inside a moving container, where V-JEPA 2 and Cosmos fail alike.

## 296. Training-Free Few-Shot Adaptation via Exponential Tilting of Latent Representations

**Keywords:** foundation models, tilting, latent representation, few-shot adaptation

[Main paper PDF](https://openreview.net/pdf?id=XjKQSAmTGd)

Adapting frozen foundation models to new few-shot tasks is often infeasible when parameters cannot be modified    e.g., under shared checkpoints or deployment policies barring mutation. We study few-shot classification under this fully frozen-model regime: no gradients, no parameter updates, no upstream data. We show that under these constraints, adaptation reduces to choosing a weighting over the support embeddings used to form class prototypes, and that exponential (Gibbs) tilting is the unique such weighting minimizing KL divergence from the empirical support distribution subject to a task-relevance constraint. We instantiate this constraint with simple support-set scores    label consistency, geometric alignment, or classifier confidence    yielding closed-form tilted prototypes with no backward pass or iterative solving. Across three frozen encoders (DINOv3, I-JEPA, CLIP) and several few-shot and cross-domain benchmarks, tilted prototypes improve over uniform-average baselines in most settings and are competitive with training-free adaptation methods that use strictly more information (query streams, upstream statistics), while gradient-based fine-tuning remains an upper bound under weaker constraints. This positions principled latent-distribution reweighting as a lightweight, gradient-free alternative to parameter-based few-shot adaptation.

## 297. Tri-JEPA: Interaction-Aware Self-Supervised Multimodal Pretraining

**Keywords:** Earth Observation, Self-supervised Learning, Multimodal Learning

[Main paper PDF](https://openreview.net/pdf?id=43G5ZZlt4z)

Self-supervised multimodal pretraining aims to learn representations from unlabeled multimodal data that transfer across downstream tasks. Different tasks, however, may rely on different multimodal interactions: information shared across modalities, information unique to a single modality, and synergistic information that emerges only when modalities are considered jointly. Since the downstream task is unknown at pretraining time, encouraging all three may yield a more broadly useful prior. Existing methods either emphasize only a subset of these interactions or capture them implicitly through objectives over fused multimodal representations. We introduce Tri-JEPA, an interaction-aware joint-embedding predictive architecture with three predictive objectives defined by different source-target configurations. For a target modality, the shared objective predicts its representation from another modality, the unique objective predicts it from the same modality, and the synergistic objective predicts it from all other modalities jointly. These assignments are cycled across modalities for balanced coverage. The tailored objectives enable us to examine how different multimodal interactions are encouraged during pretraining and how their contributions vary across downstream tasks. Under controlled settings, Tri-JEPA consistently outperforms the multimodal self-supervised baselines considered across diverse downstream tasks. Overall, our results show that interaction-aware predictive objectives are a useful design principle for self-supervised multimodal pretraining.

## 298. TumorCast: A Cancer World Model for Longitudinal Tumor Forecasting

**Keywords:** Cancer world model, Longitudinal Forecasting, precision medicine

[Main paper PDF](https://openreview.net/pdf?id=p6OVLdHD1b)

Anticipating how a tumor will grow and spread could help clinicians adapt therapy in time, yet forecasting its evolution is difficult: tumors exhibit substantial heterogeneity, and their trajectories depend on anatomical location, current disease state, local tissue context, and the patient’s clinical history. Existing approaches often predict clinical outcomes directly from observed CT scans or records, or generate future CT scans, leaving the evolution of CT latent states insufficiently modeled. To address this gap, we propose TumorCast, a cancer world model for longitudinal tumor forecasting that predicts CT latent states conditioned on clinical history, interval treatment, and transition interval. Built on the joint-embedding predictive architecture (JEPA), TumorCast learns reusable predicted CT latent states through a Representation–Dynamics–Readout curriculum, without reconstructing future CT scans. First, longitudinal CT scan pairs adapt a CT encoder and latent predictor through future-state supervision, while clinical text provides conditioning inputs for state transitions. Next, chained training learns successive state transitions through recursive rollout, with future-state supervision propagating backward through the trajectory so that later prediction errors refine earlier state transitions and predicted intermediate states. Finally, a shared clinical reader (Qwen3.5-9B/27B) combines predicted CT latent states with clinical context to forecast lesion diameter, lesion size change, and liver metastasis status. To support evaluation, we curate a multimodal tumor forecasting benchmark comprising 1,344 patients, 3,606 CT scans with corresponding radiology reports, and 11,728 structured clinical entries covering clinical history and interval treatment, yielding 2,400 forecasting examples across liver and pancreas. Experiments show that TumorCast outperforms rendered-slice vision-language models (VLMs) and text-only baselines, highlighting the success of our multimodal JEPA design and potential clinical effectiveness.

## 299. TwinJEPA: Action-Preferred Predictive Representations for Goal-Conditioned Control

**Keywords:** Reinforcement learning, Joint-Embedding Predictive Architectures, World Models

[Main paper PDF](https://openreview.net/pdf?id=Tpo8fJ5jwP)

Joint-Embedding Predictive Architectures (JEPAs) have recently emerged as a
promising paradigm for representation learning by predicting future latent
states without reconstructing observations. Recent work has adapted JEPA-style latent prediction to offline zero-shot control through action-conditioned temporal prediction, enabling representations to capture long-horizon dynamics from fixed behavioral data. However, transition-level predictive objectives largely supervise actions in isolation and provide limited information about which actions are preferable when similar states admit different goal-conditioned outcomes. We introduce \textbf{TwinJEPA}, a framework for learning action-preferred predictive representations by augmenting JEPA-based control with offline-mined action-preference supervision. TwinJEPA identifies approximately matched states across offline trajectories and constructs preference pairs via goal-conditioned reward relabeling. It then learns two complementary objectives: reward-gap regression, which preserves the magnitude of outcome differences, and preference classification, which captures the relative ordering of alternative actions. Both objectives are used only during training and incur no additional inference-time cost. We evaluate TwinJEPA across long-horizon navigation and continuous-control
benchmarks, with both state-based and pixel-based observations. TwinJEPA yields positive benchmark-level mean differences across all matched state-based evaluations, while analyses across domains and observation modalities indicate that larger gains tend to arise when local action alternatives provide more informative outcome contrasts. The results suggest that local action-comparison supervision can complement temporal prediction by encouraging JEPA-based representations to retain both long-horizon temporal structure and fine-grained distinctions among locally observed actions for offline zero-shot control.

## 300. UMM-JEPA: Generative Pretraining via Masked Next-Scale Representation Prediction for Unified Multimodal Models

**Keywords:** Unified Multimodal Models, JEPA, LLM Pretraining

[Main paper PDF](https://openreview.net/pdf?id=d5sYlJxHoh)

Unified multimodal models can support both visual understanding and generation, yet generative training does not necessarily improve understanding. We argue that this limitation may arise from a mismatch between the representation targeted by generation and the perceptual representation used for understanding. Conventional generation objectives primarily optimize synthesis-oriented spaces such as discrete visual codes or generative latents. We therefore introduce UMM-JEPA, which reformulates generation as progressive prediction of continuous visual-understanding representations. The model constructs a $64\rightarrow128\rightarrow256\rightarrow512$ representation hierarchy from coarse to fine, while pixel rendering is decoupled from representation pretraining and attached only afterward. Controlled comparisons show that the representation-prediction objective accounts for most of the understanding improvement, while a data-matched control leaves the group means nearly unchanged. The final UMM-JEPA reaches a 16-benchmark visual mean of 51.71, against 46.36 for the understanding-only Qwen-VL baseline, and the text mean also rises. Compared with discrete-code and latent-flow generation objectives, perceptual representation prediction yields stronger and more consistent transfer to understanding. Linear probes and visual-evidence interventions further reveal richer object and spatial structure and stronger use of image-specific information. These results suggest that generation can benefit understanding when it directly supervises the perceptual representations that understanding consumes.

## 301. Understanding Feature Learning Dynamics of SIGReg via BHEP Statistics

**Keywords:** Self-Supervised Learning, Learning Dynamics, JEPA, LeJEPA, Regularizer, SIGReg

[Main paper PDF](https://openreview.net/pdf?id=OAiyzoDnYk)

Self-supervised training with LeJEPA relies on the SIGReg regularizer, which pulls the embedding distribution toward an isotropic Gaussian and prevents dimensional collapse. However, its random projections make the learning dynamics hard to analyze directly. MMD-Gauss, a closed-form approximation of SIGReg, is a bandwidth mixture of BHEP statistics, and therefore we adopt BHEP as a tractable proxy that shares the same target distribution. Leveraging this theoretical proxy, we derive closed-form ODEs governing the macroscopic feature learning dynamics, exact under the BHEP proxy and our stated assumptions. Based on this formulation, we identify two phases: an initial rapid-growth $\textit{Explosion Phase}$ in which leading covariance eigenvalues overshoot, followed by a self-stabilizing $\textit{Shrinking Phase}$ in which they return toward the isotropic target while later features emerge one after another after increasingly long delays.
We show that the eigenvalue dynamics are governed by a global $\textbf{engine}$ $\alpha$, which drives every dormant feature and collapses as the top features saturate, and a $\textbf{brake}$ $\beta$, which plateaus early, so the target eigenvalue $T=\alpha/\beta$ steps down with each saturated feature. For MMD-Gauss and SIGReg the bandwidth mixture leaves no single engine and brake, but the force on a dormant feature and the common target eigenvalue survive and decrease in the same way, so the two phases and the stepwise delay carry over.

## 302. V-JEPA Hand: Simple, Accurate and Fast 3D Hand and Camera Trajectory Recovery from Egocentric Videos

**Keywords:** Egocentric Video, 4D Reconstruction, Hand Reconstruction

[Main paper PDF](https://openreview.net/pdf?id=zW7efBBL9N)

Egocentric video supports diverse applications, including robot learning,
augmented reality, and human activity understanding.
Recovering metric 3D hand trajectories from such video requires estimating
both hand motion and camera egomotion to express the hands in a consistent
reference frame.
Many existing pipelines recover hand and camera motion in separate stages,
combining hand detection, hand reconstruction, camera tracking, and
trajectory refinement.
We present \method, a simple feed-forward video model that jointly
reconstructs bilateral hand motion and camera motion from egocentric clips.
It uses a self-supervised V-JEPA~2.1 encoder to extract spatio-temporal
features from full-frame video and a query-based predictor to decode these
features into per-frame hand poses, hand presence, and camera motion.
We use the predicted camera motion to express the hand trajectories in a
common world frame.
The model accepts known focal lengths or predicts them when unavailable.
It reconstructs each clip in a single forward pass.
We train both components end to end in a single stage on a mixture of
diverse pseudo-labelled videos and high-precision 3D annotations.
A single model achieves the lowest coverage-aware mean per-joint
position error (MPJPE) among comparable baselines on ARCTIC, HOT3D,
and EgoStandard. It also yields lower world-frame trajectory errors than the compared
SLAM-based pipelines. Ablations support the benefits of video pretraining, temporal context,
and mixed supervision.
\method achieves a forward-pass throughput of $91.3$\,FPS on a single
RTX A6000.
We will publicly release our code, model weights, and training scripts.

## 303. V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents

**Keywords:** World-action-models, Language-conditioned robotic manipulation, JEPA, Single-stage method

[Main paper PDF](https://openreview.net/pdf?id=vkkAFWIjKP)

World-action models (WAMs) couple future visual-state prediction with action generation.
By adapting video generators or image-editing models pretrained at scale, a prominent line of recent WAMs inherits both predictive knowledge and the models in which it was learned.
We ask whether a predictive visual latent space induced by large-scale predictive pretraining can instead provide a sufficient foundation for effective WAM learning without inheriting a complete pretrained visual generative model.
To answer this question, we introduce \textbf{V-JEPA Policy}, a simple framework that builds a WAM on the latent space of a frozen V-JEPA 2.1 encoder.
An instruction-conditioned future-latent predictor and a flow-matching action expert are jointly learned from scratch in a single downstream stage, with the predictor's future-informed context key--value states conditioning action generation.
With 0.9B total parameters, of which 0.6B are trainable, \textbf{V-JEPA Policy} achieves competitive performance with representative WAM and vision-language-action baselines across LIBERO, LIBERO-Plus, and RoboCasa-GR1. Comparing visual foundations under the same downstream framework and training budget identifies V-JEPA latents as more effective than the discriminative, reconstructive, and video-understanding-oriented alternatives, particularly under distribution shifts.
Beyond task-specific learning, the same latent space supports acquiring transferable future-modeling knowledge from diverse in-the-wild instruction-annotated videos.
Pretraining the predictor on DROID video--instruction pairs without action labels and adapting it into a WAM within our framework yields substantial gains in downstream control and out-of-distribution generalization.
Together, these findings establish predictive visual latents as a foundation for learning effective WAMs, supporting both direct learning from task-specific demonstrations and the transfer of future-modeling knowledge acquired through predictor pretraining on broader in-the-wild videos.

## 304. Variational Streaming Flow: Probabilistic Forecasting in Physical Time

**Keywords:** Probabilistic forecasting, Generative models, Dynamical Systems, World Models

[Main paper PDF](https://openreview.net/pdf?id=F0zMVaI13l)

Probabilistic forecasting is important for predicting complex dynamical systems because intrinsic randomness and incomplete observations can cause the same observed state to evolve into multiple plausible futures. While flow matching is a flexible approach for probabilistic forecasting, it is computationally expensive. Streaming flow (SF) reformulates this approach to model temporal evolution efficiently by learning a continuous velocity field directly in physical time. However, SF learns a deterministic velocity field. Thus, it provides only a single future trajectory for a given fixed initial state and observation history. To overcome this limitation, we introduce Variational Streaming Flow (VSF). Our approach learns a latent distribution that is conditioned on the dynamics of interest. In turn, this enables probabilistic forecasting. Importantly, we retain the computational efficiency of SF by generating in physical time. Across deterministic and stochastic dynamical systems, VSF demonstrates superior predictive accuracy and distributional fidelity. We demonstrate the advantage for both long-horizon rollouts exceeding 1,000 steps, and settings with bifurcating dynamics. Moreover, VSF can be integrated into existing Joint-Embedding Predictive Architecture (JEPA)-based world models as a plug-and-play predictor to improve temporal dynamics and goal-directed success rate in navigation, motion planning, and manipulation.

## 305. Vault: One-Step Latent Generation with Positive-Anchored Rewards for Autonomous Driving

**Keywords:** End-to-End Autonomous Driving, Trajectory Planning, One-Step Generation, Drift-Based Generative Models

[Main paper PDF](https://openreview.net/pdf?id=zLcSTj1dLl)

End-to-end autonomous driving must balance multi-modal maneuver generation against real-time inference constraints. Diffusion planners capture diverse behaviors but their iterative denoising is too slow for safety-critical deployment, while one-step alternatives still imitate only the single expert demonstration, leaving neither diversity nor quality certified. To address this, we propose Vault, a framework that couples one-step latent generation with sample-based reinforcement learning guidance. Vault generates candidates in a single forward pass by drifting in a VAE latent space, built on a V-JEPA 2.1 visual representation pretrained on the full NAVSIM training imagery. During training, a reward-gated positive pool collects the full-score trajectories that the model itself discovers under the official evaluation and anchors the drift targets to these certified samples. This closes a reinforcement-learning loop purely through sample-based target construction, without policy gradients, learned reward models, or extra interaction: the generator imitates the frontier of its own certified successes, so quality and multi-modality improve together under a single fixed sampling configuration. A learned scorer predicting the official score and its sub-metrics selects the executed trajectory, and all training-only modules are discarded at inference. On the NAVSIM benchmarks, Vault achieves state-of-the-art closed-loop performance in real time.

## 306. VE-JEPA: Joint Latent and Value Learning for Offline Reinforcement Learning

**Keywords:** offline reinforcement learning, representation learning, joint-embedding predictive architectures, value learning

[Main paper PDF](https://openreview.net/pdf?id=IFgmYbPTMh)

Predictive representations are typically assessed by how accurately they predict.
We examine whether predictive accuracy is informative about downstream control
in offline reinforcement learning. We introduce VE-JEPA, a planning-free
joint-embedding predictive architecture in which a single encoder is trained
through latent prediction, reward prediction, and expectile value learning,
with an advantage-weighted policy operating directly on encoded observations.
Across three medium-replay locomotion tasks and five seeds per condition,
allowing Q and V losses to update the encoder substantially improves control over prediction-only and prediction-plus-reward encoder training.
Ablations show that latent prediction improves reward prediction from frozen
encoder features, while its incremental control
benefit varies across tasks and seeds.
Encoder learning rate also affects control performance. Reducing the encoder learning rate tenfold raises mean
AntMaze medium-play success from 5.0\% to 36.0\%, averaged across seven training
seeds. Measurements on fixed observations show reduced representation movement despite
larger encoder-gradient norms and higher predictive loss. Extensions across
locomotion datasets reveal a training-budget tradeoff: slower encoder updates
can delay performance improvements at a fixed budget. Across nine D4RL
locomotion datasets with ten seeds per method and dataset, VE-JEPA achieves an aggregate interquartile mean normalized return of 74.7 against Decision
ConvFormer's 71.5 at 200,000 training steps under fixed-target evaluation,
a difference of $+3.2$ with a 95\% bootstrap confidence interval of
$[+0.4, +5.9]$. This comparison varies across data regimes: VE-JEPA leads by
13.8 points on medium-replay and trails by 8.8 on medium-expert; the overall
ordering is sensitive to target-return selection. These results highlight
the importance of value-informed encoder training and task-dependent encoder
adaptation when learning predictive representations for offline control.

## 307. Vector-Symbolic Object Representations for Causal World Models

**Keywords:** object centric learning, trajectory inference, vector symbolic algebra, spatial semantic pointer, graph neural network

[Main paper PDF](https://openreview.net/pdf?id=5QVbiFreLk)

World models forecast latent states by learning an internal representation of an environment's dynamics. Object-centric variants factor that state into per-object slots, but a slot is an opaque learned vector that requires a trained probe to read, and only supports some edits. We replace the learned slot with a vector-symbolic expression that pairs an object's identity with an encoding of its position, and predict with a graph network over these newly defined slots. Reading a slot, editing a scene and forming the relative position of two objects all become fixed algebraic operations with no trained parameters, and the interaction between any two objects can be toggled inside the predictor. We compare this model with current state-of-the-art, including a coordinate GNN (ref) and C-JEPA on NRI spring-coupled particles and CLEVRER. Beyond single step accuracy, we evaluate the models on closed-loop rollout, recovery of the true coupling graph, and the consequence of removing an object in a setting where ground truth is available. Our model provides superior performance, scoring $0.49\times$ on rollout compared to ballistic constant velocity prediction versus $0.68\times$ (coord-GNN) and $0.58\times$ (C-JEPA), and recovers the coupling graph at $0.919{\scriptstyle\pm.005}$ ROC-AUC against $0.866{\scriptstyle\pm.003}$ (coord-GNN) and $0.810{\scriptstyle\pm.005}$ (C-JEPA).

## 308. VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models

**Keywords:** VLA, test-time scaling, JEPA

[Main paper PDF](https://openreview.net/pdf?id=WPm5HXaU34)

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversibly disrupt task progress and lead to failure. To exploit policy stochasticity, we introduce a training-free two-axis trigger that uses two initial samples to measure within-chunk temporal variation and cross-sample variance, detecting the critical states. Once triggered, a JEPA-based latent world model ranks candidate action chunks by predicting action-conditioned future latent states and the corresponding changes in task progress. By operating in latent space, the verifier avoids pixel reconstruction and enables efficient and more accurate ranking. Across three real-world tasks ($\textit{i.e.,}$ pen insertion, pipetting, and apple placement), our method raises the average completion score from 50.8% to 65.5%, while adding only 326 ms per triggered decision on a single RTX 4090. Consistent gains are also observed in simulation, where the average success rate rises from 66.4% to 73.6% in the clean setting of RoboTwin 2.0, from 62.8% to 69.6% in its randomized setting.

## 309. VidaForge: Open Research Infrastructure for Video Pretraining Data Recipes

**Keywords:** video foundation models, video data curation, video data recipes, research infrastructure, data attribution

[Main paper PDF](https://openreview.net/pdf?id=i5PeOLNXgs)

Video foundation models increasingly rely on large-scale pretraining data, yet the end-to-end data pipelines behind them remain largely closed and difficult to inspect or reuse. Researchers seeking to understand how video data recipes affect model pretraining often need to build substantial infrastructure before testing even a focused hypothesis. We present VidaForge, an open research infrastructure that represents a video data recipe as an executable five-stage workflow from raw videos to training datasets. A decision in this workflow can be varied to construct alternative datasets while preserving how every sample was produced. To demonstrate this research workflow, we compare data recipes with different coverage and quality in early from-scratch pretraining of Wan 2.1 and V-JEPA 2.1. Across both learning objectives, the broader-coverage recipe achieves the highest downstream benchmark scores, while loss-based evaluation favors different recipes. This study demonstrates how VidaForge connects data-recipe choices to downstream model performance. We further release VidaForge- 3M, containing 3.14 million scene-level clips totaling 6,475 hours, with fine-grained annotations and curation signals for video data-recipe research.

## 310. Video Foundation Models Bind Objects but Do Not Maintain Them Under Occlusion

**Keywords:** video foundation models, object permanence, object binding, occlusion, counterfactual probing, interpretability, object-centric learning, world models

[Main paper PDF](https://openreview.net/pdf?id=2KvSYrWwH6)

Video foundation models are widely assumed to acquire object-centric structure, yet whether that structure is causally used, and whether it survives the moment an object stops being visible, has not been tested. Decoding is blind to both: linear readouts recover object identity from frozen features, yet a probe trained to report the hidden object retrieves the occluder instead. We measure object binding inside the model's own prediction machinery: delete object A's early tokens from a frozen predictor's context, then read the per-object degradation of its future predictions. A leakage ratio L summarizes this against endpoints measured in the same pipeline, at K+1 forward passes per clip with no fitted parameters. In a predictive video foundation model (V-JEPA2) and a diffusion one (CogVideoX), objects are strongly bound, and in V-JEPA2 the binding is learned: L = 0.23–0.43 against untrained 1.00 and label-shuffled 1.16, surviving distance- and appearance-matched controls and generalizing to real video. The same models have no object permanence. Under occlusion the fill contrast POperm, hidden object minus occluder, is never significantly positive on our pilot scenes in five video foundation models spanning three training paradigms; where it turns positive at scale (V-JEPA2-H) it is as positive when the object never existed, and V-JEPA2's significant deficits survive subtracting the readout's own measured floor. An object-centric model with per-object recurrent state reaches +0.264; on the 62 clips both cover, the paired gap is +0.292 with the object-centric model higher on 95% of them. The obvious fix works and does not do what it appears to: two epochs of occlusion-completion fine-tuning turn permanence positive (−0.024 → +0.070 over three seeds), and eight lift occluded-object identification from 0.369 to 0.522, yet a paired counterfactual in which the object never existed reproduces 96–108% of the fill gain, identifying the fix as a largely history-blind de-occlusion prior. On this class of feedforward predictors, internal binding does not imply object permanence, and the cheap fix does not install it.

## 311. Visual-to-M/EEG Brain Encoding with Time-Frequency Dual-Path Finite Scalar Quantization

**Keywords:** Brain encoding, visual prostheses, MEG, EEG, modality alignment, frequency domain

[Main paper PDF](https://openreview.net/pdf?id=1tZgbtYkP3)

Visual brain encoding predicts neural responses from visual stimuli, advancing our understanding of visual perception. It is also an indispensable step in visual prostheses, where predicted neural responses guide electrode stimulation patterns. Prior visual brain encoding research has primarily focused on fMRI, whose limited temporal resolution restricts its applicability. While recent work has shifted toward M/EEG-based brain encoding with diffusion models, these approaches treat M/EEG as images---neglecting their frequency-domain structure---and do not explicitly leverage real neural responses in the training objective. We propose a three-stage visual brain encoding framework. In Stage 1, we propose a novel VAE, called BrainVAE, with a time-frequency dual-path encoder: the input M/EEG signal is treated as a 2D image (channels $\times$ time) and processed by a Conv2d backbone to extract local spatial-temporal features, while simultaneously transformed by FFT to obtain power spectra. The Conv2d feature tokens and Frequency Prefix Tokens are fused by a Transformer via self-attention, incorporating explicit frequency-domain priors. Finite Scalar Quantization (FSQ) discretizes the latent space without codebook collapse or auxiliary losses. In Stage 2, InfoNCE contrastive learning aligns the quantized neural latent space with I-JEPA image embeddings. In Stage 3, a Transformer-based BrainTokenRegressor predicts FSQ token sequences from I-JEPA image embeddings via cross-attention, with losses computed directly against real neural responses in both token and signal spaces. Experiments on THINGS-EEG2 and THINGS-MEG demonstrate the effectiveness of our approach.

## 312. VLA-ULAP: Interleaving Cloud VLA Calls with Ultra-Lightweight Local Action Prediction at the Edge

**Keywords:** vision-language-action models, robot learning, cloud-edge inference, edge AI, efficient inference

[Main paper PDF](https://openreview.net/pdf?id=zFXMdbr5BX)

Billion-parameter vision–language–action (VLA) policies run either onboard, consuming substantial power, or on remote servers, adding communication latency. To address these drawbacks and better balance latency and onboard energy consumption, we propose VLA-ULAP. It partitions inference across decision times, interleaving remote VLA calls with predictions from an Ultra-Lightweight Local Action Predictor (ULAP). A single ULAP has $\sim$7.4M parameters including the frozen vision encoder. It combines current views, proprioception, and executed action history to predict chunks in one pass. Trained independently, it requires no VLA hidden states, online verification, or server round trips. On Jetson Orin Nano, ULAP takes 20.7 ms and 0.122 J of idle-subtracted energy per inference, versus 289.3 ms and 40.46 J for GR00T on RTX A6000. Across four simulated base-policy/benchmark pairs, VLA-ULAP removes 45.3–77.3% of VLA calls while retaining 95.0–98.5% of baseline success rates at selected operating points. On VLA-JEPA, VLA-ULAP also surpasses local acceleration alternatives, using an estimated 49.4% less inference time and 51.5% less GPU energy per successful episode than ACT, and 77.5% less time and 80.7% less energy than SP-VLA at higher success rates. In physical SO-101 trials, it similarly removes 70.3–71.9% of VLA calls without observed success-rate loss at seen or held-out placements. Measured device costs imply 64.6–66.4% less inference time and 70.1–71.7% less idle-subtracted energy per successful episode at these call counts. Beyond these savings, faster responses help VLA-ULAP exceed $\pi_{0.5}$'s success rate by 11.0 and 15.5 percentage points (pp) on two tasks in latency-aware LIBERO-Safety simulation while approximately halving VLA calls.

## 313. vNeuro: Foundation for EEG Vision Models

**Keywords:** EEG representation learning, visual structural priors, time-frequency modeling

[Main paper PDF](https://openreview.net/pdf?id=6QNkVpV1Ux)

EEG foundation models are typically pretrained from scratch on large corpora of neural recordings. Yet experienced clinical neurophysiologists interpret EEG largely by visual inspection, recognizing spikes, rhythmic bursts, and time–frequency patterns by eye. This raises the question of whether representations learned from natural visual data can be reused for EEG. We introduce vNeuro, a framework that adapts a frozen, video-pretrained V-JEPA 2.1 encoder to EEG through a lightweight trainable interface. vNeuro converts multichannel time–frequency representations into visual tokens that preserve electrode geometry, and trains this interface on unlabeled EEG through latent forecasting with distribution regularization, while the visual backbone remains fixed. During downstream training, only the adapter and classification head are optimized. With a ViT-B backbone, vNeuro achieves balanced accuracies of 81.40% on TUAB abnormality detection and 68.35% on TUEV event classification (68.73% with ViT-G), competitive with EEG foundation models pretrained on tens of thousands of hours of EEG. Ablation and representation analyses show that both the EEG-to-visual token mapping and the regularized self-supervised adaptation contribute to performance. These results suggest that pretrained visual encoders can serve as effective EEG backbones without pretraining a large EEG-specific model.

## 314. VR-JEPA: Learning Contrastive-State Latent Guidance for Generation-based Video Reasoning

**Keywords:** Visual Reasoning, Joint-Embedding Predictive Architecture, Video Generation

[Main paper PDF](https://openreview.net/pdf?id=z0CuDjRD49)

Reasoning through video generation offers a promising path toward visual intelligence by modeling latent visual states and their dynamics. However, current video generation models often lack explicit guidance on how these states should evolve, leaving generated trajectories prone to physical and structural inconsistencies that undermine reasoning reliability. While the Video Joint-Embedding Predictive Architecture (V-JEPA) provides rich spatiotemporal priors learned through latent prediction, these general priors do not naturally adapt to the logical reasoning capabilities required for complex visual tasks. To bridge this gap, we propose VR-JEPA, a framework that aligns the V-JEPA predictor with task-specific reasoning logic through localized contrastive-state learning and uses its predicted latent trajectories to guide video generation for visual reasoning. Specifically, (i) we pair successful trajectories with generated alternatives under the same input conditions and use discrepancies in their V-JEPA representations to identify informative states and tokens for localized contrastive supervision. (ii) We further equip the V-JEPA predictor with skill-specific experts trained on anchor-task data, allowing the model to adaptively specialize its shared spatiotemporal priors across diverse cognitive domains.
Together with skill-specific experts, this contrastive supervision enables VR-JEPA to predict latent trajectories that provide task-specific logical guidance for video generation. Comprehensive experiments on the large-scale VBVR-Pro-Bench dataset demonstrate that VR-JEPA achieves an $11.33\%$ relative improvement over cutting-edge generation-based reasoning baselines, significantly mitigating physical artifacts and enhancing logical consistency. Our code and data will be released upon acceptance.

## 315. W-JEPA: Wavelet Joint-Embedding Predictive Architecture for Wearable Activity Recognition

**Keywords:** Human activity recognition (HAR), Self-supervised learning, Wearable sensing, Wavelets, Joint-embedding predictive architecture (JEPA), Time-series

[Main paper PDF](https://openreview.net/pdf?id=Z4AEwtKhHZ)

A major challenge in wearable device activity recognition is the heterogeneity across datasets in sensor placement, channel count, sampling rate and subjects. Moreover, the motion patterns that distinguish activities often appear as subtle, scale-specific variations within otherwise similar waveforms. As a result, raw signals are often ambiguous, and models trained on them tend to rely on cues specific to a particular sensor setup or participant, which limits both cross-dataset transfer and generalization to unseen participants. Addressing this requires representations that preserve such activity-relevant, scale-specific variation. We introduce W-JEPA, a self-supervised framework that exploits the multiscale structure of inertial motion and leverages a joint-embedding predictive architecture, by organizing windows into a fixed grid of wavelet tokens indexed by scale, sensor axis, and time. These wavelet tokens help expose activity-specific detail within broadly similar raw signals, and serve as the units of masked latent prediction. W-JEPA predicts masked token representations supplied by an exponential-moving-average (EMA) target encoder. Because recovering a masked token requires relating motion at one scale and axis to motion at other scales and axes, the model learns the cross-scale, cross-axis structure of human movement. Across six wearable activity benchmarks, W-JEPA outperforms state-of-the-art methods under random-window splits and remains the strongest when subjects are held out, improving average macro-F1 by 8.7 percentage points over the strongest published baseline. These results indicate that physically grounded multiscale tokenization, combined together with latent predictive learning, provides a promising foundation for transferable representations of heterogeneous wearable inertial data.

## 316. Weak Supervision Helps JEPA

**Keywords:** unsupervised, JEPA

[Main paper PDF](https://openreview.net/pdf?id=2QXboxxeb1)

When a hand picks up a cup, understanding the action requires distinguishing the hand from the cup while capturing their interaction. Yet global video self-supervision leaves these object-level distinctions implicit. We show that weak object supervision during pretraining improves the quality and data efficiency of LeVJEPA representations. We use object masks generated offline by pretrained SAM2 to supervise an auxiliary instance-separation objective, bringing together patch features belonging to the same object while separating them from other objects and the background. Furthermore, we show that instance separation alone is the best-performing auxiliary objective, outperforming variants incorporating object-level SIGReg regularization and additional object-level alignment. The encoder architecture and retained-token budget remain unchanged. SAM2 is used only for preprocessing, and the auxiliary head is removed after pretraining, leaving no additional inference cost. Across matched experiments with ViT-Tiny, ViT-Small, and ViT-Large pretrained on 50K to 1M videos, our method improves over standard LeVJEPA at every evaluated scale. Identical attentive probes on frozen encoders achieve higher early-epoch and final accuracy. At 50K videos, Top-1 accuracy improves by approximately 9.4 percentage points on both Something-Something-v2 and Kinetics-400. The SSv2 advantage persists as pretraining data increases, reaching 6.7 points at 200K videos and 4.7 points at 1M. These gains also translate into improved data efficiency. On nested datasets, our model pretrained on 50K videos outperforms standard LeVJEPA pretrained on 95K by 6.1 SSv2 Top-1 points. In a complementary cross-scale comparison, our ViT-Small reaches 51.9% SSv2 accuracy on an SSv2-enriched 200K-video corpus, within 4.3 points of the ViT-Large baseline pretrained on 1M videos. Together, these findings identify local instance separation as an effective complement to global video self-supervision: a single auxiliary objective provides useful object structure during pretraining and enables stronger representations from limited data.

## 317. What masking geometry works best for EEG foundation models?

**Keywords:** EEG, Foundation models, SSL, JEPA, MAE, Masking

[Main paper PDF](https://openreview.net/pdf?id=PGsmWBEYnL)

EEG foundation models hold promise for scalable brain-signal decoding across clinical and cognitive neuroscience applications, yet their pre-training pipelines remain poorly understood. Among design choices, the masking strategy is particularly critical: it determines what the network must predict and from which context. Yet it has never been ablated in isolation, as each new model bundles a new masking strategy with a new backbone and objective. In this paper, we formalize the design choices for spatio-temporal masking strategies and train various models with a single pipeline under varying masking configurations across two SSL frameworks (MAE and JEPA). We then systematically evaluate the resulting 58 pre-trained models on the 12 datasets of OpenEEGBench under a linear probe. Both frameworks agree on an optimal masking configuration and on shared failure modes. Outside these, performance is robust: 11 MAE and 9 JEPA configurations are statistically indistinguishable from the best. We further identify a novel JEPA-specific failure mode, tagged bias-inflation collapse, invisible to standard detectors. With a well-chosen mask, we reach REVE-level downstream performance at a fraction of its pre-training compute.

## 318. What Should Robot Policies Learn to Predict? Rethinking Supervision Targets in Vision-Language-Action Learning

**Keywords:** vision-language-action models, robot learning, auxiliary supervision, latent actions, future prediction, supervision allocation, imitation learning

[Main paper PDF](https://openreview.net/pdf?id=Z3OpVnnFqT)

Vision-language-action (VLA) policies are typically trained with action
prediction as the primary supervision signal, since robots ultimately execute
actions. Auxiliary objectives such as latent-action (LA) and future-vision (FV)
prediction are often added to improve policy learning, yet they compete with
action prediction for the same training budget. We ask whether, under a fixed
budget, allocating a substantial share of training samples to such objectives,
rather than to further action prediction, can improve policy learning. We build
a unified VLA framework that couples a two-stream multimodal diffusion
transformer (MMDiT) with a sample-level router, which assigns each training
sample to either action prediction or an auxiliary objective and thus makes
supervision allocation explicit. Within this framework, we instantiate three LA
targets based on LAPA and its DINO-feature variants, and three FV targets based
on DINOv3, V-JEPA~2, and Wan2.2 representations. Across LIBERO, CALVIN, and
four real-robot tasks, suitable LA and FV supervision outperforms action-only
training under the same budget, even when action prediction receives no more
than half of the training samples. FV generally outperforms LA, although the
strongest LA target remains competitive on CALVIN. Diagnostic analyses suggest
that DINO-based LA targets emphasize relative motion, whereas FV targets
emphasize absolute position and task identity. We therefore argue that what
robot policies learn to predict, and how training is allocated among these
targets, should be treated as explicit design choices rather than defaulting
to action-dominant training.

## 319. What Video Anomaly Probes Measure

**Keywords:** video anomaly detection, linear probing, evaluation methodology, confounds, video world models, V-JEPA 2, benchmark audit, self-supervised video representations, negative results

[Main paper PDF](https://openreview.net/pdf?id=nPjqMZBc1F)

An above-chance probe score on frozen video features is often read as evidence that the representation captures anomaly. We argue that this reading needs an evaluation contract, and we audit the supervised probe with four low-dimensional controls—scene complexity, video identity, position in video, and detected-agent counts—under scene-grouped folds, paired rows and video-clustered uncertainty, on a frozen V-JEPA 2 encoder over UCF-Crime and NWPU-Campus. On UCF-Crime, a linear probe given only the first encoder window of each clip predicts whether the clip will contain an anomaly at video-level AUROC 0.899; this is a video-level diagnostic, not evidence of temporal anticipation. On NWPU-Campus, a nine-dimensional count vector is a strong comparator under the diagnostic: with each arm's better of two heads, no tested representation arm is superior after paired Holm correction, and the count arm is the highest selected arm in every one of 25 stored seeds. That ordering is conditional on the readout: under a fixed linear head the count arm sits at chance and no arm is distinguishable from it, so we report paired tests within each head family rather than a single ranking. The seed sweep jointly varies fold assignment and optimisation and moves arms by up to 0.186 AUROC, widest for the complexity control. Under the benchmark's own normal-only protocol the same counts reach at most 60.6 micro-AUC against a published 76.9, whereas the frozen state reaches 59.1 micro-AUC and an exploratory 67.2 macro-AUC in the prespecified estimator cell: a control can dominate a supervised diagnostic without being a competitive detector. Two analytical results—that a prediction-error residual is a dispersion functional, and that a self-normalised pre-hoc hazard measures the model's own tail mass—motivate the complexity control and explain why no unsupervised anticipation arm appears. We release the protocol and every artefact, and limit the conclusion to measurement design: an anomaly score should state its target, information cutoff, controls, grouping, readout selection, aggregation and uncertainty before it is read as evidence about a representation.

## 320. When Anti-Collapse Objectives Have Collapsed Optima

**Keywords:** JEPA, representational collapse, self-supervised learning, regularization, distribution matching, reproducibility

[Main paper PDF](https://openreview.net/pdf?id=ndfEYtpRRb)

Every JEPA carries collapse-prevention machinery, and a recent line of work replaces the older heuristics with a single distribution-matching objective on the latent (LeJEPA; Rectified LpJEPA). We ask when such an objective is safe. An objective that reads the latent only through per-feature scalar statistics has a collapsed global optimum when its entrywise function is convex and non-increasing (softplus, hinge); for $\ell_1$ the minimisers are single-entry, rank-one latents. A softplus non-negativity penalty — the form a rectified target takes when written as a penalty — placed at the encoder of tabular T-JEPA degrades $28/28$ runs under its standard linear probe, $24$ to the majority-class share, locked within five epochs. The collapse is geometric rather than informational: the re-examined latents sit on one common vector with a residual of $\sim 2\times 10^{-7}$ of its scale that still carries the label — a standardised probe recovers most of it, yet stored in bf16 or fp16 every input rounds to the same vector. Under a fair probe the placement effect survives but shrinks: $16$pp for this penalty (from $26$pp), $4$--$5$pp for everyday $\ell_1$ and hinge penalties (from $22$pp), and no encoder-side deficit for the published Rectified-LpJEPA loss. A variance-floor repair restores information but not scale, and along the collapsed direction its restoring gradient vanishes with the residual while the published sliced-Wasserstein loss keeps it. A one-forward-pass check that scores objectives at a collapsed and a healthy latent flags every penalty that collapses deterministically, but it is a warning sign, not a certificate: in pre-registered runs the reference LeJEPA objective, which it scores as safe, collapses T-JEPA to the majority share when placed at the predictor ($6/9$).

## 321. When Can a World Model Decide? Certifying Elite Decisions in Sampling-Based Planning

**Keywords:** world models, model-based planning, cross-entropy method, MPPI, ensembles, JEPA

[Main paper PDF](https://openreview.net/pdf?id=cVCKr4bBU2)

Sampling-based planners such as CEM and MPPI turn a latent world model into a controller by trusting its ranking of candidate action sequences at every iteration. We show when that trust is warranted. A rollout error bound yields a decision certificate: the model places a candidate correctly in or out of the elite set whenever the candidate lies more than twice the error from the elite boundary. Executing every candidate a planner evaluates on Push-T, we find that the certified fraction falls from 0.67 to 0.29 over the search: the planner converges until its candidates differ by less than the model can resolve, and more search cannot recover the lost resolution. The certificate also names the remedy, a more accurate predictor or models with independent errors, and only the decisions at the elite boundary need it. We introduce EliteCert, in which the planning model screens every candidate and independently trained validator models re-score only a calibrated band around the K-th elite. EliteCert enters through the cost function, so CEM, iCEM and MPPI run unmodified. Under the official LeWM protocol it raises success by 9–14 points for all three planners on Push-T and by 2–3 points on Cube, beats the default configuration at 44% of its CPU time, matches re-scoring every candidate at a third of the extra compute, and adds a further 1.8 points to a planner whose predictor we retrained. An offline qualification test tells in advance which models can serve as validators. Finally, we prove and measure that gains on logged candidate pools do not transfer to the closed loop of an iterated planner, and evaluate every claim in the closed loop, with 1800 paired runs behind each headline comparison.

## 322. When Foresight Drifts: Progress Aligned Resynchronization for Cloud–Edge Robotic Control

**Keywords:** cloud-edge;WAM；Robotic

[Main paper PDF](https://openreview.net/pdf?id=45JW00zyUe)

Deploying billion-parameter vision-language-action (VLA) policies on mobile robots creates a systems tension: semantic reasoning benefits from cloud GPUs, whereas closed-loop control requires responsive local execution.
We identify two sources of foresight drift in cloud--edge robotic control.
First, uniform temporal prediction allocates representational capacity by elapsed duration rather than semantic significance, creating a pace--progress mismatch that underrepresents critical procedural transitions.
Second, physical changes can invalidate predicted continuations even when the semantic stage remains relevant, creating a state-foresight mismatch.
We propose Foresight Resync (ForRes), which integrates semantic-target-conditioned cloud prediction, progress-based edge cache addressing, and value-guided asynchronous refresh.
In the cloud, a JEPA-based predictor forecasts the next semantic milestone from causal execution history, and a lightweight adapter conditions the world action model on this target while preserving its native prediction budget.
On the edge, recurrent addressing matches observed execution to cached semantic anchors, retrieving latent guidance according to procedural progress rather than elapsed time.
Target-support gating suppresses incompatible guidance, while an alignment-conditioned critic requests refresh when its expected benefit exceeds querying costs; invalid or exhausted caches trigger refresh directly.
Edge policy maintains observation-only closed-loop control while awaiting cloud responses.
Evaluated with two cloud backbones and an X-VLA edge policy, ForRes achieves up to 78.73\% average success on RoboTwin 2.0, improving over Latent-to-Action by 4.20 percentage points with 31.11\% fewer cloud calls, and reaches 76.00\% success on real-world dual-arm tasks.

## 323. When Linear Probes Go Blind: The Order Spectrum of Learned Representations

**Keywords:** mechanistic interpretability, representation analysis, linear probing, nonlinear probing, polynomial probes, Hermite decomposition

[Main paper PDF](https://openreview.net/pdf?id=vY15YMeOuP)

Linear probes are widely used to assess properties encoded in neural network representations. However, poor linear recovery cannot distinguish absent information from information accessible through nonlinear readouts, while commonly used MLP heads do not characterize how information is distributed across orders. We formalize this distinction by introducing the order spectrum, a Hermite decomposition of the target regression function that, under Gaussian representations, resolves predictable variance by polynomial degree. Specifically, we show that optimal affine probes measure the first-degree energy of the spectrum, while increments between optimal nested polynomial probes recover successive energies. For the off-Gaussian case, we bound the discrepancy in terms of the Hermite-feature Gram deviation and a target-dependent approximation residual, and validate the bound in controlled settings. Leveraging this framework, we show that quadratic probes recover substantial board-color information in OthelloGPT and pendulum energy in a JEPA trained without energy labels, where linear probes fail. Further, by analyzing grokking in modular addition, we find that partial linear recovery can coexist with substantial quadratic accessibility, while quantitative Hermite-energy interpretations require explicit distributional and approximation conditions. More broadly, the framework provides a degree-resolved account of how target information becomes accessible in learned representations.

## 324. When the Change Carries No Energy: A Detectable Regime Change That No Learned Monitor Detects

**Keywords:** World Model, JEPA, Flow Matching, Out of Distribution, Deep Learning Theory

[Main paper PDF](https://openreview.net/pdf?id=kO6Aw9UMba)

Latent world models need reliable regime detection, yet existing monitors track only residual energy-shifts in the mean or variance of prediction error. When an environment switches between noise laws of identical variance, every prediction error keeps its size and only its shape changes, so an energy-based monitor, sensitive only to the second moment, is provably blind to the shift, a claim we verify-along with our other guarantees-in a machine-checked proof. We introduce a generative world model that pairs a joint-embedding predictive architecture with a conditional flow-matching predictor over future latent trajectories (F-JEPA-RD), which scores the full predictive density rather than its energy. An analytic Gaussian base coupled with a learned residual yields exact trajectory density ratios while preserving the representation structure the joint-embedding design protects. An audit of sequential detection benchmarks reveals a pervasive validity failure: standard protocols mistake a detection statistic's natural drift during calm periods for genuine detection, creating an illusion of success across existing methods. Under a drift-robust protocol with null controls, an oracle given the true noise law detects variance-matched shifts almost perfectly, while every learned monitor we test-including our own model's readouts-collapses to chance, on both synthetic benchmarks and a four-year real-world recording. A diagnostic locates the loss: the encoder preserves and even sharpens the shape signature, which is then diluted by the multi-lag residual the readouts consume. Applying the same shape core to a single-step innovation residual instead recovers part of the lost power in a single-seed pilot, indicating the information is still present in the representation. When regime changes instead alter the underlying dynamics, F-JEPA-RD's density ratio retains strong power while staying silent under null controls, exactly as the theory requires. We release the benchmark, proofs, and scoring code for independent re-scoring.

## 325. Where Does A Predictive GUI Verifier Lose To A Discriminative One? A Controlled Diagnosis

**Keywords:** GUI agents, step-level verification, world models, JEPA, predict-then-compare, discriminative verifier, early fusion, benchmark label audit

[Main paper PDF](https://openreview.net/pdf?id=bWYb8yjkDr)

Step-level verification asks whether an observed GUI screen is compatible with the action claimed to have produced it, the goal-free check that retry and recovery rely on. A predictive verifier forecasts the successor with a latent world model and compares the forecast with the screen; a discriminative verifier reads the action and both screens jointly. We compare the two at matched data, negatives, backbone and training budget on a pre-registered benchmark of recorded transitions. The predictive verifier is worse by 6.53 AUC points, by 6.30 on a test set built and scored once after every model was frozen, and by a wider margin at low false-positive rates. The gap is not a labelling artefact: two independent annotators find a minority of constructed negatives still compatible, and on the negatives both confirm the gap is essentially unchanged. A ladder of controlled variants between the two verifiers locates it. The four losses that align the forecast with the observed screen move aggregate AUC by only 0.19 points. Comparing the screens after encoding them apart costs 4.93; in-distribution, neither keeping every patch nor matching the comparison head recovers more than a point of it, which leaves fusion timing. Gains that narrow the gap do not survive a change of distribution, and both verifiers refuse genuine interface anomalies more often than ordinary transitions.

## 326. Where Structure Enters a World Model: From Predictive Fit to Physical Rollout

**Keywords:** World Models, Inductive Bias, V-JEPA, Equivariance, Temporal Difference Learning, Hamiltonian Neural Networks, Lagrangian Neural Networks, Planetary Dynamics, Physics Informed ML, Autonomous Rollout, Self Supervised Learning, Predictive World Models

[Main paper PDF](https://openreview.net/pdf?id=1CCWi91Myr)

Predictive world models learn to forecast observations, but accurate short-term predictions do not necessarily produce physically coherent behavior over longer horizons. We investigate how incorporating physical structure can strengthen world models while retaining their underlying predictive objectives. Across token-based models of planetary motion and JEPA-style visual models of mechanical systems, we study conserved-quantity supervision, symmetry-aware representations, temporal consistency, and learned structured dynamics. In planetary motion, angular-momentum supervision improves autonomous next-token forecasting, while the benefits of temporal regularization depend on the accompanying physical objective and representation. In visual models, generating rollouts through supervised energy-based dynamics heads produces more faithful trajectories and phase-space evolution. Together, these findings highlight the importance of how physical structure participates in prediction: improvements in an auxiliary physical readout or a local acceleration estimate do not automatically translate into more reliable long-horizon behavior. Evaluations across initial conditions and physical parameter shifts further reveal where these benefits persist and where generalization remains limited. Our study supports physical structure as a practical means of improving predictive world models and provides a unified framework for understanding its effects on representations, learned transitions, and autonomous rollouts. The central lesson is that effective physical inductive biases should help models both represent physical regularities and use them to generate future states.

## 327. World Modeling Through Spectral Alignment

**Keywords:** World models, JEPA, spectral manifold learning, robotics, planning

[Main paper PDF](https://openreview.net/pdf?id=OYNwdjRvQZ)

What information should a latent world model preserve? We study this question through the lens of spectral representation learning. We introduce SpecWM, a JEPA framework that explicitly specifies desired relationships between observations through a teacher similarity kernel and trains the encoder to reproduce those relationships in its embedding geometry. Different kernels provide different supervision, ranging from physical state information to a fully self-supervised temporal kernel requiring only the ordering of observations within trajectories. We characterize the global optima of the objective, establish conditions for linear recoverability and invariance to nuisance information, and connect temporal-kernel similarity to the behavioral successor measure under an idealized setting. Empirically, the choice of kernel strongly controls which physical quantities are recoverable from the representation. More importantly, temporal spectral alignment improves CEM planning success over LeWorldModel from 52% to 68% on OGBench Cube, 49% to 77% on OGBench Scene, and 29% to 51% on CALVIN. These results suggest that explicitly specifying representation geometry provides a simple way to steer what latent world models preserve for control.

## 328. World Models with Configurable Perception

**Keywords:** World Models, Configurable Perception, Noisy Worlds, JEPA

[Main paper PDF](https://openreview.net/pdf?id=wutrzqxrsC)

Real-world observations are noisy and often contain excessive task-irrelevant information. Effective world modeling and planning need to abstract observations into world state representations while filtering out irrelevant information. 
However, encoders in existing world models are typically non-adaptive, leading to state representations that are easily distracted  by task-irrelevant information. As a result, the model may not selectively filter observations to cater to different task demands.
To address this problem, we introduce ConfigWM, which realizes configurable perception through task-conditioned state extraction. Given a language description of the task at hand, ConfigWM uses it as a configuration signal to steer how visual embeddings are mapped into a task-specific state space, selectively preserving information relevant to the current task while suppressing task-irrelevant variations. Action-conditioned dynamics are then learned in this task-specific state space for planning.
We evaluate ConfigWM in environments with increasing levels of distraction. While existing methods exhibit substantial declines in planning success rate as the environments become increasingly noisy, ConfigWM remains comparatively stable and outperforms the strongest competing method by 22.3% on average across diverse environments.
Consistent gains in physical-quantity probing (+0.365 Pearson r) and distracted-to-clean retrieval (+75.5%) further indicate that ConfigWM learns states that preserve task-relevant information while remaining robust to distractors, supporting reliable world modeling and planning in noisy worlds.

## 329. World-as-Graph: Relational World Modeling Through Latent Space Graphs

**Keywords:** Dynamic graphs, World models, JEPA, Representation learning

[Main paper PDF](https://openreview.net/pdf?id=jyXOlNbLfq)

World models aim to learn representations of real-world environments and predict their future evolution. Recent object-centric world models have made expressive progress by representing visual scenes as sets of object-level latent states, but object-object relations are often captured only implicitly, which limits explicit relational and temporal structure modeling and object-centric dynamic memory modeling. To address such challenges, we propose World-As-Graph (WAG), a graph-based object-centric world model that introduces relational inductive bias into JEPA-style predictive representation learning. The proposed WAG contains two main modules: (1) Relation-aware structure induction, which constructs time-varying latent graphs from object-centric slots and designs relation-aware object masking policies to guide relational object representation learning in latent space; (2) Object-centric memory transition, which maintains and updates object-level dynamic states by combining relational information from neighboring objects with historical memory, enabling effective autoregressive future prediction. Extensive experiments on both visual reasoning and robotic manipulation tasks could demonstrate the superior performance of our proposed WAG.

## 330. world2vec: Stable inference of mechanistic world models

**Keywords:** world models, self-supervised learning, JEPA, dynamical systems, system identification

[Main paper PDF](https://openreview.net/pdf?id=qbry6md4vj)

World models learned from raw pixels have become a practical basis for planning and control, and recent joint-embedding predictive architectures can be trained stably end-to-end. Yet these models are typically evaluated in environments whose dynamics are largely driven by the agent’s actions, and stable training alone does not ensure that learned latent representations recover the underlying state or dynamics of the environment. Here, we introduce world2vec, a framework for learning mechanistic world models directly from observations. We show that world2vec recovers the ground-truth state under nonlinear observation mixing and learns latent dynamics that faithfully reproduce the true system over long prediction horizons while using one order of magnitude fewer parameters than existing world models. We show state of the art performance in controlling continuous control environments from pixels. world2vec treats the representation objective and dynamics model as hyperparameters, allowing their inductive biases to be automatically matched to the data-generating process. This enables recovery of ground-truth dynamical systems and their governing equations across simple physical environments and a dataset of 71 strange attractors and paves the way towards using world2vec for scientific discovery.

## 331. World4Scorer: Outcome-Grounded World Modeling for Autonomous Driving

**Keywords:** Autonomous Driving, World Model

[Main paper PDF](https://openreview.net/pdf?id=kx17FJ7sj6)

Autonomous driving requires choosing a safe and efficient plan as surrounding traffic evolves. Generate-and-select planners propose multiple trajectories
and score them for execution, and they have outperformed representative directprediction baselines on NAVSIM. Their scorer must compare plans that were
never executed. Driving logs record the future of only the executed trajectory,
so matching the logged future can leave predictions for the alternatives unconstrained; a simulator, in contrast, can label the outcome of every candidate. We
introduce World4Scorer, which builds the scorer as a trajectory-conditioned JEPAstyle predictor: it predicts a state for each candidate and reads the candidate’s
scores from that state. Simulator outcome labels supervise the states of all candidates, and the observed future of the executed trajectory anchors the predictor
to real scene evolution. Because one predictor produces every candidate’s state,
the anchor can constrain shared parameters used to score unexecuted plans, while
the future itself is needed only during training. Generated candidates mostly score
well, so a scene-matched bank adds low-scoring plans to the outcome supervision;
framewise choices can conflict, so inertial re-ranking keeps consecutive selections
consistent. World4Scorer achieves state-of-the-art NAVSIM-v2 performance and
a strong adapted-system result on closed-loop Bench2Drive. With the LeWM
world model and planning budget fixed, outcome-based scoring also improves
manipulation planning on the OGBench-Cube benchmark.

## 332. WorldModelLens: From Attention to Rollouts - A framework for World Model Interpretability

**Keywords:** World models, mechanistic interpretability, capability-typed interface, hook-and-cache tooling, activation patching, sparse autoencoders, probing, intervention replay, imagination rollouts, joint-embedding predictive architectures

[Main paper PDF](https://openreview.net/pdf?id=ovYQQy77Rd)

Interpreting world models requires action-, step-, and rollout-level abstractions that existing language-model hook-and-cache tools don't provide, forcing researchers to rebuild bespoke analysis code for every new architecture. We present WorldModelLens, an open-source toolkit that unifies recurrent state-space models (e.g., Dreamer), token-based models (e.g., IRIS), and joint-embedding architectures (e.g., I-JEPA) behind a single typed adapter API and a shared hook-and-cache layer, so researchers can write one analysis and run it across model families. Applying it to the I-JEPA ViT-H/14 checkpoint, we find that Integrated Gradients achieves a small but statistically robust localization signal in insertion-based patch restoration (-0.19 standardized effect, p < 10⁻⁴), a much weaker version of the effect found in pixel-reconstruction masked autoencoders (-1.15), suggesting I-JEPA's predictor relies more heavily on distributed context than a pixel-reconstruction objective does, though not to the point of being fully non-localizing. Our latent-attribution method recovers this same ranking while requiring ~180× fewer model evaluations than exhaustive patching, and correlates with costlier head and block-level interventions (r=0.70-0.93). By collapsing architecture-specific plumbing into a common adapter surface, WorldModelLens lets the same hooks trace a prediction from an individual attention head up through block-level dynamics to full rollout behavior, turning interpretability of world models from a per-architecture engineering problem into a matter of choosing where, on that continuum, to look.

## 333. WorldTraces: A Data Attribution Framework for Predictive World Models

**Keywords:** Training-data attribution, Predictive world models

[Main paper PDF](https://openreview.net/pdf?id=1dROUvGCyh)

Data attribution measures how much each training sample shapes what a model predicts. However, it has not been explored in predictive world models that learn representations from large-scale sequential data such as trajectories and rollouts. We remark that there is a disconnection between existing training-data attribution methods and distinct behaviors learned by a world model such as JEPA. Specifically, the majority of existing data attribution methods are built around a differentiable loss against a ground-truth label, whereas  JEPA's exponential moving average target and multi-step latent rollouts leave no single scalar output for a sample's influence to be traced back to. To fill this gap, we propose WorldTraces to measure training data's attribution in future-latent prediction, representation
consistency, and temporal latent structure. It combines these responses into a
query-conditioned ranking of training examples. While the architectures of existing world models varied differently from each other, we focus on JEPA because it has become a leading architecture for learning general-purpose world representations, making it a practically important test case for tracing which training data drives its learned dynamics and downstream behaviors. Experiments show that WorldTraces rankings predict the behavioral
effects of grouped checkpoint-level forgetting-directed interventions across several subset sizes and maintain a
consistent ordering across all three behaviors. WorldTraces aligns more closely with the effects observed under subset interventions and shows a sharper response when top-ranked examples are corrupted. It also avoids the need for subset retraining or stored training trajectories, with runtime scaling roughly linearly in the candidate pool size. Together, these results position WorldTraces as a practical foundation for training-data attribution of world models.

## 334. Would an Untrained Encoder Do as Well? The Missing Baseline in Graph Self-Supervised Learning

**Keywords:** self-supervised learning, graph representation learning, joint-embedding predictive architecture, structural entropy, untrained baselines, evaluation methodology, repeated cross-validation, graph classification

[Main paper PDF](https://openreview.net/pdf?id=BHz7VrHDRo)

Graph self-supervised learning is judged by freezing a pretrained encoder, fitting a linear probe, and comparing accuracies on small benchmarks, where methods are separated by a point or two. These comparisons almost never ask whether the same encoder, never trained, would do as well. We run this control for graph joint-embedding predictive architectures (JEPAs) on seven benchmarks, with three partitioners, two read-outs and two implementations, including the official Graph-JEPA code, whose published accuracies we reproduce. We find that pretraining adds no detectable accuracy over a randomly initialised copy of the encoder except on the smallest dataset, and that under the published read-out the untrained encoder is significantly better on three datasets. Pooled over benchmarks, every setting excludes a common gain above one and a half points. Pretraining does reshape the representation, without improving what a linear probe reads, and the most robust partition effect, structural-entropy over METIS partitions on NCI1, is nearly as large for the never-trained encoder as for the trained one. The benchmarks set the boundary: under a corrected test they cannot resolve gains below two to six points, several times the margins that rank published methods. An untrained encoder costs one run with zero epochs, and graph self-supervised learning should be measured against it.

## 335. You Only Live Once: Stop the Gradient or Regularize and Replay?

**Keywords:** JEPA, world modeling, anti-collapsing, test-time training

[Main paper PDF](https://openreview.net/pdf?id=3oyf1wlIWQ)

An agent that learns a world model from its own experience sees one finite trajectory, streamed in time order. We study JEPA in this you-only-live-once (YOLO) setting and find that the standard stop-gradient target fails silently: with finite data, the encoder can lock onto spurious noise correlations while its latent variance and training loss look healthy. An analysis of the objective motivates this failure. Removing stop-gradient and adding a variance floor regularizer prevents the collapse, and replaying past experience widens the samples for estimating the variance. Our Replay Variance Floor (RVF) recovers the latent dynamics in controlled linear systems and improves planning over the stop-gradient baseline on a range of visual control tasks.

## 336. Your Probabilistic JEPA Is Secretly a Hidden Markov Model: A State-Space Interpretation of Joint-Embedding Predictive Learning

**Keywords:** probabilistic JEPA, hidden Markov models, state-space models, representation learning, self-supervised learning

[Main paper PDF](https://openreview.net/pdf?id=QiL3g00IHS)

A hidden Markov model (HMM) combines three roles: inference of a hidden-state belief from observations, propagation through a Markov transition, and emission back to observation space. We show that full, time-indexed Predictive Information Bottleneck VJEPA (PIB-VJEPA) exposes the same computational structure: a stochastic context encoder plays the role of an amortized filtering distribution, a probabilistic predictor defines latent-state dynamics, and a decoder, inverse target encoder, or induced implicit conditional supplies the emission direction. We formalize four progressively stronger levels of correspondence, from computational analogy to exact sequence-level and model-and-objective equivalence, and give sufficient conditions under which a probabilistic temporal JEPA admits an exact HMM representation. We instantiate this view with Markov-Chain JEPA (MCJEPA), which replaces the latent predictor by a learned transition matrix; in the finite time-homogeneous case, matrix powers guarantee exact multi-horizon Chapman--Kolmogorov consistency. The framework extends naturally to conditioned discrete-state transitions, continuous-state Markov kernels, continuous-time dynamics, and deterministic Dirac-kernel dynamics. We further reinterpret predictive information-bottleneck learning as Markov-state construction: compression promotes \textit{minimality}, while residual predictability diagnoses \textit{insufficiency}. Controlled experiments support transition recovery and composition, the filtering interpretation of the context encoder, recovery of a known minimal predictive state, and HMM-style sequence training of probabilistic JEPA, including hybrid JEPA--HMM objectives. Together, these results give probabilistic temporal JEPA a principled state-space interpretation and connect joint-embedding predictive learning with probabilistic dynamical modeling.

## 337. Your World Model Is Not Blind, Your Detector Is: Native Prediction Errors for Regime Detection

**Keywords:** World Model, JEPA, Deep Learning Theory

[Main paper PDF](https://openreview.net/pdf?id=PpwzEfEMRu)

A world model that has learned how a system evolves should be the first to notice when that system starts to evolve differently. Yet learned representations are routinely judged blind to regime change: a predictive representation that recovers the hidden state of a dynamical system still lets standard sequential change-point detectors miss most changes. We show that this blindness belongs to the detector, not the representation. While standard detectors assume latent states follow a linear process, we instead query the world model directly-scoring each transition by its one-step predictive error normalized by covariance fitted on nominal (calm) data. This native-residual detector requires no retraining and elevates detection rates from a small minority of shifts to near the exact-likelihood ceiling. We then prove why this gap exists. The standard detector’s variance channel can only gather evidence above a threshold fixed by its alternative hypothesis grid, which no grid refinement resolves. Furthermore, we prove an absorption principle: a flexible predictor trained on calm data systematically explains away the component of a regime shift aligned with its learned dynamics, while a learned variance head re-weights the residual back toward nominal behavior. This reveals why standardizing by model uncertainty is inherently deceptive. Across convolutional, transformer, and period-folding backbones, native-residual detection alarms roughly three times faster than classical baselines, fails predictably only when an encoder discards one-step temporal order, and outperforms recent detector families, calm-fitted forecasters, and a zero-shot foundation model.
