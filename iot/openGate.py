from machine import Pin, PWM
import time

lol = Pin(4,1)
buzzer = Pin(5, Pin.OUT)
p = PWM(lol, freq=100, duty=0)
green = Pin(13, Pin.OUT)

buzzer.value(1)
green.value(1)
time.sleep(0.5)
for i in range(0,360,1):
    p.duty(i)
    time.sleep(0.01)
buzzer.value(0)
green.value(0)



    