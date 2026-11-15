#!/usr/bin/env bash
# Assemble 04_Final_Handoff/research_handoff/ and research_handoff.zip from the project tree.
# Usage: bash scripts/package_handoff.sh   (run from the project root)
set -euo pipefail
ROOT=$(pwd)
H=04_Final_Handoff/research_handoff
rm -rf "$H" 04_Final_Handoff/research_handoff.zip
mkdir -p "$H"/workstreams "$H"/supporting/scripts
# core deliverables (written into 04_Final_Handoff/ by the coordinator)
for f in READ_FIRST.md research_brief.md disputes_and_followups.md revision_candidates.json; do
  cp 04_Final_Handoff/$f "$H"/
done
cp 01_Evidence/sources.json 01_Evidence/evidence.json "$H"/
cp 00_Start_Here/run_log.md "$H"/
# supporting material
cp 01_Evidence/id_mapping.json 01_Evidence/register_stats.json 01_Evidence/evidence_digest_by_proposition.md 01_Evidence/source_index.md "$H"/supporting/
cp 00_Start_Here/research_instructions.md 00_Start_Here/drive_manifest.json "$H"/supporting/
cp scripts/*.py scripts/*.sh scripts/manual_overrides.json "$H"/supporting/scripts/
# workstreams: round 1 workers, round 2 reviews, round 3 follow-ups
for d in 02_Workstreams/*/; do
  n=$(basename "$d"); mkdir -p "$H/workstreams/round1_$n"
  cp "$d"/*.md "$d"/*.json "$H/workstreams/round1_$n/" 2>/dev/null || true
done
mkdir -p "$H/workstreams/round2_adversarial_review"
cp 03_Challenge_and_Followup/round2_protocol.md 03_Challenge_and_Followup/R2* "$H/workstreams/round2_adversarial_review/" 2>/dev/null || true
for d in 03_Challenge_and_Followup/R3*/; do
  n=$(basename "$d"); mkdir -p "$H/workstreams/round3_$n"
  cp "$d"/* "$H/workstreams/round3_$n/" 2>/dev/null || true
done
cp 03_Challenge_and_Followup/round3_*.md "$H/workstreams/" 2>/dev/null || true
cp 03_Challenge_and_Followup/round2_comparison.md "$H/workstreams/round2_adversarial_review/" 2>/dev/null || true
# validation (run against the assembled handoff)
python3 -I scripts/validate_handoff.py "$H" "$H/validation_results.md" > /dev/null || echo "VALIDATION REPORTED ERRORS - see $H/validation_results.md"
# no secrets / no PDFs
if find "$H" -type f \( -name "*.pdf" -o -name ".env" -o -name "*cookie*" -o -name "*credential*" -o -name "*token*" \) | grep -q .; then
  echo "WARNING: disallowed files present"; find "$H" -type f \( -name "*.pdf" -o -name ".env" -o -name "*cookie*" -o -name "*credential*" -o -name "*token*" \)
fi
(cd 04_Final_Handoff && zip -qr research_handoff.zip research_handoff)
ls -la 04_Final_Handoff/research_handoff.zip
find "$H" -type f | wc -l
