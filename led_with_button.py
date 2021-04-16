from signal import pause

from gpiozero import LED, Button

led = LED(14)
button = Button(15)

button.when_pressed = led.on
button.when_released = led.off

pause()
