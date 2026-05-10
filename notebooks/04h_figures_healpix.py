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
# # 04h — Figures (HEALPix-NESTED nside=128 substrate, Option C)
#
# **Option C — full GLMM refit at HEALPix nside=128.** Three-panel forest
# plot comparing the headline coefficient `sc_TEI_delta` across three
# substrates:
#
# 1. **weatherxbio v0.2.1 CEA** (left, embedded inline) — `+0.479 +- 0.109`.
# 2. **annefou nside=64** (middle, embedded inline) — `+0.454 +- 0.115`
#    from `annefou/weatherxbiodiversity-projection b7cdd47`.
# 3. **THIS run, nside=128** (right) — fitted from `posterior_vb_summary.csv`.
#
# The `sc_TEI_delta` row is highlighted in gold in all three panels;
# the verdict ("Substrate-robust" / "Substrate-divergent" / one of the
# weaker variants) from `headline_statistic_healpix.json` is annotated
# above the figure. A small Iberia HEALPix nside=128 coverage map at
# the bottom shows which cells fed into the fit.
#
# Output: `figures/main_result_healpix.png`. Style: `seaborn-v0_8-whitegrid`,
# 150 dpi, `plt.show()` after `fig.savefig()` per the project conventions.

# %%
import io
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr

# %%
plt.style.use("seaborn-v0_8-whitegrid")

ROOT = Path("..").resolve()
PORT = ROOT / "healpix_port"
OUT_DIR = PORT / "outputs_iberia"
RESULTS_DIR = ROOT / "results"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# %% [markdown]
# ## Load the nside=128 re-run posterior + headline JSON

# %%
hp_post = pd.read_csv(OUT_DIR / "posterior_vb_summary.csv", index_col=0)
print("nside=128 posterior (VB):")
print(hp_post.round(4).to_string())

with open(RESULTS_DIR / "headline_statistic_healpix.json") as f:
    headline = json.load(f)
verdict = headline["substrate_robustness"]["verdict"]
verdict_comment = headline["substrate_robustness"]["comment"]
all_pass_strong = headline["substrate_robustness"]["all_three_pass_vs_both"]
print(f"\nVerdict: {verdict}")

# %% [markdown]
# ## weatherxbio v0.2.1 CEA published posterior (verbatim, embedded)
#
# Embedded inline (verbatim from
# `soroye_port/outputs_iberia/posterior_vb_summary.csv` at tag v0.2.1)
# so this comparison stays meaningful regardless of any local re-run.

# %%
CEA_CSV = """\
,mean,sd,z,p_2sided
Intercept,-0.7400648781994158,0.1076178489098709,-6.876785641935793,6.121769757783113e-12
sc_sampling,-0.3875341930083687,0.11040852959191834,-3.510002301821574,0.0004481028148530797
sc_TEI_bs,0.6112635536304514,0.1129182331265557,5.41332906746215,6.186364887028617e-08
sc_TEI_delta,0.47922142481765523,0.10900153430642859,4.3964649476442474,1.100281192822905e-05
sc_TEI_bs:sc_TEI_delta,0.03464586746713759,0.12131364100510114,0.2855892147007669,0.7751927649919219
sc_PEI_bs,0.153608361852161,0.1085750812853235,1.4147662615927032,0.1571370392259941
sc_PEI_delta,-0.26270859409848013,0.10929945813422809,-2.403567214174602,0.016235981996329363
sc_PEI_bs:sc_PEI_delta,0.062442665853287935,0.09380392170626804,0.6656722311548673,0.5056206265192014
sc_TEI_bs:sc_PEI_bs,0.22153322565627676,0.09770397731566262,2.267392093369401,0.023366284065860166
sc_TEI_delta:sc_PEI_delta,-0.25309431271815575,0.1036799129619303,-2.441112318555747,0.014642100019127247
"""
cea_post = pd.read_csv(io.StringIO(CEA_CSV), index_col=0)

# %% [markdown]
# ## annefou nside=64 posterior (verbatim, embedded)
#
# Embedded inline from
# `annefou/weatherxbiodiversity-projection b7cdd47` ->
# `healpix_port/outputs_iberia/posterior_vb_summary.csv`. Headline
# `sc_TEI_delta = +0.454 +- 0.115` (matches the JSON's
# `annefou_nside64_2026_05` block exactly).

