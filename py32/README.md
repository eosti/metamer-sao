# PY32
This is the code use for the bootstrap I2C MCU. 
It's the PY32F002B, so the cheapest one possible. 

The structure of the repo is largely taken from [py32f0-template](https://github.com/IOsetting/py32f0-template) -- I still don't know how Makefiles work, and that's okay. 
Building is as easy as `make`.

The version of the MCU code is stored in register 0x86. 

### Known Issues
On v0 firmware, the driver will be unable to communicate on I2C due to the MCU assuming the same address as the driver. 
In v1, the MCU will not only disable its own address, but also deinit the I2C peripheral after sending it's packet.
Problem solved!

The MCU will send a burst of I2C packets right at boot thay may conflict with other goings-ons on the bus. 
Theoretically, this should occur before the Pico on the badge is able to boot, but it's a shared bus and it's not the most considerate to other users on the bus to unexpectedly have a multi-master situation. 
If you run into any issues, a workaround is to cut off the I2C pins on the SAO connector: the SAO will still turn on as expected, but will not be controllable from the badge (obviously).
