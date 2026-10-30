# Release-readiness checklist: v1.0.0

Status as of 30 October 2026. Each entry is **PASS** (done and verified), **BLOCKED** (cannot proceed until
something outside this repository changes) or **NOT YET DONE** (a step for the maintainer, which nothing here
does automatically).

**Verdict: no blocker remains.** Every data file may be redistributed (A5). What is left are the release steps
themselves (section E) and one optional decision on the completions series (A9).

## A. Data and licensing

| # | Check | Status | Evidence |
|---|---|---|---|
| A1 | Every data file listed with provider, source URL, retrieval time, provider update, terms, attribution and redistribution status | PASS | `DATA_SOURCES.csv` (56 data files and 8 retrieval records), built by `data_sources.py`; `test_data_sources.py` |
| A2 | INE terms verified | PASS | INE Portal terms: CC BY 4.0, cite "Fonte: Instituto Nacional de Estatística, IP – Portugal" (`DATA_SOURCES.md`) |
| A3 | Eurostat terms verified | PASS | Eurostat copyright notice: reuse authorised with acknowledgement, dataset DOIs `10.2908/<DATASET>` |
| A4 | ECB terms verified | PASS | ECB statistics usage policy: free reuse with the source quoted, no modification |
| A5 | Every data file redistributable | PASS | The PORDATA transcription (no reuse licence) was replaced by INE indicator 0000076, fetched by the workflow task `national`; identical values 1995–2025. `data_sources.py --check-redistribution` passes |
| A6 | Code and documentation licence kept separate from third-party data; no relicensing of data under Apache-2.0 | PASS | README "Citing and licences", `DATA_SOURCES.md`, `.zenodo.json` description; `test_release.py` |
| A7 | A release cannot silently include a file that is not cleared | PASS | The `release` task runs `python data_sources.py --check-redistribution` before creating the release and stops on any file not cleared; `test_data_sources.py` |
| A8 | PORDATA file removed from the repository | PASS | Deleted from `data/` and the manifest; it remains in the git history |
| A9 | Optional: national completions on INE's long series instead | NOT YET DONE | INE 0011725 (pinned as a cross-check) is 2–37% higher than 0000076 in every year; INE's metadata gives no reason. 0000076 is kept, consistent with the municipal panel (`DATA_SOURCES.md`) |

## B. External evidence

| # | Check | Status | Evidence |
|---|---|---|---|
| B1 | Banco de Portugal cohort ownership figures | PASS (with qualification) | Costa, Farinha, Lourenço and Mesquita (2023): households with reference person aged 25–34, censuses 1981–2021, about 70%, 60% and 40% (slide 12). Press-reported 61% and 42% replaced; the bulletin text itself was not retrieved |
| B2 | Vacant and secondary dwellings, 2021 | PASS | INE Censos 2021, indicator 0011495: 12.1% vacant, 18.5% secondary; OECD no longer cited |

## C. Reproducibility and figures

| # | Check | Status | Evidence |
|---|---|---|---|
| C1 | Full test suite | PASS | 123 tests pass on Python 3.10 and 3.13, locally and in CI |
| C2 | Manifest validation | PASS | `sha256sum --check data/SHA256SUMS` (64 files) and `reproduce.py` step 1 |
| C3 | `reproduce.py` | PASS | Prints `REPRODUCED` locally and in CI. Result files rebuild byte-identically in both; figures byte-identically locally and pixel-identically in CI (C6) |
| C4 | Generated results match committed values | PASS | Replacing the completions source changed no value: only its provenance fields and long-series check in `results.json`, one renamed cross-check in `results_regional.json`, `DATA_SOURCES.csv`, and the source line of `fig_integrated_national.png` |
| C5 | All 21 figures inspected visually | PASS | Four fixed (coverage colour bar, specifications legend, one overlapping label, one overlapping legend); no plotted value changed |
| C6 | PNG byte differences between environments explained | PASS | Pixels: text hinting came from a site-wide `matplotlibrc`; now set in the figure style. Bytes: Pillow's zlib level (3 locally, 6 from PyPI); pixels identical. No PNG replaced (`REVIEW.md`) |
| C7 | Optional: replace the secondary y-axes in `fig_integrated_national.png` with separate panels | NOT YET DONE | Design improvement, not a defect; values are correct |

## D. Publication metadata

| # | Check | Status | Evidence |
|---|---|---|---|
| D1 | Author name, ORCID and contact e-mail consistent | PASS | `CITATION.cff`, `.zenodo.json`, report header; `test_release.py` |
| D2 | Institutional affiliation | PASS | "Faculdade de Media Artes e Design, Universidade Técnica do Porto" (Portaria n.º 332-A/2026/1, 11 August 2026) |
| D3 | Version | PASS | 1.0.0 in `CITATION.cff`, `.zenodo.json`, report, release notes |
| D4 | Release date | NOT YET DONE | Recorded by the GitHub release and the Zenodo record; add `date-released` to `CITATION.cff` with the DOI (E5) |
| D5 | DOI | NOT YET DONE | None recorded or invented; Zenodo mints it when it archives the GitHub release |
| D6 | Citations and references | PASS | Report references updated (Costa et al. 2023; INE 0011495; Eurostat HICP manual and rent recommendations; INE rent-survey note) |
| D7 | Reproducibility instructions | PASS | README "Reproducing the release", report Appendix A, `reproduce.py` docstring |

## E. Release steps

| # | Step | Status |
|---|---|---|
| E1 | Merge the readiness pull requests (Medium-Blog #388 and #395; this repository #1) | PASS |
| E2 | Clear A5 (replace or license the PORDATA file), rebuild `DATA_SOURCES.csv`, rerun `reproduce.py` | PASS |
| E3 | Make the repository public and enable it in Zenodo's GitHub settings | NOT YET DONE |
| E4 | Run the `release` task on `main`: tag, GitHub release, Zenodo archive and DOI | NOT YET DONE |
| E5 | Add the DOI and release date to `CITATION.cff`, the README and the report | NOT YET DONE |

No zip is built or uploaded by hand: Zenodo archives the GitHub release itself, with the metadata in
`.zenodo.json`. `CITATION.cff` drives GitHub's "Cite this repository".

### Steps, in order

1. **Public repository and Zenodo (E3).** Zenodo's GitHub integration works only with public repositories.
   - In the repository settings, change the visibility to public.
   - Sign in to Zenodo with GitHub, open <https://zenodo.org/account/settings/github/>, select *Sync now* if the
     repository is not listed, and switch it on. Zenodo then archives every new GitHub release of the repository.
2. **Release (E4).** In GitHub Actions, run the `portugal-housing-generations` workflow on `main` with task
   `release`. It reproduces every result, checks that every data file may be redistributed, and creates the tag
   `portugal-housing-generations-v1.0.0` and the GitHub release, with `RELEASE_NOTES_v1.0.0.md` as its text.
   Zenodo archives the release within minutes and mints a DOI for the version and a concept DOI for all versions.
3. **DOI (E5).** In a follow-up pull request:
   - add `doi:` (the version DOI) and `date-released:` to `CITATION.cff`;
   - add the DOI to the README citation block and the report header.
