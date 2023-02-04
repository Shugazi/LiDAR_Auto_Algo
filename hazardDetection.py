import rplidar
import math

# Connect to the lidar
lidar = rplidar.RPLidar('/dev/ttyUSB0')

# Start the scan
lidar.start_motor()

# Set the threshold distance for a hazard
threshold_distance = 1000  # in mm

# Get the scan data
for scan in lidar.iter_scans():
    for angle, distance in scan:
        if distance <= threshold_distance:
            # Convert the angle to degrees
            angle = angle / 64.0

            # Determine the direction of the hazard
            if angle >= 0 and angle < 45:
                print("Hazard detected to the right front")
            elif angle >= 45 and angle < 90:
                print("Hazard detected to the front")
            elif angle >= 90 and angle < 135:
                print("Hazard detected to the left front")
            elif angle >= 135 and angle < 180:
                print("Hazard detected to the left")
            elif angle >= 180 and angle < 225:
                print("Hazard detected to the left back")
            elif angle >= 225 and angle < 270:
                print("Hazard detected to the back")
            elif angle >= 270 and angle < 315:
                print("Hazard detected to the right back")
            else:
                print("Hazard detected to the right")

# Stop the scan and disconnect from the lidar
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
