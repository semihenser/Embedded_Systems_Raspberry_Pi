from machine import Pin
from time import sleep
led = Pin(3, Pin.OUT)    
push_button = Pin(27, Pin.IN)  

while True:
  led.value(0)
  logic_state=0
  logic_state = push_button.value()
  
  if (logic_state == 1):     
      led.value(1)           
  else :                       
      led.value(0)             