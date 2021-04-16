from time import sleep

from gpiozero import LED

led = LED(14)

led.on()
sleep(2)
led.off()
