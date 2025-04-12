import RPi.GPIO as GPIO
import time

PIN = int(input("PIN: "))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

print("Turning ON pin 11")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(10)

print("Turning OFF pin 11")
GPIO.output(PIN, GPIO.LOW)
GPIO.cleanup()
