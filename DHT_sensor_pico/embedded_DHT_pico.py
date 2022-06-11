from machine import Pin
from gpio_lcd import GpioLcd
from time import sleep
from dht import DHT11
led_kirmizi = Pin(16,Pin.OUT)
led_sari = Pin(18,Pin.OUT)
led_yesil = Pin(17,Pin.OUT)


pin = Pin(15,Pin.IN)
dht11 = DHT11(pin,None,dht11=True)

while True:
    sleep(1)
    T,H = dht11.read()
    if T is None:
        print(" sensor error")
    else:
        print("Temperature :" + str(T) + "C   "+ "Humidity:"+ str(H) +"%")
    sleep(1)
    if T<23:
        led_kirmizi.value(1)
        led_sari.value(0)
        led_yesil.value(0)

    elif T==23:
        led_kirmizi.value(0)
        led_sari.value(1)
        led_yesil.value(0)
    else:
        led_kirmizi.value(0)
        led_sari.value(0)
        led_yesil.value(1)