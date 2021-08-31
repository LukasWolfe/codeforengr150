import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

brightness = 1
period = 0.1

T_on = brightness * period
T_off = period - T-on

while True:
    led.value = True
    time.sleep(T_on)
    led.value = False
    time.sleep(T_off)
