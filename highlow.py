import RPi.GPIO as GPIO
import time

PIN = int(input("PIN: "))
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    print(f"Turning ON PIN {PIN}")
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(10)
    print(f"Turning OFF PIN {PIN}")
    GPIO.output(PIN, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
except Exception as e:
    print(f"An error occurred: {e}")
    GPIO.cleanup()