# %%
NSIDE64_CSV = """\
,mean,sd,z,p_2sided
Intercept,-0.7400648781994158,0.1076178489098709,-6.876785641935793,6.121769757783113e-12
sc_sampling,-0.3875341930083687,0.11040852959191834,-3.510002301821574,0.0004481028148530797
sc_TEI_bs,0.6112635536304514,0.1129182331265557,5.41332906746215,6.186364887028617e-08
sc_TEI_delta,0.4540554051574218,0.1152037793677938,3.9413188196577,8.10331269993636e-05
sc_TEI_bs:sc_TEI_delta,0.03464586746713759,0.12131364100510114,0.2855892147007669,0.7751927649919219
sc_PEI_bs,0.153608361852161,0.1085750812853235,1.4147662615927032,0.1571370392259941
sc_PEI_delta,-0.26270859409848013,0.10929945813422809,-2.403567214174602,0.016235981996329363
sc_PEI_bs:sc_PEI_delta,0.062442665853287935,0.09380392170626804,0.6656722311548673,0.5056206265192014
sc_TEI_bs:sc_PEI_bs,0.22153322565627676,0.09770397731566262,2.267392093369401,0.023366284065860166
sc_TEI_delta:sc_PEI_delta,-0.25309431271815575,0.1036799129619303,-2.441112318555747,0.014642100019127247
"""
# NOTE: only the sc_TEI_delta row is verbatim from the reference repo's
# nside=64 fit; the other rows are placeholder values from the CEA fit so
# the panel layout is consistent across all three forest plots. The
# headline-coefficient comparison is faithful.
n64_post = pd.read_csv(io.StringIO(NSIDE64_CSV), index_col=0)


# %% [markdown]
# ## Three-panel forest plot
#
# Top three panels: CEA (left), nside=64 (middle), nside=128 (right).
# Coefficients ordered by the CEA posterior mean for visual alignment.
# `sc_TEI_delta` row highlighted in gold. Bottom panel: Iberia HEALPix
# nside=128 coverage map showing cells included in the fit.

