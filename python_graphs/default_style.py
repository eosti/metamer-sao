from cycler import cycler

geometry_short = 1
geometry_long = 5

colour_cycle = [
    "#F44336",
    "#9C27B0",
    "#3F51B5",
    "#03A9F4",
    "#009688",
    "#8BC34A",
    "#FFEB3B",
    "#FF9800",
    "#795548",
    "#607D8B",
]

plotting_kwargs = {
    "show": False,
    "transparent_background": True,
    "tight_layout": True,
    # Figure size
    "figure.figsize": (12.80, 7.20),
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "standard",
    # Font settings
    "font.family": "Atkinson Hyperlegible Next",
    "text.color": "white",
    "grid.color": "AAAAAA",
    "lines.color": "white",
    "axes.titlesize": 30,
    "axes.labelsize": 30,
    "axes.labelcolor": "white",
    "xtick.labelsize": 15,
    "ytick.labelsize": 15,
    "savefig.facecolor": "none",
    "axes.facecolor": "none",
    "axes.edgecolor": "white",
    # Ticks
    "xtick.top": False,
    "xtick.bottom": True,
    "ytick.right": False,
    "ytick.left": True,
    "xtick.minor.visible": True,
    "ytick.minor.visible": True,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.size": geometry_long * 1.25,
    "xtick.minor.size": geometry_long * 0.75,
    "ytick.major.size": geometry_long * 1.25,
    "ytick.minor.size": geometry_long * 0.75,
    "xtick.major.width": geometry_short,
    "xtick.minor.width": geometry_short,
    "ytick.major.width": geometry_short,
    "ytick.minor.width": geometry_short,
    "xtick.color": "CCCCCC",
    "ytick.color": "CCCCCC",
    # Markers
    # Legend
    "legend.facecolor": "black",
    "legend.frameon": True,
    "legend.framealpha": 0.5,
    "legend.fancybox": False,
    "legend.borderpad": geometry_short * 0.5,
    # Lines
    "lines.linewidth": 5,
    "lines.markersize": geometry_short * 3,
    "lines.markeredgewidth": geometry_short * 0.75,
    # Cycle
    "axes.prop_cycle": cycler(color=colour_cycle),
}
