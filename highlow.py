import RPi.GPIO as GPIO
import time

# Set up the GPIO pin
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Define the brightness levels
brightness_levels = [0, 25, 50, 75, 100, 75, 50, 25]

# Create the glowing animation
try:
    while True:
        for brightness in brightness_levels:
            # Set the PWM duty cycle to control the LED brightness
            pwm = GPIO.PWM(LED_PIN, 1000)
            pwm.start(brightness)
            time.sleep(0.1)
            pwm.stop()
except KeyboardInterrupt:
    # Clean up the GPIO pins
    GPIO.cleanup()
