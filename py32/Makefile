##### Project #####

PROJECT			?= metamersao
# The path for generated files
BUILD_DIR		= build

# MCU types: 
#   PY32F002Ax5
#   PY32F002Bx5
#   PY32F003x4, PY32F003x6, PY32F003x8,
#   PY32F030x6, PY32F030x8, 
#   PY32F072xB
MCU_TYPE		= PY32F002Bx5

##### Options #####

# Use LL library instead of HAL, y:yes, n:no
USE_LL_LIB ?= n
# Enable printf float %f support, y:yes, n:no
ENABLE_PRINTF_FLOAT	?= n
# Build with FreeRTOS, y:yes, n:no
USE_FREERTOS	?= n
# Build with CMSIS DSP functions, y:yes, n:no
USE_DSP			?= n
# Build with Waveshare e-paper lib, y:yes, n:no
USE_EPAPER		?= n
# Programmer, jlink or pyocd
FLASH_PROGRM	?= pyocd

##### Toolchains #######

#ARM_TOOCHAIN	?= /opt/gcc-arm/gcc-arm-11.2-2022.02-x86_64-arm-none-eabi/bin
#ARM_TOOCHAIN	?= /opt/gcc-arm/arm-gnu-toolchain-11.3.rel1-x86_64-arm-none-eabi/bin
#ARM_TOOCHAIN	?= /opt/gcc-arm/arm-gnu-toolchain-13.2.Rel1-x86_64-arm-none-eabi/bin
ARM_TOOCHAIN ?= /opt/homebrew/bin

# path to JLinkExe
JLINKEXE		?= /opt/SEGGER/JLink/JLinkExe
# path to PyOCD
PYOCD_EXE		?= pyocd

##### Paths ############

# C and CPP source folders
CDIRS		:= src 
# Single C and CPP source files
CFILES		:= 
CPPFILES	:= 

# ASM source folders
ADIRS		:= src
# Single ASM source files
AFILES		:= 

# Include paths
INCLUDES	:= lib/CMSIS/Core/Include \
			lib/CMSIS/Device/PY32F0xx/Include \
			src

##### Library Paths ############

# Library flags
LIB_FLAGS		= $(MCU_TYPE)
# JLink device (Uppercases)
JLINK_DEVICE	?= $(shell echo $(MCU_TYPE) | tr '[:lower:]' '[:upper:]')
# PyOCD device (Lowercases)
PYOCD_DEVICE	?= $(shell echo $(MCU_TYPE) | tr '[:upper:]' '[:lower:]')
# Link descript file: 
LDSCRIPT		= lib/LDScripts/$(PYOCD_DEVICE).ld


ifneq (,$(findstring PY32F002B,$(MCU_TYPE)))

# PY32F002B >>>
CFILES		+= lib/CMSIS/Device/PY32F0xx/Source/system_py32f002b.c

ifeq ($(USE_LL_LIB),y)
CDIRS		+= lib/PY32F002B_LL_Driver/Src \
		lib/PY32F002B_LL_BSP/Src
INCLUDES	+= lib/PY32F002B_LL_Driver/Inc \
		lib/PY32F002B_LL_BSP/Inc
LIB_FLAGS   += USE_FULL_LL_DRIVER
else
CDIRS		+= lib/PY32F002B_HAL_Driver/Src \
		lib/PY32F002B_HAL_BSP/Src
INCLUDES	+= lib/PY32F002B_HAL_Driver/Inc \
		lib/PY32F002B_HAL_BSP/Inc
endif
# Startup file
AFILES	:= lib/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f002b.s
# PY32F002B <<<

else ifneq (,$(findstring PY32F07,$(MCU_TYPE)))

#  PY32F07x >>>
CFILES		+= lib/CMSIS/Device/PY32F0xx/Source/system_py32f07x.c

CDIRS		+= lib/PY32F07x_HAL_Driver/Src \
		lib/PY32F07x_HAL_BSP/Src
