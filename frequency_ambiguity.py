#!/bin/env python3.6

##
# A Python script to better understand frequency ambiguity.
#
# From Understanding DSP: "When sampling at a rate of fs samples/second,
# if k is any positive or negative integer, we cannot distinguish between
# the sampled values of a sinewave of f0 Hz and a sinewave of (f0 + kfs)Hz."
#

import matplotlib.pyplot as plt
import numpy as np

# Create a new figure
plt.figure(0)

# Plot the graph for this many seconds
t_end = 1

# x-coordinate sequence of values
t_plot = np.arange(0, t_end, 0.001)

# The frequency of the "original" waveform, in cycles/second (Hz)
f0 = 1

# The sampling frequency, in samples/second
fs = 6

# Plot the original sinewave
plt.plot(t_plot, np.sin(2 * np.pi * f0 * t_plot))

# Plot a sinewave of (f0 + kfs) Hz.
k = -2
plt.plot(t_plot, np.sin(2 * np.pi * (f0 + k * fs) * t_plot))

# Now, we sample the signal.
x_sample = np.arange(0, t_end, 1.0/fs)
y_sample = np.sin(2 * np.pi * f0 * x_sample)

# Plot the samples
plt.scatter(x_sample, y_sample, c='red', linestyle='--')

# Draw the horizontal axis for better visualization
plt.axhline(0, color = 'k', linewidth = 0.3)

# Show time!
plt.show()
