# 05 — FORRT Replication Outcome

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify the actual numerical results first** by reading `results/` and `notebooks/03_analysis.py`. Don't quote numbers from memory. See `docs/verify-before-drafting.md`.

## Field-by-field draft

### Short URI suffix for outcome ID (text input, required)

```
soroye2020-iberian-bombus-substrate-extension-nside128-validated
```

### Plain-text label for the outcome (text input, required)

```
Soroye et al. 2020 TEI-based extirpation mechanism: HEALPix nside=128 substrate extension on Iberian Bombus (full GLMM refit; SSP3-7.0 projection)
```

### Search for a FORRT replication study (search/select, required)

URI of the Replication Study published in step 04 of THIS chain. Pull from `nanopubs/PUBLISHED.md` after step 04 is live.

```
<replace-with-published-Study-URI-from-step-04>
```

### Repository URL (text input, required)

```
https://github.com/annefou/weatherxbiodiversity-projection-nside128
```

### Completion date (date picker, required)

```
2026-05-10
```

### Validation status (dropdown, required)

- [x] **Validated**
- [ ] PartiallySupported
- [ ] Contradicted

Maps to CiTO `confirms` in step 06. Refitting Soroye's GLMM at HEALPix nside=128 (~46 km, the native pixelisation of DestinE Climate DT IFS-NEMO standard) recovers a positive, large, credible coefficient on standardised TEI_delta — within ±30% of the original CEA replication and the nside=64 sibling, confirming the TEI mechanism is substrate-robust across three independent pixelisations.

### Confidence level (dropdown, required)

```
High
```

(Posterior 95% HDI on the headline coefficient excludes zero; same sign and order of magnitude as both the original CEA fit and the nside=64 sibling within ±30 percent; substrate-robustness is now confirmed across three independent pixelisations spanning ~46–100 km cell resolution.)

### Describe the overall conclusion about the original claim (textarea, required)

```
This repository extends the canonical Iberian Bombus replication (weatherxbiodiversity-projection at HEALPix nside=64) by refitting Soroye et al.'s (2020) GLMM at HEALPix nside=128 — the native pixelisation of DestinE Climate DT IFS-NEMO standard, with cells ~46 km across (4× finer than the canonical sibling).

The headline GLMM coefficient on standardised TEI_delta at nside=128 is +0.347 (95% HDI [+0.139, +0.533]) — positive, large, credibly above zero. Compared with the canonical CEA fit (+0.479) and the nside=64 sibling (+0.454), all three estimates are within ±30 percent, sign-aligned, and order-of-magnitude consistent. Soroye's central biological claim — that thermal-niche exceedance increases extirpation probability — replicates at three independent spatial substrates spanning ~46–100 km cell resolution.

The Tier-2 SSP3-7.0 projection (DestinE Climate DT, 2020–2029 + 2030–2039 horizons) at substrate-matched nside=128 shows the same drift-toward-niche-edge pattern as the nside=64 sibling: mean future TEI rises systematically across most species, but no species crosses TEI > 1 (Soroye's actual extirpation threshold) at any currently-occupied cell over the next 15 years. The 2030–2039 horizon is the early-warning period under SSP3-7.0, not the extirpation period itself.

Per-species ranking at this substrate is reported via the protocol established in the methodological sibling repo weatherxbiodiversity-substrate-sensitivity: filter to species with at least 10 occupied cells AND use main-effects-only η at projection time. At this filter, the cross-substrate Spearman correlation with the nside=64 sibling is +0.97 (mid-term horizon) — the per-species ranking IS substrate-stable for species above the cell-count threshold. The substrate-stable highest-risk Iberian species at nside=128 are B. humilis, B. muscorum, B. ruderarius (matching the nside=64 sibling's top 3); the lowest-risk are B. terrestris, B. pascuorum, B. pratorum.
```

### Describe the evidence that supports your conclusion (textarea, required)

