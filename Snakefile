# Snakefile — orchestrates the Option C HEALPix nside=128 substrate-robustness
# pipeline end-to-end + the Tier 2 (DestinE Climate DT future-climate
# projection) extension. The whole repo is the nside=128 branch -- there is no
# CEA reproduction here (that is the upstream weatherxbio v0.2.1 reference)
# and no nside=64 reproduction here (that is the sibling repo
# annefou/weatherxbiodiversity-projection at commit b7cdd47).
#
# Each rule converts the jupytext .py to .ipynb and executes it in place
# (per docs/cicd-conventions.md § jupyter execute --inplace) so the
# downstream MyST Jupyter Book build picks up cell outputs.
#
# Tier-2 rules wrap the four DestinE-projection notebooks. 05 is guarded
# by `_tier2_guard` (DestinE-platform only); 06/07/08 only need the GRIBs
# to be on disk. Tier-2 outputs are NOT in `rule all`; the user invokes
# `snakemake --cores 1 tier2` only when running on the DestinE platform
# OR when GRIBs have been transferred to a local Mac.
#
# Usage:
#   snakemake --cores 1                       # Tier 1 (default)
#   snakemake --cores 1 -n                    # dry run, Tier 1
#   snakemake --cores 1 figures/main_result_healpix.png
#   snakemake --cores 1 tier2                 # Tier 2 (DestinE)
#   snakemake --cores 1 tier2 -n              # dry run, Tier 2

NOTEBOOKS = "notebooks"
DATA = "data"
RESULTS = "results"
FIGURES = "figures"
HPORT = "healpix_port"


rule all:
    input:
        # HEALPix-NESTED nside=128 substrate-robustness pipeline (Option C)
        f"{FIGURES}/main_result_healpix.png",
        f"{RESULTS}/headline_statistic_healpix.json",


# ---------- 01: Data download ----------
# Self-contained: the GBIF Iberia download (DOI 10.15468/dl.3frmsq) and
# the Soroye Figshare deposit (DOI 10.6084/m9.figshare.9956471). No
# credentials needed -- both endpoints are publicly accessible.
rule data_download:
    output:
        f"{DATA}/gbif_dl/0006204-260423192947929.csv",
        f"{DATA}/gbif_bombus_iberia_metadata.json",
        directory("reference/Bumblebee_repo_wbombusdat/0_ClimateData"),
    log:
        f"{RESULTS}/logs/01_data_download.log",
    shell:
        "mkdir -p $(dirname {log}) && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 01_data_download.py && "
        "jupyter execute --inplace 01_data_download.ipynb 2>&1 | tee ../{log}"


# ---------- 02h: Data clean (HEALPix nside=128 substrate) ----------
# Wraps healpix_port/01_clean_data_iberia_healpix.py +
# 02_presence_absence_healpix.py + 03_sampling_continent_healpix.py +
# 04_climate_tei_pei_healpix.py.
rule data_clean_healpix:
    input:
        f"{DATA}/gbif_dl/0006204-260423192947929.csv",
        "reference/Bumblebee_repo_wbombusdat/0_ClimateData",
    output:
        f"{HPORT}/outputs_iberia/bombus_clean_healpix.csv",
        f"{HPORT}/outputs_iberia/presence_absence_healpix.nc",
        f"{HPORT}/outputs_iberia/sampling_continent_healpix.nc",
        f"{HPORT}/outputs_iberia/climate_tei_pei_healpix.nc",
    log:
        f"{RESULTS}/logs/02h_data_clean_healpix.log",
    shell:
        "mkdir -p $(dirname {log}) && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 02h_data_clean_healpix.py && "
        "jupyter execute --inplace 02h_data_clean_healpix.ipynb 2>&1 | tee ../{log}"


