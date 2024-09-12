from utils import MockGPIO
leftSensorPIN = 
middleSensorPIN = 
rightSensorPIN = 
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
