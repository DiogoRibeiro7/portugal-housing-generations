"""Shared style of every release figure: colours and matplotlib settings. Importing this module applies them."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE, ORANGE, AQUA, INK, INK2, MUTED, GRID, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#0b0b0b", "#52514e", "#9a9993", "#e6e5e1", "#c9c8c2"

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9.5, "axes.edgecolor": MUTED, "axes.labelcolor": INK2,
    "axes.titlecolor": INK, "axes.titlesize": 10.5, "axes.titleweight": "bold", "axes.titlelocation": "left",
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "axes.axisbelow": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "legend.frameon": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.dpi": 170,
    # Set here, not left to a site-wide matplotlibrc: hinting changes how text is rasterised, so a different
    # default (matplotlib's own is "default") moves text pixels in every figure. The release figures use none.
    "text.hinting": "no_hinting",
})
