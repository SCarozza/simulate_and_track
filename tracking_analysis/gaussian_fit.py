__author__ = 'Sara'

import numpy as np
import csv
import scipy.optimize as optimize
from numpy import unravel_index
import IO




def gauss2D((x,y),xc,yc,A,sx,sy,b):
  """
  Defines a 2D Gaussian function, given the arrays x and y and the Gaussian peak parameters: the amplitude A, 
  the standard deviations in x and y directions sx, sy and the offset b.
  The Gaussian function has to be projected in 1D to be used later as fitting function.
  """
  
  gauss = b + A*np.exp((-1/2)*((x-xc)/sx)**2)*np.exp((-1/2)*((y-yc)/sy)**2)
  gauss = gauss.ravel()     # projected to 1D
  return gauss
  


  
def fit_frame(frame):
  """
  Performs a Gaussian fit on an image (frame) containing a peak. 
  The gauss2D function is used for the fit, and guesse must be given for the fit parameters (coordinates of the peak x and y, 
  amplitude and offset of the peak, width of the peak in x and y directions). The coordinates, amplitude and offset are calculated 
  from the image, while the widths (harder to calculate) are given a default value 1.
  The function returns an array containing the best fit parameters and the fit function.
  """
    
  size = np.sqrt(frame.size)    # calculates the size of the frame
  x = np.arange(0,size)         # creates x and y arrays
  y = np.arange(0,size)
  data = frame.ravel()            # 1D projection of the data in the frame
  x,y = np.meshgrid(x,y)

  coordguess = unravel_index(np.argmax(frame), frame.shape)   # creates an array with the x and y coordinates of the maximum pixel in the frame
                                                              # argmax gives the max value in flattened array, unravel_index is to reobtain the max x and y
  xguess = coordguess[1]                                      # (for some reason x and y got exchanged)
  yguess = coordguess[0]
  bguess = np.amin(data)
  aguess = np.amax(data) - bguess    # amplitude = value of the most intense pixel (- offset)
  x0 = np.array([xguess, yguess, aguess, 1.0, 1.0, bguess])    # array with parameters to guess (xc, yc, A, wx, wy, offset)  

  fit_par, fit_cov = optimize.curve_fit(gauss2D, (x,y), data, x0, sigma=None)   # optimize.curve_fit returns a tuple containing two arrays,
                                                                              # containing the best fit parameters and the covariances.
                                                                              # Here I divide them
  fit = gauss2D((x,y), *fit_par)   # the fit function is rebuilt using the best fit parameters
  fit = fit.reshape(size,size) 
 
  return fit_par, fit
  
  
  
  
def fit_movie(filename):         
  """
  Given a movie, finds in each frame the Gaussian peak and fits it.
  The coordinates of the peak obtained in each frame are collected in a trace.
  """   
  
  reader = csv.reader(open(filename +'Info','rb'))   # opens the movie metafile and reads infos
  Info = dict(reader)
  N = int(Info["trace length"])
  size = int(Info["size frames"])
  coordfit = np.zeros(shape=(N,2))        # initializes an array for the coordinates
  
  for i in range(0,N):          # fills the array with the coordinates of each time step
    framei = IO.open_frame(filename,int(i),size)    # opens the ith frame
    fit_par = fit_frame(framei)[0]    # fits the ith frame with fit_frame, that returns the fit parameters
    x = fit_par[0]                    # the first two fit parameters are the x and y coordinates of the Gaussian peak
    y = fit_par[1]
    coordfit[i] = [x,y]     # fills ith position in the array with the ith coordinates
    i=+1
    
  time = np.arange(0,N,1).reshape(N,1)     # reshapes the t array to collumn
  fitted_trace = np.c_[ time, coordfit]        # creates a trace array with the time and the coordinates
   
  return fitted_trace
  
  

    

  
  
     
