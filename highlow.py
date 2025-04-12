import RPi.GPIO as GPIO
import time

# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Use physical pin 11 (which is GPIO 17 on the Pi)
led_pin = 11

# Set the pin as an output
GPIO.setup(led_pin, GPIO.OUT)

print("Starting LED blink loop using BOARD mode...")

try:
    while True:
        # Turn LED ON
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        time.sleep(5)

        # Turn LED OFF
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        time.sleep(5)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()
    print("GPIO cleanup done")
