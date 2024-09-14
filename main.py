from flask import Flask, render_template, redirect, url_for, flash
import time
from machine import Pin

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

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
    """Move the motor backward for a specified duration."""
    MotorPin1.value(0)  
    MotorPin2.value(1)  
    MotorPin3.value(0)  
    MotorPin4.value(1)  
    print("Moving backward...")
    time.sleep(duration)  
    stop_motor()

def stop_motor():
    """Stop the motor."""
    MotorPin1.value(0)  
    MotorPin2.value(0)  
    MotorPin3.value(0)  
    MotorPin4.value(0)  
    print("Motor stopped.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move_forward/<int:duration>')
def move_forward_route(duration):
    try:
        move_forward(duration)
        flash(f'Motor moved forward for {duration} seconds.', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('home'))

@app.route('/move_backward/<int:duration>')
def move_backward_route(duration):
    try:
        move_backward(duration)
        flash(f'Motor moved backward for {duration} seconds.', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('home'))

@app.route('/stop')
def stop_route():
    stop_motor()
    flash('Motor stopped.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
