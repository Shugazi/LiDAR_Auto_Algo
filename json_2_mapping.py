import json
import numpy as np
import matplotlib.pyplot as plt

# Read data from file that measure_new.py creates
data_list = []
with open("test.json") as f:
    for line in f:
        data_list.append(json.loads(line))

# Extract necessary fields from the json
angle = []
distance = []
for d in data_list:
    angle.append(d['angle'])
    distance.append(d['distance'])

# Convert to numpy arrays
angle = np.array(angle)
distance = np.array(distance)

# Convert angle and distance to x and y coordinates
x = distance * np.sin(np.deg2rad(angle))
y = distance * np.cos(np.deg2rad(angle))

# Create 2D scatter plot
plt.scatter(x, y, s=1)
plt.xlabel('X (mm)')
plt.ylabel('Y (mm)')
plt.axis('equal')
plt.show()
