import RPi.GPIO as GPIO
import time

PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

for i in range(100):
    print("ON")
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(1)
    print("OFF")
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()
