import RPi.GPIO as GPIO
import time

PIN = int(input("PIN: "))
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

print(f"Turning ON PIN {PIN}")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(10)

print(f"Turning OFF PIN {PIN}")
GPIO.output(PIN, GPIO.LOW)
GPIO.cleanup()
