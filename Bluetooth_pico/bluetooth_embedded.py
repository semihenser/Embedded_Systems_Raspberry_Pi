from machine import Pin, UART

uart0 = UART(0, 9600)
led = Pin(15, Pin.OUT)
led.value(0)

while True:
    
    if uart0.any() > 0:
        data = uart0.read(1)
        if "a" in data:
            led.value(1)
            uart0.write("LED ON \r\n")
        elif "b" in data:
            led.value(0)
            uart0.write("LED OFF \r\n1")