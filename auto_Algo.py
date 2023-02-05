import rplidar

# Connect to the lidar
lidar = rplidar.RPLidar('/dev/ttyUSB0')

# Start the scan
lidar.start_motor()
print("starting")
# Set the threshold distance for a hazard
threshold_distance = 200  # in mm
num = 0
try:
    for scan in lidar.iter_scans():
        num += 1
        hazard_detected = False
        for intensity, angle, distance in scan:
            # check if there is a hazard
            if distance <= threshold_distance:
                hazard_detected = True
                # convert angle to servo duty cycle
                print("Avoding obstacle\n")
        # drive forward if no hazards are detected
        if not hazard_detected:
            print(f"Driving Forward {num}")
except KeyboardInterrupt:
    pass

# Stop the scan and disconnect from the lidar
lidar.stop()
lidar.stop_motor()
lidar.disconnect()
