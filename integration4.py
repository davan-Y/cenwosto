from gpiozero import Button
from gpiozero import OutputDevice
from time import sleep
import time
import smbus
from gpiozero import DigitalOutputDevice
import serial  # brown --> rx, blue --> tx
import math

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT  = 0x43
GYRO_YOUT  = 0x45
GYRO_ZOUT  = 0x47

button_pin_1 = 19
button_pin_2 = 26
button_pin_3 = 23
button_pin_4 = 18

relay_pin_1 = 17
relay_pin_2 = 24
relay_pin_3 = 25
relay_pin_4 = 4
relay_pin_5 = 14
relay_pin_6 = 15
relay_pin_7 = 27
relay_pin_8 = 22
relay_pin_9 = 10
relay_pin_10= 9
relay_pin_11= 11
relay_pin_12= 0
relay_pin_13= 5
relay_pin_14= 6
relay_pin_15= 13
initial = 0

direction_pin = 8
pulse_pin = 7
cw_direction = 0
ccw_direction = 1

direction_line = DigitalOutputDevice(direction_pin)
pulse_line = DigitalOutputDevice(pulse_pin)

button_1 = Button(button_pin_1)
button_2 = Button(button_pin_2)
button_3 = Button(button_pin_3)
button_4 = Button(button_pin_4)

relay_1 = OutputDevice(relay_pin_1, active_high=False, initial_value=False)
relay_2 = OutputDevice(relay_pin_2, active_high=False, initial_value=False)
relay_3 = OutputDevice(relay_pin_3, active_high=False, initial_value=False)
relay_4 = OutputDevice(relay_pin_4, active_high=False, initial_value=False)
relay_5 = OutputDevice(relay_pin_5, active_high=False, initial_value=False)
relay_6 = OutputDevice(relay_pin_6, active_high=False, initial_value=False)
relay_7 = OutputDevice(relay_pin_7, active_high=False, initial_value=False)
relay_8 = OutputDevice(relay_pin_8, active_high=False, initial_value=False)
relay_9 = OutputDevice(relay_pin_9, active_high=False, initial_value=False)
relay_10 = OutputDevice(relay_pin_10, active_high=False, initial_value=False)
relay_11 = OutputDevice(relay_pin_11, active_high=False, initial_value=False)
relay_12 = OutputDevice(relay_pin_12, active_high=False, initial_value=False)
relay_13 = OutputDevice(relay_pin_13, active_high=False, initial_value=False)
relay_14 = OutputDevice(relay_pin_14, active_high=False, initial_value=False)
relay_15 = OutputDevice(relay_pin_15, active_high=False, initial_value=False)
arr_relay = [relay_1, relay_2, relay_3, relay_4,relay_5, relay_6, relay_7, relay_8,relay_9, relay_10, relay_11 ,relay_12, relay_13 ,relay_14,relay_15]


button_1_pressed = False
button_2_pressed = False
button_3_pressed = False
button_4_pressed = False

ADS1115_ADDRESS = 0x48

CONFIG_REG = 0x01
MUX_REG = 0x00
bus = smbus.SMBus(1) 
Device_Address = 0x68  

def MPU_Init():
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    bus.write_byte_data(Device_Address, CONFIG, 0)

    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = ((high << 8) | low)

    if value > 32768:
        value = value - 65536
    return value

MPU_Init()

def find_launch_angle(initial_speed, target_range, gravity):
    launch_angle_radians = math.asin((target_range * gravity) / (initial_speed**2)) / 2
    
    launch_angle_degrees = math.degrees(launch_angle_radians)
    
    return launch_angle_degrees

