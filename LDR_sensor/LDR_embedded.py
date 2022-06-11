import utime
from machine import Pin, PWM
from time import sleep


led1 = Pin(15, Pin.OUT)
led2 = Pin(13, Pin.OUT)

analog_value = machine.ADC(28)


while True:
    led1.value(0)
    led2.value(0)
    reading = analog_value.read_u16()
    if reading > 750 :
        led1.value(1)
        led2.value(0)
        
        
    else:       
        led1.value(0)
        led2.value(1)
        