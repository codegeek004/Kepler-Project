from machine import Pin
import time

# Pin setup
MotorPin1 = Pin(13, Pin.OUT)  
MotorPin2 = Pin(12, Pin.OUT)
MotorPin3 = Pin(11, Pin.OUT)
MotorPin4 = Pin(10, Pin.OUT)

def move_forward(duration):
    """Move the motor forward for a specified duration."""
    MotorPin1.value(1) 
    MotorPin2.value(0)  
    MotorPin3.value(1)  
    MotorPin4.value(0)  
    print("Moving forward...")
    time.sleep(duration)  
    stop_motor()
    
def move_backward(duration):
    """Move the motor forward for a specified duration."""
    MotorPin1.value(0)  
    MotorPin2.value(1)  
    MotorPin3.value(0)  
    MotorPin4.value(1)  
    print("Moving forward...")
    time.sleep(duration)  
    stop_motor()

def stop_motor():
    """Stop the motor."""
    MotorPin1.value(0)  
    MotorPin2.value(0)  
    MotorPin3.value(0)  
    MotorPin4.value(0)  
    print("Motor stopped.")


if __name__ == '__main__':
    try:
        move_forward(4)  
    except KeyboardInterrupt:
        stop_motor()  
        print("Stopped by user.")
