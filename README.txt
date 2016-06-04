This project is divided in two parts: simulation and analysis.

1. simulate_diffusion simulates a movie of a particle undergoing 2D free diffusion. The particle is simulated as a Gaussian peak moving within frames containing random noise.

2. tracking_analysis performs the tracking analysis of a movie containing a particle undergoing 2D free diffusion: a fit of every frame in the movie is performed to find the coordinates of the peak, and the coordinates are used to reconstruct a trajectory. A Mean Square Displacement analysis is performed on the trajectory, and from the fit of the Mean Square Displacement the diffusion coefficient D is obtained. The analysis can be applied to simulated movies, but also to real movies.  



1. SIMULATE_DIFFUSION:


-The name of the movie to write is given by command line.
The user will be required inputs indicating: the diffusion coefficient of the particle,
the number of time steps within the trace,
the frame size in pixels,
the amplitude of the gaussian peak,
the standard deviation of the peak,
the amplitude of the noise in the frames,
the offset to apply to the peak intensity.

-simulate_diffusion_trace generates the 2D coordinates of the movement, given as input the number of time steps N, the frame size, the diffusion coefficient D, the number of time steps N, and the width of the time steps (set to 1 as default). the program returns a 'trace' array, containing the time and the x and y coordinates;

-write_frames_ascii generates a frame for each step within the trace. Each frame is generated as numpy array, containing the Gaussian peak with coordinates defined by the current step. The program takes as input the name of the file to write, the trace array, the frame size, standard deviation of the peak, amplitude of the peak, noise of the frame, offset. An ASCII file is generated to contain the frames;

- plot_trajectory generates a 2D plot of the trajectory, writing it to a .png file with the same name as the movie, + 'trajectory';

- frames_to_movie writes a movie file (.mp4) showing the frames. The program requires as inputs the name of the file to write, the frame size, the number of time steps (or frames), the frames per second. 


IO contains the code for the input/output operations
gaussian_fit contains the code to perform fits using the Gaussian function




2. TRACKING_ANALYSIS

-the path of the movie to analyze is given by command line.

-gaussian_fit fits the movie: in every frame a peak is found and fitted with a Gaussian function, to find its coordinates. it returns an array containing the time and the coordinates extracted from the fit;

-frames_to_movie creates a new movie file (.mp4) where a circle indicating the peak recreated from the Gaussian fit is overlapped to each original frame;

-plot_trajectory creates a plot of the 2D trajectory obtained from the fit. The plot is saved to a .png image, which name is the same name of the movie + 'trajectory';

-MSD performs the Mean Displacement Analysis of the trajectory. It returns an array containing the MSD array;

-fit_MSD fits the MSD array and extract the diffusion coefficient of the particle;

-plot_MSD creates 2 plots: one containing the MSD in function of time, the other containing the first part of the MSD overlapped with its fit. The two plots are saved in an .png image.


IO contains the code for the input/output operations
gaussian_fit contains the code to perform fits using the Gaussian function
MSD contains the code calculating and fitting the Mean Square Displacement of a trajectory