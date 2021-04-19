import time, os
import gpiozero as io # using LED zero
led_gr = io.LED(4) # make pin 4 into an output
led_red = io.LED(17) #
print("LED blinker using gpiozero - By Mike Cook")

print("Ctrl C to quit")

while True:
 led_gr.on()
 time.sleep(0.50)
 led_gr.off()
 led_red.on()
 time.sleep(0.50)
 led_red.off()


