# from gpiozero import Button
# from signal import pause
# from gpiozero import OutputDevice
# from time import sleep

# # # Define the GPIO pin for the button
# button_pin = 18
# relay_pin = 17

# # # Create a Button object
# button = Button(button_pin)
# relay = OutputDevice(relay_pin, active_high=False, initial_value=False)

# # # Define a callback function to be executed when the button is pressed
# def button_pressed():
#     print("Button pressed!")
#     relay.on()
#     sleep(2)  
#     relay.on()
    

# # # Assign the callback function to the button's when_pressed event
# button.when_pressed = button_pressed

# # # Keep the program running to listen for button presses
# pause()



# Define the GPIO pin connected to the relay
  # Change this to the actual GPIO pin you're using

# # Create an OutputDevice object for the relay

# try:
#     while True:
#         # Turn on the relay (close the switch)
#         print("Relay ON")
#         relay.on()
#         sleep(2)  # Wait for 2 seconds

#         # Turn off the relay (open the switch)
#         print("Relay OFF")
#         relay.off()
#         sleep(2)  # Wait for 2 seconds

# except KeyboardInterrupt:
#     # Clean up GPIO on Ctrl+C exit
#     relay.close()

# from gpiozero import Button
# from signal import pause
# from gpiozero import OutputDevice
# from time import sleep

# # Define the GPIO pin for the button
# button_pin = 18
# relay_pin = 17

# # Create a Button object
# button = Button(button_pin)
# relay = OutputDevice(relay_pin, active_high=False, initial_value=False)

# # Define a callback function to be executed when the button is pressed
# def button_pressed():
#     # print("Button pressed!")
#     relay.on()
#     sleep(0.2)
#     relay.off()  # Turn off the relay after 2 seconds

# # Assign the callback function to the button's when_pressed event
# button.when_pressed = button_pressed

# # Keep the program running to listen for button presses
# pause()


# from gpiozero import OutputDevice
# from time import sleep

# # Define the GPIO pin connected to the relay
# relay_pin = 17  # Change this to the actual GPIO pin you're using

# # Create an OutputDevice object for the relay
# relay = OutputDevice(relay_pin, active_high=False, initial_value=False)

# try:
#     while True:
#         # Turn on the relay (close the switch)
#         print("Relay ON")
#         relay.on()
#         sleep(2)  # Wait for 2 seconds

#         # Turn off the relay (open the switch)
#         print("Relay OFF")
#         relay.off()
#         sleep(2)  # Wait for 2 seconds

# except KeyboardInterrupt:
#     # Clean up GPIO on Ctrl+C exit
#     relay.close()



# from gpiozero import Button
# from signal import pause
# from gpiozero import OutputDevice
# from time import sleep

# # Define the GPIO pin for the button
# button_pin = 18
# relay_pin_1 = 2
# relay_pin_2 = 3
# relay_pin_3 = 4
# relay_pin_4 = 17
# initial=1



# # Create a Button object
# button = Button(button_pin)
# relay_1 = OutputDevice(relay_pin_1, active_high=False, initial_value=False)
# relay_2 = OutputDevice(relay_pin_2, active_high=False, initial_value=False)
# relay_3 = OutputDevice(relay_pin_3, active_high=False, initial_value=False)
# relay_4 = OutputDevice(relay_pin_4, active_high=False, initial_value=False)
# arr_relay=[relay_1,relay_2,relay_3,relay_4]


# # Define a callback function to be executed when the button is pressed

# def button_pressed():
#     # print("Button pressed!")
#     global initial
#     arr_relay[initial].on()
#     sleep(0.2)
#     arr_relay[initial].off()  # Turn off the relay after 2 seconds
#     initial+=1

# # Assign the callback function to the button's when_pressed event
# button.when_pressed = button_pressed

# # Keep the program running to listen for button presses
# pause()



# from gpiozero import Button
# from signal import pause
# from gpiozero import OutputDevice
# from time import sleep

# # Define the GPIO pin for the button
# button_pin = 18
# relay_pin_1 = 2
# relay_pin_2 = 3
# relay_pin_3 = 4
# relay_pin_4 = 17
# initial = 0

# # Create a Button object
# button = Button(button_pin)
# relay_1 = OutputDevice(relay_pin_1, active_high=False, initial_value=False)
# relay_2 = OutputDevice(relay_pin_2, active_high=False, initial_value=False)
# relay_3 = OutputDevice(relay_pin_3, active_high=False, initial_value=False)
# relay_4 = OutputDevice(relay_pin_4, active_high=False, initial_value=False)
# arr_relay = [relay_1, relay_2, relay_3, relay_4]

# # Define a callback function to be executed when the button is released
# def button_released():
#     global initial
#     if initial < len(arr_relay):
#         arr_relay[initial].on()
#         sleep(0.2)
#         arr_relay[initial].off()  # Turn off the relay after 0.2 seconds
#         initial += 1

# # Assign the callback function to the button's when_released event
# button.when_released = button_released

# # Keep the program running to listen for button releases
# pause()


