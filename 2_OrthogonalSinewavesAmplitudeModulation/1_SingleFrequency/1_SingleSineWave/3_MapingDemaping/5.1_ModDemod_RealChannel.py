import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
amplitudes_l = []

for amp in AMPL_VECTOR:
    # modulation
    Tx = amp*Carrier
    # channel
    Rx = Tx + np.random.normal(0, 0.3, len(Tx))
    # demodulation
    dot = np.dot(Rx, Carrier)
    ampl = dot / np.dot(Carrier, Carrier)
    amplitudes_l.append(ampl)

ampl1 = np.array(AMPL_VECTOR)
ampl2 = np.array(amplitudes_l)
errors = ampl1 - ampl2

# PRESENTATION
# Tx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()
#
np.set_printoptions(precision=16, legacy='1.25')
print(f'received amplitudes: {amplitudes_l}')
print(f'errors        : {errors}')


