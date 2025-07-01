import serial
import numpy as np
import cv2

# Configuration
SERIAL_PORT = 'COM6'
FRAME_WIDTH = 320
FRAME_HEIGHT = 240
FRAME_SIZE = FRAME_WIDTH * FRAME_HEIGHT
HEADER = b'\xAA\x55\xAA\x55'

# Open serial port
ser = serial.Serial(SERIAL_PORT, timeout=0.1)

def wait_for_header():
    """Synchronize to the frame header"""
    sync = bytearray()
    while True:
        byte = ser.read(1)
        if not byte:
            continue
        sync += byte
        if len(sync) > 4:
            sync = sync[-4:]
        if sync == HEADER:
            return

try:
    while True:
        wait_for_header()
        
        # Read frame
        buffer = bytearray()
        while len(buffer) < FRAME_SIZE:
            chunk = ser.read(FRAME_SIZE - len(buffer))
            if not chunk:
                continue
            buffer.extend(chunk)

        # Convert and display
        frame = np.frombuffer(buffer, dtype=np.uint8).reshape((FRAME_HEIGHT, FRAME_WIDTH))
        cv2.imshow("OV7670 Live Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user.")

finally:
    ser.close()
    cv2.destroyAllWindows()
