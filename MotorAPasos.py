import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

motorlA = 24 # INI
motorlB = 23 # IN2
motorlC = 25 # EN1

GPIO.setup(motorlA, GPIO.OUT)
GPIO.setup(motorlB, GPIO.OUT)
GPIO.setup(motorlC, GPIO.OUT)
print('setup complete')

for i in range (3):
    print('cycle #:' + str(1))
    GPIO.output (motorlA, GPIO.HIGH)
    GPIO.output (motorlB,GPIO.LOW)
    GPIO.output (motorlC, GPIO.HIGH )
    print("Moving forwards")
    
    sleep(3)
    GPIO.output (motorlA, GPIO.LOW)
    GPIO.output (motorlB,GPIO.HIGH)
    GPIO.output (motorlC, GPIO.HIGH)
    print("Moving backwards")


print("Stop")
GPIO.output (motorlC,GPIO.LOW)

print ("clean up")
GPIO.cleanup()