def read_adc(channel):
    filter_size = 10
    values = [0] * filter_size

    for i in range(filter_size):
        config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
        config |= (channel << 12)  # Set the channel
        bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

        # Wait for conversion to complete (could also use timeout)
        time.sleep(0.01)

        # Read the conversion result
        data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
        result = (data[0] << 8) | data[1]

        values[i] = result

    # Return the median value
    return sorted(values)[filter_size // 2]


def read_tf03_data():
    # while True:

    bytes_serial = ser.read(9)  # read 9 bytes
    ser.reset_input_buffer()  # reset buffer

    if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59:  # check first two bytes
        distance = bytes_serial[2] + bytes_serial[3] * 256  # distance in next two bytes
        strength = bytes_serial[4] + bytes_serial[5] * 256  # signal strength in next two bytes

        print(f"Distance: {distance / 100} m, Strength: {strength}")   # if x_value<51000 :
        #     direction_line.value = cw_direction
        #     for x in range(200):
        #         pulse_line.on()
        #         sleep(0.004)
        #         pulse_line.off()
        #         sleep(0.004)
        

        # if x_value>58000 :
        #     direction_line.value = ccw_direction
        #     for x in range(200):
        #         pulse_line.on()
        #         sleep(0.004)
        #         pulse_line.off()
        #         sleep(0.004)# print sample data

        launch_angle = find_launch_angle(34.39, distance / 100, 99.8)
        launch_angle=int(launch_angle)

        print(f"launch at:{launch_angle}")
        current_angle=0
        while current_angle!=launch_angle:
            acc_x = read_raw_data(ACCEL_XOUT)
            acc_y = read_raw_data(ACCEL_YOUT)
            acc_z = read_raw_data(ACCEL_ZOUT)
            gyro_x = read_raw_data(GYRO_XOUT)
            gyro_y = read_raw_data(GYRO_YOUT)
            gyro_z = read_raw_data(GYRO_ZOUT)

            Ax = acc_x/16384.0
            Ay = acc_y/16384.0 
            Az = acc_z/16384.0

            Gx = gyro_x/131.0
            Gy = gyro_y/131.0
            Gz = gyro_z/131.0

            in_min = 1
            in_max = -1
            out_min = 0
            out_max = 180

            value = (Ay - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
            current_angle = int(value)
            print(f"current angle:{current_angle}")
            if current_angle<launch_angle:
                direction_line.value = cw_direction
                for x in range(500):
                    pulse_line.on()
                    sleep(0.004)
                    pulse_line.off()
                    sleep(0.004)
                    # print('clock wise')
            if current_angle>launch_angle:
                 direction_line.value = ccw_direction
                 for x in range(200):
                    pulse_line.on()
                    sleep(0.004)
                    pulse_line.off()
                    sleep(0.004)
            print(value)

        print(f"If the initial speed is 34.39 meters per second and the projectile covers a distance of {distance/100} meters, the launch angle is approximately {launch_angle:.2f} degrees.")

if not ser.isOpen():
    print("opening port...")
    ser.open()
try:
    while True:

        # acc_x = read_raw_data(ACCEL_XOUT)
        # acc_y = read_raw_data(ACCEL_YOUT)
        # acc_z = read_raw_data(ACCEL_ZOUT)
        # gyro_x = read_raw_data(GYRO_XOUT)
        # gyro_y = read_raw_data(GYRO_YOUT)
        # gyro_z = read_raw_data(GYRO_ZOUT)

        # Ax = acc_x/16384.0
        # Ay = acc_y/16384.0 
        # Az = acc_z/16384.0

        # Gx = gyro_x/131.0
        # Gy = gyro_y/131.0
        # Gz = gyro_z/131.0

        # in_min = 1
        # in_max = -1
        # out_min = 0
        # out_max = 180

        # value = (Ay - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # value = int(value)
        # print(value)
        # read_tf03_data() 
        x_value = read_adc(0)
        y_value = read_adc(1)
        x_value1 = read_adc(2)
        y_value1 = read_adc(3)
        print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")
        print(f"X 1ADC Value: {x_value1}, Y 1DC Value: {y_value1}")


        if y_value1>38000 and y_value1<40000:
            direction_line.value = cw_direction
            for x in range(200):
                pulse_line.on()
                sleep(0.004)
                pulse_line.off()
                sleep(0.004)

                print("clock")
        

        if y_value1>25000 and y_value1<27000:
            direction_line.value = ccw_direction
            for x in range(200):
                pulse_line.on()
                sleep(0.004)
                pulse_line.off()
                sleep(0.004)
                print("counter clock")
        if button_1.is_active and not button_1_pressed:
            button_1_pressed = True
            read_tf03_data() 
            # if initial<len(arr_relay):
            #     arr_relay[initial].on()
            #     sleep(0.2)
            #     arr_relay[initial].off()
            #     initial+=1
            # else:
            #     initial=0
            button_1_pressed = False
        if button_2.is_active and not button_2_pressed:
            button_2_pressed = True
            if initial<len(arr_relay):
                for i in range(3):
                  if initial+i<len(arr_relay):
                    arr_relay[initial+i].on()
                    sleep(0.2)
                    arr_relay[initial+i].off()
                    sleep(0.2)
                if initial==len(arr_relay):
                  initial=0
                else:
                   initial+=3 
            else:
                initial=0
            button_2_pressed = False

        if button_3.is_active and not button_3_pressed:
            button_3_pressed = True
            if initial<len(arr_relay):
                for i in range(5):
                  if initial+i<len(arr_relay):
                    arr_relay[initial+i].on()
                    sleep(0.2)
                    arr_relay[initial+i].off()
                    sleep(0.2)

                if initial==len(arr_relay):
                  initial=0
                else:
                   initial+=5 
            else:
                initial=0
            button_3_pressed = False
        if button_4.is_active and not button_4_pressed:
            button_4_pressed = True
            if initial<len(arr_relay):
                for i in range(15):
                  if initial+i<len(arr_relay):
                    arr_relay[initial+i].on()
                    sleep(0.2)
                    arr_relay[initial+i].off()
                    sleep(0.2)

                if initial==len(arr_relay):
                  initial=0
                else:
                   initial+=15 
            else:
                initial=0
            button_4_pressed = False
    # ser.close()

except KeyboardInterrupt:
    
    for relay in arr_relay:
        relay.off()   