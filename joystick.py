import time
import smbus

# ADS1115 address on the I2C bus
ADS1115_ADDRESS = 0x48

# Configuration
CONFIG_REG = 0x01
MUX_REG = 0x00

# Create the I2C bus
bus = smbus.SMBus(1)  # Change the bus number if needed

# Function to read ADC values
def read_adc(channel):
    config = 0x8583  # Single-ended, +/-4.096V, 860 SPS, AINx
    config |= (channel << 12)  # Set the channel
    bus.write_i2c_block_data(ADS1115_ADDRESS, CONFIG_REG, [(config >> 8) & 0xFF, config & 0xFF])

    # Wait for conversion to complete (could also use timeout)
    time.sleep(0.1)

    # Read the conversion result
    data = bus.read_i2c_block_data(ADS1115_ADDRESS, 0x00, 2)
    result = (data[0] << 8) | data[1]

    return result

# Main loop
try:
    while True:
        # Read joystick values
        x_value = read_adc(0)
        y_value = read_adc(1)

        # Map the raw ADC values to joystick positions
        x_position = (x_value -5000)/5000
        y_position = (y_value -5000)/5000

        # Print joystick positions
        print(f"X Position: {x_position:.2f},{y_position:.2f}")

        # Add a delay to control the sampsling rate
        time.sleep(0.1)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass
finally:
    # Clean up resources
    bus.close()

