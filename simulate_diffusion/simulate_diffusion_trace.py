__author__ = 'Sara'
import numpy as np
import random


 
def trace(N,size,D,t):             
  """
  Generates a trajectory of 2D coordinates undergoing free diffusion.
  Input values are: the number of time steps N, the size of the frame (in pixel), the diffusion coefficient D and the width of the time steps t.
  The trace array contains the 1D time array and the 2D array of the 2 coordinates in time.
  """

  x0 = random.random()*size/2 + size/4    # the initial coordinates are random, but within the center of the image
  y0 = random.random()*size/2 + size/4
  initial_coord = ([x0,y0])  
  array_coord = np.array([x0,y0])         # initialize an array for the coordinates
  
  w = np.sqrt((2*D*t))          # in free diffusion every step is extracted from a normal distribution
                                # with width sqrt(2*D*t)
  i=0
  while i<N-1:                        # every step is created from the previous one, and added to the array of the coordinates:
    step = np.random.normal(0,w,2)    # extracts the step from the normal distribution    
    coord_i = initial_coord + step    
    initial_coord = coord_i           # the position obtained will be the initial position for the next iteration
    array_coord = np.vstack((array_coord,coord_i))    
    i += 1 
    
  time = np.arange(0,N*t,t).reshape(N,1)       # reshapes the time vector to make a column. 
  trace = np.c_[ time, array_coord]          # creates the trace array containing the time and the coordinates
  return trace
    

