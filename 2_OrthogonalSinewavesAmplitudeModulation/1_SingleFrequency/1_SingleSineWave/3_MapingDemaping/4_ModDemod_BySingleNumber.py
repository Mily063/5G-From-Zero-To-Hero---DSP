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
    Rx = Tx # ideal one
    Ref = np.sin(t)
    # demodulation
    dot = np.dot(Rx, Ref)
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