# ---------- 03h: Analysis (HEALPix nside=128 substrate) ----------
# Wraps healpix_port/05_regression_healpix.py +
# 05b_regression_statsmodels_healpix.py and writes the
# CEA-vs-nside64-vs-nside128 substrate-robustness JSON.
rule analysis_healpix:
    input:
        f"{HPORT}/outputs_iberia/presence_absence_healpix.nc",
        f"{HPORT}/outputs_iberia/sampling_continent_healpix.nc",
        f"{HPORT}/outputs_iberia/climate_tei_pei_healpix.nc",
    output:
        f"{RESULTS}/headline_statistic_healpix.json",
        f"{RESULTS}/glmm_coefficients_healpix.csv",
        f"{RESULTS}/posterior_bambi_healpix.nc",
        f"{HPORT}/outputs_iberia/posterior_vb_summary.csv",
        f"{HPORT}/outputs_iberia/dataGLMM_extinction.parquet",
    log:
        f"{RESULTS}/logs/03h_analysis_healpix.log",
    shell:
        "mkdir -p $(dirname {log}) && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 03h_analysis_healpix.py && "
        "jupyter execute --inplace 03h_analysis_healpix.ipynb 2>&1 | tee ../{log}"


# ---------- 04h: Figures (HEALPix nside=128 substrate) ----------
# Three-panel forest plot: weatherxbio v0.2.1 CEA published values
# (left, embedded inline) + annefou nside=64 published values (middle,
# embedded inline) + this run's HEALPix nside=128 fit (right). The
# `sc_TEI_delta` row is highlighted in gold; an Iberia HEALPix nside=128
# coverage map at the bottom shows cells included in the fit.
rule figures_healpix:
    input:
        f"{HPORT}/outputs_iberia/posterior_vb_summary.csv",
        f"{RESULTS}/headline_statistic_healpix.json",
    output:
        f"{FIGURES}/main_result_healpix.png",
    log:
        f"{RESULTS}/logs/04h_figures_healpix.log",
    shell:
        "mkdir -p $(dirname {log}) && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 04h_figures_healpix.py && "
        "jupyter execute --inplace 04h_figures_healpix.ipynb 2>&1 | tee ../{log}"


# =============================================================================
# Tier 2 — DestinE Climate DT projection (opt-in, DestinE platform only)
# =============================================================================
# Aggregate target: `snakemake --cores 1 tier2`. 05_destine_download self-skips
# when DestinE credentials are absent (see `notebooks/_tier2_guard.py`); 06/07/08
# only need the GRIBs to be on disk. This is the Option-C path: GLMM and
# projection both at nside=128, so β and σ scales match (no Option B fork).

DATA_DESTINE = f"{DATA}/destine"


rule tier2:
    input:
        f"{RESULTS}/projection_headline.json",
        f"{FIGURES}/projection_species_rank.png",
        f"{FIGURES}/projection_risk_map_2020_2029.png",
        f"{FIGURES}/projection_risk_map_2030_2039.png",
        f"{FIGURES}/projection_summary.png",


# ---------- 05: DestinE GRIB retrieve (DestinE platform only) ----------
# Polytope-only retrieve; writes raw global HEALPix-NESTED GRIBs to
# data/destine/raw/. No xarray decode here — the DestinE platform's
# eccodes HEALPix Geoiterator only supports RING ordering and fails on
# NESTED. After this step the user transfers the GRIBs to local Mac;
# 06 decodes locally with the eccodes Python API (no Geoiterator),
# subsets to the Iberian HEALPix-NESTED nside=128 cells.
rule destine_download:
    output:
        f"{DATA_DESTINE}/raw/destine_2020_2029_t2m.grib",
        f"{DATA_DESTINE}/raw/destine_2020_2029_tp.grib",
        f"{DATA_DESTINE}/raw/destine_2030_2039_t2m.grib",
        f"{DATA_DESTINE}/raw/destine_2030_2039_tp.grib",
    log:
        f"{RESULTS}/logs/05_destine_download.log",
    shell:
        "mkdir -p $(dirname {log}) && mkdir -p " + DATA_DESTINE + " && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 05_destine_download.py && "
        "jupyter execute --inplace 05_destine_download.ipynb 2>&1 | tee ../{log}"


