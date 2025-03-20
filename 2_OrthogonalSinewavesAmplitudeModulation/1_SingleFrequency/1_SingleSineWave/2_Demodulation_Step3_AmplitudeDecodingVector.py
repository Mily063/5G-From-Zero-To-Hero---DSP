import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60
PERIOD_NUMBER = 5

# loading Rx vector from file and..
Rx = np.load('TxSignal_Exercise.npy')

# .. ploting it
plt.plot(Rx)
plt.grid()
plt.show()

# spliting vector into time slots coresponding to single periods
RxPeriods = np.reshape(Rx,(5,60))

# decoding amplitudes of Rx time slots

a_list = [] # create amplitude list
for RxPeriod in RxPeriods:
    # decode amplitude and append it to list
    # use as many code rows as you need
    t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)
    Ref = np.sin(t)
    dot = np.dot(RxPeriod, Ref)
    ampl = dot / np.dot(Ref, Ref)
    a_list.append(ampl)

np.set_printoptions(precision=16, legacy='1.13')
print(a_list)  # print list




