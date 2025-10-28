import math
from argparse import ArgumentParser
from dataclasses import dataclass
from typing import List, Optional

import strictyaml as yaml
from path import Path


@dataclass
class LED:
    name: str
    pn: str
    index: int
    test_current_ma: int
    max_current_ma: int
    brightness_mcd: int
    wavelength_dominant: Optional[int] = None
    wavelength_peak: Optional[int] = None
    color_temperature: Optional[int] = None
    bandwidth: Optional[int] = None


def parse_leds(file: Path) -> List[LED]:
    led_schema = yaml.Map(
        {
            "name": yaml.Str(),
            "pn": yaml.Str(),
            "test_current_ma": yaml.Int(),
            "max_current_ma": yaml.Int(),
            yaml.Optional("wavelength_dominant"): yaml.Int(),
            yaml.Optional("wavelength_peak"): yaml.Int(),
            yaml.Optional("color_temperature"): yaml.Int(),
            yaml.Optional("bandwidth"): yaml.Int(),
            "brightness_mcd": yaml.Int(),
            "index": yaml.Int(),
        }
    )
    root_schema = yaml.MapCombined(
        {"leds": yaml.Seq(led_schema)}, yaml.Str(), yaml.Any()
    )

    input_data = yaml.load(file.bytes().decode("utf-8"), root_schema)
    output: List[LED] = []
    for i in input_data["leds"]:
        # ** unpacks dict into keyword arguments
        output.append(LED(**i.data))

    return output


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="generate_default_values.py",
        description="Takes LED specs and outputs a (mostly) normalized default value array",
    )
    parser.add_argument("input_file", help="YAML file with LED specs", type=Path)
    args = parser.parse_args()

    ledlist = parse_leds(args.input_file)

    min_bright = 1000000
    output = ["0"] * 18
    for i in ledlist:
        if i.brightness_mcd < min_bright:
            min_bright = i.brightness_mcd

    for i in ledlist:
        output[i.index] = int(math.ceil(min_bright / i.brightness_mcd * 100 * 2.55))

    outputdec = "uint8_t default_values[] = { "
    for i in output:
        outputdec += f"{i}, "

    outputdec = outputdec[:-2]
    outputdec += " };"
    print(outputdec)

    output_wavelength = []
    output_bw = []
    output_bright = []
    for i in ledlist:
        if i.bandwidth:
            if i.wavelength_peak:
                output_wavelength.append(i.wavelength_peak)
            else:
                output_wavelength.append(i.wavelength_dominant)

            output_bw.append(i.bandwidth)
            output_bright.append(i.brightness_mcd)


    print(output_wavelength)
    print(output_bw)
    print(output_bright)

