import sys
import time
import serial
import numpy as np
import cv2
from serial.tools import list_ports

# Image parameters (must match STM32 settings)
IMAGE_WIDTH = 160
IMAGE_HEIGHT = 120
IMAGE_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT * 2  # 16-bit per pixel

def find_stm32_port():
    """Find the STM32 virtual COM port"""
    ports = list_ports.comports()
    for port in ports:
        if "STM" in port.description or "STMicroelectronics" in port.description:
            return port.device
    return None

def receive_image(ser):
    """Receive image data from STM32"""
    # Send capture command
    ser.write(b'CAPTURE\n')
    
    # Wait for response
    while True:
        line = ser.readline().decode().strip()
        if line == "IMAGE_START":
            break
    
    # Receive image data
    received_data = bytearray()
    while len(received_data) < IMAGE_SIZE:
        chunk = ser.read(IMAGE_SIZE - len(received_data))
        received_data.extend(chunk)
    
    # Convert to numpy array
    img_data = np.frombuffer(received_data, dtype=np.uint8)
    
    # Reshape and convert to RGB
    img = img_data.reshape((IMAGE_HEIGHT, IMAGE_WIDTH, 2))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR5652RGB)
    
    return img_rgb

def main():
    # Find and open serial port
    port = find_stm32_port()
    if port is None:
        print("STM32 not found!")
        return
    
    try:
        ser = serial.Serial(port, baudrate=115200, timeout=5)
        print(f"Connected to {port}")
        
        # Receive image
        print("Requesting image...")
        img = receive_image(ser)
        
        # Save image
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"capture_{timestamp}.png"
        cv2.imwrite(filename, img)
        print(f"Image saved as {filename}")
        
        # Show image
        cv2.imshow("Captured Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

if __name__ == "__main__":
    main()