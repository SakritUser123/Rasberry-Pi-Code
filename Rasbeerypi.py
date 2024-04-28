import RPi.GPIO as GPIO
import time
LedPin = 17
def setup():
    # Set the GPIO modes to BCM Numbering.
    GPIO.setmode(GPIO.BCM)
    # sets it as output an sets to defalut when the code runs to make the ledpin off.
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)

    #main function to make it turn off and on.

    
def main():
    while True:
        seconds = 5
        print('...LED ON')
        #make the led turn on 
        GPIO.output(LedPin, GPIO.LOW)
        #0.5 second pause between blinks.
        time.sleep(0.5)
        print('...LED OFF')
        #turn off led
        GPIO.output(LedPin,GPIO.HIGH)
        time.sleep(seconds)



def destroy():
    #turns the led of after we destroy the program.
    GPIO.output(LedPin,GPIO.HIGH)
    #Cleans up code
    GPIO.cleanup()

if 5 == 5:
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()

        



   





