import RPi.GPIO as GPIO

# Speed Configuration
FORWARD_SPEED = 50
BACKWARDS_SPEED = 50
LEFT_P1_SPEED = 50
LEFT_P2_SPEED = 50
RIGHT_P1_SPEED = 50
RIGHT_P2_SPEED = 50

# GPIO Pins
P1_PWM_PIN = 33
P1_DIR_PIN = 24
P2_PWM_PIN = 32
P2_DIR_PIN = 16

# Motor Initilization
GPIO.setmode(GPIO.BOARD)
GPIO.setup(P1_PWM_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(P2_PWM_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(P1_DIR_PIN, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(P2_DIR_PIN, GPIO.OUT, initial=GPIO.HIGH)

# Left Side
p1 = GPIO.PWM(P1_PWM_PIN, 100.0)
p1.start(0)
# Right Side
p2 = GPIO.PWM(P2_PWM_PIN, 100.0)
p2.start(0)

def stop():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)

def quit():
    stop()
    p1.stop()
    p2.stop()
    GPIO.cleanup()

stop()

quit()