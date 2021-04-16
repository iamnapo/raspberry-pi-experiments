from signal import pause

from gpiozero import LED, DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory

led = LED(14)

# HY-SRF05 (use diagram from docs, OUT pin is unused)
factory = PiGPIOFactory()  # This is used for better accuracy (needs `sudo pigpiod` first)
sensor = DistanceSensor(echo=23, trigger=24, max_distance=4, pin_factory=factory, threshold_distance=0.2)  # max distance supported is 4 meters

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

pause()
