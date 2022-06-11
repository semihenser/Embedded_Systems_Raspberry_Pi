from machine import Pin
from servo import Servo
import utime
pin = 21
motor = Servo(pin)

while True:
    motor.move(0)
    utime.sleep(0.5)
    motor.move(60)
    utime.sleep(0.5)
 
    