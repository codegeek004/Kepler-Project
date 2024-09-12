from utils import MockGPIO
HPIN = 
GPIO.setmode(GPIO.BCM)
GPIO.setup(HPIN, GPIO.IN)

def detect_heat():
    return GPIO.input(HPIN)

def cleanup():
    GPIO.cleanup()
