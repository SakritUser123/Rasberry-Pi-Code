import RPi.GPIO as GPIO
import time 
P_Red = 17
P_Green = 18
P_Blue = 27

def setup():
    GPIO.setmode = (GPIO.BCM)
    GPIO.setmode(GPIO.OUT,initial = GPIO.LOW)
    