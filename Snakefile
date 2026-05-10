# Snakefile — orchestrates the Option C HEALPix nside=128 substrate-robustness
# pipeline end-to-end. The whole repo is the nside=128 branch -- there is no
# CEA reproduction here (that is the upstream weatherxbio v0.2.1 reference)
# and no nside=64 reproduction here (that is the sibling repo
# annefou/weatherxbiodiversity-projection at commit b7cdd47).
#
# Each rule converts the jupytext .py to .ipynb and executes it in place
# (per docs/cicd-conventions.md § jupyter execute --inplace) so the
# downstream MyST Jupyter Book build picks up cell outputs.
#
# Usage:
#   snakemake --cores 1                       # full pipeline
#   snakemake --cores 1 -n                    # dry run
#   snakemake --cores 1 figures/main_result_healpix.png

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