# ---------- 06: DestinE clean ----------
# Recompute TEI / PEI per species under future-decade climate at the
# nside=128 substrate, holding species' historical niche limits fixed.
# No parent aggregation — substrate matches the GLMM.
rule destine_clean:
    input:
        f"{DATA_DESTINE}/raw/destine_2020_2029_t2m.grib",
        f"{DATA_DESTINE}/raw/destine_2020_2029_tp.grib",
        f"{DATA_DESTINE}/raw/destine_2030_2039_t2m.grib",
        f"{DATA_DESTINE}/raw/destine_2030_2039_tp.grib",
        f"{HPORT}/outputs_iberia/climate_tei_pei_healpix.nc",
        f"{HPORT}/outputs_iberia/sampling_continent_healpix.nc",
    output:
        f"{HPORT}/outputs_iberia/climate_tei_pei_future_2020_2029_healpix.nc",
        f"{HPORT}/outputs_iberia/climate_tei_pei_future_2030_2039_healpix.nc",
    log:
        f"{RESULTS}/logs/06_destine_clean.log",
    shell:
        "mkdir -p $(dirname {log}) && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 06_destine_clean.py && "
        "jupyter execute --inplace 06_destine_clean.ipynb 2>&1 | tee ../{log}"


# ---------- 07: Projection ----------
# Sample 1000 draws from the Tier-1 nside=128 bambi posterior, apply to
# nside=128 future TEI/PEI, write per-species posterior-mean η + 95% HDI
# to projection_headline.json and the per-cell community-mean η raster
# to results/projection_<horizon>.nc (gitignored).
rule projection:
    input:
        f"{RESULTS}/posterior_bambi_healpix.nc",
        f"{HPORT}/outputs_iberia/dataGLMM_extinction.parquet",
        f"{HPORT}/outputs_iberia/sampling_continent_healpix.nc",
        f"{HPORT}/outputs_iberia/presence_absence_healpix.nc",
        f"{HPORT}/outputs_iberia/climate_tei_pei_future_2020_2029_healpix.nc",
        f"{HPORT}/outputs_iberia/climate_tei_pei_future_2030_2039_healpix.nc",
    output:
        f"{RESULTS}/projection_headline.json",
        f"{RESULTS}/projection_2020_2029.nc",
        f"{RESULTS}/projection_2030_2039.nc",
    log:
        f"{RESULTS}/logs/07_projection.log",
    shell:
        "mkdir -p $(dirname {log}) && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 07_projection.py && "
        "jupyter execute --inplace 07_projection.ipynb 2>&1 | tee ../{log}"


# ---------- 08: Projection figures ----------
# Risk-rank chart (per horizon) + per-cell community-mean risk maps
# (LAEA Europe primary; Mollweide-vs-LAEA comparison panel).
rule projection_figures:
    input:
        f"{RESULTS}/projection_headline.json",
        f"{RESULTS}/projection_2020_2029.nc",
        f"{RESULTS}/projection_2030_2039.nc",
    output:
        f"{FIGURES}/projection_species_rank.png",
        f"{FIGURES}/projection_risk_map_2020_2029.png",
        f"{FIGURES}/projection_risk_map_2030_2039.png",
        f"{FIGURES}/projection_proj_comparison_2020_2029.png",
        f"{FIGURES}/projection_proj_comparison_2030_2039.png",
        f"{FIGURES}/projection_summary.png",
    log:
        f"{RESULTS}/logs/08_projection_figures.log",
    shell:
        "mkdir -p $(dirname {log}) && "
        "cd " + NOTEBOOKS + " && "
        "jupytext --to notebook 08_projection_figures.py && "
        "jupyter execute --inplace 08_projection_figures.ipynb 2>&1 | tee ../{log}"
