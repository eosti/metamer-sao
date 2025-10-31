# Runs open/short checks on boards for production.
from machine import I2C, Pin

from aw210xx import AW210xx, AW210xxOpenShortDetect


def parse_openshort(leds: AW210xx, display_name: str):
    results = leds.get_open_short_status()
    if results == 0:
        print(f"{display_name}: no faults detected")
        return []

    faults = []
    for i in range(leds.NUM_CHANNELS):
        if results & (1 << i) != 0:
            faults.append(i)

    print(f"{display_name}: faults on channels {faults} detected")
    return faults


def openshort_check(leds: AW210xx) -> None:
    assert leds.chip_enabled()

    # Set all LEDs to consume 1mA as recommended in datasheet
    global_current_max = int(0.001 / leds.max_current() * 255)
    leds.global_current(global_current_max)
    print(f"Set LED current to {leds.max_global_current() * 1000:.3f}mA")
    for i in range(leds.NUM_CHANNELS):
        leds.col(i, 255)
        leds.br(i, 255)
    leds.update()

    # Run the tests now
    leds.open_short_detect(AW210xxOpenShortDetect.OPEN_ENABLE)
    opens = parse_openshort(leds, "Open results")

    end_result = True

    if 3 not in opens and 4 not in opens:
        print("Both teals populated, fancy!")
    elif 3 not in opens or 4 not in opens:
        print("One teal populated, standard")
    else:
        print("Missing both teals!")
        end_result = False

    for i in opens:
        if i in [16, 17, 18, 19, 20, 21, 22, 23]:
            continue

        if i in [3, 4]:
            # we already dealt with the teals above
            continue

        elif i == 6:
            print("Partially assembled board (560nm missing)")
        elif i == 11:
            print("Partially assembled board (640nm missing)")
        else:
            print("Unexpected open (", i, ")")
        end_result = False

    leds.open_short_detect(AW210xxOpenShortDetect.SHORT_ENABLE)
    shorts = parse_openshort(leds, "Short results")

    if shorts != []:
        print("Unexpect short results!")
        end_result = False

    print()
    if end_result is False:
        print("Failed :(")
    else:
        print("Passed :)")


def main():
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
    leds = AW210xx(i2c, r_ext=3650, model="AW21024")

    leds.reset()
    leds.chip_enabled(True)
    print(
        f"Driver ID: 0x{leds.get_id():02X}, Driver Version: 0x{leds.get_version():02X}"
    )
    leds.global_current(255)

    print(f"Maximum current per channel is {leds.max_global_current()}A")

    for i in range(leds.NUM_CHANNELS):
        leds.col(i, 255)

    openshort_check(leds)


if __name__ == "__main__":
    main()
