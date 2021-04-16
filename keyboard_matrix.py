import time

from gpiozero import DigitalInputDevice, DigitalOutputDevice

pins = [4, 15, 18, 23, 24, 25, 8, 7]  # From left to right on the keypad

cols = [DigitalOutputDevice(pin) for pin in pins[:4]]
rows = [DigitalInputDevice(pin) for pin in pins[4:]]


def readLine(line, characters):
    cols[line].on()
    for ind, row in enumerate(rows):
        if row.value == 1:
            print(characters[ind])
            break
    cols[line].off()


while True:
    readLine(0, ["1", "2", "3", "A"])
    readLine(1, ["4", "5", "6", "B"])
    readLine(2, ["7", "8", "9", "C"])
    readLine(3, ["*", "0", "#", "D"])
    time.sleep(0.25)
