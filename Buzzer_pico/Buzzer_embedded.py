from machine import Pin, PWM
from time import sleep

buzzerPIN=16
BuzzerObj=PWM(Pin(buzzerPIN))

def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):

    buzzerPinObject.duty_u16(int(65536*0.2))
    buzzerPinObject.freq(frequency)
    sleep(sound_duration)
    buzzerPinObject.duty_u16(int(65536*0))
    sleep(silence_duration)
while True:

buzzer(BuzzerObj,440,1,0.1)
buzzer(BuzzerObj,540,1,0.1)