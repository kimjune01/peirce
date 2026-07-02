# Peirce Work Log

## 2026-07-01 - Machine-drafted the rest of the corpus with codex

Ran the **remaining 882 manuscript pages** through codex (GPT-5.5) via
`scripts/transcribe_priority.sh` on the codex subscription pool -- **876 ok / 6
fail** on the first pass, then a resume pass recovered all 6 (transient
timeouts), landing **882/882, 0 fail**. Worklist built by scanning
`_classify/result_*.json` for `manuscript_page` across all 64 non-priority,
non-reference folders (call-slips, dividers, non-manuscript, and L75/REF_ketner
excluded) and dropping any page already on disk. With the 284 priority pages from
06-29 this brings the whole photographed set to a machine draft: **1166 `.txt`
files across 74 R-folders, ~1.16 MB** of diplomatic markup, one file per page,
named by image so it maps to the scan and the archive.org source.

This machine-drafts *everything*, including the earlier Lecture III draughts
(460-463) that TRANSCRIPTION-TRIAGE marks skim/skip -- deliberately: the machine
draft is cheap, and the draft-triage governs where the *human squint* effort
goes, not where the scaffold reaches. Each page is a hypothesis, the image its
kill condition; June's corrections land as git diffs. Next: the squint pass in
`tools/squint/`.

## 2026-06-29 - The transcription program: four layers, and the critic he never had

The trip log ended pointing here: Harvard will post the images, never the
searchable text, so the work that survives is the transcription. This sets the
method before the labor.

**Originals cleared.** Deleted the 1992 HEIC camera originals (~2.7 GB) now that
the Glacier backup holds and every one has a full-res by-item JPG; 12 orphans
with no derivative kept. The full-res JPGs + 512px thumbs are the working
authority. Triage written to `houghton-export/TRANSCRIPTION-TRIAGE.md`: most of
the 78 folders are singletons with no draft to choose, the only deep draft-stack
is Lecture III (latest = the 3rd draught, R 464 + 465; skip the 2nd draughts and
the plain 460, 466 is reuse), and the order to actually work in is relevance to
methodeutics and probable reasoning first -- R 760 necessary reasoning, 741
figures and methods of logic, 736 qualitative logic, 767 induction-and-abduction,
768 statistical deduction, 763 doctrine of chances, 761/762 probability, 1093
economy of research, 472 the sixth lecture.

**Why, restated.** Not an archive -- a continuation of the methodeutic. E-values
as the running form of his induction (the severe-testing line that goes from
Peirce through Mayo to Vovk/Grünwald/Ramdas/Wang), a classification for evidence
trajectories, thinking tools for whoever wants them. The CC0 images already drew
the provenance edge to the root of the canon; the transcriptions are how a reader
or a coding agent inherits him by replaying the page instead of trusting a name.

**The output is four layers, and they never leak.**

1. *Document* -- what is on the page, deletions and insertions and draughts
   intact. Kill condition: the scan.
2. *Mind* -- what he meant. Reconstructed intent, citeable, defeasible.
3. *Critique* -- where he is genuinely wrong or short. A claim that can itself
   fail.
4. *Continuation* -- the improved, extended version: the methodeutic
   operationalized, the math he reached for and did not have.

The instant a correction edits the transcription, or a reading gets passed off as
what the page says, it is the attestation-for-verification failure the whole
program exists to indict. The opening pledge of this log -- stop writing over him
-- made structural.

**The deletions are the point.** A man with no critic was his own. A struck word
is a killed claim, a rewrite is re-entry, six draughts are an inquiry trajectory:
a hypothesis graph run by hand. The draught-to-draught diff is the abductor XOR,
his cuts against his additions, the figure he changed against the ground he kept.
So the Critique layer only touches what survived his own last revision -- where
he struck it, he already caught it. The external critic is owed exactly the seam
where his self-correction hit the wall of a method he did not have.

**But the criticism is the main event.** Charity is its setup, not deference.
Pretending everything he said was right is the disservice, and it breaks his own
rule: what cannot be false cannot be true, Peirce included -- make him
unfalsifiable and you make him untrue. Steelman so the refutation lands on the
real claim, then mark the genuine errors plainly, with receipts: the evolutionary
metaphysics (tychism, agapism) as untestable reach, the foundational holes in his
frequentist probability, the flat technical mistakes any 2000-page corpus from a
working mathematician carries. The charity bar sorts (don't swing at gaps or
prescience as if they were blunders); it never softens a real hit. The man is
owed the hit he never got.

