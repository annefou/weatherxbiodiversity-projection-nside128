# 04 — FORRT Replication Study

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify code first:** read the actual reproduction script in `notebooks/03_analysis.py` before writing the methodology field. See `docs/verify-before-drafting.md`.

## Field-by-field draft

### Short URI suffix for study ID (text input, required)

Slug. Use kebab-case.

```
soroye2020-iberian-bombus-healpix-nside128-substrate-extension
```

### Label/name of replication study (text input, required)

Human-readable title.

```
Soroye et al. 2020 TEI mechanism — HEALPix nside=128 substrate extension on Iberian Bombus (full GLMM refit at native DestinE Climate DT pixelisation)
```

### Study type (dropdown, required)

- [ ] Reproduction Study — direct reproduction: same methodology, same tools.
- [x] **Replication Study** — replication with different methodology or conditions.
- [ ] Reproduction/Replication Study — both.

This is a methodological replication: same GLMM specification and same climate inputs as the canonical sibling, but at a finer spatial substrate (HEALPix nside=128 ~46 km cells vs the canonical nside=64 ~92 km / Soroye's CEA ~100 km).

### Search for a FORRT claim (search/select, required)

URI of the Claim published in step 03. Pull from `nanopubs/PUBLISHED.md`.

```
<replace-with-published-Claim-URI-from-step-03>
```

### Describe what part of the claim is reproduced/replicated (textarea, required)

The **scope** of the claim being tested. Which aspect, what's in/out of scope. NOT methodology. NOT results. See `docs/pico-study-outcome-levels.md`.

```
SCOPE: the GLMM coefficient on standardised TEI_delta at HEALPix nside=128 (the native pixelisation of DestinE Climate DT IFS-NEMO standard), Iberian Bombus only.

IN SCOPE
  - Soroye 2020's GLMM specification (identical to the canonical nside=64 sibling).
  - Soroye 2020's CRU TS 3.24.01 climate inputs (identical, kept unchanged).
  - HEALPix-NESTED nside=128 on the WGS84 ellipsoid (~46 km cells; the native DestinE Climate DT pixelisation).
  - Tier 1 historical fit on the 1901–1974 baseline period and 2000–2014 recent period.
  - Tier 2 SSP3-7.0 future projection at substrate-matched nside=128 (no parent-aggregation deviation between fit and projection grids).

OUT OF SCOPE for this Replication Study (handled by separate chains)
  - The canonical CEA + nside=64 substrate-comparison at coarser resolution — see weatherxbiodiversity-projection.
  - Cross-substrate methodological diagnostic — see weatherxbiodiversity-substrate-sensitivity.
  - Bombus species outside the Iberian peninsula.
```

### Describe how the claim is reproduced/replicated (textarea, required)

The **method** in plain prose. Read `notebooks/03_analysis.py` and any config files first. NOT exact numerical results.

```
METHOD

The methodology mirrors the canonical nside=64 sibling exactly except for the spatial substrate. Cell coverage and per-species niche limits are computed on HEALPix-NESTED nside=128 cells of the WGS84 ellipsoid (using the healpix-geo Python library); per-species niche limits and the GLMM are refit at this substrate.

GLMM specification (identical to Soroye 2020 and to the canonical sibling):
    extinction ~ continent + sc_sampling + sc_TEI_bs + sc_TEI_delta + sc_TEI_bs:sc_TEI_delta + sc_PEI_bs + sc_PEI_delta + sc_PEI_bs:sc_PEI_delta + sc_TEI_bs:sc_PEI_bs + sc_TEI_delta:sc_PEI_delta + (1|species)

Inference: variational-Bayes via statsmodels.BinomialBayesMixedGLM (fast first pass) and full-posterior NUTS via bambi/PyMC, 4 chains × 2000 samples (authoritative HDIs).

Tier 2 — SSP3-7.0 future projection. DestinE Climate DT IFS-NEMO standard SSP3-7.0 GRIB files retrieved via polytope on LUMI for the 2020–2029 and 2030–2039 horizons, decoded with eccodes (Python API, NESTED-aware), subset to pre-computed Iberian HEALPix nside=128 cells. The future-period TEI_delta and PEI_delta are computed on the SAME substrate the GLMM was fit on (no cross-substrate aggregation step). Per-species ranking is reported following the protocol established in the methodological sibling chain (n_cells ≥ 10, main-effects-only η at projection time).

Code: notebooks/01_data_download.py, notebooks/02h_data_clean_healpix.py, notebooks/03h_analysis_healpix.py, notebooks/04h_figures_healpix.py, notebooks/05_destine_download.py, notebooks/06_destine_clean.py, notebooks/07_projection.py, notebooks/08_projection_figures.py.
```

### Describe any deviations from original methodology (textarea, optional)

What's different from the original method. Verify against the actual code, don't guess.

```
1. Pixelisation. Soroye 2020 fit at the CEA grid (~100 km, equal-area cylindrical). This Study fits at HEALPix-NESTED nside=128 on the WGS84 ellipsoid (~46 km). Cell area is ~4× smaller than Soroye's; cell shape and topology differ. This is the SAME deviation kind as the canonical nside=64 sibling, just at a finer resolution.

2. Region. Iberian peninsula only — same as the canonical sibling.

3. Inference engine. Two independent Python implementations (statsmodels VB, bambi/PyMC NUTS) — same as the canonical sibling.

4. Prior choices. Bambi defaults (Half-StudentT on group SDs) rather than Soroye's MCMCglmm informative inverse-Wishart — same deviation as the canonical sibling.

5. Climate inputs. Soroye's bundled CRU TS 3.24.01 from his Figshare deposit, used unchanged — NOT a deviation.

6. Tier 2 projection grid alignment. Unlike the canonical nside=64 sibling, this Study fits AND projects at the same native HEALPix nside=128 substrate — no parent-cell aggregation between fit and projection grids. This eliminates one source of cross-substrate aggregation noise but introduces a finer-grained per-cell extrapolation tail (more cells lie far outside the training distribution per species).
```

### Search keywords (Wikidata) (multi-select, optional)

Provide labels (not QIDs) — the Wikidata search picks up labels.

- bumblebee
- climate change
- generalized linear mixed model
- HEALPix
- species distribution model
- Iberian Peninsula
- replication study
- DestinE Climate DT

### Search discipline (Wikidata) (search, optional)

Provide labels.

- macroecology
- biogeography
- conservation biology

### Search discipline (Wikidata) (search, optional)

Provide labels.

- _Discipline label: ___

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 04.
