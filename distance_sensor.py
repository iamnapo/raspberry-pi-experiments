from time import sleep

from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory

# HY-SRF05 (use diagram from docs, OUT pin is unused)
factory = PiGPIOFactory()  # This is used for better accuracy (needs `sudo pigpiod` first)
sensor = DistanceSensor(echo=23, trigger=24, max_distance=4, pin_factory=factory)  # max distance supported is 4 meters

while True:
    print(f"Distance to the nearest object is {sensor.distance * 100} cm")
    sleep(1)