# from gpiozero import Button
# from signal import pause
# from gpiozero import OutputDevice
# from time import sleep

# # Define the GPIO pin for the button
# button_pin = 18
# relay_pin_1 = 2
# relay_pin_2 = 3
# relay_pin_3 = 4
# relay_pin_4 = 17
# initial = 0

# # Create a Button object
# button = Button(button_pin)
# relay_1 = OutputDevice(relay_pin_1, active_high=False, initial_value=False)
# relay_2 = OutputDevice(relay_pin_2, active_high=False, initial_value=False)
# relay_3 = OutputDevice(relay_pin_3, active_high=False, initial_value=False)
# relay_4 = OutputDevice(relay_pin_4, active_high=False, initial_value=False)
# arr_relay = [relay_1, relay_2, relay_3, relay_4]

# # Define a callback function to be executed when the button is released
# def button_released():
#     global initial
#     if initial < len(arr_relay):
#         arr_relay[initial].on()
#         sleep(0.2)
#         arr_relay[initial].off()  # Turn off the relay after 0.2 seconds
#         initial += 1
#     if initial == len(arr_relay):
#         initial =0

# # Assign the callback function to the button's when_released event
# # button.when_released = button_released

# if button.is_active:
#     button_released()

# # Keep the program running to listen for button releases
# pause()




from gpiozero import Button
from gpiozero import OutputDevice
from time import sleep

# Define the GPIO pin for the button
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

# Create a Button object
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

# Flag to track whether the button has been pressed
button_1_pressed = False
button_2_pressed = False
button_3_pressed = False
button_4_pressed = False

try:
    while True:
        # Check if the button is pressed
        if button_1.is_active and not button_1_pressed:
            button_1_pressed = True
            if initial<len(arr_relay):
                arr_relay[initial].on()
                sleep(0.2)
                arr_relay[initial].off()
                initial+=1
            else:
                initial=0
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
                  # arr_relay[initial+1].on()
                  # sleep(0.2)
                  # arr_relay[initial+1].off()
                  # sleep(0.2)
                  # arr_relay[initial+2].on()
                  # sleep(0.2)
                  # arr_relay[initial+2].off()
                  # sleep(0.2)
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
                    # arr_relay[initial+1].on()
                    # sleep(0.2)
                    # arr_relay[initial+1].off()
                    # sleep(0.2)
                    # arr_relay[initial+2].on()
                    # sleep(0.2)
                    # arr_relay[initial+2].off()
                    # sleep(0.2)
                    # arr_relay[initial+3].on()
                    # sleep(0.2)
                    # arr_relay[initial+3].off()
                    # sleep(0.2)
                    # arr_relay[initial+4].on()
                    # sleep(0.2)
                    # arr_relay[initial+4].off()
                    # sleep(0.2)

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
                    # arr_relay[initial+1].on()
                    # sleep(0.2)
                    # arr_relay[initial+1].off()
                    # sleep(0.2)
                    # arr_relay[initial+2].on()
                    # sleep(0.2)
                    # arr_relay[initial+2].off()
                    # sleep(0.2)
                    # arr_relay[initial+3].on()
                    # sleep(0.2)
                    # arr_relay[initial+3].off()
                    # sleep(0.2)
                    # arr_relay[initial+4].on()
                    # sleep(0.2)
                    # arr_relay[initial+4].off()
                    # sleep(0.2)
                    # arr_relay[initial+5].on()
                    # sleep(0.2)
                    # arr_relay[initial+5].off()
                    # sleep(0.2)
                    # arr_relay[initial+6].on()
                    # sleep(0.2)
                    # arr_relay[initial+6].off()
                    # sleep(0.2)
                    # arr_relay[initial+7].on()
                    # sleep(0.2)
                    # arr_relay[initial+7].off()
                    # sleep(0.2)
                    # arr_relay[initial+8].on()
                    # sleep(0.2)
                    # arr_relay[initial+8].off()
                    # sleep(0.2)
                    # arr_relay[initial+9].on()
                    # sleep(0.2)
                    # arr_relay[initial+9].off()
                    # sleep(0.2)
                    # arr_relay[initial+10].on()
                    # sleep(0.2)
                    # arr_relay[initial+10].off()
                    # sleep(0.2)
                    # arr_relay[initial+11].on()
                    # sleep(0.2)
                    # arr_relay[initial+11].off()
                    # sleep(0.2)
                    # arr_relay[initial+12].on()
                    # sleep(0.2)
                    # arr_relay[initial+12].off()
                    # sleep(0.2)
                    # arr_relay[initial+13].on()
                    # sleep(0.2)
                    # arr_relay[initial+13].off()
                    # sleep(0.2)
                    # arr_relay[initial+14].on()
                    # sleep(0.2)
                    # arr_relay[initial+14].off()
                    # sleep(0.2)

                if initial==len(arr_relay):
                  initial=0
                else:
                   initial+=15 
            else:
                initial=0
            button_4_pressed = False

        # You can add other tasks or sleep here as needed

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    
    for relay in arr_relay:
        relay.off()




