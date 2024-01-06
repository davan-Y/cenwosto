# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values
# def read_adc(channel):
#     config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#     config |= (channel << 12)  # Set the channel
#     bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#     # Wait for conversion to complete (could also use timeout)
#     time.sleep(0.1)

#     # Read the conversion result
#     data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#     result = (data[0] << 8) | data[1]

#     return result

# # Main loop
# try:
#     while True:
#         # Read joystick values
#         x_value = read_adc(0)
#         y_value = read_adc(1)

#         # Map the raw ADC values to joystick positions (0 to 1000)
#         y_position = int((y_value - 5000) / 10) + 500

#         # Ensure the values are within the desired range (0 to 1000)
#         y_position = max(0, min(1000, y_position))

#         # Print joystick positions
#         print(f"Y Position: {y_position}")

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()



# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values
# def read_adc(channel):
#     config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#     config |= (channel << 12)  # Set the channel
#     bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#     # Wait for conversion to complete (could also use timeout)
#     time.sleep(0.1)

#     # Read the conversion result
#     data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#     result = (data[0] << 8) | data[1]

#     return result

# # Main loop
# try:
#     while True:
#         # Read joystick values
#         x_value = read_adc(0)
#         y_value = read_adc(1)

#         # Print ADC values
#         print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()


# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values
# def read_adc(channel):
#     config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#     config |= (channel << 12)  # Set the channel
#     bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#     # Wait for conversion to complete (could also use timeout)
#     time.sleep(0.1)

#     # Read the conversion result
#     data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#     result = (data[0] << 8) | data[1]

#     return result

# # Main loop
# try:
#     while True:
#         # Read joystick values
#         x_value = read_adc(0)
#         y_value = read_adc(1)

#         # Print ADC values
#         print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")

#         # Map the raw ADC values to joystick positions (0 to 1000)
#         y_position = int((y_value - 65520) / 10) + 500

#         # Ensure the values are within the desired range (0 to 1000)
#         y_position = max(0, min(1000, y_position))

#         # Print joystick positions
#         print(f"Y Position: {y_position}")

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()


# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values
# def read_adc(channel):
#     config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#     config |= (channel << 12)  # Set the channel
#     bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#     # Wait for conversion to complete (could also use timeout)
#     time.sleep(0.1)

#     # Read the conversion result
#     data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#     result = (data[0] << 8) | data[1]

#     return result

# # Main loop
# try:
#     while True:
#         # Read joystick values
#         x_value = read_adc(0)
#         y_value = read_adc(1)

#         # Print ADC values
#         print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")

#         # Map the raw ADC values to joystick positions (0 to 1000)
#         y_position = int((y_value - 65520) / 10) + 500

#         # Ensure the values are within the desired range (0 to 1000)
#         y_position = max(0, min(1000, y_position))

#         # Invert the Y-axis mapping for a more intuitive result
#         y_position = 1000 - y_position

#         # Print joystick positions
#         print(f"Y Position: {y_position}")

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()







# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values
# def read_adc(channel):
#     config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#     config |= (channel << 12)  # Set the channel
#     bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#     # Wait for conversion to complete (could also use timeout)
#     time.sleep(0.1)

#     # Read the conversion result
#     data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#     result = (data[0] << 8) | data[1]

#     return result

# # Main loop
# try:
#     while True:
#         # Read joystick values
#         x_value = read_adc(0)
#         y_value = read_adc(1)

#         # Print ADC values
#         print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")

#         # Map the raw ADC values to joystick positions (0 to 1000)
#         y_position = int((y_value - 65520) / 10) + 500

#         # Ensure the values are within the desired range (0 to 1000)
#         y_position = max(0, min(1000, y_position))

#         # Invert the Y-axis mapping for a more intuitive result
#         y_position = 1000 - y_position

#         # If the joystick is in the bottom position, set Y-position to 0
#         if y_position < 50:
#             y_position = 0

#         # Print joystick positions
#         print(f"Y Position: {y_position}")

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()


# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values
# def read_adc(channel):
#     config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#     config |= (channel << 12)  # Set the channel
#     bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#     # Wait for conversion to complete (could also use timeout)
#     time.sleep(0.1)

#     # Read the conversion result
#     data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#     result = (data[0] << 8) | data[1]

#     return result

# # Main loop
# try:
#     while True:
#         # Read joystick values
#         x_value = read_adc(0)
#         y_value = read_adc(1)

#         # Print ADC values
#         print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()

# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values with a median filter
# def read_adc(channel):
#     # Apply a simple median filter (adjust the filter size as needed)
#     filter_size = 5
#     values = [0] * filter_size

#     for i in range(filter_size):
#         config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#         config |= (channel << 12)  # Set the channel
#         bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#         # Wait for conversion to complete (could also use timeout)
#         time.sleep(0.1)

#         # Read the conversion result
#         data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#         result = (data[0] << 8) | data[1]

