# simulated-pulsar-period-analysis
_Overveiw_
This project explores how Fast Fourier Transform detect periodic signals (eg: of pulsars)

_Background_
A pulsar is a rotating neutron star that emits periodic bursts of electromagnetic radiation. In real life the periodic signal is buried under noise and has to be filtered out.
Fourier Analysis convert the signals from time domain to frequency domain.
Periodic signals produce sharp peaks at their respective frequencies while noise is random and is spread all over.

_Methodology_
1.simulated a pulsar signal using sine
2.added gaussian noise to resemble observational data
3.applied fast fourier transform 
4.identified the dominant frequency peak
5.recovered the pulsar signal using T=1/f where T-> time period and f->frequency

_Results_
The fourier spectrum revealed a sharp peak at the simulated pulsar frequency.
This demonstrates how frequency domain methods can be used to detect the underlying periodic signals.
