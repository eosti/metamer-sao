import strictyaml as yaml
from dataclasses import dataclass
from typing import Optional, List
from path import Path
from csnake import Variable


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


def parse_leds(file: Path) -> List[LED]:
    led_schema = yaml.Map({'name': yaml.Str(), 'pn': yaml.Str(), 'test_current_ma': yaml.Int(), 'max_current_ma': yaml.Int(), yaml.Optional('wavelength_dominant'): yaml.Int(), yaml.Optional('wavelength_peak'): yaml.Int(), yaml.Optional('color_temperature'): yaml.Int(), 'brightness_mcd': yaml.Int(), 'index': yaml.Int()})
    root_schema = yaml.MapCombined({"leds": yaml.Seq(led_schema)}, yaml.Str(), yaml.Any())

    input_data = yaml.load(file.bytes().decode('utf-8'), root_schema)
    output: List[LED] = []
    for i in input_data["leds"]:
        # ** unpacks dict into keyword arguments
        output.append(LED(**i.data))

    return output


if __name__ == "__main__":
    p = Path('./leds.yaml')
    ledlist = parse_leds(p)

    min_bright = 1000000
    output = ["0"] * 18
    for i in ledlist:
        if i.brightness_mcd < min_bright:
            min_bright = i.brightness_mcd

    for i in ledlist:
        output[i.index] = int(round(min_bright / i.brightness_mcd * 100 * 2.55))

    outputdec = "uint8_t default_values[] = { "
    for i in output:
        outputdec += f"{i}, "

    outputdec = outputdec[:-2]
    outputdec += " };"
    print(outputdec)


