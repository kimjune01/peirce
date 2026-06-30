# Prior Art

The state of computational work on the Peirce manuscripts, as of June 2026, and what it means for this project. Researched 2026-06-29.

## The main one: "Peirce Interprets Peirce"

A **four-year funded research project** (Alessandro Adamou, Sebastian Feil, Davide Picca, Carlo Teo Pedretti, Dario Rodighiero, Lorenzo Zangari) doing machine-assisted transcription, semantic modeling, and visualization of the Peirce manuscripts. Public prototype on TEI Publisher: [peirce.humanitiesconnect.net](https://peirce.humanitiesconnect.net). Two visible outputs:

- **"Peirce Interprets Peirce: Digitization, Automation, and Interpretation"** ([dariorodighiero.com](https://dariorodighiero.com/peirce-interprets-peirce-digitization-automation-and-interpretation-in-charles-peirce-s-manuscripts)) — the transcription + edition work.
- **"Moving Pictures of Thought"** (Pedretti, Picca, Rodighiero, [arXiv:2511.13378](https://arxiv.org/abs/2511.13378), 2025) — VLM detection and semiotic interpretation of *diagrams* (not transcription). Code: `anonymous.4open.science/r/PIP-Manuscripts-Processor-0147`; data: [Zenodo 10.5281/zenodo.16113285](https://doi.org/10.5281/zenodo.16113285).

What they have built that overlaps our plan:

- VLM transcription of Peirce's hand, at scale (goal: the full Harvard 233-item / 15,695-image corpus).
- **Diplomatic TEI markup that preserves authorial revisions** (deletions, insertions, substitutions), aligned to the IIIF facsimile. That is our Document layer.
- Text, diagrams, revisions, and color treated as "a single semiotic surface."
- Planned next: critical apparatus + ontology annotations.

## The result that settles our Step 2

On Peirce's hand, **a zero-shot VLM beats a fine-tuned HTR model**:

| System | CER | WER (strict) |
|---|---|---|
| Google Gemini Flash 3 (zero-shot) | **2.36%** | **4.41%** |
| PyLaia / Transkribus (fine-tuned, 80 pp) | 4.98% | 13.95% |

Their note: the fine-tuned HTR is "locally plausible but lexically unstable" on Peirce, where the VLM holds at word level. This is corroborated by the general trend (LLMs hitting SOTA on handwritten historical transcription, [arXiv:2411.03340](https://arxiv.org/abs/2411.03340)).

**Consequence:** go vision-first. Do not stand up Transkribus. The calibration question in `TRANSCRIPTION_PLAN.md` Step 2 is answered before we run it.

## Where this project is still ours

Honest accounting: a funded team is already doing the raw VLM transcription and diplomatic markup of the *digitized* corpus, and doing it well. Re-transcribing the 233 digitized items would be redundant. What is still genuinely ours:

1. **The 71 un-digitized items.** Their corpus is the Harvard 233-item digitized set. Our cross-check (`hollis/digitized-crosscheck.tsv`) shows 71 of our 78 are *not* in it. We shot outside the digitization wall, so our scans are material their pipeline cannot reach yet. Transcribing those is a first, and the CC0 images + transcriptions extend the corpus they depend on.
2. **The Continuation layer.** Their project ends at edition + analysis + visualization. Ours continues the methodeutic: e-values for the inductive program, the evidence-trajectory classification, the critique-and-improve layers. They build the reading substrate; we build the argument on top.
3. **The representational-reading gap, which is our home turf.** Their explicit unsolved problem: VLMs are "strong at the morphological level (counting cuts, lines, spots) and the relational level (containment, connection), but [show] systematic failure at the representational level, where the diagram must be read as a logical formula." Reading Existential Graphs *as logic* is exactly what our typed-inference / hypothesis-graph work is about. This is a precise open problem we are equipped for.
4. **Agent-discoverable, verifiable framing.** Their output is a TEI Publisher edition for human scholars. Ours is replayable and agent-facing: each transcription a hypothesis with the page image as its kill condition, CC0, so an agent inherits it by checking, not trusting.

## Move

- Update Step 2 to vision-first; drop the Transkribus branch.
- Point transcription effort at the 71 un-digitized items and the flagship methodeutic pieces, not the digitized 233.
- Consider reaching out. Complementary, not competing: our un-digitized scans + the logic/EG representational angle against their corpus + infrastructure. Start small, offer something concrete (the cross-check, a few transcriptions of items they lack).

## Secondary

- "Unlocking the Archives" ([arXiv:2411.03340](https://arxiv.org/html/2411.03340v1)) — LLMs achieve SOTA on handwritten historical transcription. General validation of vision-first.
- HTR-LLM workflows for hard hands (e.g. abbreviated Latin court hand, [arXiv:2507.04132](https://arxiv.org/pdf/2507.04132)) — the correction-loop pattern, if a hybrid is ever wanted.
