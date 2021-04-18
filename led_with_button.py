from signal import pause

from gpiozero import LED, Button

led = LED(14)
button = Button(15)

led.source = button

pause()
