from gpiozero import Button
from time import sleep

# Define the GPIO pins for the keypad rows and columns
rows = [16, 20, 21, 26]  # GPIO pin numbers for rows
cols = [5, 6, 13, 19]    # GPIO pin numbers for columns
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Create Button objects for each row
row_buttons = [Button(row, bounce_time=0.5) for row in rows]

# Create Button objects for each column
col_buttons = [Button(col, bounce_time=0.5) for col in cols]

def read_key():
    for col_num, col_button in enumerate(col_buttons):
        print(f"Waiting for column {col_num} press...")
        # Activate the current column
        print('waiting')
        col_button.wait_for_press()
        print(f"State of column {col_num} button: {col_button.is_pressed}")

        for row_num, row_button in enumerate(row_buttons):
            if row_button.is_pressed:
                print('waiting aaagaya')
                return keys[row_num][col_num]
        col_button.wait_for_release()
    return None

def perform_action(key):
    # Add your specific actions based on the keypress
    print(f'Performing action for key: {key}')

while True:
    print("hjb")
    key = read_key()
    if key:
        perform_action(key)
    sleep(0.1)
