#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

// Includes
#include "py32f002b_hal.h"

// SAO Defines
#define LED_GPIO_PIN    GPIO_PIN_1
#define LED_GPIO_PORT   GPIOB
#define I2C_CLOCKSPEED  100000
#define AW210XX_ADDRESS 0x30

// Exports
extern I2C_HandleTypeDef hi2c;

#ifdef __cplusplus
}
#endif

#endif