**Flagship.** His own science-on-trial -- the self-correcting science that is the
headwater of error-statistics, the same claim as the Science on Trial post a
century apart -- run through all four layers first, because the Continuation is
already half-written across that post and the e-value classification. Candidate
folders: R 771 essays on the rationale of science, 769/770 logic of science, 766
synopsis of the ground of induction.

**Next.** Pull the Lecture III draught stack and lay the strike-throughs and
rewrites side by side, as proof the method holds before it scales; or take R 760
or 741 through a vision pass, which doubles as a readability calibration on his
hand before standing up any HTR pipeline. Host on the separate `reading-src/`
Astro app under /reading/, per-page deep links to archive.org IIIF.

## 2026-06-29 - Transcription plan written

Wrote `TRANSCRIPTION_PLAN.md`, scoped to image-to-text. Step 0 is a HOLLIS
cross-check to find what Harvard already digitized -- it reorders the image
work, not the text work: their scans beat phone shots, but they never post
searchable text, so everything still gets transcribed. Order of work is
relevance-first (the methodeutics / probability manuscripts) and
latest-draught-only per the triage. Pipeline: vision calibration on Peirce's
hand -> LLM-vision diplomatic transcription as a per-page hypothesis (deletions
preserved, gaps flagged, image as kill condition) -> human correction -> status
ladder (raw/machine/checked/verified); Transkribus HTR only if vision falls
short. Output is the Document layer in markdown with light editorial tags,
per-page archive.org IIIF links, hosted at reading-src /reading/methodeutics.

## 2026-06-29 - HOLLIS digitization cross-check

Pulled the finding-aid CSV (`hollis/hou02614-finding-aid.csv`) and joined it
against the 78 photographed items, by item number and box as suspected:
Component Identifier = Robin #, Container Info = box, Digital Content Link =
the digitization flag. Result in `hollis/digitized-crosscheck.tsv`.

Only **5 of 78 are already digitized at Harvard**: R462, R464 (Lowell Lecture
III draughts, Box 32); R797, R798, R802 (Box 50). Each has a resolving
`nrs.harvard.edu/URN-3:FHCL.HOUGH:*` persistent URL (Harvard page-turner /
IIIF, higher quality than the phone shots). The other **71 are not digitized**,
so our scans are the only freely available copies -- confirms the upload's
irreplaceability. The collection has 424 digitized components in total, but
they are overwhelmingly correspondence and behind-the-wall boxes we could not
shoot; the 5 overlaps are the items that were both on the desk and already
scanned.

Method: dev-browser was required (hollisarchives 404s to plain fetch; the
`/digital_only` path is dead, the live facet is `f[access][]=online`). The CSV
download (`/download_collection_csv/hou02614.csv`) is the clean authoritative
source and is now mirrored in `hollis/`.

## 2026-06-29 - Prior-art scan: a funded team is already on this

Wrote `PRIOR_ART.md`. The main prior art is **"Peirce Interprets Peirce"**, a
four-year funded project (Adamou, Feil, Picca, Pedretti, Rodighiero, Zangari):
VLM transcription + diplomatic TEI markup (deletions/insertions preserved) +
semantic modeling + visualization of the Peirce manuscripts. Public TEI
Publisher prototype at peirce.humanitiesconnect.net; the diagram paper "Moving
Pictures of Thought" is arXiv:2511.13378 (2025).

Settles our Step 2: on Peirce's hand, zero-shot **Gemini Flash 3 beats
fine-tuned PyLaia/Transkribus** (2.36 vs 4.98 CER; 4.41 vs 13.95 WER). Go
vision-first, drop HTR.

Honest accounting: they already do raw VLM transcription + diplomatic markup of
the *digitized* corpus, well, so re-transcribing those 233 items is redundant.
What stays ours: (1) the **71 un-digitized items** are outside their corpus
(the cross-check proves the disjointness); (2) the **continuation layer**
(e-values, evidence trajectories, critique-and-improve) is unbuilt by them;
(3) their one named failure -- VLMs can't read existential graphs *as logical
formulas* (representational level) -- is our home turf; (4) agent-replayable
CC0 vs their human-facing TEI edition. Move: vision-first, target the
un-digitized 71 + flagship pieces, reach out as complementary (un-digitized
scans + the logic/EG angle for their corpus + infrastructure).

## 2026-06-29 - Pulled Harvard web-quality for the 5 digitized items