INCLUDES	+= lib/PY32F07x_HAL_Driver/Inc \
		lib/PY32F07x_HAL_BSP/Inc
LIB_FLAGS   += USE_HAL_DRIVER
# Startup file
AFILES	:= lib/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f072.s
#  PY32F07 <<<

else

# PY32F002A,003,030 >>>
CFILES		+= lib/CMSIS/Device/PY32F0xx/Source/system_py32f0xx.c

ifeq ($(USE_LL_LIB),y)
CDIRS		+= lib/PY32F0xx_LL_Driver/Src \
		lib/PY32F0xx_LL_BSP/Src
INCLUDES	+= lib/PY32F0xx_LL_Driver/Inc \
		lib/PY32F0xx_LL_BSP/Inc
LIB_FLAGS   += USE_FULL_LL_DRIVER
else
CDIRS		+= lib/PY32F0xx_HAL_Driver/Src \
		lib/PY32F0xx_HAL_BSP/Src
INCLUDES	+= lib/PY32F0xx_HAL_Driver/Inc \
		lib/PY32F0xx_HAL_BSP/Inc
endif
# Startup file
ifneq (,$(findstring PY32F002A,$(LIB_FLAGS)))
AFILES	:= lib/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f002a.s
endif
ifneq (,$(findstring PY32F003,$(LIB_FLAGS)))
AFILES	:= lib/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f003.s
endif
ifneq (,$(findstring PY32F030,$(LIB_FLAGS)))
AFILES	:= lib/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f030.s
endif
# PY32F002A,003,030 <<<

endif

######## Additional Libs ########

ifeq ($(USE_FREERTOS),y)
CDIRS		+= lib/FreeRTOS \
			lib/FreeRTOS/portable/GCC/ARM_CM0

CFILES		+= lib/FreeRTOS/portable/MemMang/heap_4.c

INCLUDES	+= lib/FreeRTOS/include \
			lib/FreeRTOS/portable/GCC/ARM_CM0
endif

ifeq ($(USE_DSP),y)
CFILES 		+= lib/CMSIS/DSP/Source/BasicMathFunctions/BasicMathFunctions.c \
		lib/CMSIS/DSP/Source/BayesFunctions/BayesFunctions.c \
		lib/CMSIS/DSP/Source/CommonTables/CommonTables.c \
		lib/CMSIS/DSP/Source/ComplexMathFunctions/ComplexMathFunctions.c \
		lib/CMSIS/DSP/Source/ControllerFunctions/ControllerFunctions.c \
		lib/CMSIS/DSP/Source/DistanceFunctions/DistanceFunctions.c \
		lib/CMSIS/DSP/Source/FastMathFunctions/FastMathFunctions.c \
		lib/CMSIS/DSP/Source/FilteringFunctions/FilteringFunctions.c \
		lib/CMSIS/DSP/Source/InterpolationFunctions/InterpolationFunctions.c \
		lib/CMSIS/DSP/Source/MatrixFunctions/MatrixFunctions.c \
		lib/CMSIS/DSP/Source/QuaternionMathFunctions/QuaternionMathFunctions.c \
		lib/CMSIS/DSP/Source/StatisticsFunctions/StatisticsFunctions.c \
		lib/CMSIS/DSP/Source/SupportFunctions/SupportFunctions.c \
		lib/CMSIS/DSP/Source/SVMFunctions/SVMFunctions.c \
		lib/CMSIS/DSP/Source/TransformFunctions/TransformFunctions.c
INCLUDES	+= lib/CMSIS/DSP/Include \
		lib/CMSIS/DSP/PrivateInclude
endif

ifeq ($(USE_EPAPER),y)
CDIRS		+= lib/EPaper/Lib \
			lib/EPaper/Examples \
			lib/EPaper/Fonts \
			lib/EPaper/GUI

INCLUDES	+= lib/EPaper/Lib \
			lib/EPaper/Examples \
			lib/EPaper/Fonts \
			lib/EPaper/GUI
endif

include ./rules.mk
