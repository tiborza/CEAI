"""
Separation of 2 groups of points in a 2D space with a line that crosses the origin
@author: tibor.zavadil
"""

import csv
import matplotlib.pyplot as plt
from math import atan2, pi


# Read data
# ---------

# Coordinates
x = []
y = []
datafile  = open('linsep-traindata.csv', "r")
dataraw = csv.reader(datafile)
for row in dataraw:
    x.append(float(row[0]))
    y.append(float(row[1]))    
#print(x,y)

# Labels
l = []
lfile  = open('linsep-trainclass.csv', "r")
lraw = csv.reader(lfile)
for row in lraw:
    l.append(int(row[0]))    
#print(l)

# Split data by label
x1=[]
y1=[]
x2=[]
y2=[]
index = 0
for label in l:
    if label==-1:
        x1.append(x[index])
        y1.append(y[index])
    else:
        x2.append(x[index])
        y2.append(y[index])
    index = index + 1
#print(x1, y1, x2, y2)        

# Plot all points
plt.plot(x1, y1, 'ro', x2, y2, 'bo')


# Find corner points
# ------------------

# Calculate angles of the lines going from the origin to each point
u1 = [atan2(y,x) for x, y in zip(x1, y1)]
u2 = [atan2(y,x) for x, y in zip(x2, y2)]

# Find the minimum and maximum angle in each group (+ corresponding indeces)
maxu1 = max(u1)
minu1 = min(u1)
maxu2 = max(u2)
minu2 = min(u2)
imaxu1 = u1.index(maxu1)
iminu1 = u1.index(minu1)
imaxu2 = u2.index(maxu2)
iminu2 = u2.index(minu2)

# Plot lines to the border points
plt.plot([0, x1[iminu1]], [0, y1[iminu1]], 'r', [0, x1[imaxu1]], [0, y1[imaxu1]], 'r')
plt.plot([0, x2[iminu2]], [0, y2[iminu2]], 'b', [0, x2[imaxu2]], [0, y2[imaxu2]], 'b')


# Plot separation line
# --------------------

# In each group, all points lie to the left from the minimum angle and to the right from the maximum angle.
# Therefore the angle of separation line must be bigger than the max angle and smaller than the min angle in both groups.

# Max angle of the separation line
if maxu1 > maxu2:
    xmaxU = x1[imaxu1]
    ymaxU = y1[imaxu1]
else:
    xmaxU = x2[imaxu2]
    ymaxU = y2[imaxu2]
plt.plot([-xmaxU, xmaxU], [-ymaxU, ymaxU], 'k--')

# Min angle of the separation line
if minu1 < minu2 + pi:  # adding pi due to quandrant change
    xminU = x1[iminu1]
    yminU = y1[iminu1]
else:
    xminU = x2[iminu2]
    yminU = y2[iminu2]
plt.plot([-xminU, xminU], [-yminU, yminU], 'k--')

# Plot the optimal seperation line
plt.plot([(xminU - xmaxU)/2 , (xmaxU - xminU)/2], [(yminU - ymaxU)/2, (ymaxU - yminU)/2], 'g', lw=2)
