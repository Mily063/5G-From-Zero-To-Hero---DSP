import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMS
TIME_VECTOR_SIZE = 100

A_tx = 2
B = 2

# CALCULATIONS
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Sin_A_tx = A_tx * np.sin(t)
Sin_B = B * np.sin(t)
dot = np.dot(Sin_A_tx,Sin_B)
A_rx = dot/np.dot(Sin_B,Sin_B)

# PRESENTATION
print(f'A_tx = {A_tx}')
print(f'B = {B}')
print(f'dot = {dot:0.2f}')
print(f'A_rx = {A_rx:0.2f}')