```
TIER 1 — historical fit at HEALPix nside=128 (1901–2014 CRU TS 3.24.01 from Soroye Figshare; GBIF Iberian Bombus occurrences via own download DOI; full GLMM refit at native nside=128).

GLMM headline coefficient sc_TEI_delta:
  - HEALPix nside=128 (~46 km, this run): +0.347   (95% HDI [+0.139, +0.533])
  - HEALPix nside=64 (~92 km, sibling):   +0.454   (95% HDI [+0.130, +0.751])
  - CEA (~100 km, canonical):             +0.479
  All three within ±30 percent. Sign, magnitude, and HDI mutually consistent.

Verdict: substrate-robust across the three pixelisations.

Cross-fit sanity check at nside=128: variational-Bayes via statsmodels BinomialBayesMixedGLM reports +0.347 ± 0.079 (VB SD), consistent with the bambi/PyMC NUTS posterior to within VB-underestimation noise. See results/headline_statistic_healpix.json.

TIER 2 — SSP3-7.0 projection at substrate-matched nside=128 (DestinE Climate DT, IFS-NEMO standard, native HEALPix nside=128, 2020–2029 + 2030–2039 horizons; no parent-aggregation deviation between fit and projection grids).

Mean future TEI per species, 2030–2039 horizon (substrate-invariant physical metric, ρ_Spearman vs nside=64 sibling = +0.66 at n≥1, +0.90 at n≥10):
  - Most-shifted species (top of ranking): B. humilis, B. muscorum, B. ruderarius
  - Least-shifted (bottom of ranking): B. terrestris, B. pascuorum, B. pratorum
  - Same top-3 / bottom-3 as the nside=64 sibling's substrate-stable ranking.

Per-species community-mean η under SSP3-7.0 (filtered to n_cells≥10 at both substrates, main-effects-only η — ρ_Spearman vs nside=64 = +0.97 mid-term, +0.96 near-term).

Fraction of currently-occupied cells where future TEI exceeds 1.0 at 2030–2039: 0.00 for every studied species at nside=128 — same as the nside=64 sibling. The TEI > 1 threshold is not crossed under SSP3-7.0 over the next 15 years on Iberia.

Files: results/headline_statistic_healpix.json (Tier 1), results/projection_headline.json (Tier 2 per-species rank), results/posterior_bambi_healpix.nc (full nside=128 posterior); figures figures/main_result_healpix.png + figures/projection_summary.png.

Cross-substrate diagnostic: see weatherxbiodiversity-substrate-sensitivity (DOI to be minted) for the full five-variant Spearman concordance table, per-species η decomposition, and recommended reporting protocol.
```

### Describe what limits the conclusions of the study (textarea, optional)

```
1. Substrate-coupling at projection time. Per-species ranking under SSP3-7.0 is grid-coupled at the projection step for species observed in fewer than ~10 historical Iberian cells at this substrate (~46 km, nside=128). This affects narrowly-distributed Pyrenean specialists (B. pyrenaeus, B. mucidus, B. mendax, B. wurflenii, B. monticola, B. mesomelas) — precisely the species the public most worries about. The full mechanism, validated and refuted hypotheses, and recommended reporting protocol are documented in the methodological sibling repo weatherxbiodiversity-substrate-sensitivity. The rankings reported in this Outcome are filtered per that diagnostic (n_cells ≥ 10, main-effects-only η at projection time).

2. Reporting on η, not p_extirp. As in the nside=64 sibling, Tier-2 reports the GLMM linear predictor η rather than its logistic transform. Future predictors lie 2–4σ outside the Tier-1 training distribution at this substrate — wider than at nside=64 because per-cell future-period climate deltas have higher within-cell variance at the finer grid. Absolute extirpation probabilities derived from this projection are NOT interpretable as-is.

3. Negative-η species reflect random intercepts, not climate-driven benefit. The GLMM's species random effect dominates the projected η for B. terrestris and B. pascuorum, encoding lower-than-average historical extirpation susceptibility from the 1901–2014 GBIF training data. All climate-driven term contributions are positive for both species at both substrates. The correct reading is "historically robust species, with SSP3-7.0 adding moderate climate forcing on top" — NOT "projected to benefit from SSP3-7.0".

4. Sampling effort held at recent-period mean for the projection — same caveat as the nside=64 sibling.

5. DestinE Climate DT archive coverage. SSP3-7.0 IFS-NEMO archive populated through 2039 only at time of analysis; mid- and end-of-century horizons deferred.

6. Daily Tmax/Tmin from 4-times-daily 2t snapshots — same caveat as the nside=64 sibling. Defensible at decadal mean; biased high on Tmax extremes by an unknown but small amount.

7. tp 1-time-per-day approximation — same caveat as the nside=64 sibling.

8. Why nside=128 and not coarser-aggregated nside=64 at projection time. The canonical nside=64 sibling aggregates DestinE nside=128 data via parent-cell averaging before projection. This Outcome refits the GLMM at native nside=128 to eliminate any cross-substrate aggregation step between fit and projection. Both approaches yield substrate-robust headline coefficients within ±30%, but per-species rankings at the species-cell level differ (see substrate-sensitivity sibling for the exhaustive cross-substrate comparison).

9. Geographic scope. Iberian peninsula only. The same caveat as the nside=64 sibling applies.

10. n_cells distribution at nside=128. Because the cell area is 4× smaller than nside=64, the same physical species range generally translates to ~4× more occupied cells per species. This makes more species cross the n_cells ≥ 10 reliability threshold at nside=128 than at nside=64 (a positive side-effect of the resolution doubling), but the ranking concordance with the canonical nside=64 sibling is what bounds the trustworthy interpretation, not the per-substrate n_cells distribution alone.
```

> **Drafter notes — additional context for finalising this Outcome.**
>
> - This Outcome is for a **substrate-extension chain** that confirms the canonical replication. CiTO step 06 should `cito:confirms` Soroye 2020 (the original paper) AND `cito:extends` the canonical nside=64 sibling chain.
> - The substrate-sensitivity diagnostic chain (weatherxbiodiversity-substrate-sensitivity) is the upstream consumer of this Outcome and the canonical nside=64 sibling — those three Outcomes together form the cross-substrate evidence base.

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 05.
