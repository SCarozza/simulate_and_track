__author__ = 'Sara'

import sys
import simulate_diffusion_trace
import IO


"""
Simulates a particle undergoing free diffusion and creates a movie: the name of the movie is given by command line.
1. Generates the coordinates of the movement, simulating a free diffusion: the parameters of the diffusion are given as input: 
diffusion coefficient D, number of time steps N, width of each time step t, size frame.
2. For every step in the trace, a frame is generated (as np array), containing a Gaussian peak with the defined 
coordinates. The peak and frame features are given as input (ampiltude A, width w and offset b of the peak, background noise level n).
The trajectory is plotted to an image file.
3. Creates a movie (mp4) collecting all the frames.
"""



def main():   #inputs to give: trace_file_name
  
  print "Give the properties of the desired trace:"   
  D = input("diffusion coefficient:")     #diffusion coefficient
  N = input("number of points:")    #time points
  size = input("size of each frame:")    #size frame in pix
  
  
  print "Now give the properties of the Gaussian peak:"
  A = input("amplitude:")    #amplitude
  sx = sy = input("standar deviation:")     #width in x and y. in most of the case the peak is symmetric so wx = wy
  n = input("noise:")        #noise
  b = input("offset:")         #offset
  

  filename = sys.argv[1]     # takes from command line the name of the file to write
  trace = simulate_diffusion_trace.trace(N,size,D,1)   # creates a trace of free diffusing coordinates
  
  IO.write_frames_ascii(filename,trace,size,sx,sy,A,n,b)   # generates a file (.ascii) containing the frames (arrays) corresponding to each time step. 
                                                                              # Inputs: name of the ascii file, the trace, the size of the frame, the Gaussian peak properties.
  
  filename_plot = filename + 'trajectory.png'       # creates a path for the file containing the trajectory plot
  IO.plot_trajectory(trace, filename_plot)      # plots the trajectory and writes it to a a file (.png)
  
  
  IO.frames_to_movie(filename, size, N, 10, 0)     # writes a movie (.mp4) containing all the frames. Inputs: name of the ascii file from which to read the frames, 
                                                                        # size of each frame, total number of frames N, fps (frames per second), a boolean that indicates whether 
                                                                        # to add the fit to the images or not. 
  
  
  
  
  
  
    
  
  
  
if __name__=='__main__':

  main()
	
	