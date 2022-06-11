import machine
from machine import Pin
import utime

led_1 = Pin(0, Pin.OUT)
led_2 = Pin(1, Pin.OUT)
led_3 = Pin(2, Pin.OUT)
led_4 = Pin(3, Pin.OUT)
led_5 = Pin(4, Pin.OUT)
led_6 = Pin(5, Pin.OUT)
led_7 = Pin(6, Pin.OUT)
led_8 = Pin(16, Pin.OUT)
analog_value = machine.ADC(28)

while True:
    
    reading = analog_value.read_u16()
    if reading < 2000:
        led1.value(1)
    else:
        led1.value(0)
    if 2000 < reading < 5000:
        led2.value(1)
    else:
        led2.value(0)
    if 5000 < reading < 10000:
        led3.value(1)
    else:
        led3.value(0)
    if 10000 < reading < 15000:
        led4.value(1)
    else:
        led4.value(0)
    if 15000 < reading < 20000:
        led5.value(1)
    else:
        led5.value(0)
    if 20000 < reading < 25000:
        led6.value(1)
    else:
        led6.value(0)
    if 25000 < reading < 30000:
        led7.value(1)
    else:
        led7.value(0)  
    if 30000 < reading < 35000:
        led8.value(1)
    else:
        led8.value(0)  
    


 
