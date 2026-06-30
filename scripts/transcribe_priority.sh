#!/bin/bash
# Transcribe priority Peirce pages via codex (GPT-5.5) into transcriptions/.
# Resumable: skips any page whose output already exists and is non-empty.
# Usage: scripts/transcribe_priority.sh [worklist.tsv]   (tab cols: robin <tab> imgpath <tab> outpath)
cd "$(dirname "$0")/.." || exit 1            # repo root
WORKLIST="${1:-/tmp/peirce_worklist.tsv}"
LOG="transcriptions/_run.log"
mkdir -p transcriptions
[ -f "$WORKLIST" ] || { echo "no worklist: $WORKLIST"; exit 1; }

PROMPT='Transcribe this single page of a handwritten Charles S. Peirce manuscript (early 1900s, difficult late hand; logic and philosophy). DIPLOMATIC transcription, not a clean reading:
- Only what is visibly on the page. Do NOT modernize, complete, or invent words.
- Preserve line breaks.
- deletions {del}...{/del}, insertions {add}...{/add}.
- [illegible] for unreadable; [unclear: best-guess?] for uncertain.
- diagrams/figures: [diagram: one-line description]. formulas: transcribe if clear else [formula: see image].
Output ONLY the transcription.'

total=$(wc -l < "$WORKLIST" | tr -d ' '); n=0; ok=0; fail=0; skip=0
echo "=== run $(date '+%m-%d %H:%M:%S')  $total pages ===" >> "$LOG"
while IFS=$'\t' read -r rb img out; do
  n=$((n+1))
  [ -z "$out" ] && continue
  if [ -s "$out" ]; then skip=$((skip+1)); continue; fi
  if [ ! -f "$img" ]; then echo "[$n/$total] MISS $img" | tee -a "$LOG"; continue; fi
  mkdir -p "$(dirname "$out")"
  printf '%s\n' "$PROMPT" | timeout 220 codex exec -i "$img" -o "$out" >/dev/null 2>&1
  if [ -s "$out" ]; then ok=$((ok+1)); echo "[$n/$total] ok   $out" | tee -a "$LOG"
  else fail=$((fail+1)); echo "[$n/$total] FAIL $img" | tee -a "$LOG"; fi
done < "$WORKLIST"
echo "=== DONE $(date '+%H:%M:%S'): ok=$ok fail=$fail skip=$skip | $(ls transcriptions/R*/*.txt 2>/dev/null | wc -l | tr -d ' ') files ===" | tee -a "$LOG"
