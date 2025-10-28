import colour
import matplotlib.pyplot as plt
from default_style import plotting_kwargs

medium_cmf_spectra = colour.colorimetry.MSDS_CMFS_STANDARD_OBSERVER[
    "CIE 1931 2 Degree Standard Observer"
].to_sds()[1]

medium_cmf = colour.plotting.plot_single_sd(
    medium_cmf_spectra, title="", **plotting_kwargs
)
medium_cmf[1].set_ylabel("Probability")
plt.savefig("medium_cmf.png")

colour.plotting.plot_single_cmfs(
    "CIE 1931 2 Degree Standard Observer",
    title="",
    filename="cie1931_cmf.png",
    **plotting_kwargs
)

ideal_short_cmf = medium_cmf_spectra.copy()
ideal_long_cmf = medium_cmf_spectra.copy()
IDEAL_OFFSET = 100

w = ideal_short_cmf.wavelengths
w = [i - IDEAL_OFFSET for i in w]
ideal_short_cmf.wavelengths = w

w = ideal_long_cmf.wavelengths
w = [i + IDEAL_OFFSET for i in w]
ideal_long_cmf.wavelengths = w

ideal_short_cmf.align(colour.SpectralShape(360, 820, 1))
ideal_long_cmf.align(colour.SpectralShape(360, 820, 1))
medium_cmf_spectra.align(colour.SpectralShape(360, 820, 1))

ideal_cmf_data = list(
    zip(ideal_long_cmf.values, medium_cmf_spectra.values, ideal_short_cmf.values)
)
labels = ["Ideal Long Cone", "Ideal Medium Cone", "Ideal Short Cone"]

ideal_cmf = colour.MultiSpectralDistributions(
    ideal_cmf_data,
    medium_cmf_spectra.wavelengths,
    labels=labels,
    display_name="Fake Ideal Observer",
)

ideal_cmf_plot = colour.plotting.plot_single_cmfs(
    ideal_cmf,
    title="Ideal Color Matching Function",
    filename="ideal_cmfs.png",
    **plotting_kwargs
)

# Ideal LEDs
ideal_green_sd = colour.sd_single_led(555, half_spectral_width=15)
ideal_red_sd = colour.sd_single_led(655, half_spectral_width=15)
ideal_blue_sd = colour.sd_single_led(455, half_spectral_width=15)

ideal_green_sd.align(colour.SpectralShape(360, 820, 1))
ideal_red_sd.align(colour.SpectralShape(360, 820, 1))
ideal_blue_sd.align(colour.SpectralShape(360, 820, 1))

ideal_sd_data = list(
    zip(ideal_red_sd.values, ideal_green_sd.values, ideal_blue_sd.values)
)
labels = ["Optimal Red LED", "Optimal Green LED", "Optimal Blue LED"]

ideal_sd = colour.MultiSpectralDistributions(
    ideal_sd_data,
    ideal_green_sd.wavelengths,
    labels=labels,
    display_name="Optimal LED wavelengths",
)
ideal_sd_plot = colour.plotting.plot_multi_cmfs(
    ideal_sd, title="LED spectra at optimal wavelengths", **plotting_kwargs
)
plt.fill_between(
    ideal_red_sd.wavelengths,
    ideal_red_sd.values,
    where=(ideal_red_sd.wavelengths > 620),
    color="red",
    alpha=0.5,
)
plt.fill_between(
    ideal_green_sd.wavelengths,
    ideal_green_sd.values,
    where=(ideal_green_sd.wavelengths < 620) & (ideal_green_sd.wavelengths > 500),
    color="green",
    alpha=0.5,
)
plt.fill_between(
    ideal_blue_sd.wavelengths,
    ideal_blue_sd.values,
    where=(ideal_blue_sd.wavelengths < 500),
    color="blue",
    alpha=0.5,
)
plt.savefig("ideal_leds.png")

ax = plt.gca()
ax.set_title("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.get_legend().remove()
plt.savefig("ideal_leds_superimpose.png")

real_led_spectra = colour.SDS_LIGHT_SOURCES["3-LED-2 (473/545/616)"].align(
    colour.SpectralShape(360, 820, 1)
)
colour.plotting.plot_single_sd(real_led_spectra, **plotting_kwargs)

ax = plt.gca()
ax.set_title("")
ax.set_xlabel("")
ax.set_ylabel("")
plt.savefig("real_leds_superimpose.png")
