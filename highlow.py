import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(1)  # Wait for 1 second
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(1)  # Wait for 1 second
GPIO.cleanup()
