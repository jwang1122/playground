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

x = np.arange(0, 1, 0.01)
y = x**4 + 2
x1 = np.arange(0, 100)
z1 = 1/(math.e**(x1-55) + 1) - 1/(math.e**(x1-49) + 1)
z2 = 0.5/(math.e**(x1-81) + 1) - 0.5/(math.e**(x1-85) + 1)
l = z1 + y + z2

fig=plt.figure()
ax=fig.add_subplot(311)
ax.plot(x, y)

ax=fig.add_subplot(312)
ax.plot(x, z1)

ax=fig.add_subplot(313)
ax.plot(x, l)

plt.xlabel('Angle')
plt.ylabel('delta + x^4')

plt.show()

#fft_plot(l, 100)