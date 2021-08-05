#
#   This code is meant to visually ilustrate the density
#   of sampling points for all the notes on a guitar (in
#   standard tuning) and to aid in the selection of a 
#   suitable sample frequency upon future code for the
#   project will be based
#
import numpy as np
from numpy.core.function_base import linspace
import matplotlib.pyplot as plt


def signal(x, frequency):
    return np.sin(2 * np.pi * frequency * x)

guitar_frequencies = [82.41, 110.00, 146.83, 196.00, 246.94, 330] # list of guitar frequencies from low to high
pitches = ["E_2", "A_2", "D_3", "G_3", "B_3", "E_4"] # list of scientific pitch notations for all of the notes on the guitar

Sample_Period = 25e-6   # time between samples [s]
SPS = 1 / Sample_Period # total number of Samples Per Second based on specified time between samples (SPS = sampling frequency)
start = 0               # start time of the simulation [s]
stop = 20e-3            # stop time for the simulation [s]

time = linspace(start, stop, int((stop - start)*SPS)) # create list of points at which signal will be sampled based on specified parameters

fig, ax = plt.subplots(3,2) #create plot figure and axes

for i in range(0, len(guitar_frequencies)): #populate the axes with graphs

    #Generate graph coordinates
    col = 1 - int((i+1) % 2)
    row = int(np.floor((i/ 2)))

    ax[row, col].plot(time, signal(time, guitar_frequencies[i]), color=("C{}".format(i)),marker="o")
    ax[row, col].set_title("Sampling points for {}".format(pitches[i]))
    ax[row, col].set_xlabel("Time [s]")
    ax[row, col].set_ylabel("Magnitude")
    ax[row, col].grid(True)

fig.tight_layout(pad=0.2) #Add spacing to subplots
plt.show()
