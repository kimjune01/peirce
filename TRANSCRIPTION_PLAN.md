# Transcription Plan

Turn the 2026 Houghton photographs into verifiable, searchable text. The images are the easy half, and the half Harvard will eventually do better. The text is the half that survives, and the half no library posts.

## Why

Peirce named the methodeutic and had no machine to run it. Transcribing him is how that work continues: hand his inductive program the modern severe-testing machinery (e-values, anytime-valid inference), build a classification for evidence trajectories, and put the result where anyone, a person or a coding agent, can pick it up. The text is also how the provenance edge gets drawn. A transcription bound to its page image is replayable, so a reader inherits Peirce by checking the manuscript instead of trusting an editor. License and ethos are settled in the [README](README.md): CC0 images, CC BY-SA text. This plan is only about getting from image to text.

## Step 0 — Find what Harvard has already digitized

Harvard is digitizing the whole collection, and many boxes were closed mid-trip for exactly that. Before spending effort, cross-check each photographed item against the HOLLIS finding aid (`hollisarchives.lib.harvard.edu/repositories/24/resources/6437`) and the Houghton IIIF.

This reorders the *image* work, not the *text* work:

- **Items Harvard already has at higher quality.** Their scans beat handheld phone shots, so drop the re-archiving. Still transcribe them, because Harvard posts images and never searchable text.
- **Items Harvard has not digitized.** The images are irreplaceable. Archive and transcribe both.

Output: a `digitized?` column in the manifest, with the HOLLIS / IIIF link where one exists.

## Step 1 — Order of work

Two filters, both from `houghton-export/TRANSCRIPTION-TRIAGE.md`:

- **Relevance first.** The methodeutics and probable-reasoning manuscripts lead: R 760 necessary reasoning, 741 figures and methods of logic, 736 qualitative logic, 767 induction-and-abduction, 768 statistical deduction, 763 doctrine of chances, 761/762 probability, 1093 economy of research, 472 the sixth lecture.
- **Latest draught only.** Most items are single copies. Where drafts exist, transcribe the last stage and skim the rest (Lecture III: the 3rd draught, R 464 + 465).

## Step 2 — Image to text

1. **Calibrate.** Run a few representative pages (one clean, one heavily revised, one with a diagram) through a vision model to see how far it gets on Peirce's hand. That decides whether a trained HTR model (Transkribus) is worth standing up, or whether vision plus correction is enough.
2. **Draft.** LLM-vision produces a diplomatic transcription per page: only what is on the page, deletions and insertions and draught marks preserved, gaps flagged rather than filled, uncertain readings marked. Each page is a hypothesis and the image is its kill condition.
3. **Correct.** Squint at the flagged pages, fix, feed corrections back. Per-page status: `raw`, `machine`, `checked`, `verified`.
4. The deletions are kept, not cleaned. They are his self-criticism, and the draught-to-draught diff is its own object.

## Step 3 — Form and home

Markdown with light editorial tags (`[unclear: ...]`, `[illegible]`, `{del}`, `{add}`, `[diagram: ...]`), one file per manuscript. This is the **Document** layer; the reading, critique, and continuation layers build on it later. Each page links to its archive.org image (IIIF). Hosted on the `reading-src` Astro app under `/reading/methodeutics/`.

## Done when

Each priority manuscript has a checked transcription, bound to its archive.org images, discoverable as text.
