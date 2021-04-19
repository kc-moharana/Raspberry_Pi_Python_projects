import time, os
import gpiozero as io # using LED zero
led = io.LED(4) # make pin 4 into an output

print("LED blinker using gpiozero - By Mike Cook")

print("Ctrl C to quit")

while True:
 led.on()
 time.sleep(0.50)
 led.off()
 time.sleep(0.50)
