from machine import Pin, PWM
import time

buzzer = Pin(5, Pin.OUT)
buzzer.value(1)
time.sleep(1)
buzzer.value(0)
