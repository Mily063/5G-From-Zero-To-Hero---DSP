from idlelib.iomenu import errors

import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.bipartite.basic import color
pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR_SIN = (1,-1,1,-1)
AMPL_VECTOR_COS = (1,1,-1,-1)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
carrier_sin = ref_sin = np.sin(t)
carrier_cos = ref_cos = np.cos(t)
amplitudes_sin = list()
amplitudes_cos = list()
NOISE_DEVIATION = 6
TRANSMISSION_NR = 10
for i in range(TRANSMISSION_NR):
    for ampl_sin, ampl_cos in zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS):
        # modulation
        Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)
        # real channel
        Rx = Tx + np.random.normal(0, NOISE_DEVIATION, len(Tx))
        # demodulation
        ampl1 = (np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE)*2
        amplitudes_sin.append(ampl1)
        ampl2 = (np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE)*2
        amplitudes_cos.append(ampl2)
# PRESENTATION
# Rx plot
for j in range(len(amplitudes_sin)):
    plt.scatter(amplitudes_sin[j], amplitudes_cos[j], color=('red', 'orange', 'green', 'blue')[j%4])
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')
plt.title("RX amplitudes")
plt.xlabel("cos ampl.")
plt.ylabel("sin ampl.")
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.grid()
plt.show()
