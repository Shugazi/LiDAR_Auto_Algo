import rplidar

# Connect to the lidar
lidar = rplidar.RPLidar('/dev/ttyUSB0')

# Start the scan
lidar.start_motor()
print("starting")

num = 0
threshold_distance = 350
try:
    for scan in lidar.iter_scans():
        num += 1
        hazard_detected = False
        for intensity, angle, distance in scan:
            if distance <= threshold_distance:
                print(angle)
                if 22 <= angle < 60:
                    print("Hazard detected to the right front")
                    print("Moving to the Left \n")

                elif 325 <= angle or angle < 22:
                    print("Hazard detected to the front")
                    print("Moving to the Right\n")

                elif 315 <= angle < 337:
                    print("Hazard detected to the left front")
                    print("Moving to the Right\n")

except KeyboardInterrupt:
    pass

# Stop the scan and disconnect from the lidar
lidar.stop()
lidar.stop_motor()
lidar.disconnect()