from machine import Pin
from time import sleep
led = Pin(3, Pin.OUT)    
push_button1 = Pin(27, Pin.IN)  
push_button2 = Pin(22, Pin.IN)  

while True:
  led.value(0)
  logic_state1 = push_button1.value()
  logic_state2 = push_button2.value()
  
  if(logic_state1 == 1):
    led.value(1)             
  if(logic_state2 == 1):
    led.value(0)
