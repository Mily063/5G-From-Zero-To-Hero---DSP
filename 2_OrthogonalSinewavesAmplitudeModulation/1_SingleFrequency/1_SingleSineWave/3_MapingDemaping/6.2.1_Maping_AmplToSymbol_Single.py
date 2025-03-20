import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

SYMBOL_NR = 2

symbols_l = list()
ampl_l = np.linspace(-1.5, 1.5, 100)
for ampl in ampl_l:
    symbol = ampl_to_symbol(SYMBOL_NR, ampl)
    symbols_l.append(symbol)
plt.plot(ampl_l, symbols_l, 'p')

plt.grid()
plt.title(f'SYMBOL_NR = {SYMBOL_NR}')
plt.xlabel('Amplitude')
plt.ylabel('Symbol')
plt.show()





