import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from mylib import myDFT, my_stem_plot
# loads samples from .wav file with exemplary DTFM signal
# adapt file path
samples = read(r'wav/a.wav')
samplig_freq = samples[0]
samples = samples[1]
samples = samples[:1024]
# use commenst to swith between myDTF and numpy DTF (FFT)
#fft = np.fft.fft(samples)
#real = fft.real
#imag = fft.imag
samples1 = samples - np.mean(samples)
plt.plot(samples1)
plt.show()

real, imag = myDFT(samples1)

plt.title("myDFT")
plt.plot(real,label='real')
plt.plot(imag,label='imag')
plt.grid()
plt.legend()
plt.show()

t = np.linspace(0, samplig_freq, len(samples1))
#frequencies on x
plt.plot(t, real, label='real')
plt.plot(t, imag, label='imag')
plt.grid()
plt.show()
#amplitude of sinusoids
amplitude = np.sqrt(np.array(real)**2 + np.array(imag)**2)
plt.title("Amplitude of sinusoids")
plt.plot(t, amplitude, label='amplitude')
plt.grid()
plt.legend()
plt.show()

#culd be usefool for zooming
plt.xlim(0,100)
plt.ylim(-20_000,20_000)
print(samplig_freq)