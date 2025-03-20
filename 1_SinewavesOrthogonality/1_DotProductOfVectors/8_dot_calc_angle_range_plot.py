import matplotlib.pyplot as plt
import numpy as np
from mylib import rotate_vector
v = np.array([0, 1])

angle_list = []
dot_list = []

for angle in range(0,370,10):
    angle_list.append(angle)
    v_rot = rotate_vector(v, angle)
    dot = np.sum(v_rot*v)
    dot_list.append(dot)

plt.plot(angle_list,dot_list, '-p')

plt.xlabel("Angle")
plt.ylabel("Dot product")

plt.grid()
plt.show()



