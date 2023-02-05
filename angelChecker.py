import rplidar

# Connect to the lidar
lidar = rplidar.RPLidar('/dev/ttyUSB0')

# Start the scan
lidar.start_motor()
print("starting")

num = 0
try:
    for scan in lidar.iter_scans():
        num += 1
        hazard_detected = False
        for intensity, angle, distance in scan:
            print(angle)
except KeyboardInterrupt:
    pass

# Stop the scan and disconnect from the lidar
lidar.stop()
lidar.stop_motor()
lidar.disconnect()