import matplotlib.pyplot as plt
import numpy as np
from mapper_lib import symbol_to_ampl
from mapper_lib import ampl_to_symbol
# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000
NOISE_DEVIATION = 3.0
SYMBOL_NR = [2,4,8]
t = np.linspace(0, 2 * np.pi, TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
Ref = Carrier
# TRANSMISION-RECEPTION
for symbols in SYMBOL_NR:
    noise_dev_list = list()
    for noise_dev in np.linspace(0, NOISE_DEVIATION, 20):
        symbols_tx = np.random.randint(0, symbols, TRANSMISIONS_NR)
        symbols_rx = list()
        error_nr = 0
        for symbol in symbols_tx:
            symbol1 = symbol
            # modulation
            ampl = symbol_to_ampl(symbols,symbol)
            Tx = ampl * Carrier
            # real channel
            Rx = Tx + np.random.normal(0, noise_dev, TIME_VECTOR_SIZE)
            # demodulation
            ampl = (np.dot(Rx, Ref) / TIME_VECTOR_SIZE) * 2
            symbol = ampl_to_symbol(symbols, ampl)
            symbols_rx.append(symbol)
            if symbol != symbol1:
                error_nr += 1
        noise_dev_list.append((noise_dev, error_nr))
    noise_dev_plot = [x[0] for x in noise_dev_list]
    error_nr_plot = [x[1] for x in noise_dev_list]
    plt.plot(noise_dev_plot, error_nr_plot, '-p', label=f'symbol nr = {symbols}')
# PRESENTATION
symbols_rx = np.array(symbols_rx)  # list to numpy array
plt.grid()
plt.legend()
plt.xlabel('noise deviation')
plt.ylabel('error nr')
plt.show()


