import numpy as numpy
import matplotlib.pyplot as plt

# 1.Time Axis

sample_freq = 1000  # sampling frequency in Hz (samples per second)
T = 2               # total duration of the signal (seconds)
time = numpy.linspace(0, T, sample_freq*T, endpoint=False)  # time vector

# 2.Pulsar Period 

period = 0.5                                                # pulsar period (seconds)
freq= 1 / period                                            # convert period to frequency (Hz)
signal = numpy.sin(2 * numpy.pi * freq * time)   #pure sin signal

# plot the time domain of the pure pulsar signal
plt.plot(time, signal)
plt.title("Simulated Pulsar Signal (Time-Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# 3. add gaussian noise - this mimics real observations

noise = numpy.random.normal(0, 0.5, len(time))  # random noise (with mean 0, std 0.5)
noisy_signal= signal + noise                    # add noise to the original signal

# plot the noisy signal
plt.plot(time, noisy_signal)
plt.title("Noisy Pulsar Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude" )
plt.show()

# 4.Fast Fourier transform filters the signal from noise using frequency domain

fft_vals = numpy.fft.fft(noisy_signal)                            # compute FFT of noisy signal
fft_freq = numpy.fft.fftfreq(len(time),1/sample_freq)             # frequency bins for the FFT
fft_magnitude = numpy.abs(fft_vals)                               # magnitude spectrum

# real signals are symmetric - select only the positive frequencies
positive = fft_freq >0

# plot the frequency spectrum
plt.plot(fft_freq[positive], fft_magnitude[positive])
plt.title("Frequency Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

# peak frequency plots the actual frequency of the periodic signal
peak_index= numpy.argmax(fft_magnitude[positive])
peak_frequency = fft_freq[positive][peak_index]

print("Detected Frequency:", peak_frequency, "Hz")
print("Detected Period:", 1/peak_frequency, "seconds")


