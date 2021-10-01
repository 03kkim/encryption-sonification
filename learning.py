import numpy as np # Amazing math library for python
import scipy.signal as signal # Additional signal processing library
import matplotlib.pyplot as plt # Convenient plotting library emulating the format of matlab
from ipywidgets import interact # Allow buttons and sliders on graphs
from IPython.display import Audio # Allow audio playing
from scipy.io.wavfile import read # Allow opening of .wav files

# We are going to generate a 250 Hz sine wave that is two seconds long and sampled at 2000 Hz

# Waveform parameters
fs = 5000 # Sampling rate in Hz
duration = 2 # length of wavefrom in seconds
total_samples = fs * duration # number of samples in entire waveform
freq = 250 # Frequency of the sine wave in Hz

# Generate the waveform
audio_time = np.linspace(0, duration, total_samples) # Generate the list of times in seconds that each sample is taken (used for plotting)
audio_radians = 2 * np.pi * freq * audio_time # Convert the frequency of the sinewave from Hz to radians
audio_amplitude = np.sin(audio_radians) # Generate the amplitude (instantaneous pressure) for each sample

# Plot one hundreth of a second of the sinewave
plt.figure(figsize=(13,8)) # Create a new figure object, give it a size
plt.stem(audio_time, audio_amplitude) # time is x-axis, amplitude is y-axis
plt.title("250 Hz Sine Wave Samples")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim([0, .01]) # plot only the times from 0 to one hundreth of a second
plt.show() # display the plot