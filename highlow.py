import RPi.GPIO as GPIO
import time

# Set up the GPIO pin for the on-board LED
LED_PIN = 35  # The on-board LED is connected to GPIO35 on the Raspberry Pi Model 2 B

# Set the GPIO mode and configure the LED pin as an output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn the LED off
if input("ON/OFF")=="ON":
  print("HIGH NOW")
  GPIO.output(LED_PIN, GPIO.HIGH)
else:
  print("LOW NOW")
  GPIO.output(LED_PIN, GPIO.LOW)

time.sleep(10)
# Clean up the GPIO pins
GPIO.cleanup()
