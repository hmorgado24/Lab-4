#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import json

GPIO.setwarnings(False)

ledpin1 = 13
ledpin2 = 19
ledpin3 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin1, GPIO.OUT)
GPIO.setup(ledpin2, GPIO.OUT)
GPIO.setup(ledpin3, GPIO.OUT)

pwm1 = GPIO.PWM(ledpin1, 100)
pwm2 = GPIO.PWM(ledpin2, 100)
pwm3 = GPIO.PWM(ledpin3, 100)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

while True:
  with open("jsonstor.txt", 'r') as f:
    data = json.load(f)
    pwm = str(data['slider1'])
    led = str(data['LED'])

    if led == 1 :
      pwm1.ChangeDutyCycle(pwm)
      time.sleep(.1)
    if led == 2 :
      pwm2.ChangeDutyCycle(pwm)
      time.sleep(.1)
    if led == 3 :
      pwm3.ChangeDutyCycle(pwm)
      time.sleep(.1)

pwm1.stop()
pwm2.stop()
pwm3.stop()

GPIO.cleanup()