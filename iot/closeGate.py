from machine import Pin, PWM
import time

lol = Pin(4,1)
buzzer = Pin(5, Pin.OUT)
p = PWM(lol, freq=100, duty=0)
red = Pin(12, Pin.OUT)

buzzer.value(1)
red.value(1)
time.sleep(0.5)
for i in range(150,0,-1):
    p.duty(i)
    time.sleep(0.01)
buzzer.value(0)
red.value(0)
