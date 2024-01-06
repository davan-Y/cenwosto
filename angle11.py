import math

def calculate_range(theta, u, g):
    # Calculate range using the given launch angle
    return (u**2 * math.sin(2 * math.radians(theta))) / g

def find_launch_angle(target_range, u, g, tolerance=1e-6, max_iterations=1000):
    # Initial guesses for bisection method
    theta_low = 0.0
    theta_high = 45.0

    # Bisection method
    for _ in range(max_iterations):
        theta_mid = (theta_low + theta_high) / 2
        current_range = calculate_range(theta_mid, u, g)

        if math.isclose(current_range, target_range, rel_tol=tolerance):
            return theta_mid
        elif current_range < target_range:
            theta_low = theta_mid
        else:
            theta_high = theta_mid

    # If no solution is found within the maximum iterations
    return None

# Given values
target_range = 80  # meters
initial_speed = 112  # feet per second
gravity = 32.174  # feet per second squared

# Convert initial speed to meters per second
initial_speed_mps = initial_speed / 3.281

# Find the launch angle
launch_angle = find_launch_angle(target_range, initial_speed_mps, gravity)

if launch_angle is not None:
    print(f"To achieve a range of {target_range} meters, the launch angle is approximately {launch_angle:.2f} degrees.")
else:
    print("No solution found within the maximum iterations.")
