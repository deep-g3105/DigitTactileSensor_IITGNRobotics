import serial
import struct
import numpy as np
from PIL import Image

# --- Configuration ---
SERIAL_PORT = 'COM3'         # Change this to your port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
BAUD_RATE = 115200           # Must match your STM32 USART2 baud rate
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 120
BYTES_PER_PIXEL = 2          # RGB565
TOTAL_BYTES = IMAGE_WIDTH * IMAGE_HEIGHT * BYTES_PER_PIXEL

SAVE_RAW_PATH = 'output_image.raw'
SAVE_PNG_PATH = 'output_image.png'

# --- Open Serial Port ---
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=10)

print(f"Waiting to receive {TOTAL_BYTES} bytes...")

# --- Receive Data ---
data = ser.read(TOTAL_BYTES)
ser.close()

print(f"Received {len(data)} bytes.")

# --- Save as raw file ---
with open(SAVE_RAW_PATH, 'wb') as f:
    f.write(data)
print(f"Raw image saved to {SAVE_RAW_PATH}")

# --- Convert RGB565 -> RGB888 and Save as PNG ---
def rgb565_to_rgb888(byte1, byte2):
    value = (byte1 << 8) | byte2
    r = ((value >> 11) & 0x1F) << 3
    g = ((value >> 5) & 0x3F) << 2
    b = (value & 0x1F) << 3
    return r, g, b

pixels = []
for i in range(0, len(data), 2):
    r, g, b = rgb565_to_rgb888(data[i], data[i+1])
    pixels.append((r, g, b))

image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))
image.putdata(pixels)
image.save(SAVE_PNG_PATH)

print(f"Image saved to {SAVE_PNG_PATH}")
