from time import sleep
from gpiozero import InputDevice
no_rain = InputDevice(18)
while True:
    if not no_rain.is_active:
        print("No rain")
    else:
        print("Raining")
        sleep(1)