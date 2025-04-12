import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

print("Turning ON pin 11")
GPIO.output(11, GPIO.HIGH)
time.sleep(10)

print("Turning OFF pin 11")
GPIO.output(11, GPIO.LOW)
GPIO.cleanup()
