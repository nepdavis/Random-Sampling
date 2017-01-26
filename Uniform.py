################################
# Samples from X,Y~U(0,1) with #
# n=100, 2d uniform random     #
# sample which is plotted      #
################################

import matplotlib.pyplot as plt

def unif(n = 100, width = 1, height = 1):

    '''Function that takes default sample number n
    to be 100, and also default x,y limits are 1.
    Creates 2d uniform sample and plots.'''
    
    x = np.random.uniform(0,width,n)
    y = np.random.uniform(0,height,n)
    
    plt.scatter(x,y,color='black')

#Calls uniform function with default parameters
unif()
