import serial  # brown --> rx, blue --> tx

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)


def read_tf03_data():
    # while True:

    bytes_serial = ser.read(9)  # read 9 bytes
    ser.reset_input_buffer()  # reset buffer

    if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:  # check first two bytes
        distance = bytes_serial[2] + bytes_serial[3] * 256  # distance in next two bytes
        strength = bytes_serial[4] + bytes_serial[5] * 256  # signal strength in next two bytes

        print(f"Distance: {distance / 100} m, Strength: {strength}")  # print sample data


# if not ser.isOpen():
#     print("opening port...")
#     ser.open()  # open serial port if not open

while True:


    read_tf03_data()  # read values

ser.close()