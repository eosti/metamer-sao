# Turns all the LEDs on all the way. Because you can. 

from machine import I2C, Pin 

from aw210xx import AW210xx

def main():
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
    print(i2c.scan())
    leds = AW210xx(i2c, r_ext=3650, model="AW21024")

    leds.reset()
    leds.chip_enabled(True)
    print(
        f"Driver ID: 0x{leds.get_id():02X}, Driver Version: 0x{leds.get_version():02X}"
    )
    leds.global_current(255)

    for i in range(16):
        leds.br(i, 255)
        leds.col(i, 255)

    leds.update()


if __name__ == "__main__":
    main()
