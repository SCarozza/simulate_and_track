__author__ = 'Sara'
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize



def MSD(trace):
  """
  Given a trace (coordinates and time), calculates the Mean Square Displacement (MSD) array. 
  The array contains the time delays and the square displacements averaged for each given time delay. 
  """

  array = np.zeros(3)    # initializes an array
  N = trace.shape[0]
  for j in range (1,N):
    count = 0
    sum = 0
    for i in range (0,N-1):   # the array of displacements squared (rsq) is calculated 
      if (i+j) <= N-1:                   # for a fixed j (time step), fo every i:
          xi = trace[int(i), 1]          # rsq = sum over j of (x(i+j)-x(i))^2 + (y(i+j)-y(i))^2
          xiplusj = trace[int(j+i), 1]
          yi = trace[int(i), 2]
          yiplusj = trace[int(j+i), 2]
          ti = trace[int(i),0]
          tiplusj = trace[int(i+j), 0]
          a = (xiplusj-xi)**2+(yiplusj-yi)**2
          sum = sum+a                     
          deltat = (tiplusj-ti)        # and deltat = t(i+j)-t(i): it's the amplitude of the j step in time unit
          count =count+1               # saves the number of couples (i and i+j steps) that there are for the current j step
    array = np.vstack((array,[deltat, sum, count]))  # creates an array of the rsqs and their correspondent delta t and number of couples

  array_deltat = array[1:,0]             # the first point in the array (0,0) is excluded
  array_rsq = array[1:,1]/array[1:,2]    # divides each rsq by the number of couples (used as weight)  
  MSD = np.vstack((array_deltat, array_rsq))     # creates the MSD array, formed by the rsq and delta_t values        
  
  return MSD
  
  
  
  
  
def MSD_func(t,D,s):  
  """
  Defines the MSD in function of the diffusion parameters.
  For a 2D free diffusing motion: MSD (t) = 4Dt + (positional accuracy)^2
  where t is the time delay considered within the trace.
  """     
    
  MSD = s**2 + 4*D*t    
  return MSD
    




def fit_MSD(array_MSD):           
  """
  Given a MSD array of a trace, fits the MSD with the function MSD_func and obtains the diffusion coefficient D (and the positional
  accuracy s, which I don't use here). 
  Usually only the first 10% of the points is used for the MSD fit, because for large time delays the contribute of the noise in the diffusion dominates on 
  the dependence of D on the time delay t. However, it is good to use not less than 10 points to obtain a precise fit, so 10 points will be used by default
  if the trace length is <100 points.
  """
  
  N = array_MSD.shape[1]     # calculated the number of points in the MSD plot  
  if N <= 100:               # it is good practice to take only the first 10% of the MSD points (N/10)
     n = 10                  # unless the trace is less than 100 points long (we want to use at least 10 points anyway)
  else: 
    n = N/10                           
  t = array_MSD[0,:n]
  MSD = array_MSD[1,:n]
  
  x0 = ([1,1])              # guess for the parameters used in MSD_func
  fit_par, fit_cov = optimize.curve_fit(MSD_func, t, MSD, x0)     
  fit = MSD_func(t, fit_par[0], fit_par[1])     #rebuilds the fit function, using the best fit parameters
  return fit_par, fit





def plot_MSD(array_MSD, MSD_fit, imagename):
  """
  Generates two plots: the first one contains MSD curve, the second one shows the MSD curve overlapped to its fit.
  As only the first points of a MSD trace are used for the fit, the second plot contains only the first part of the
  MSD array. The plots are saved to a .png file.
  """

  t = array_MSD[0,:]           # extracts t and MSD from the MSD_array
  MSD = array_MSD[1,:]  
  
  plt.figure(1)                # first plot: MSD trace
  plt.subplot(211)
  plt.xlabel('deltat')
  plt.ylabel('MSD')
  plt.title("MSD plot")
  plt.plot(t,MSD)
  
  l = MSD_fit.shape[0]          # extracts the length of the fit trace   
  t = array_MSD[0,:l]           # for the second plot I use only the first part of MSD, t
  MSD = array_MSD[1,:l] 
   
  plt.subplot(212)             # second plot: initial part of the MSD trace and fit    
  plt.plot(t,MSD, marker = 'o')        
  plt.plot(t,MSD_fit)
  plt.xlabel('deltat')
  plt.ylabel('MSD')
  plt.title("MSD plot and fit")
  plt.subplots_adjust(top=2.0)  
  
  plt.savefig(imagename, bbox_inches='tight')    # without specifying bbox_inches, subplots tend to overlap

    

  
    
          

  