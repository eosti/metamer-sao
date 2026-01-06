# Metamer SAO
A collection of files related to the [Metamer SAO](https://reidsoxharris.me/metamer-sao)

v2 of the badge (first seen at Hackaday 2024) can be found in the `v2_altium` directory, though it's just boardfiles and schematic PDFs. 
Because reasons I had to port it into KiCAD for v2.1, which can be found in the `v2.1_kicad` directory along with all generated gerbers and PnP files required for assembly. 
The `generators` directory has some code for auto-generating C data structures for normalizing brightness. 

Some MicroPython code that you can run on the badge is found in the `micropython` directory. 
The code used on the PY32F002B MCU used to bootstrap I2C is in the `py32` directory, and current builds are in `py32/releases`.

The code I used to generate the graphs for my talk, [Beyond RGB](https://reidsoxharris.me/beyondrgb/) can be found in `python_graphs`.
