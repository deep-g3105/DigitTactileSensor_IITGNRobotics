#include "ov7670.h"
#include "stm32f4xx_hal.h"

#define OV7670_ADDR 0x42

static void ov7670_write(I2C_HandleTypeDef *hi2c, uint8_t reg, uint8_t val)
{
    HAL_I2C_Mem_Write(hi2c, OV7670_ADDR, reg, I2C_MEMADD_SIZE_8BIT, &val, 1, 100);
    HAL_Delay(1);
}

void ov7670_init(I2C_HandleTypeDef *hi2c)
{
    ov7670_write(hi2c, 0x12, 0x80); // Reset
    HAL_Delay(100);

    ov7670_write(hi2c, 0x12, 0x14); // QVGA RGB
    ov7670_write(hi2c, 0x8C, 0x02); // COM15: Set RGB565
    ov7670_write(hi2c, 0x40, 0x10); // COM15: RGB565 mode

    ov7670_write(hi2c, 0x11, 0x01); // Prescaler for XCLK
    ov7670_write(hi2c, 0x6B, 0x0A); // PLL on
    ov7670_write(hi2c, 0x15, 0x00); // PCLK not invertedyes

    // QVGA windowing
    ov7670_write(hi2c, 0x32, 0x80);
    ov7670_write(hi2c, 0x17, 0x16);
    ov7670_write(hi2c, 0x18, 0x04);
    ov7670_write(hi2c, 0x03, 0x6A);
    ov7670_write(hi2c, 0x19, 0x02);
    ov7670_write(hi2c, 0x1A, 0x7A);
}
