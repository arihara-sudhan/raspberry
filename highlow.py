import RPi.GPIO as GPIO
import time

# Set up the GPIO pin for the on-board LED
LED_PIN = 47  # The on-board LED is connected to GPIO47 on the Raspberry Pi

# Set the GPIO mode and configure the LED pin as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn the LED on
GPIO.output(LED_PIN, GPIO.HIGH)
print("LED is on")

# Wait for 2 seconds
time.sleep(5)

# Turn the LED off
GPIO.output(LED_PIN, GPIO.LOW)
print("LED is off")
time.sleep(5)

# Clean up the GPIO pins
GPIO.cleanup()
