from utils import MockGPIO
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

