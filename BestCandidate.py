##########################################
# Mitchell's Best Candidate              #
# random sample written in Python.       #
# Takes parameters candidate sample size #
# and general sample size. Plots 2d      #
# sample.                                #
##########################################


import math
import random
import matplotlib.pyplot as plt


def dist(a, b):

    '''Distance fn that equates standard Euclidean distance
    between two 2d points'''

    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)



def findClosest(plst, samples):

    '''This is a helper function returns the minimum distance between 
    a point and all of the points in the samples list, then returns the
    largest minimum point location'''
    
    distances = []    
    
    for i in samples:
        
        distance = [dist(i,j) for j in plst]
        distances.append(min(distance))
        
    mx = [i for i, j in enumerate(distances) if j == max(distances)]
        
    return mx[0]
    



def sample(plst, k, w, l):

    '''This function randomly generates numCandidates points and returns 
    the point with the maximum distance to the point_list'''

    samples = [[random.random()*w, random.random()*l] for i in range(k)]
    
    max_pos = findClosest(plst, samples)
    
    return samples[max_pos]



def main(n, w, l, k):

    '''Main function that sets up beginning sample point and calls
    all other functions. Loops through process n-1 times. Takes
    parameters n sample size, w x-limit from 0, l y-limit from
    0, and k candidate sample size for each iteration. Returns list
    with length n of all finalized points'''
    
    plst = []
    
    plst.append([random.random()*w,random.random()*l])
    
    while len(plst) < n:
        
        plst.append(sample(plst, k, w, l))
    
    return plst
    
    

lst = main(100, 1, 1, 10)

x = [i[0] for i in lst]
y = [i[1] for i in lst]

plt.scatter(x,y,color='black')
