# simulated-pulsar-period-analysis
_Overview_
Pulsars are extremely precise, even more precise than atomic clocks.
They act like a celestial GPS, helping us navigate the dark void of space and map the vast reaches of our galaxy.
They are invaluable for science as they help test Einstein's theory of relativity and/or detect gravitational waves.
This project explores how Fast Fourier Transform (FFT) detects periodic signals (eg: of pulsars)

_Background_
A pulsar is a rapidly spinning neutron star that emits periodic bursts of electromagnetic radiation that appear as beams of light sweeping the sky.
Due to the conservation of angular momentum and the extreme density of neutron stars, pulsars are highly stable. 
In real life the periodic signal is buried under noise and has to be filtered out.
Fourier Analysis converts the signals from the time domain to the frequency domain.
Periodic signals produce sharp peaks at their respective frequencies while noise is random and is spread all over.

More about Fast Fourier transform: https://en.wikipedia.org/wiki/Fast_Fourier_transform

_Methodology_
1. Simulated a pulsar signal using sine wave.
2. Added Gaussian noise to resemble real world observational data.
3. Applied Fast Fourier transform. 
4. Identified the dominant frequency peak.
5. Recovered the pulsar signal using T=1/f where T-> time period and f->frequency.

_Results_
The Fourier spectrum revealed a sharp peak at the simulated pulsar frequency.
Periodic signals concentrate their strength at one particular frequency while noise being random is spread across different frequencies.
This demonstrates how frequency domain methods can be used to detect the underlying periodic signals.
Real life examples of pulsar period analysis (PSR B1919+21) and 21cm hydrogen line observation use the same mathematical principles.

_Limitations_
This project assumes the pulsar signal is a perfect sine signal while real pulsars have more complex pulse profiles.
Noise model is simplified and purely Gaussian, real life noise might include interference and other non random components.
The methodology ensures a controlled and idealised SNR (signal to noise ratio) ~6.02dB, real pulsars might have negative SNR.

_Inference_
This simple project gives valuable insight into signal processing at its very core.
It gives visual insight into time domain and frequency domain representations.
This project demonstrates how apparent randomness can have underlying patterns waiting to be discovered.

_Real Life Applications_
1. Radio Astronomy:
FFT is used to detect periodic signals from pulsars and to analyze spectral lines such as the 21 cm hydrogen line, helping us to map the structure and composition of galaxies.
2. Medical Imaging(MRI):
In Magnetic Resonance Imaging, FFT transforms raw data into spatial images.
3. Neuroscience (EEG):
FFT is used to analyze brain wave frequencies that help the identification of patterns associated with sleep, cognition and neurological disorders
4. Telecommunications:
FFT enables signal compression, filtering and transmission by separating signals into frequency components. This is essential for wireless communication and GPS navigation. 

_Future Work Ideas_
1. Apply the same methodology to real observational data.
2. Extend the model to detect multiple pulsar signals.
3. Incorporate methods that can handle irregular sampling.
