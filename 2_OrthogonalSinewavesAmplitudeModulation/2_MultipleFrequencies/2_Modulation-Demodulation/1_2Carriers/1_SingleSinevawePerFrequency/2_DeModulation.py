import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60

# loading Rx vector from file and..
Rx = np.load('TxSignal.npy')

# .. ploting it
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# callculation
t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)

ref_f1 = np.sin(1*t)
ref_f2 = np.sin(2*t)
         
dot_f1 = np.dot(Rx,ref_f1)
dot_f2 = np.dot(Rx,ref_f2)

ampl_f1 = dot_f1/np.dot(ref_f1,ref_f1)
ampl_f2 = dot_f2/np.dot(ref_f2,ref_f2)

# presentation
print(f'ampl_f1 = {ampl_f1:0.2f}, ampl_f2 = {ampl_f2:0.2f}')



