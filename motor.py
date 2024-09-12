from utils import MockGPIO as GPIO
MotorPinForward = 1
MotorPinBackward = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(MotorPinForward, GPIO.OUT)
GPIO.setup(MotorPinBackward, GPIO.OUT)

def move_forward():
    GPIO.output(MotorPinForward, GPIO.HIGH)
    GPIO.output(MotorPinBackward, GPIO.LOW)

def move_backward():
    GPIO.output(MotorPinForward, GPIO.LOW)
    GPIO.output(MotorPinBackward, GPIO.HIGH)

def stop_motor():
    GPIO.output(MotorPinForward, GPIO.LOW)
    GPIO.output(MotorPinBackward, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

