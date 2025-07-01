#include "main.h"
#include "i2c.h" // If you are using I2C2
#include "dcmi.h"
#include "dma.h"
#include "gpio.h"

// OV7670 register table for QVGA RGB565
typedef struct {
    uint8_t reg;
    uint8_t val;
} OV7670_Reg_Config_t;

// Example register table (minimal, you can expand later)
OV7670_Reg_Config_t ov7670_init_regs[] = {
    {0x12, 0x80}, // Reset register
    {0x11, 0x01}, // Clock prescaler (Optional tuning)
    {0x12, 0x14}, // QVGA RGB565
    {0x40, 0xd0}, // RGB565 output
    {0x3a, 0x04}, // Set TSLB: UV ordering
    {0x8c, 0x00}, // RGB444 disable
    {0x17, 0x16}, // HSTART
    {0x18, 0x04}, // HSTOP
    {0x32, 0x80}, // HREF
    {0x19, 0x02}, // VSTART
    {0x1a, 0x7a}, // VSTOP
    {0x03, 0x0a}, // VREF
    {0xff, 0xff}  // End marker
};

void OV7670_WriteReg(uint8_t reg, uint8_t data) {
    HAL_I2C_Mem_Write(&hi2c2, 0x42, reg, 1, &data, 1, HAL_MAX_DELAY);
}

void OV7670_Init(void) {
    HAL_Delay(100); // Wait after reset
    for (int i = 0; ov7670_init_regs[i].reg != 0xff; i++) {
        OV7670_WriteReg(ov7670_init_regs[i].reg, ov7670_init_regs[i].val);
        HAL_Delay(1);
    }
}