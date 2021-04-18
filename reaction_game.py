from random import uniform
from time import sleep

from gpiozero import LED, Button

game_led = LED(14)
break_button = Button(25)

player_1_button = Button(15)
player_1_led = LED(24)
player_2_button = Button(18)
player_2_led = LED(23)

break_button.when_pressed = lambda: exit(0)

while True:

    time_to_wait = uniform(3, 6)
    sleep(time_to_wait)

    game_led.on()

    while True:
        if player_1_button.is_pressed:
            player_1_led.on()
            break
        elif player_2_button.is_pressed:
            player_2_led.on()
            break

    game_led.off()
    sleep(2)
    player_1_led.off()
    player_2_led.off()
