import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)
print("LED ON")
GPIO.output(led_pin, GPIO.HIGH)
time.sleep(2)
print("LED OFF")
GPIO.output(led_pin, GPIO.LOW)
time.sleep(2)
GPIO.cleanup()
