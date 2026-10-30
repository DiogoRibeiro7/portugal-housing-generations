# Release-readiness checklist: v1.0.0

Status as of 30 October 2026. Each entry is **PASS** (done and verified), **BLOCKED** (cannot proceed until
something outside this repository changes) or **NOT YET DONE** (a step for the maintainer, which nothing here
does automatically).

**Verdict: released.** v1.0.0 was published on 30 October 2026 and archived on Zenodo with DOI
[10.5281/zenodo.23816265](https://doi.org/10.5281/zenodo.23816265) (section E). One decision is left for a later version: the completions
series (A9).

## A. Data and licensing

| # | Check | Status | Evidence |
|---|---|---|---|
| A1 | Every data file listed with provider, source URL, retrieval time, provider update, terms, attribution and redistribution status | PASS | `docs/data-sources.csv` (56 data files and 8 retrieval records), built by `housing_pt.sources.data_sources`; `tests/test_data_sources.py` |
| A2 | INE terms verified | PASS | INE Portal terms: CC BY 4.0, cite "Fonte: Instituto Nacional de Estatística, IP – Portugal" (`docs/data-sources.md`) |
| A3 | Eurostat terms verified | PASS | Eurostat copyright notice: reuse authorised with acknowledgement, dataset DOIs `10.2908/<DATASET>` |
| A4 | ECB terms verified | PASS | ECB statistics usage policy: free reuse with the source quoted, no modification |
| A5 | Every data file redistributable | PASS | The PORDATA transcription (no reuse licence) was replaced by INE indicator 0000076, fetched by the workflow task `national`; identical values 1995–2025. `housing_pt.sources.data_sources --check-redistribution` passes |
| A6 | Code and documentation licence kept separate from third-party data; no relicensing of data under Apache-2.0 | PASS | README "Citing and licences", `docs/data-sources.md`, `.zenodo.json` description; `tests/test_release.py` |
| A7 | A release cannot silently include a file that is not cleared | PASS | The `package` and `release` tasks run `python -m housing_pt.sources.data_sources --check-redistribution` before building the archive and stop on any file not cleared; `tests/test_data_sources.py` |
| A8 | PORDATA file removed from the repository | PASS | Deleted from `data/` and the manifest; it remains in the git history |
| A9 | Optional: national completions on INE's long series instead | NOT YET DONE | INE 0011725 (pinned as a cross-check) is 2–37% higher than 0000076 in every year; INE's metadata gives no reason. 0000076 is kept, consistent with the municipal panel (`docs/data-sources.md`) |

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
| C4 | Generated results match committed values | PASS | Replacing the completions source changed no value: only its provenance fields and long-series check in `results/results.json`, one renamed cross-check in `results/results_regional.json`, `docs/data-sources.csv`, and the source line of `fig_integrated_national.png` |
| C5 | All 21 figures inspected visually | PASS | Four fixed (coverage colour bar, specifications legend, one overlapping label, one overlapping legend); no plotted value changed |
| C6 | PNG byte differences between environments explained | PASS | Pixels: text hinting came from a site-wide `matplotlibrc`; now set in the figure style. Bytes: Pillow's zlib level (3 locally, 6 from PyPI); pixels identical. No PNG replaced (`docs/review.md`) |
| C7 | Optional: replace the secondary y-axes in `fig_integrated_national.png` with separate panels | NOT YET DONE | Design improvement, not a defect; values are correct |

## D. Publication metadata

| # | Check | Status | Evidence |
|---|---|---|---|
| D1 | Author name, ORCID and contact e-mail consistent | PASS | `CITATION.cff`, `.zenodo.json`, report header; `tests/test_release.py` |
| D2 | Institutional affiliation | PASS | "Faculdade de Media Artes e Design, Universidade Técnica do Porto" (Portaria n.º 332-A/2026/1, 11 August 2026) |
| D3 | Version | PASS | 1.0.0 in `CITATION.cff`, `.zenodo.json`, report, release notes |
| D4 | Release date | PASS | 30 October 2026, in `CITATION.cff`, the GitHub release and the Zenodo record |
| D5 | DOI | PASS | 10.5281/zenodo.23816265 (version 1.0.0), minted by Zenodo; in `CITATION.cff`, the README and the report; `tests/test_release.py` |
| D6 | Citations and references | PASS | Report references updated (Costa et al. 2023; INE 0011495; Eurostat HICP manual and rent recommendations; INE rent-survey note) |
| D7 | Reproducibility instructions | PASS | README "Reproducing the release", report Appendix A, `reproduce.py` docstring |

## E. Release steps

Verified on 30 October 2026 at commit `265f6a2` of `main`: all release pull requests merged (Medium-Blog #386, #388,
#395, #398; this repository #1, #2); CI green on Python 3.10 and 3.13; 123 tests, 64 checksums and
`reproduce.py` pass locally; every data file may be redistributed; `CITATION.cff` valid (CFF 1.2.0); no tag or
release exists. A local dry run built the archive deterministically (12,386,103 bytes, 142 files) and the GitHub
source zip of the same commit, which Zenodo archives, matched its per-file manifest in every file.

| # | Step | Status |
|---|---|---|
| E1 | Merge the release pull requests | PASS |
| E2 | Clear A5 (PORDATA file replaced by INE 0000076) | PASS |
| E3 | Repository public | PASS |
| E4 | Repository switched on in Zenodo's GitHub settings | PASS (Zenodo archived the release) |
| E5 | `package` run: archive, SHA-256 and per-file manifest reviewed and approved | PASS: run 41107511863 on `b0916fa`; approved SHA-256 `a31ee6da2388e1c6b9e7c8a7fd52f82d8cac421c9fdbf09355e587193bc44b0b` |
| E6 | `release` run: annotated tag and GitHub release with the approved archive | PASS: run 41110765765 rebuilt the archive with the approved SHA-256; annotated tag on `b0916fa`; release published 18:55 UTC with the zip, `.zip.sha256` and `.files.sha256` |
| E7 | Zenodo record checked against the per-file manifest | PASS: record 23816265 matches `.zenodo.json`; its file has the MD5 of GitHub's source zip of the tag (`94e18dc3…`), whose 150 files match the manifest |
| E8 | DOI and release date added to `CITATION.cff`, `README.md` and `docs/report.md` | PASS (this follow-up pull request) |

Commands are for PowerShell with the GitHub CLI; `R` is the repository.

```powershell
$R = "DiogoRibeiro7/portugal-housing-generations"
$T = "portugal-housing-generations-v1.0.0"
```

**E4. Zenodo.** Sign in to Zenodo with GitHub, open <https://zenodo.org/account/settings/github/>, select
*Sync now*, and switch the repository on. Do this before E6: Zenodo archives only releases created after the switch.
It archives GitHub's source zip of the release, not files attached to it, with the metadata in `.zenodo.json`.

**E5. Package and approve (publishes nothing).**
```powershell
gh workflow run portugal-housing-generations.yml --repo $R --ref main -f task=package
gh run list --repo $R --workflow portugal-housing-generations.yml --limit 1      # note the run ID
gh run watch <run-id> --repo $R --exit-status
gh run download <run-id> --repo $R --name $T --dir release-candidate
cd release-candidate
$expected = (Get-Content "$T.zip.sha256").Split(" ")[0]
$actual = (Get-FileHash "$T.zip" -Algorithm SHA256).Hash.ToLower()
"zip SHA-256: $actual  match: $($expected -eq $actual)"
Expand-Archive "$T.zip" -DestinationPath extracted
cd "extracted/$T"
Get-Content "../../$T.files.sha256" | ForEach-Object {
  $hash, $path = $_ -split "  ", 2
  if ((Get-FileHash $path -Algorithm SHA256).Hash.ToLower() -ne $hash) { "MISMATCH $path" }
}
python reproduce.py      # optional: REPRODUCED from the archive itself
```
The run's annotation (*Artifact*) shows the same SHA-256. Approval means recording that value.

**E6. Release (only after authorisation).** The task rebuilds the archive from the same commit and stops unless
its SHA-256 equals the approved value. It then creates the annotated tag and the GitHub release, with
`docs/release/notes-v1.0.0.md` as text and the zip, `.zip.sha256` and `.files.sha256` attached.
```powershell
gh workflow run portugal-housing-generations.yml --repo $R --ref main -f task=release -f approved_sha256=<approved SHA-256>
gh run watch <run-id> --repo $R --exit-status
git fetch origin --tags                  # in a clone of the repository
git cat-file -t $T                       # must print "tag" (annotated)
gh release view $T --repo $R
gh release download $T --repo $R --pattern "*.sha256" --dir released
```

**E7. Zenodo.** Within minutes of E6, Zenodo creates the record and mints two DOIs: one for this version and a
concept DOI for all versions. Both appear at <https://zenodo.org/account/settings/github/repository/DiogoRibeiro7/portugal-housing-generations>.
- Check the metadata against `.zenodo.json`: title, creator, ORCID, affiliation, licence, version 1.0.0, keywords.
- Download the record's zip, expand it, enter its top folder (`DiogoRibeiro7-portugal-housing-generations-<commit>`)
  and run the same per-file loop as in E5 against `released/$T.files.sha256`. It prints nothing when every file
  matches. Zenodo's zip is GitHub's, so its own SHA-256 differs from the approved archive's; the files must not.

If Zenodo must hold the approved zip byte for byte, switch the repository off in Zenodo before E6 and upload
`$T.zip` with its `.sha256` files as a new Zenodo upload, with the metadata from `.zenodo.json`. Using both routes
would create two records with two DOIs.

**E8. DOI pull request.** With the version DOI that Zenodo shows and the release date:
- `CITATION.cff`: add `doi: <version DOI>` and `date-released: "<YYYY-MM-DD>"` at the top level, and `doi:`
  under `preferred-citation`;
- `README.md`: replace "No DOI exists yet…" with the version DOI and the concept DOI, and add the DOI to the
  citation;
- `docs/report.md`: add the DOI to the header line;
- `tests/test_release.py`: replace the no-DOI test with one that checks the same DOI in all three files;
- this table: mark D4, D5 and E5–E8 as done.

`.zenodo.json` stays without a DOI: Zenodo assigns one to each new version.
