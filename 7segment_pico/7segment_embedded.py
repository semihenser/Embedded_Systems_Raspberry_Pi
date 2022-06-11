from machine import Pin
from time import sleep
led_kirmizi = Pin(20,Pin.OUT)
#############################
sag_ust=Pin(16,Pin.OUT)#orta
ust=Pin(17,Pin.OUT)#sol ust
sol_ust=Pin(18,Pin.OUT)#ust
orta=Pin(19,Pin.OUT)#sag ust
alt=Pin(13,Pin.OUT)#alt
sag_alt=Pin(14,Pin.OUT)#alt
nokta=Pin(15,Pin.OUT)#sol alt
sol_alt=Pin(12,Pin.OUT)#nokta
def sıfır():
    sag_ust.value(1)
    ust.value(1)
    sol_ust.value(1)
    alt.value(1)
    sag_alt.value(1)
    sol_alt.value(1)
def bir():
    sag_alt.value(1)
    sag_ust.value(1)
def iki():
    ust.value(1)
    orta.value(1)
    sag_ust.value(1)
    sol_alt.value(1)
    alt.value(1)
def uc():
    orta.value(1)
    sag_ust.value(1)
    sag_alt.value(1)
    ust.value(1)
    alt.value(1)
def dort():
    sag_ust.value(1)
    sol_ust.value(1)
    sag_alt.value(1)
    orta.value(1)
def bes():
    ust.value(1)
    sol_ust.value(1)
    orta.value(1)
    alt.value(1)
    sag_alt.value(1)
def altı():
    ust.value(1)
    sol_ust.value(1)
    orta.value(1)
    alt.value(1)
    sag_alt.value(1)
    sol_alt.value(1)
def yedi():
    ust.value(1)
    sag_alt.value(1)
    sag_ust.value(1)
def sekiz():
    sag_ust.value(1)
    ust.value(1)
    sol_ust.value(1)
    orta.value(1)
    alt.value(1)
    sag_alt.value(1)
    sol_alt.value(1)
def dokuz():
    sag_ust.value(1)
    ust.value(1)
    sol_ust.value(1)
    orta.value(1)
    alt.value(1)
    sag_alt.value(1)
    nokta.value(1)
def clear():
    orta.value(0)
    sol_ust.value(0)
    ust.value(0)
    sag_ust.value(0)
    sag_alt.value(0)
    alt.value(0)
    sol_alt.value(0)
    nokta.value(0)
def A():
    ust.value(1)
    orta.value(1)
    sag_ust.value(1)
    sol_ust.value(1)
    sol_alt.value(1)
    sag_alt.value(1)
    sleep(1)
    clear()     
while True:
  clear()
  led_kirmizi.value(1)
  sleep(0.2)
  led_kirmizi.value(0)
  sıfır()
  sleep(1)
  clear()
  ###
  bir()
  sleep(1)
  clear()
  ###
  iki()
  sleep(1)
  clear()
  ###
  uc()
  sleep(1)
  clear()
  ###
  dort()
  sleep(1)
  clear()
  ###
  bes()
  sleep(1)
  clear()
  ###
  altı()
  sleep(1)
  clear()
  ###
  yedi()
  sleep(1)
  clear()
  ###
  sekiz()
  sleep(1)
  clear()
  ###
  dokuz()
  sleep(1)
  clear()
  A()
  ###
  

