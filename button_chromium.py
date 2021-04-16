from signal import pause
from subprocess import Popen

from gpiozero import Button

button = Button(15)


def visitIamNapo():
    Popen("chromium https://iamnapo.me", shell=True)


button.when_pressed = visitIamNapo

pause()
