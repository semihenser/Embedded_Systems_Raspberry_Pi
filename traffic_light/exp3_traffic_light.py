from machine import Pin
from time import sleep
led_kirmizi = Pin(3,Pin.OUT)
led_sari = Pin(4,Pin.OUT)
led_yesil = Pin(5,Pin.OUT)
while True:
  #kirmizi 5sn yan.
  led_kirmizi.value(1)
  sleep(5)
  #kirmizi yanarken sari acilsin brilikte 2sn.
  led_sari.value(1)
  sleep(2)
  #kirmizi ve sari sonsun
  led_sari.value(0)
  led_kirmizi.value(0)
  #yesil 5sn yansin
  led_yesil.value(1)
  sleep(5)
  #yesil sonsun sarı tek basina 2sn yansin
  led_yesil.value(0)
  led_sari.value(1)
  sleep(2)
  #sari sonsun dongu basa gitsin.
  led_sari.value(0)
