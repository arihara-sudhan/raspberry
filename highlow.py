import RPi.GPIO as GPIO
import time

PIN = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

print("ON")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(3)
print("OFF")
GPIO.output(PIN, GPIO.LOW)
time.sleep(3)
print("ON")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(3)
print("OFF")
GPIO.output(PIN, GPIO.LOW)
time.sleep(3)

GPIO.cleanup()
