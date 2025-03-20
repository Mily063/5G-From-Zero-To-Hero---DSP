import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2, 3.4)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
# modulation
Carrier = np.sin(t)
Tx = np.array([])
for amp in AMPL_VECTOR:
    Tx = np.append(Tx, amp * Carrier)
# channel
Rx=Tx # ideal one
# demodulation
RxPeriods = np.reshape(Rx,(5,60))
amplitudes_l = [] # create amplitude list
for RxPeriod in RxPeriods:
    Ref = np.sin(t)
    dot = np.dot(RxPeriod, Ref)
    ampl = dot / np.dot(Ref, Ref)
    amplitudes_l.append(ampl)
# PRESENTATION
# Tx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()
#
np.set_printoptions(precision=16, legacy='1.25')
print(f'received amplitudes: {amplitudes_l}')


