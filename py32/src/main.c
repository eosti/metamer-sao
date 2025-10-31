#include "main.h"

// TODO:  add a dummy register marker to show MCU code version
//        Linting, formatting
//        Documentation
//        PWM for LED?

#define VERSION_NUMBER 0x02

I2C_HandleTypeDef hi2c;

static void HAL_I2CConfig(void);
static void HAL_GpioConfig(void);
inline static void aw210xx_write(uint8_t reg, uint8_t val);
void ErrorHandler(void);

/**
 * @brief  The main function!
 * @retval int
 */
int main(void) {
    HAL_Init();
    HAL_I2CConfig();
    HAL_GpioConfig();

    // Starting config is local I2C
    HAL_GPIO_WritePin(I2C_MUX_PORT, I2C_MUX_PIN, GPIO_PIN_RESET);
    HAL_GPIO_WritePin(LED_GPIO_PORT, LED_GPIO_PIN, GPIO_PIN_SET);

    // GCR = 0x01 (chip enable)
    aw210xx_write(0x00, 0x01);
    // GCCR = 0xFF (max global current)
    aw210xx_write(0x6E, 0xFF);

    uint8_t default_values[] = {6, 11, 11, 12, 9, 2, 255, 34, 11, 12, 10, 11, 1, 1, 1, 1, 0, 0};
    for (int i = 0; i < 16; i++) {
        // BRn = default_values[i] (scaled brightness)
        aw210xx_write(0x01 + i, default_values[i]);
        // COLn = 0xFF (max channel current)
        aw210xx_write(0x4A + i, 0xFF);
    }

    // UPDATE = 0x00 (update)
    aw210xx_write(0x49, 0x00);

    // GBRH = VERSION
    // Misusing a register for the badge to determine MCU code version
    aw210xx_write(0x86, VERSION_NUMBER);

    HAL_I2C_DeInit(&hi2c);

    // Once bootstrapped, connect I2C bus to badge
    HAL_GPIO_WritePin(I2C_MUX_PORT, I2C_MUX_PIN, GPIO_PIN_SET);
    HAL_GPIO_WritePin(LED_GPIO_PORT, LED_GPIO_PIN, GPIO_PIN_RESET);

    while (1) {
        // nop
    }
}

/**
 * @brief Configures the GPIO
 */
static void HAL_GpioConfig(void) {
    GPIO_InitTypeDef GPIO_InitStruct;

    __HAL_RCC_GPIOB_CLK_ENABLE(); /* Enable GPIOA clock */

    // PB1 -> white status LED
    GPIO_InitStruct.Pin   = LED_GPIO_PIN;
    GPIO_InitStruct.Mode  = GPIO_MODE_OUTPUT_PP;  /* Push-pull output */
    GPIO_InitStruct.Pull  = GPIO_PULLUP;          /* Enable pull-up */
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH; /* GPIO speed */
    HAL_GPIO_Init(LED_GPIO_PORT, &GPIO_InitStruct);
    //
    // PB5 -> I2C mux pin (0 = local I2C, 1 = badge I2C)
    GPIO_InitStruct.Pin   = I2C_MUX_PIN;
    GPIO_InitStruct.Mode  = GPIO_MODE_OUTPUT_PP;  /* Push-pull output */
    GPIO_InitStruct.Pull  = GPIO_PULLDOWN;        /* Enable pull-down */
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH; /* GPIO speed */
    HAL_GPIO_Init(I2C_MUX_PORT, &GPIO_InitStruct);
}

/**
 * @brief Configures the I2C peripheral
 */
static void HAL_I2CConfig(void) {
    hi2c.Instance             = I2C;
    hi2c.Init.ClockSpeed      = I2C_CLOCKSPEED;
    hi2c.Init.DutyCycle       = I2C_DUTYCYCLE_16_9;
    hi2c.Init.OwnAddress1     = 0;
    hi2c.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
    hi2c.Init.NoStretchMode   = I2C_NOSTRETCH_DISABLE;

    if (HAL_I2C_Init(&hi2c) != HAL_OK) { ErrorHandler(); }
}

/**
 * @brief  helper to write to the AW210XX
 */
inline static void aw210xx_write(uint8_t reg, uint8_t val) {
    if (HAL_I2C_Mem_Write(&hi2c, AW210XX_ADDRESS << 1, reg, I2C_MEMADD_SIZE_8BIT, &val, 1, 1000) != HAL_OK) {
        ErrorHandler();
    }
}

/**
 * @brief  Error executing function.
 */
void ErrorHandler(void) {
    while (1) {
        // Flashing LED = something went wrong
        HAL_GPIO_TogglePin(LED_GPIO_PORT, LED_GPIO_PIN);
        HAL_Delay(500);
    }
}
