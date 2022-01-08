from machine import Pin
from time import sleep
led_kirmizi = Pin(3,Pin.OUT)
while True:
  sleep(1)
  led_kirmizi.value(1)
  sleep(1)
  led_kirmizi.value(0)