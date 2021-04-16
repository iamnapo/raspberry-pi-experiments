from time import sleep

import Adafruit_DHT

pin = 14

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
    print(f"Temperature: {temperature}°C | Humidity: {humidity}%")
    sleep(2)
