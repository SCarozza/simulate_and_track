__author__ = 'Sara'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
from itertools import islice

import gaussian_fit




def open_frame(filename,framenumber,size):    
  """
  Opens a frame from an ASCII file. 
  Inputs: name of the file, number of the desired frame and the size of the frame in pixel.
   """  
 
  file = str(filename)
  with open(file) as lines:                  # reads from the file 
    start = int(framenumber*size)            # offset in the file (in rows) corresponding to the desired frame
    frameasked = np.genfromtxt(islice(lines, start, size+start))    
  return frameasked  
  

               



def frames_to_movie(filename,size,N,fps,add_fit):
  """
  Creates a movie (.mp4) using the frames saved in an ascii file. 
  Inputs: the size of each frame, the number of frames (N) and the desired fps (frames per second). 
  add_fit is a boolean that allows to choose whether to overlap the Gaussian fit of the peak in every frame 
  (1 = overlap, 0 = no fit overlap).
  """
    
  fig = plt.figure()
  ax = fig.add_subplot(111)          #creates an image to append the frames to
    
  def update_img(i):                                                 
    ax.clear()
    frame = open_frame(filename,int(i),size)      # opens the ith frame
    im = ax.imshow(frame, interpolation='nearest', cmap = cm.Greys_r)      # adds the frame to the image
      
    if add_fit == 1:          # if I want to overlap the fit to each image
      x = np.arange(0,size)              #x and y must be defined, as they will be used to rebuilt the gaussian fit
      y = np.arange(0,size)
      x,y = np.meshgrid(x,y)
      fitPar = gaussian_fit.fit_frame(frame)[0]     # the first output of fit_frame is a tuple containing the fit parameters
      l = (fitPar[2]/2)+fitPar[5]               # number of levels used for the representation of the Gaussian fit, calculated from the fit values of peak amplitude and noise
      fit = gaussian_fit.fit_frame(frame)[1]     # the second output of fit_frame is the Gaussian function used for the best fit
      ax.contour(x, y, fit, levels=[l], linewidth=1, colors='r')           # the Gaussian fit is overlapped to each image as contour
      im.set_data(frame)         
    return im

  movie = animation.FuncAnimation(fig,update_img,frames=int(N-1),interval=10, blit=True)     # the animation functions are in the matplotlib animation package
  writer = animation.writers['ffmpeg'](fps=fps)
  if add_fit == 1:                               # creates the name of the movie file
     moviename = filename + 'fit.mp4'
  else:
     moviename = filename + '.mp4'
  movie.save(moviename,writer=writer,dpi=100)
  plt.clf()





def plot_trajectory(trace, imagename):        
  """  
  Generates a plot showing the 2D trajectory of a trace and saves it to a file. 
  """
  coord = trace[:, 1:3]
  x = coord[:,0]
  y = coord[:,1]
  
  plt.plot(x,y, marker = 's')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title("2D trajectory")
  plt.savefig(imagename)
  plt.clf()

  







