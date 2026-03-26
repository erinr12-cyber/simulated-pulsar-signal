import numpy as np
import  matplotlib.pyplot as plt

# 1. Time Period

sample_freq = 1000   # number of samples every second - temporal resolution (Hz)
T = 2                # Total duration (s) - 2000 data points
time = np.linspace(0, T, sample_freq*T, endpoint=False)   #Time Vector - (start_time, stop_time, number of data points)

# 2. Pulsar Signal

period = 0.2                              # pulsar period (s)
frequency = 1/period                      # pulsar frequency (Hz)
signal = np.sin(2*np.pi*frequency*time)   # pure sine signal - represents the pulsar signal

# Time domain plot of the sin signal
plt.plot(time, signal)
plt.title("Simulated Pulsar Signal (Time-Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# 3. Gaussian noise

noise = np.random.normal(0,0.5,len(time)) # Normal Gaussian distribution - (mean-0, std-0.5, array length)
noisy_signal = signal + noise             # add noise to the sin signal - this is to mimic real life observations where the pulsar signal is buried in noise

 # Plot the noisy signal
plt.plot(time, noisy_signal)
plt.title("Noisy Pulsar Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# 4. Fast Fourier Transform

fft_vals = np.fft.fft(noisy_signal)                             # calculate FFT of the noisy signal - decomposes complex signal into sum of sine and cosine waves of different frequencies
fft_freq = np.fft.fftfreq(len(time), 1/sample_freq)             # frequency bins for FFT - calculate which frequency each bin in FFT represents
fft_magnitude = np.abs(fft_vals)                                # magnitude spectrum - gives the strength of each frequency

# Select only the positive frequencies (real signals are symmetric in FFT)
positive = fft_freq > 0     # (~1000 data points)

# Plot the frequency spectrum
plt.plot(fft_freq[positive], fft_magnitude[positive])
plt.title("Frequency Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

#Find peak frequency
peak_index = np.argmax(fft_magnitude[positive])     # index of the highest (tallest) value
peak_frequency = fft_freq[positive][peak_index]     # the frequency the index represents

#print the values
print("Detected Frequency:", peak_frequency, "Hz")
print("Detected Period:", 1/peak_frequency, "seconds")