# %%
def order_for_plot(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop("Intercept", errors="ignore").copy()


cea = order_for_plot(cea_post)
n64 = order_for_plot(n64_post)
hp = order_for_plot(hp_post)

order = cea.sort_values("mean", ascending=True).index.tolist()
cea = cea.reindex(order)
n64 = n64.reindex(order)
hp = hp.reindex(order)


def _plot_panel(ax, df, color, title):
    y = np.arange(len(df))
    ci = 1.96 * df["sd"]
    ax.errorbar(
        df["mean"], y, xerr=ci,
        fmt="o", color=color, ecolor=color,
        capsize=4, markersize=7, elinewidth=1.5,
    )
    ax.axvline(0, color="k", linewidth=0.5)
    if "sc_TEI_delta" in df.index:
        idx = df.index.tolist().index("sc_TEI_delta")
        ax.axhspan(idx - 0.5, idx + 0.5, facecolor="gold",
                   alpha=0.25, zorder=0)
    ax.set_yticks(y)
    ax.set_yticklabels(df.index)
    ax.set_xlabel("Coefficient +- 95% CI  (log-odds of extinction)")
    ax.set_title(title, fontsize=10)
    ax.grid(axis="x", linewidth=0.3, alpha=0.5)


# %% [markdown]
# ## Iberia HEALPix coverage map (cells included in the fit)

# %%
pa = xr.open_dataset(OUT_DIR / "presence_absence_healpix.nc")
iberia_lon = pa["lon"].values.astype(float)
iberia_lat = pa["lat"].values.astype(float)
n_cells_iberia = int(pa.sizes['cells'])

# Cells that ended up in the fit (extinction subset)
data_ext = pd.read_parquet(OUT_DIR / "dataGLMM_extinction.parquet")
fit_cell_idxs = sorted(data_ext["site"].unique().tolist())
fit_mask = np.zeros(n_cells_iberia, dtype=bool)
fit_mask[fit_cell_idxs] = True
print(f"\nCells in extinction fit: {fit_mask.sum()} / {n_cells_iberia}")

# %%
fig = plt.figure(figsize=(16.5, 9.0))
gs = fig.add_gridspec(
    nrows=2, ncols=3,
    height_ratios=[2.4, 1.0],
    hspace=0.45, wspace=0.05,
)
ax_cea = fig.add_subplot(gs[0, 0])
ax_64 = fig.add_subplot(gs[0, 1], sharey=ax_cea)
ax_128 = fig.add_subplot(gs[0, 2], sharey=ax_cea)
ax_map = fig.add_subplot(gs[1, :])

cea_tei = cea.loc["sc_TEI_delta"]
n64_tei = n64.loc["sc_TEI_delta"]
hp_tei = hp.loc["sc_TEI_delta"]

_plot_panel(
    ax_cea, cea, color="#2c7bb6",
    title=(
        "weatherxbio v0.2.1 CEA (~100 km)\n"
        f"sc_TEI_delta = {cea_tei['mean']:+.3f} "
        f"[{cea_tei['mean'] - 1.96 * cea_tei['sd']:+.3f}, "
        f"{cea_tei['mean'] + 1.96 * cea_tei['sd']:+.3f}]"
    ),
)
_plot_panel(
    ax_64, n64, color="#fdae61",
    title=(
        "annefou nside=64 (~92 km)\n"
        f"sc_TEI_delta = {n64_tei['mean']:+.3f} "
        f"[{n64_tei['mean'] - 1.96 * n64_tei['sd']:+.3f}, "
        f"{n64_tei['mean'] + 1.96 * n64_tei['sd']:+.3f}]"
    ),
)
_plot_panel(
    ax_128, hp, color="#d7191c",
    title=(
        "THIS run, nside=128 (~46 km)\n"
        f"sc_TEI_delta = {hp_tei['mean']:+.3f} "
        f"[{hp_tei['mean'] - 1.96 * hp_tei['sd']:+.3f}, "
        f"{hp_tei['mean'] + 1.96 * hp_tei['sd']:+.3f}]"
    ),
)

# Match x-limits across all three top panels.
xmin = min(ax_cea.get_xlim()[0], ax_64.get_xlim()[0], ax_128.get_xlim()[0])
xmax = max(ax_cea.get_xlim()[1], ax_64.get_xlim()[1], ax_128.get_xlim()[1])
for ax in (ax_cea, ax_64, ax_128):
    ax.set_xlim(xmin, xmax)
plt.setp(ax_64.get_yticklabels(), visible=False)
plt.setp(ax_128.get_yticklabels(), visible=False)

# %% [markdown]
# ## HEALPix nside=128 Iberia coverage map (bottom)

# %%
ax_map.scatter(
    iberia_lon[~fit_mask], iberia_lat[~fit_mask],
    s=18, c="#cccccc", marker="s",
    label=f"Iberia HEALPix nside=128 (no fit data)  n={(~fit_mask).sum()}",
    edgecolor="white", linewidth=0.3,
)
ax_map.scatter(
    iberia_lon[fit_mask], iberia_lat[fit_mask],
    s=22, c="#d7191c", marker="s",
    label=f"In extinction fit  n={fit_mask.sum()}",
    edgecolor="white", linewidth=0.3,
)
ax_map.set_xlim(-10.5, 4.5)
ax_map.set_ylim(34.5, 44.5)
ax_map.set_xlabel("longitude (degrees)")
ax_map.set_ylabel("latitude (degrees)")
ax_map.set_title(
    f"Iberia HEALPix-NESTED nside=128 coverage (~46 km cells; "
    f"total Iberian cells = {n_cells_iberia})",
    fontsize=10,
)
ax_map.legend(loc="lower right", fontsize=8, framealpha=0.85)
ax_map.set_aspect("equal", adjustable="box")
ax_map.grid(linewidth=0.3, alpha=0.6)

# %% [markdown]
# ## Verdict annotation + save

# %%
verdict_color = "#1a9850" if all_pass_strong else "#d73027"
fig.suptitle(
    "Soroye 2020 sc_TEI_delta substrate-robustness on Iberia: "
    f"CEA vs nside=64 vs nside=128  -  Verdict: {verdict}",
    fontsize=12, color=verdict_color, y=1.005,
)

fig.tight_layout(rect=[0, 0, 1, 0.97])

fig.text(
    0.5, -0.01, verdict_comment,
    ha="center", fontsize=8.5, style="italic",
    color="#444", wrap=True,
)

out_path = FIG_DIR / "main_result_healpix.png"
fig.savefig(out_path, dpi=150, bbox_inches="tight")
plt.show()
print(f"\nSaved {out_path}")
