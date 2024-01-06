import smbus
import math
import time

# MPU6050 registers and addresses
MPU6050_ADDR = 0x68
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47

# MPU6050 constants
ACCEL_SCALE = 16384.0
GYRO_SCALE = 131.0

# Complementary filter constants
alpha = 0.98
dt = 0.01

# Initialize the I2C bus
bus = smbus.SMBus(1)

def read_word(reg):
    high = bus.read_byte_data(MPU6050_ADDR, reg)
    low = bus.read_byte_data(MPU6050_ADDR, reg + 1)
    value = (high << 8) + low
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val

def set_power_mgmt_1():
    bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

def read_data():
    accel_x = read_word_2c(ACCEL_XOUT) / ACCEL_SCALE
    accel_y = read_word_2c(ACCEL_YOUT) / ACCEL_SCALE
    accel_z = read_word_2c(ACCEL_ZOUT) / ACCEL_SCALE

    gyro_x = read_word_2c(GYRO_XOUT) / GYRO_SCALE
    gyro_y = read_word_2c(GYRO_YOUT) / GYRO_SCALE
    gyro_z = read_word_2c(GYRO_ZOUT) / GYRO_SCALE

    return accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z

def complementary_filter(prev_angle, gyro_rate, accel_angle):
    # Apply complementary filter to combine accelerometer and gyroscope data
    alpha = 0.98
    angle = alpha * (prev_angle + gyro_rate * dt) + (1 - alpha) * accel_angle
    return angle


if __name__ == "__main__":
    set_power_mgmt_1()

    gyro_angle_x = 0.0
    accel_angle_x = 0.0

    try:
        while True:
            accel_x, _, _, gyro_x, _, _ = read_data()

            accel_angle_x = math.atan2(accel_x, 9.8) * (180.0 / math.pi)
            gyro_rate_x = gyro_x

            gyro_angle_x = complementary_filter(gyro_angle_x, gyro_rate_x, accel_angle_x)

            print(f"Roll Angle: {gyro_angle_x:.2f} degrees")
            time.sleep(dt)

    except KeyboardInterrupt:
        pass
