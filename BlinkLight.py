import RPi.GPIO as GPIO
import time

LedPin = 11 #Sets what GPIO Pin the LED goes into

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)
    print ('using pin%d'%LedPin)

def loop():
    while True:
        GPIO.output (LedPin, GPIO.HIGH)
        print ('This Bitch just turned on')
        time.sleep(1)
        GPIO.output (LedPin, GPIO.LOW)
        print ('This Bitch OFF')
        time.sleep(1)

def destroy():
    GPIO.cleanup()
    print ('GPIO Pins cleared')

if __name__ == '__main__':
    print ('We starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()