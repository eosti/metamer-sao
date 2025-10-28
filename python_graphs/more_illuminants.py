import colour
import matplotlib.pyplot as plt
from fruit_dataset import apple_spectra
from default_style import plotting_kwargs
from cycler import cycler

sao = colour.sd_multi_leds(
    [655, 620, 611, 591, 573, 560, 518, 505, 496, 470, 465, 405],
    half_spectral_widths=[20, 20, 17, 15, 15, 17, 17, 12, 12, 12, 12, 13],
    peak_power_ratios=[100, 110, 90, 100, 30, 4, 600, 120, 85, 100, 100, 50],
)
sao.display_name = "SAO 12-Color Illuminant"

colour.plotting.plot_single_sd(sao, filename="sao_illuminant.png", **plotting_kwargs)

ones = colour.sd_ones().trim(colour.SpectralShape(350, 780, 1))
colour.plotting.plot_single_sd(
    ones,
    filename="visible_spectrum.png",
    title="The Visible Spectrum",
    **plotting_kwargs
)
colour.plotting.plot_single_sd(
    ones,
    filename="visible_spectrum_noclip.png",
    title="The Visible Spectrum (in RGB)",
    out_of_gamut_clipping=False,
    **plotting_kwargs
)

colour_cycle = ["red", "green", "blue", "lime", "cyan", "orange", "darkred", "indigo"]

plotting_kwargs.update({"axes.prop_cycle": cycler(color=colour_cycle)})

red = colour.sd_single_led(616, half_spectral_width=20).normalise(1.3)
red.display_name = "616nm Red"
green = colour.sd_single_led(520, half_spectral_width=30)
green.display_name = "520nm Green"
blue = colour.sd_single_led(465, half_spectral_width=20)
blue.display_name = "465nm Blue"
lime = colour.sd_single_led(
    560, half_spectral_width=80, display_name="580nm Lime"
).normalise(0.7)
cyan = colour.sd_single_led(
    490, half_spectral_width=30, display_name="490nm Cyan"
).normalise(0.7)
amber = colour.sd_single_led(
    590, half_spectral_width=80, display_name="590nm Amber"
).normalise(0.5)
deep_red = colour.sd_single_led(
    660, half_spectral_width=20, display_name="660nm Deep Red"
).normalise(1)
violet = colour.sd_single_led(
    440, half_spectral_width=20, display_name="440nm Indigo"
).normalise(1)

rgb_sum = red + green + blue
rgb_sum.display_name = "RGB"
fig, ax = colour.plotting.plot_single_sd(
    rgb_sum, use_sd_colours=False, **plotting_kwargs
)
colour.plotting.plot_multi_sds(
    [red, green, blue],
    filename="build_rgb.png",
    axes=ax,
    bounding_box=(350, 780, 0, 2),
    **plotting_kwargs
)

fig, ax = colour.plotting.plot_single_sd(
    rgb_sum + lime, use_sd_colours=False, **plotting_kwargs
)
colour.plotting.plot_multi_sds(
    [red, green, blue, lime],
    filename="build_lime.png",
    axes=ax,
    bounding_box=(350, 780, 0, 2),
    title="RGB + Lime",
    **plotting_kwargs
)

fig, ax = colour.plotting.plot_single_sd(
    rgb_sum + lime + cyan, use_sd_colours=False, **plotting_kwargs
)
colour.plotting.plot_multi_sds(
    [red, green, blue, lime, cyan],
    filename="build_cyan.png",
    axes=ax,
    bounding_box=(350, 780, 0, 2),
    title="RGB + Lime + Cyan",
    **plotting_kwargs
)

fig, ax = colour.plotting.plot_single_sd(
    rgb_sum + lime + cyan + amber, use_sd_colours=False, **plotting_kwargs
)
colour.plotting.plot_multi_sds(
    [red, green, blue, lime, cyan, amber],
    filename="build_amber.png",
    axes=ax,
    bounding_box=(350, 780, 0, 2),
    title="RGB + Lime + Cyan + Amber",
    **plotting_kwargs
)

fig, ax = colour.plotting.plot_single_sd(
    rgb_sum + lime + cyan + amber + deep_red + violet,
    use_sd_colours=False,
    **plotting_kwargs
)
colour.plotting.plot_multi_sds(
    [red, green, blue, lime, cyan, amber, deep_red, violet],
    filename="build_final.png",
    axes=ax,
    bounding_box=(350, 780, 0, 2),
    **plotting_kwargs,
    title="RGB + Lime + Cyan + Amber + Deep Red + Indigo"
)

plotting_kwargs.update(
    {"figure.figsize": (12.8, 12.8), "bounding_box": (-0.1, 0.9, -0.1, 0.9)}
)
colour.plotting.diagrams.plot_sds_in_chromaticity_diagram(
    [red, green, blue, lime, cyan, amber, deep_red, violet],
    filename="build_cie1931.png",
    title="8-Emitter Array",
    annotate_kwargs={"annotate": False},
    **plotting_kwargs
)