#         values[i] = result

#     # Return the median value
#     return sorted(values)[filter_size // 2]

# # Main loop
# try:
#     while True:
#         # Read joystick values with filtering
#         x_value = read_adc(0)
#         y_value = read_adc(1)

#         # Print ADC values
#         print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()

# import time
# import smbus

# # ADS1115 address on the I2C bus
# ADS1115_ADDRESS = 0x48

# # Configuration
# CONFIG_REG = 0x01
# MUX_REG = 0x00

# # Create the I2C bus
# bus = smbus.SMBus(1)  # Change the bus number if needed

# # Function to read ADC values with a median filter
# def read_adc(channel):
#     # Apply a simple median filter (adjust the filter size as needed)
#     filter_size = 10
#     values = [0] * filter_size

#     for i in range(filter_size):
#         config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
#         config |= (channel << 12)  # Set the channel
#         bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

#         # Wait for conversion to complete (could also use timeout)
#         time.sleep(0.1)

#         # Read the conversion result
#         data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
#         result = (data[0] << 8) | data[1]

#         values[i] = result

#     # Return the median value
#     return sorted(values)[filter_size // 2]

# # Main loop
# try:
#     while True:
#         # Read joystick values with filtering
#         x_value = read_adc(0)
#         y_value = read_adc(1)
#         x_value1 = read_adc(2)
#         y_value1 = read_adc(3)
#         # Print ADC values
#         print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")
#         print(f"X 1ADC Value: {x_value1}, Y 1DC Value: {y_value1}")

#         # print(f"X ADC Value: {read_adc(2)}, Y ADC Value: xx")
#         # print(read_adc(s1))

#         # Add a delay to control the sampling rate
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     # Handle Ctrl+C gracefully
#     pass
# finally:
#     # Clean up resources
#     bus.close()

# from gpiozero import DigitalOutputDevice
# from time import sleep

# direction_pin = 20
# pulse_pin = 21
# cw_direction = 0
# ccw_direction = 1

# # Create DigitalOutputDevices for the GPIO pins
# direction_line = DigitalOutputDevice(direction_pin)
# pulse_line = DigitalOutputDevice(pulse_pin)

# try:
#     while True:
#         print("Direction CW")
#         sleep(5)
#         direction_line.value = cw_direction
#         for x in range(200):
#             pulse_line.on()
#             sleep(0.004)
#             pulse_line.off()
#             sleep(0.004)

#         print("Direction CCW")
#         sleep(1)  # Adjust the delay as needed
#         direction_line.value = ccw_direction
#         for x in range(200):
#             pulse_line.on()
#             sleep(0.004)
#             pulse_line.off()
#             sleep(0.004)

# except KeyboardInterrupt:
#     print("Exiting program.")
# finally:
#     direction_line.close()
#     pulse_line.close()




import time
import smbus
from gpiozero import DigitalOutputDevice
from time import sleep

direction_pin = 8
pulse_pin = 7
cw_direction = 0
ccw_direction = 1

direction_line = DigitalOutputDevice(direction_pin)
pulse_line = DigitalOutputDevice(pulse_pin)

# ADS1115 address on the I2C bus
ADS1115_ADDRESS = 0x48

# Configuration
CONFIG_REG = 0x01
MUX_REG = 0x00

# Create the I2C bus
bus = smbus.SMBus(1)  # Change the bus number if needed

# Function to read ADC values with a median filter
def read_adc(channel):
    # Apply a simple median filter (adjust the filter size as needed)
    filter_size = 10
    values = [0] * filter_size

    for i in range(filter_size):
        config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
        config |= (channel << 12)  # Set the channel
        bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

        # Wait for conversion to complete (could also use timeout)
        time.sleep(0.1)

        # Read the conversion result
        data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
        result = (data[0] << 8) | data[1]

        values[i] = result

    # Return the median value
    return sorted(values)[filter_size // 2]

# Main loop
try:
    while True:
        # Read joystick values with filtering
        x_value = read_adc(0)
        y_value = read_adc(1)
        x_value1 = read_adc(2)
        y_value1 = read_adc(3)
        # Print ADC values
        print(f"X ADC Value: {x_value}, Y ADC Value: {y_value}")
        print(f"X 1ADC Value: {x_value1}, Y 1DC Value: {y_value1}")


        if x_value<51000 :
            direction_line.value = cw_direction
            for x in range(200):
                pulse_line.on()
                sleep(0.004)
                pulse_line.off()
                sleep(0.004)
        

        if x_value>58000 :
            direction_line.value = ccw_direction
            for x in range(200):
                pulse_line.on()
                sleep(0.004)
                pulse_line.off()
                sleep(0.004)
        
        # print(f"X ADC Value: {read_adc(2)}, Y ADC Value: xx")
        # print(read_adc(s1))

        # Add a delay to control the sampling rate
        time.sleep(0.1)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass
finally:
    # Clean up resources
    bus.close()