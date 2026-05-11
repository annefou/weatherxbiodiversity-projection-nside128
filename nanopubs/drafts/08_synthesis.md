# 08 — Research Synthesis (optional)

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> Use this template only when this chain is **one of several** testing facets of a shared underlying property. The Synthesis names the cross-cutting conclusion and lists the multiple Outcomes as supporting sources.

**Form heading:** *"Science Live Research Synthesis — Synthesise findings across multiple replication outcomes with conclusions, recommendations, conditions, and limitations."*

## Field-by-field draft

### Short URI suffix for synthesis ID (text input, required)

Slug. Use kebab-case.

```
soroye2020-iberian-bombus-tei-mechanism-substrate-robust-nside128-extension
```

### Label of the synthesis (text input, required)

A one-line summary.

```
HEALPix nside=128 substrate-extension confirms Soroye et al. 2020's TEI mechanism is substrate-robust on Iberian Bombus across three pixelisations
```

### Conclusion of the synthesis (textarea, required)

The aggregate finding across the underlying outcomes.

```
The Tier-1 GLMM coefficient on standardised TEI_delta from this chain (HEALPix nside=128, +0.347, 95% HDI [+0.139, +0.533]) combines with the canonical nside=64 sibling chain (+0.454, HDI [+0.130, +0.751]) and Soroye et al.'s original CEA fit (+0.479) into a three-substrate substrate-robustness check spanning ~46–100 km cell resolution. All three estimates are within ±30% of each other, sign-aligned, and order-of-magnitude consistent. Soroye's central biological claim — that thermal-niche exceedance increases extirpation probability — is substrate-robust on Iberian Bombus at the GLMM-fit step. The substrate-specific projection-step caveat (per-species ranking is grid-coupled for low-N species) is documented separately in the sibling chain weatherxbiodiversity-substrate-sensitivity.
```

### Recommendations (textarea, required)

Actionable guidance for practitioners.

```
1. When fitting TEI-style GLMMs at HEALPix substrates for use with DestinE Climate DT data, fit at the native nside=128 to eliminate parent-cell aggregation between fit and projection grids — but expect headline coefficients consistent (within ±30%) with coarser substrates such as nside=64 or CEA.

2. The factor-of-4 increase in cell count per area at nside=128 vs nside=64 brings more species across the n_cells ≥ 10 reliability threshold for projection-time reporting — favouring nside=128 as the reporting substrate when DestinE input data is available.

3. Cite both the canonical nside=64 sibling and this nside=128 extension when reporting substrate-robust Iberian Bombus TEI results, because the cross-substrate agreement IS the substrate-robustness evidence — neither chain alone is sufficient to claim substrate-robustness.

4. For per-species projection ranking under SSP3-7.0 at nside=128, apply the recommended protocol from weatherxbiodiversity-substrate-sensitivity (n_cells ≥ 10 + main-effects-only η at projection time).
```

### Conditions under which the synthesis applies (textarea, required)

Scope: data types, methods, domains, regions, time periods.

```
- Region: Iberian peninsula only.
- Species set: Bombus species observed in GBIF on the Iberian peninsula in 1901–2014.
- Climate forcing for fit: CRU TS 3.24.01 monthly temperature and precipitation, identical to Soroye et al. 2020.
- Spatial substrates synthesised: CEA (~100 km), HEALPix-NESTED nside=64 (~92 km), HEALPix-NESTED nside=128 (~46 km, this chain).
- GLMM specification: Soroye et al. 2020's full formula with main effects, four interaction terms, and per-species random intercept.
- Inference: full-posterior NUTS via bambi/PyMC; HDIs reported.
- Synthesis statement applies to the GLMM FIT step.
```

### Limitations of the synthesis (textarea, required)

What was not tested? What might not generalise?

```
1. Three substrates only. Substrate-robustness across coarser HEALPix levels or against non-HEALPix grids (EASE-Grid 2.0, S2) was not tested.

2. One region only. Same caveat as the canonical sibling chain — Iberian peninsula only.

3. One climate dataset (CRU TS 3.24.01). Climate-input robustness is not addressed by this synthesis.

4. Fit step only. The synthesis does NOT extend to projection-time substrate-robustness — that is qualified by the substrate-sensitivity sibling chain.

5. Substrate-extension is not a strict cross-validation. The substrate-robustness conclusion rests on Bayesian credibility-interval overlap and ±30% magnitude agreement, not on an out-of-sample predictive comparison.
```

### Completion date (date picker, required)

```
2026-05-11
```

### Supporting sources (repeatable group, required ≥1)

Each entry is a URL — typically the FORRT Outcome URIs being synthesised. Pull from `nanopubs/PUBLISHED.md` (and/or registries from sibling repos).

- This chain's Outcome (step 05): `<replace-with-published-Outcome-URI-from-step-05>`
- Sibling canonical nside=64 chain's Outcome: `<replace-with-nside64-sibling-Outcome-URI>` (or, before publication: https://doi.org/10.5281/zenodo.20113777)
- Sibling substrate-sensitivity chain's Outcome: `<replace-with-substrate-sensitivity-Outcome-URI>` (or, before publication: https://doi.org/10.5281/zenodo.20113786)
- Soroye, Newbold & Kerr (2020): https://doi.org/10.1126/science.aax8591

### Search topics (Wikidata) (multi-select, optional)

Provide labels (not QIDs).

- bumblebee
- climate change
- species distribution model
- generalized linear mixed model
- HEALPix
- replication
- DestinE Climate DT
- Iberian Peninsula

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 08.
