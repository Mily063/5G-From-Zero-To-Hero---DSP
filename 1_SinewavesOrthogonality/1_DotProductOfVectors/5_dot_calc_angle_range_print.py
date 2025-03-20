import numpy as np
import math
from mylib import *

green = [0,1]

for i in range(0,370,10):
    blue = rotate_vector(green, i)
    dot_product = np.dot(green, blue)
    dot_rounded = np.round(dot_product,10)
    print(str(i) + " degree dot product is " + str(dot_rounded))