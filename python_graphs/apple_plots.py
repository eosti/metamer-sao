import colour
import matplotlib.pyplot as plt
from fruit_dataset import apple_spectra
from default_style import plotting_kwargs

# SDSs
colour.plotting.plot_single_illuminant_sd(
    "D65", filename="D65_illuminant.png", **plotting_kwargs
)
colour.plotting.plot_single_illuminant_sd(
    "3-LED-2 (473/545/616)", filename="rgb_illuminant.png", **plotting_kwargs
)
blackbody = colour.sd_blackbody(3200)
blackbody.display_name = "3200K Blackbody Radiation"
colour.plotting.plot_single_sd(
    colour.sd_blackbody(3200), filename="blackbody_illuminant.png", **plotting_kwargs
)
light_style = plotting_kwargs.copy()
light_style.update(
    {
        "lines.color": "black",
        "axes.edgecolor": "black",
        "grid.color": "444444",
        "text.color": "black",
        "legend.facecolor": "white",
        "axes.labelcolor": "black",
        "xtick.color": "333333",
        "ytick.color": "333333",
    }
)
colour.plotting.plot_single_illuminant_sd(
    "Phosphor LED YAG", filename="white_illuminant.png", **light_style
)

# Apple!
apple = colour.SpectralDistribution(apple_spectra, name="Apple Spectra")
colour.plotting.plot_single_sd(apple, filename="apple.png", **plotting_kwargs)

# Combination
apple_interpolated = apple.copy().align(colour.SpectralShape(400, 770, 1))
sun_spectra = (colour.SDS_ILLUMINANTS["D65"] * apple_interpolated).align(
    colour.SpectralShape(400, 770, 5)
)
sun_spectra.display_name = "Apple under sunlight"
colour.plotting.plot_single_sd(
    sun_spectra.normalise(),
    filename="appleInSun.png",
    name="Apple in sunlight",
    **plotting_kwargs
)

led_spectra = (
    colour.SDS_LIGHT_SOURCES["3-LED-2 (473/545/616)"] * apple_interpolated
).align(colour.SpectralShape(400, 770, 5))
led_spectra.display_name = "Apple under RGB light"
colour.plotting.plot_single_sd(
    led_spectra.normalise(), filename="appleInLED.png", **plotting_kwargs
)

# Apple with medium cone
medium_cmf_spectra = colour.colorimetry.MSDS_CMFS_STANDARD_OBSERVER[
    "CIE 1931 2 Degree Standard Observer"
].to_sds()[1]
medium_apple = (medium_cmf_spectra * apple_interpolated).align(
    colour.SpectralShape(410, 760, 1)
)
medium_apple.display_name = "Apple under sunlight, medium cone"
plotting_kwargs.update({"axes.titlesize": 25})
medium_apple_plot = colour.plotting.plot_single_sd(medium_apple, **plotting_kwargs)
for i in medium_apple_plot[1].patches:
    i.remove()
plt.fill_between(medium_apple.wavelengths, medium_apple.values, color="gray", alpha=0.5)
ax = plt.gca()
ax.set_ylim([0, 1])
plt.savefig("medium_apple.png")
