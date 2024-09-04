from fft_impl import *
import numpy as np
import matplotlib.pyplot as plt

from scipy.fft import fftfreq

def sin(freq,duration, sample_rate=128):
	npoints = np.linspace(0,duration,duration*sample_rate)
	frequencies = npoints*freq
	s = np.sin(2*np.pi*frequencies)
	return npoints,s

if __name__ == '__main__':

	sample_rate = 512
	duration = 2
	freq = 15

	x,y  = sin(freq,duration, sample_rate=512)
	
	fft_y = fft(y)
	f = fftfreq(sample_rate*duration, 1/sample_rate)

	plt.subplot(211)
	plt.plot(x,y)
	
	plt.subplot(212)
	plt.plot(f,np.real(fft_y))

	plt.show()