import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

t = np.linspace(0, 2 * pi, 30)
phaseShift = np.linspace(0, 3, 30, endpoint=False)
Ref = np.sin(t)

dot_products = []

for phase in phaseShift:
    shifted = np.sin(t + phase)
    dot_product = np.dot(shifted, Ref)
    dot_products.append(dot_product)

plt.plot(phaseShift, dot_products, '-p')
plt.xlabel('shift')
plt.ylabel('dot')
plt.ylim(-15,15)
plt.axhline(0, color='black')
plt.grid()
plt.show()


