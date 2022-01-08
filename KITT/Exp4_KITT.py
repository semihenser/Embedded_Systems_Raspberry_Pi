from machine import Pin
from time import sleep
led_1 = Pin(0,Pin.OUT)
led_2 = Pin(2,Pin.OUT)
led_3 = Pin(3,Pin.OUT)
led_4 = Pin(4,Pin.OUT)
led_5 = Pin(5,Pin.OUT)
led_6 = Pin(6,Pin.OUT)
led_7 = Pin(7,Pin.OUT)
led_8 = Pin(8,Pin.OUT)
ledler=[led_1,led_2,led_3,led_4,led_5,led_6,led_7,led_8]
while True:
  for i in range(0,8):
    ledler[i].value(1)
    sleep(0.25)
    ledler[i].value(0)
  for j in range(7,0,-1):
    ledler[j].value(1)
    sleep(0.25)
    ledler[j].value(0)


 
