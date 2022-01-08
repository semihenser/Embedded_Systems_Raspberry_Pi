from machine import Pin
from time import sleep

led_red= Pin(5,Pin.OUT)
led_green= Pin(4,Pin.OUT)
led_blue= Pin(3,Pin.OUT)

def set_rgb(x,y,z):
  led_red.value(x)
  led_green.value(y)
  led_blue.value(z)

while True:
  set_rgb(1,0,0) #kirmizi
  sleep(1)

  set_rgb(0,1,0) #yesil
  sleep(1)
  
  set_rgb(0,0,1) #mavi
  sleep(1)

  set_rgb(1,1,1) #beyaz
  sleep(1)


  set_rgb(0,0,0) #sonuk
  sleep(1)
