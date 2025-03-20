import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

for symbol_nr in 2, 4, 8:
    ampl_l = np.linspace(-1.5, 1.5, 100)
    symbols_l = list()
    for ampl in ampl_l:
        symbol = ampl_to_symbol(symbol_nr, ampl)
        symbols_l.append(symbol)
    plt.plot(ampl_l, symbols_l, '-p', label=f'symbol nr = {symbol_nr}')

plt.legend()
plt.grid()
plt.xlabel('Symbol')
plt.ylabel('Amplitude')
plt.show()



