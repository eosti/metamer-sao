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
