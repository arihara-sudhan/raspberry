import RPi.GPIO as GPIO
import time

PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

print("ON")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(30)

GPIO.cleanup()
