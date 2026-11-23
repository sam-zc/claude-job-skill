# Agent-run direct PDF editing and verification

The source and output format are PDF. Work only on `workflows/<company>/<job>/resume.pdf`, copied from the owned job's unchanged `source/frontend-base.pdf`. No DOCX or Word conversion is part of this flow.

1. Use Python 3.10+ with the packages in `skills/ai-tailor/scripts/requirements.txt` and Poppler (`pdftotext`, `pdftoppm`, `pdffonts`, `pdfinfo`). Follow the repository README setup; no external PDF skill or host-specific runtime-discovery tool is required. Install missing packages into an isolated environment as needed. Verify the actual Calibri fonts/glyph coverage available for replacements. Never silently substitute fonts or turn text into images/outlines.
2. Verify the job token/source binding and `source/protected-hashes.json`. Inspect both BASE pages, inventory its text, fonts, links and layout, and retain the source text extraction. Prepare `expected.txt` from this source plus the approved before/after ledger **before** checking the edited PDF. Include complete final text in reading order with actual bullet markers. This independent intended text must not be copied from the edited file as a self-comparison.
3. Edit `resume.pdf` directly with a text-aware PDF tool. Preserve unaffected objects/layout, font mappings, searchable text, links and existing tags/annotations. Remove replaced text correctly: an opaque white rectangle does not remove its searchable old text. Reflow only the affected regions, shortening truthful wording when needed to retain two readable pages. Save/reopen after substantive edits and inspect the affected area for hidden duplicates, missing glyphs or overlap.
4. Create a **new** `exports/<iteration>/`: copy the exact saved working PDF to `direct.pdf`, and the independently prepared intended text to `expected.txt`. Write `provenance.json`: absolute `sourceBasePath`, `sourceBaseSha256`, `sourceCopyPath`, `sourceCopySha256`, `workingPdfPath`, `workingPdfSha256`, `expectedTextSha256`, `capturedAt`, `generatedAt`, editing-tool/version/font details and `ownershipToken`. Exclude the token from user-facing reports. Keep the before/after/evidence ledger with the iteration.
5. Run with real absolute paths and the prepared Python environment:

```bash
rtk proxy "$PDF_PYTHON" skills/ai-tailor/scripts/verify_job.py \
  --workspace /Users/SANJEEV.S/projects/misc \
  --job-dir "$JOB_DIR" --provenance "$ITERATION/provenance.json" \
  --expected-text "$ITERATION/expected.txt" --pdf "$ITERATION/direct.pdf" \
  --out "$QA_ITERATION"
```

The guard verifies ownership, local BASE/copy lineage, protected inputs, working/iteration PDF identity, intended-text hash and job-contained paths. No DOCX is read. Layout expectations come from the selected BASE.

6. Read `status.json`, `qa/final/checks.json`, `qa/final/pdf/audit.json`, expected-versus-PDF word diffs, raw extraction, font/Unicode maps and links. Compare original BASE text with the edited result and reconcile every material difference with the change ledger/evidence. Retain Poppler raw/layout/default, pypdf plain/layout, pdfplumber default and PyMuPDF sorted/unsorted results with versions. Text selection alone is not proof of correct role/reading-order parsing.
7. Clean files are copied unchanged. The checker retains a narrow legacy spacing-metadata repair only for `/ActualText <FEFF200B>` over a painted `<0003> Tj` mapped to a space. If present, require the guarded object-graph and every-page pixel comparisons; it does not authorize general cleanup. Unknown glyph, metadata or content defects require editing/tool investigation, never broad normalization or tag removal.
8. Inspect **every final PDF page** with the image viewer. Check original typography/hierarchy, margins, density, bullets, complete roles/projects, date/location alignment, hyperlinks and absence of clipping, overlap, orphan headings or hidden old text. Compare the expected wording/JD phrase ledger with the actual extractable text. Record page-by-page observations and input protection checks. Fix the working PDF and repeat in a new iteration after any failure.

After actually completing those reviews, write `review.json` in the checked QA iteration directory (the output of `verify_job.py`, alongside `status.json`). Required fields:

```json
{
  "candidateSha256": "the exact checked candidate hash",
  "expectedTextSha256": "the independent intended-text hash",
  "reviewedAt": "actual review time with Asia/Kolkata offset",
  "evidenceReviewed": true,
  "jdReconciled": true,
  "protectedInputsVerified": true,
  "pages": [
    {"page": 1, "observations": "Actual page-specific layout/content observations"},
    {"page": 2, "observations": "Actual page-specific layout/content observations"}
  ]
}
```

This is the agent's review record, not automated proof of a visual judgment; never populate it for unseen pages or unperformed evidence checks. It binds that review to exact candidate/intended-text bytes. Any subsequent edit invalidates the record and requires new QA/review. ai-apply's upload gate requires this review plus the actual successful mechanical QA/provenance/input artifacts; a caller-supplied PDF hash alone cannot pass.
9. Live employer parsing stays `NOT_TESTED` unless separately authorized and observed for these exact bytes. Local QA or historical portal tests never establish a new live ATS pass.
10. Only after evidence, mechanical, visual and protection gates pass, copy checked `candidate.pdf` to the final PDF filename, re-hash, update status/log and release this invocation's claim. Caller-mode ai-apply retains its token/status. Deliver PDF plus analysis; no DOCX is generated.

A mechanical pass leaves independent evidence and all-page visual review outstanding. Preserve current job requirements and truthful scope; never relax a check merely to pass an edited file.

Editing note for this BASE: keep the original encoded text-drawing operation and its position/order when possible. Check glyph mappings and widths first. Reusing extracted subset font bytes as a full Unicode font can produce wrong glyphs; appending a replacement text operation can change parser order. Hyperlink checks must bind destination to displayed text, not just compare the set of URLs.
