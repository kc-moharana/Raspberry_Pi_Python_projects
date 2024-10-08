'''
 Play Buzzer with musical notes
'''
import time, os, random
import gpiozero as io # using LED zero
led_gr = io.PWMLED(4) # make pin 4 into an output
led_red = io.PWMLED(17) #
#buz = io.Buzzer(27) #
buz = io.PWMOutputDevice(27)
duty = 0.4 # sounds good 


print("Buzzer/LED blinker using gpiozero")

print("Ctrl C to quit")


tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}


#----------------------------------------
# Nokia
#----------------------------------------

nokia= {
 'notes':['E5', 'D5', 'FS4', 'GS4', 
  'CS5', 'B4', 'D4', 'E4', 
  'B4', 'A4', 'CS4', 'E4',
  'A4'],

 'durations':[
  8, 8, 4, 4,
  8, 8, 4, 4,
  8, 8, 4, 4,
  2]
}
#-------------------------------------------
# Happy Birthday
#-------------------------------------------
HBD = {
 'notes':[
  'C4',  'C4',  
  'D4',  'C4',  'F4', 
  'E4',  'C4',  'C4',  
  'D4',  'C4',  'G4', 
  'F4',  'C4',  'C4', 
  'C5',  'A4',  'F4',  
  'E4',  'D4',  'AS4',  'AS4', 
  'A4',  'F4',  'G4', 
  'F4'],

 'durations':[
  4, 8, 
  4, 4, 4,
  2, 4, 8, 
  4, 4, 4,
  2, 4, 8,
  
  4, 4, 4, 
  4, 4, 4, 8,
  4, 4, 4,
  2]
}
#to calculate the note duration, take one second divided by the note type.
# e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.

#to distinguish the notes, set a minimum time between them.
#the note's duration + 30% seems to work well


def playtone(frequency, t):
    led_red.on()   
    buz.frequency = frequency
    buz.value = duty
    time.sleep(t)
    #buz.on()    

def bequiet(t):
    led_red.off()
    buz.off()
    print('Be quiet for', t, 'Sec')
    time.sleep(t)

def playsong(song):
    assert len(song['durations']) == len(song['notes']), "Lengths of durations and Notes mismatch"
    for i in range(len(song['notes'])):
        t = float(1/song['durations'][i])
        pauseBetweenNotes = t * 1.3

        print('Playing',song['notes'][i], 'for', t, 'Sec')
        playtone(tones[song['notes'][i]], t)        
        bequiet(pauseBetweenNotes)
    bequiet(0)


led_gr.blink(on_time=1, off_time=1, fade_in_time=0.5, fade_out_time=0.5, n=2, background=False)
playsong(nokia)