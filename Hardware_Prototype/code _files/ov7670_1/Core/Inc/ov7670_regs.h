#ifndef OV7670_REGS_H
#define OV7670_REGS_H

// OV7670 I2C Address (0x21 or 0x42)
#define OV7670_ADDR 0x42  // 7-bit address (0x21 << 1)

// Key Registers
#define REG_GAIN     0x00  // AGC gain
#define REG_COM7     0x12  // Control 7 (reset + format)
#define REG_CLKRC    0x11  // Clock control (FPS)
#define REG_COM15    0x40  // RGB565 mode
#define REG_SCALING_PCLK_DIV 0x73  // Pixel clock divider (FPS adjust)

// Common Configurations
#define QVGA_RGB565  0x0C  // COM7 value for QVGA + RGB565
#define RGB565_MODE  0xD0  // COM15 value for RGB565

#endif