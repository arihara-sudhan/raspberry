import RPi.GPIO as GPIO
import time

PIN = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)
time.sleep(30)

GPIO.cleanup()
