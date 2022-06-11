from machine import Pin,ADC,PWM
from time import sleep

led_kirmizi = Pin(16,Pin.OUT)
led_yesil = Pin(17,Pin.OUT)
led_kirmizi2 = Pin(25,Pin.OUT)
analogPin= ADC(28)
moisture_val=0

while True:
    moisture_val=analogPin.read_u16()
    if moisture_val>50000:
        print("deger:",moisture_val)
        led_kirmizi.value(1)
        led_yesil.value(0)
  
    else:
        print("deger:",moisture_val)
        led_kirmizi.value(0)
        led_yesil.value(1)
