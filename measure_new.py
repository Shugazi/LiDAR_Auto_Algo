#!/usr/bin/env python3
'''Records measurments to a given file. Usage example:

$ ./record_measurments.py out.txt'''
import sys
from rplidar import RPLidar
import json

PORT_NAME = '/dev/ttyUSB0'


def run(path):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    outfile = open(path, 'w')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurment in lidar.iter_measurments():
            # We need a data structure so we will use dictionary
            data = {
                'intensity': measurment[1],
                'angle': measurment[2],
                'distance': measurment[3],
            }
            # Write the dictionary as a JSON string to the file
            outfile.write(json.dumps(data) + '\n')

    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    outfile.close()


if __name__ == '__main__':
    run(sys.argv[1])
