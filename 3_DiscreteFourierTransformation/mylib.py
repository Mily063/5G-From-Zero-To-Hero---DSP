import numpy as np
from math import cos, sin

def rotate_vector(vec,deg):
    theta = np.deg2rad(deg)
    rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
    return np.dot(vec,rot)


import numpy as np
import matplotlib.pyplot as plt


def my_stem_plot(y, title, y_range=None):
    x = np.arange(len(y))
    plt.stem(x, y, '-p')

    plt.xticks(x)
    if y_range:
        plt.ylim(y_range)
        plt.yticks(np.arange(*y_range))

    plt.grid()
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(4, 3.6)
    plt.show()


# ----------------------------

def myDFT(samples):
    N = len(samples)
    real = list()
    imag = list()
    t = np.linspace(0, 2 * np.pi, N, endpoint=False)

    for f in range(N):
        real.append(np.dot(samples, np.cos(t * f)))
        imag.append(np.dot(samples, np.sin(t * f)))

    return real, imag




