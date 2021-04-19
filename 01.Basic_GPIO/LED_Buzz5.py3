import time, os, random
import gpiozero as io # using LED zero
led_gr = io.PWMLED(4) # make pin 4 into an output
led_red = io.PWMLED(17) #
#buz = io.Buzzer(27) #
buz = io.PWMOutputDevice(27)
print("LED blinker using gpiozero - By Mike Cook")

print("Ctrl C to quit")

while True:
 #led_gr.blink(on_time=1, off_time=1, fade_in_time=0.5, fade_out_time=0.5, n=2, background=False)
 #time.sleep(0.50)
 led_red.blink(on_time=1, off_time=1, fade_in_time=0.5, fade_out_time=0.5, n=2, background=False)
 time.sleep(0.50)
 #buz.beep(on_time=3, off_time=1, n=2, background=False)
 for f in [2031,58,12,1001,98,650] :
  buz.frequency =f
  buz.value = round(random.uniform(0,1),2)
  buz.on()
  time.sleep(0.50)
  buz.off()
  print("Freq: ", buz.frequency)


