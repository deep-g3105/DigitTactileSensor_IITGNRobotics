import serial

SERIAL_PORT = 'COM6'  # Change to your COM port
BAUD_RATE = 115200    # Might be ignored if CDC, but put something valid
ser = serial.Serial(SERIAL_PORT, timeout=1)

try:
    while True:
        data = ser.read(100)  # Read 100 bytes
        if data:
            print(f"Received: {len(data)} bytes: {data[:10]}")
except KeyboardInterrupt:
    ser.close()
    print("Serial closed.")