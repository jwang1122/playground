import math
import numpy as np
import matplotlib.pyplot as plt
import scipy


def fft_plot(audio, sampling_rate):
    n = len(audio)
    index = int(n // 2)
    T = 1.0 / sampling_rate

    yf = scipy.fft.fft(audio)

    xf = np.linspace(0.0, 1.0 / (2.0 * T), index)
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0 / n * np.abs(yf[:index]))
    plt.grid()
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    return plt.show()


samples = 100.0
a1 = 3
w1 = 4
a2 = 1
w2 = 19
x = np.arange(samples)
y1 = a1*np.sin(2 * math.pi * w1 * (x / samples))
y2 = a2*np.sin(2 * math.pi * w2 * (x / samples))
plt.figure()
# plt.stem(x,y1,'r',)
plt.plot(x, y1, 'b',)
plt.plot(x, y2, 'g')
plt.plot(x, y1 + y2, 'r')
plt.xlabel('TIme -->')
plt.ylabel("Amplitude")
plt.show()

fft_plot(y1 + y2, samples)
