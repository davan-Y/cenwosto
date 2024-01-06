import serial
import time

# Set the serial port and baud rate
serial_port = "/dev/tty0"  # Raspberry Pi 5 serial port
baud_rate = 115200

# Create a serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=5)

try:
    while True:
        # Read data from the TF03
        raw_data = ser.readline()
        print("Raw Data:", raw_data)
        
        data = raw_data.decode('utf-8').strip()
        # Display the distance datas
        print("Distance:", data)

        # Wait for a short duration (adjust as needed)
        time.sleep(0.1)

except KeyboardInterrupt:
    # Close the serial connection on program exit
    ser.close()
    print("Serial connection closed.")

# except KeyboardInterrupt:
#     # Close the serial connection on program exit
#     ser.close()
#     print("Serial connection closed.")
