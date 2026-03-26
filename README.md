# simulated-pulsar-period-analysis
_Overveiw_
This project explores how Fast Fourier Transform detect periodic signals (eg: of pulsars)

_Background_
A pulsar is a rotating neutron star that emits periodic bursts of electromagnetic radiation. In real life the periodic signal is buried under noise and has to be filtered out.
Fourier Analysis converts the signals from time domain to frequency domain.
Periodic signals produce sharp peaks at their respective frequencies while noise is random and is spread all over.

More about Fast Fourier transform : https://en.wikipedia.org/wiki/Fast_Fourier_transform

_Methodology_

1.simulated a pulsar signal using sine

2.added gaussian noise to resemble observational data

3.applied Fast Fourier transform 

4.identified the dominant frequency peak

5.recovered the pulsar signal using T=1/f where T-> time period and f->frequency

_Results_
The fourier spectrum revealed a sharp peak at the simulated pulsar frequency.
This demonstrates how frequency domain methods can be used to detect the underlying periodic signals.
Real life examples of pulsar period analysis (PSR B1919+21) and 21cm hydrogen line observation use the same methodology.


_Inference_
This simple project gives valuable insight into signal processing at its very core.
It gives visual insight into time domain and frequency domain representations.
Signal processing is extremely relevant in radio astronomy and medical fields, where it helps identify underlying patterns.


