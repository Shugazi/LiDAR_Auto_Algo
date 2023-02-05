import rplidar

# Connect to the lidar
lidar = rplidar.RPLidar('/dev/ttyUSB0')

# Start the scan
lidar.start_motor()
print("starting")
# Set the threshold distance for a hazard
threshold_distance = 200  # in mm
### All the Motors code -------------------------
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


#  Motor Direction Defintions
def forward():
    GPIO.output(P1_DIR_PIN, GPIO.LOW)
    GPIO.output(P2_DIR_PIN, GPIO.LOW)
    p1.ChangeDutyCycle(FORWARD_SPEED)
    p2.ChangeDutyCycle(FORWARD_SPEED)


def backwards():
    GPIO.output(P1_DIR_PIN, GPIO.HIGH)
    GPIO.output(P2_DIR_PIN, GPIO.HIGH)
    p1.ChangeDutyCycle(BACKWARDS_SPEED)
    p2.ChangeDutyCycle(BACKWARDS_SPEED)


def left():
    GPIO.output(P1_DIR_PIN, GPIO.LOW)
    GPIO.output(P2_DIR_PIN, GPIO.HIGH)
    p1.ChangeDutyCycle(LEFT_P1_SPEED)
    p2.ChangeDutyCycle(LEFT_P2_SPEED)


def right():
    GPIO.output(P1_DIR_PIN, GPIO.HIGH)
    GPIO.output(P2_DIR_PIN, GPIO.LOW)
    p1.ChangeDutyCycle(RIGHT_P1_SPEED)
    p2.ChangeDutyCycle(RIGHT_P2_SPEED)


def stop():
    p1.ChangeDutyCycle(0)
    p2.ChangeDutyCycle(0)


def quit():
    stop()
    p1.stop()
    p2.stop()
    GPIO.cleanup()


### All Yessir -----------------------------------


num = 0
try:
    for scan in lidar.iter_scans():
        num += 1
        hazard_detected = False
        for intensity, angle, distance in scan:

            # check if there is a hazard
            if distance <= threshold_distance:
                hazard_detected = True
                print(angle)

                if 22 <= angle < 60:
                    print("Hazard detected to the right front")
                    print("Moving to the Left \n")
                    left()

                elif 325 <= angle or angle < 22:
                    print("Hazard detected to the front")
                    print("Moving to the Right\n")
                    right()

                elif 315 <= angle < 337:
                    print("Hazard detected to the left front")
                    print("Moving to the Right\n")
                    right()

        # drive forward if no hazards are detected
        if not hazard_detected:
            print(f"Driving Forward {num}")
            forward()
except KeyboardInterrupt:
    pass

# Stop the scan and disconnect from the lidar
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
