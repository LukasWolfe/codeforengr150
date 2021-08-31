import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    for state in [True, False]:
        led.value = state
        time.sleep(0.75)
    for state in [True, True, False]:
        led.value = state
        time.sleep(1.5)
    for state in [True, False]:
        led.value = state
        time.sleep(0.75)
