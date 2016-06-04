__author__ = 'Sara'
import sys
import gaussian_fit
import MSD
import IO

"""
Performs the tracking analysis of a movie containing a peak undergoing free diffusion. The path of the movie is given by command line.
1. Fit of the movie: in every frame a peak is found and fitted with a Gaussian function, to extract its coordinates.
Writes a movie where the original frames are overlapped with the peak obtained from the Gaussian fit (shown as a red circle on each frame).
2.The coordinates obtained from the fit are used to generate a trace. A plot with the trajectory of the trace is saved to file.
2. A Mean Square Displacement (MSD) analysis is performed on the trace, to get the diffusion coefficient D of the peak.
"""
  
  
  
    
def main():
  
  filename = sys.argv[1]         #the path of the movie to analyze is given as input from command line
    
  tracefit = gaussian_fit.fit_movie(filename)            #fits the movie and obtains a trace
  
  IO.frames_to_movie(filename,300,20,10,1)     #creates a movie containing the frames overlapped to the Gaussian fit
  
  imagename = filename + 'trajectory.png'
  IO.plot_trajectory(tracefit, imagename)      #plots the obtained trajectory in a file
  
  MSDarray = MSD.MSD(tracefit)                           #calculates the MSD of the trajectory
  MSDfit = MSD.fit_MSD(MSDarray)[1]                      #fits the MSD and find D
  
  MSDimagename = filename + 'MSDplots.png'
  MSD.plot_MSD(MSDarray,MSDfit,MSDimagename)             # plots the MSD trace and its fit to a file


  
  
  

if __name__=='__main__':

    main()
	
	
	
	
	

  


