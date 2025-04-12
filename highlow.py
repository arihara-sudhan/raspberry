import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

print("Starting LED blink loop...")

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        time.sleep(5)

        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        time.sleep(5)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()
    print("GPIO cleanup done")