Grabbed all 5 already-digitized items from Harvard IIIF at web size (1600px long
edge) into `houghton-export/harvard-web/` (gitignored): R462 (96pp), R464 (72pp),
R797 (9pp), R798 (6pp), R802 (4pp) = 187 pages, 67 MB. Mechanism: nrs URL ->
viewer.lib.harvard.edu -> IIIF v3 manifest at `<urn>:MANIFEST:3` -> images from
`mps.lib.harvard.edu/assets/images/drs:NNN/full/1600,/0/default.jpg`.

Correction to an earlier assumption: Harvard's masters are NOT higher resolution
than our phone shots. For these items the master caps at 2546x2693 (~6.9 MP) vs
our 4032x3024 (~12 MP). Their value is the professional capture (flat, even
light, true color, no phone glare/skew) and the canonical IIIF link, not a
resolution upgrade. Pulled web-quality only, per June; no high-res stored.
TRANSCRIPTION_PLAN.md Step 0 corrected to match.

## 2026-06-29 - archive.org references + completeness audit

Built `references/archive-org-items.tsv`: all 77 uploaded items mapped robin ->
IA identifier (`peirce-msam1632-<4-digit>`; L75 -> `-l75`) -> details / IIIF
manifest / download URLs. archive.org serves IIIF
(`iiif.archive.org/iiif/<id>/manifest.json`, verified 200), so the reading site
can deep-link our own CC0 uploads per page; the 5 Harvard-digitized items also
carry Harvard IIIF as a second reference.

Completeness audit (asked to finish any partial uploads): filename-level check of
all 77 items, local `by-item` pages vs IA originals. **Result: COMPLETE, 77/77,
every local page present, 0 gaps.** The apparent +1 per item was archive.org's
auto-generated `__ia_thumb.jpg` (tagged source=original), not a page.
Deliberately absent by prior curation, not gaps: REF (Ketner 1977 bibliography,
in copyright) and the non-manuscript context shots (locker, reading room, box
labels). Nothing to finish.

## 2026-06-30 - Priority set transcribed (codex scaffold)

Ran the 10 methodeutic / probability priority items through codex (GPT-5.5) via
`scripts/transcribe_priority.sh`: **284 content pages** (call-slips and dividers
skipped via the classification), **283 ok / 0 fail / 1 skip**, ~1.1 MB of
diplomatic-markup text in `transcriptions/R<robin>/<IMG>.txt` (one file per page,
named by image so it maps to the scan and the archive.org file). All on the
**codex subscription pool**, ~18k tokens/page, none on the Claude weekly bucket.

Quality is strong cold: the statistical syllogism (R768), Port Royal logic
(R736), Zeno (R814 sample), Hamilton's quantified predicate (R741), probability
as "logic quantitatively considered" (R762) all read coherently, with
`{del}`/`{add}`/`[unclear:]`/`[illegible]` markup preserved; 0 refusals. This is
the editable scaffold for the human squint pass -- machine draft = hypothesis,
page image = kill condition, June's corrections land as git diffs (the entitlement
ledger in version history). Mechanism notes for re-runs: `codex exec -i` is
variadic, so the prompt MUST come via stdin (`printf "$P" | codex exec -i IMG -o OUT`);
`xargs` + exported functions fails on macOS bash 3.2, so the runner is a
sequential, resumable while-loop (skips pages already on disk).

## 2026-06-30 - Squint: proofreading GUI for the transcription scaffold

Built `tools/squint/` -- a dependency-free local viewer (Python stdlib server +
one HTML file, **port 1913**) to proofread the codex scaffold against the page
images. NOT a standalone editor: it is a companion to a coding agent. Three
columns: thumbnail rail | manuscript image | text pane. The text pane edits the
raw inline markup like markdown -- toolbar buttons (`{del}` `{add}` `[unclear]`
`[illeg]` `[diagram]`, plus Cmd-D/I/U) WRAP the highlighted text in the tags or
INSERT the tag pair at the cursor when nothing is selected. The tags are
color-matched to their buttons (red `{del}`, green `{add}`, purple brackets) via
a colored backdrop layer synced behind a transparent textarea -- real plain-text
editing, colored tokens, no WYSIWYG.

Data-format decision: the canonical form stays the lightweight inline markup, NOT
rich text, so it ports trivially (the textarea IS the canonical text; nothing to
convert). Workflow: squint at the image, mark or fix in
the box, hit copy -> clipboard gets the canonical markup PLUS a pointer (file
path + archive.org source image + cite) -> paste into your coding agent, which
edits `transcriptions/R<robin>/<IMG>.txt` -> hit refresh to re-read the file and
see the edit reflected. Neutral grayscale palette per june.kim/design.
Run: `python3 tools/squint/server.py`.
