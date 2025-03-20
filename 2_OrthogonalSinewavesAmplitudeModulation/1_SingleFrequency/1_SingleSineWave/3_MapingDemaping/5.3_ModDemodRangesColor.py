import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1, 2, 3, 4)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
amplitudes_l = []
NOISE_DEVIATION = 1
TRANSMISSION_NR = 100

for i in range(TRANSMISSION_NR):
    amp = AMPL_VECTOR[i % 4]
    # modulation
    Tx = amp*Carrier
    # channel
    Rx = Tx + np.random.normal(0, NOISE_DEVIATION, len(Tx))
    # demodulation
    dot = np.dot(Rx, Carrier)
    ampl = dot / np.dot(Carrier, Carrier)
    amplitudes_l.append(ampl)

# PRESENTATION
# Tx plot
plt.plot(amplitudes_l[0::4], 'p', color='red')
plt.plot(amplitudes_l[1::4], 'p', color='orange')
plt.plot(amplitudes_l[2::4], 'p', color='green')
plt.plot(amplitudes_l[3::4], 'p', color='blue')
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()
#
np.set_printoptions(precision=16, legacy='1.25')


