import colour
import matplotlib.pyplot as plt
from default_style import plotting_kwargs

plotting_kwargs.update(
    {"figure.figsize": (12.8, 12.8), "bounding_box": (-0.1, 0.9, -0.1, 0.9)}
)
colour.plotting.plot_chromaticity_diagram_CIE1931(
    filename="cie1931_plot.png", **plotting_kwargs
)
colour.plotting.plot_RGB_colourspaces_in_chromaticity_diagram_CIE1931(
    ["sRGB", "ITU-R BT.2020", "Display P3"],
    filename="cie1931_gamut.png",
    **plotting_kwargs
)

ideal_green_sd = colour.sd_single_led(555, half_spectral_width=30)
ideal_red_sd = colour.sd_single_led(655, half_spectral_width=30)
ideal_blue_sd = colour.sd_single_led(455, half_spectral_width=30)

ideal_sd_data = list(
    zip(ideal_red_sd.values, ideal_green_sd.values, ideal_blue_sd.values)
)
labels = ["Optimal Red LED", "Optimal Green LED", "Optimal Blue LED"]
ideal_led_sd = colour.MultiSpectralDistributions(
    ideal_sd_data,
    ideal_green_sd.wavelengths,
    labels=labels,
    annotate=False,
    display_name="Optimal LED wavelengths",
)

colour.plotting.plot_sds_in_chromaticity_diagram_CIE1931(
    [ideal_led_sd], filename="cie1931_rgb_points.png", **plotting_kwargs
)
