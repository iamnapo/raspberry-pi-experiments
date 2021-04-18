from signal import pause
from subprocess import run

from gpiozero import Button

button = Button(15)

button.when_pressed = lambda: run(["chromium", "https://iamnapo.me"])

pause()
