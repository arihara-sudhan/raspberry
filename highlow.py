import RPi.GPIO as GPIO
import time

PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)
print("TURNED ON")
time.sleep(30)

GPIO.cleanup()
