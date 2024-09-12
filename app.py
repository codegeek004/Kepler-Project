from flask import Flask, render_template, request, flash
from utils import MockGPIO as GPIO


app = Flask(__name__)

@app.route('/')
def index():
    distance = get_distance()
    line_status = check_line_status()
    heat_detected = detect_heat()

    #in cms
    objectThreshold = 10
    object_detected = distance < objectThreshold

    return render_template('index.html', distance = distance, line_status=line_status, heat_detected = heat_detected, object_detected=object_detected)

@app.route('/control', methods = ['POST'])
def control():
    action = request.form['action']

    if action == 'forward':
        move_forward()
    elif action == 'backward':
        move_backward()
    elif action == 'stop':
        stop_motor()
    else:
        flash('Invalid input', 'error')

    return "Input Processed Successfully"

if name == 'main':
    try:
        app.run()
    finally:
        from ultrasonic import cleanup as ultrasonic_cleanup
        from ir_sensor import cleanup as ir_cleanup
        from heat_sensor import cleanup as heat_cleanup
        from motor import cleanup as motor_cleanup

        ultrasonic_cleanup()
        ir_cleanup()
        heat_cleanup()
        motor_cleanup()



#Motor code
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
    
    
#Heat code
HPIN = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(HPIN, GPIO.IN)

def detect_heat():
    return GPIO.input(HPIN)

def cleanup():
    GPIO.cleanup()
    
    
#IR Sensor code
leftSensorPIN = 5 
middleSensorPIN = 6
rightSensorPIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(leftSensorPIN, GPIO.IN)
GPIO.setup(middleSensorPIN, GPIO.IN)
GPIO.setup(rightSensorPIN, GPIO.IN)
def check_line_status():
    left_sensor = GPIO.input(leftSensorPIN)
    middle_sensor = GPIO.input(middleSensorPIN)
    right_sensor = GPIO.input(rightSensorPIN)

    if middle_sensor == 1:
        if left_sensor == 0 and right_sensor == 0:
            return "Move Forward"
        elif left_sensor == 0 and right_sensor == 1:
            return "Turn right"
        elif left_sensor == 1 and right_sensor == 0:
            return "Turn left"
        elif left_sensor == 1 and right_sensor == 1:
            return "Move forward"
    else:
        if left_sensor == 1 and right_sensor == 0:
            return "Turn right"
        elif left_sensor == 0 and right_sensor == 1:
            return "Turn right"
        else:
            return "Stop"

def cleanup():
    GPIO.cleanup()


#ultrasonic sensor code
import time
TriggerPIN = 3
EchoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(TriggerPIN, GPIO.OUT)
GPIO.setup(EchoPIN, GPIO.IN)

def get_distance():
    GPIO.output(TriggerPIN, True)
    time.sleep(0.1)
    print('sleeping')
    GPIO.output(TriggerPIN, False)

    start_time = time.time()
    while GPIO.input(EchoPIN == 0):
        start_time = time.time()

    while GPIO.input(EchoPIN == 1):
        end_time = time.time()

    elapsed_time = end_time - start_time
    distance = (elapsed_time*34300)/2
    return distance

def cleanup():
    GPIO.cleanup()

    
    





