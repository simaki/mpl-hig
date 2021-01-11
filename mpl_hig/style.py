import matplotlib
import seaborn

from . import hig


def set(style=None) -> None:
    """
    Set style.

    Parameters
    ----------
    - style : dict, None, or one of {darkgrid, whitegrid, dark, white, ticks}
        A dictionary of parameters or the name of a preconfigured set.
    """
    style = seaborn.axes_style(style)

    style["axes.edgecolor"] = hig.GRAY
    style["axes.linewidth"] = 1.6
    style["axes.prop_cycle"] = hig.cycle
    style["figure.dpi"] = 300
    style["grid.color"] = hig.GRAY
    style["legend.edgecolor"] = hig.GRAY
    style["savefig.bbox"] = "tight"
    style["savefig.pad_inches"] = 0.1

    matplotlib.rcParams.update(style)
