# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 02h — Data clean (HEALPix-NESTED nside=128 substrate)
#
# **Option C — full GLMM refit at HEALPix nside=128.** This notebook is
# a thin orchestration wrapper around the four cleaning + indexing
# scripts in `healpix_port/`, fitting the Soroye-2020 mechanism on the
# **HEALPix nside=128 NESTED** substrate (~46 km cells, ~16x finer in
# area than the reference repo's nside=64 fit).
#
# Per `DOMAIN.md`, HEALPix indexing is **always NESTED** (hierarchical
# bit-shift refinement: parent = `pix >> 2`, children = `(pix << 2) | k`).
# We use **`healpix-geo`**, not `healpy`, because healpy's
# cosmology-first lon convention (0-360) and absent CRS handling
# accumulate small biases that are unacceptable for biodiversity-precision
# climate-impact work over Iberia.
#
# **Cross-substrate frame**: this repo is the nside=128 sibling of
# `annefou/weatherxbiodiversity-projection` (commit `b7cdd47`), which
# runs the same pipeline at nside=64. The headline question for THIS
# repo is whether the substrate-robustness verdict (sc_TEI_delta within
# +-30% of weatherxbio v0.2.1's CEA value of +0.479) still holds at
# this finer scale.
#
# Scripts run in order:
#
# 1. `01_clean_data_iberia_healpix.py` — clean GBIF Iberia + Kerr 2015
#    species filter + HEALPix nside=128 cell assignment.
# 2. `02_presence_absence_healpix.py` — per-(species x cell x period_season)
#    presence/absence on the flat Iberia HEALPix cell list (440 cells
#    from `data/precomputed/iberia_pix_nside128_nested.npy`).
# 3. `03_sampling_continent_healpix.py` — per-cell sampling-effort
#    raster (distinct LYIDs) + continent code (constant 2 / Europe).
# 4. `04_climate_tei_pei_healpix.py` — bilinear-sample CRU TS 3.24.01
#    at HEALPix cell centres + compute TEI / PEI per species per cell
#    per period. **Per-species niche limits derived from nside=128
#    baseline-occupied cells** (Option C — not species-level inheritance
#    from nside=64).

# %%
import os
import subprocess
import sys
from pathlib import Path

# %%
ROOT = Path("..").resolve()
PORT = ROOT / "healpix_port"
OUT_DIR = PORT / "outputs_iberia"

env = {**os.environ}


def run(script: str) -> None:
    print(f"\n=== {script} ===", flush=True)
    subprocess.run(
        [sys.executable, script],
        cwd=PORT,
        env=env,
        check=True,
    )


# %% [markdown]
# ## Run the four upstream cleaning + indexing scripts (HEALPix substrate)

# %%
run("01_clean_data_iberia_healpix.py")
run("02_presence_absence_healpix.py")
run("03_sampling_continent_healpix.py")
run("04_climate_tei_pei_healpix.py")

# %% [markdown]
# ## Summary of intermediate artefacts produced

# %%
expected = [
    OUT_DIR / "bombus_clean_healpix.csv",
    OUT_DIR / "presence_absence_healpix.nc",
    OUT_DIR / "sampling_continent_healpix.nc",
    OUT_DIR / "climate_tei_pei_healpix.nc",
]
print("\nIntermediate artefacts (HEALPix nside=128 NESTED):")
for p in expected:
    if p.exists():
        size = p.stat().st_size
        print(f"  ok    {p.relative_to(ROOT)}  ({size:,} bytes)")
    else:
        print(f"  MISS  {p.relative_to(ROOT)}")

# %%
import pandas as pd  # noqa: E402

import xarray as xr  # noqa: E402

clean_csv = OUT_DIR / "bombus_clean_healpix.csv"
if clean_csv.exists():
    df = pd.read_csv(clean_csv)
    print(f"\nbombus_clean_healpix.csv -> {len(df):,} rows, "
          f"{df['species'].nunique()} species")
    print(f"  HEALPix cells with at least one occurrence: "
          f"{df['cell_id_hp'].nunique()}")
    print(f"  periods present: {sorted(df['period'].dropna().unique().tolist())}")
    print(f"  seasons present: {sorted(df['season'].dropna().unique().tolist())}")

pa_nc = OUT_DIR / "presence_absence_healpix.nc"
if pa_nc.exists():
    pa = xr.open_dataset(pa_nc)
    depth = pa.attrs['dggs_grid_refinement_level']
    print(
        f"\nIberia HEALPix substrate: {int(pa.sizes['cells'])} cells "
        f"(nside={2**depth}, depth={depth}, "
        f"scheme={pa.attrs['dggs_grid_indexing_scheme']!r})"
    )
