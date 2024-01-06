# θ=21​arcsin(v02​R⋅g​)
# angle = 1/2

import math

def calculate_launch_angle(initial_velocity, range_, height):
    # Convert range_ and height to positive values
    range_ = abs(range_)
    height = abs(height)

    # Acceleration due to gravity
    g = 9.8

    # Calculate launch angle
    term = (initial_velocity**2 * range_) / (g * (range_ * math.tan(math.radians(45)) - height))
    
    # Ensure the term inside the arctan is non-negative
    if term >= 0:
        launch_angle = math.degrees(math.atan(term))
        return launch_angle
    else:
        return None  # No real solution for the given parameters

# Example usage:
initial_velocity = 34.29   # meters per second
range_ = 120  # meters
height = 9  # meters (assuming the gun is fired from the same height)

launch_angle = calculate_launch_angle(initial_velocity, range_, height)

if launch_angle is not None:
    print(f"The launch angle is approximately {launch_angle:.2f} degrees.")
else:
    print("No real solution for the given parameters.")
