import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ramp_time = 8
period = 0.01
step = period / ramp_time

while True:
    brightness = 0
    while brightness < 1:
        T_on = brightness * period
        T_off = period - T_on
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        brightness += step

    brightness = 1
    while brightness > 0:
        T_on = brightness * period
        T_off = period - T_on
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        brightness -= step
