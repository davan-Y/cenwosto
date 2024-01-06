import math

def find_initial_velocity(target_range, launch_angle, gravity):
    launch_angle_radians = math.radians(launch_angle)
    
    # Calculate initial velocity using the range formula
    initial_velocity = math.sqrt((target_range * gravity) / math.sin(2 * launch_angle_radians))
    
    return initial_velocity

# Given values
target_range = 120  # meters
launch_angle = 45  # degrees
gravity = 9.8  # meters per second squared

# Find the initial velocity
initial_velocity = find_initial_velocity(target_range, launch_angle, gravity)

print(f"To achieve a range of {target_range} meters at a launch angle of {launch_angle} degrees, the initial velocity should be approximately {initial_velocity:.2f} meters per second.")


# import math

# import math

def find_launch_angle(initial_speed, target_range, gravity):
    # Calculate launch angle using the inverse of the range formula
    launch_angle_radians = math.asin((target_range * gravity) / (initial_speed**2)) / 2
    
    # Convert radians to degrees
    launch_angle_degrees = math.degrees(launch_angle_radians)
    
    return launch_angle_degrees

# Given values
initial_speed = 34.39  # meters per second
target_range = 100.68 # meters
gravity = 9.8  # meters per second squared

# Find the launch angle
launch_angle = find_launch_angle(initial_speed, target_range, gravity)

print(f"If the initial speed is {initial_speed} meters per second and the projectile covers a distance of {target_range} meters, the launch angle is approximately {launch_angle:.2f} degrees.")


# import math

def calculate_range(initial_speed, launch_angle, gravity):
    launch_angle_radians = math.radians(launch_angle)
    return (initial_speed**2 * math.sin(2 * launch_angle_radians)) / gravity

# Given values
initial_speed = 34.39  # meters per second
launch_angle = 45  # degrees
gravity = 9.8  # meters per second squared

# Calculate the range
target_range = calculate_range(initial_speed, launch_angle, gravity)

print(f"If the initial speed is {initial_speed} meters per second and the launch angle is {launch_angle} degrees, the projectile will cover a horizontal distance of approximately {target_range:.2f} meters.")
