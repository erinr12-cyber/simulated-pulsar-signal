import numpy as np
import matplotlib.pyplot as plt

# 1. Create time axis

fs = 1000  # Sampling frequency in Hz (samples per second)
T = 2       # Total duration of the signal in seconds
t = np.linspace(0, T, fs*T, endpoint=False)  # Time vector

# 2. Define pulsar signal

period = 0.5                 # Pulsar period in seconds
frequency = 1 / period   # Convert period to frequency (Hz)
signal = np.sin(2 * np.pi * frequency * t)  # Pure sinusoidal signal

# Plot time-domain signal
plt.plot(t, signal)
plt.title("Simulated Pulsar Signal (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# 3. Add Gaussian noise

noise = np.random.normal(0, 0.5, len(t))  # Random noise with mean 0, std 0.5
noisy_signal = signal + noise                   # Add noise to original signal

# Plot noisy signal
plt.plot(t, noisy_signal)
plt.title("Noisy Pulsar Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# 4. Apply Fourier Transform

fft_vals = np.fft.fft(noisy_signal)                # Compute FFT of noisy signal
fft_freq = np.fft.fftfreq(len(t), 1/fs)            # Frequency bins for FFT
fft_magnitude = np.abs(fft_vals)               # Magnitude spectrum

# Select only positive frequencies (real signals are symmetric in FFT)
positive = fft_freq > 0

# Plot frequency spectrum
plt.plot(fft_freq[positive], fft_magnitude[positive])
plt.title("Frequency Spectrum (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

# Find peak frequency
peak_index = np.argmax(fft_magnitude[positive])
peak_frequency = fft_freq[positive][peak_index]

print("Detected Frequency:", peak_frequency, "Hz")
print("Detected Period:", 1/peak_frequency, "seconds")
