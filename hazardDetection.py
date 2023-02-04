import rplidar
import math

# Connect to the lidar
lidar = rplidar.RPLidar('/dev/ttyUSB0')

# Start the scan
lidar.start_motor()
print("starting")
# Set the threshold distance for a hazard
threshold_distance = 200  # in mm

# Get the scan data
for scan in lidar.iter_scans(max_buf_meas=100):
    for deez, angle, distance in scan:
        if distance <= threshold_distance:
            print(angle)
            # Determine the direction of the hazard
            if 0 <= angle < 45:
                print("Hazard detected to the right front")
                print("Moving to the Left \n")
            elif 45 <= angle < 90:
                print("Hazard detected to the front")
                print("Moving to the Right\n")

            elif 90 <= angle < 135:
                print("Hazard detected to the left front")
                print("Moving to the Right\n")

            elif 135 <= angle < 180:
                print("Hazard detected to the left")
            elif 180 <= angle < 225:
                print("Hazard detected to the left back")
            elif 225 <= angle < 270:
                print("Hazard detected to the back")
            elif 270 <= angle < 315:
                print("Hazard detected to the right back")
            elif 315 <= angle < 360:
                print("Hazard detected to the right")
    print("Going Forward! \n")


# Stop the scan and disconnect from the lidar
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
