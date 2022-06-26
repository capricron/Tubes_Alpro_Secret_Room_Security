from machine import Pin, PWM
import time

lol = Pin(4,1)
buzzer = Pin(5, Pin.OUT)
p = PWM(lol, freq=100, duty=0)
green = Pin(13, Pin.OUT)

p.duty(0
)
green.value(0)
