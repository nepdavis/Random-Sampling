#################################
# Plots a standard sample of    #
# n=100 coordinates that are    #
# all equidistant of each other #
# so that a comparison serves   #
# for random samples.           #
#################################

import math
import matplotlib.pyplot as plt

def dist(a, b):
    '''Returns Euclidean distance between two
    inputted 2d coordinates'''

    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

#Creates x
x = []
for i in range(10):
    x.extend(([(i)*.11111111111])*10)

#Creates y
y = [0,.1111111111,.2222222222,.3333333333,.4444444444,.5555555555,
     .6666666666,.7777777777,.8888888888,.9999999999]*10

plt.scatter(x,y,color='black')
