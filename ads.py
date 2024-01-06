import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create analog input channels for the joystick module
x_channel = AnalogIn(ads, ADS.P0)
y_channel = AnalogIn(ads, ADS.P1)

# Main loop
try:
    while True:
        # Read joystick values
        x_value = x_channel.value
        y_value = y_channel.value

        # Map the raw ADC values to joystick positions
        x_position = (x_value - 32767) / 32767.0
        y_position = (y_value - 32767) / 32767.0

        # Print joystick positions
        print(f"X Position: {x_position:.2f}, Y Position: {y_position:.2f}")

        # Add a delay to control the sampling rate
        time.sleep(0.1)

except KeyboardInterrupt:
    # Handle Ctrl+C gracefully
    pass
finally:
    # Clean up resources
    ads.deinit()
