import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol
# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000
NOISE_DEVIATION = 2
SYMBOL_NR = 2
t = np.linspace(0, 2 * np.pi, TIME_VECTOR_SIZE, endpoint=False)
carrier_sin = ref_sin = np.sin(t)
carrier_cos = ref_cos = np.cos(t)
# TRANSMISION-RECEPTION
symbols_tx_sin = np.random.randint(0, SYMBOL_NR, TRANSMISIONS_NR)
symbols_tx_cos = np.random.randint(0, SYMBOL_NR, TRANSMISIONS_NR)
noise_dev_list = list()
for noise_dev in np.linspace(0, NOISE_DEVIATION, 10):
    symbols_rx_sin = list()
    symbols_rx_cos = list()
    for symbol_sin, symbol_cos in zip(symbols_tx_sin, symbols_tx_cos):
        # modulation
        ampl_sin = symbol_to_ampl(SYMBOL_NR, symbol_sin)
        ampl_cos = symbol_to_ampl(SYMBOL_NR, symbol_cos)
        Tx = ampl_sin * carrier_sin + ampl_cos * carrier_cos
        # real channel
        Rx = Tx + np.random.normal(loc=0, scale=noise_dev, size=len(Tx))
        # demodulation
        ampl_sin = np.dot(ref_sin, Rx) / TIME_VECTOR_SIZE * 2
        ampl_cos = np.dot(ref_cos, Rx) / TIME_VECTOR_SIZE * 2
        symbol_sin = ampl_to_symbol(SYMBOL_NR, ampl_sin)
        symbol_cos = ampl_to_symbol(SYMBOL_NR, ampl_cos)
        symbols_rx_sin.append(symbol_sin)
        symbols_rx_cos.append(symbol_cos)
    symbols_rx_sin = np.array(symbols_rx_sin)
    symbols_rx_cos = np.array(symbols_rx_cos)
    errors_sin = sum(symbols_rx_sin != symbols_tx_sin)
    errors_cos = sum(symbols_rx_cos != symbols_tx_cos)
    noise_dev_list.append(((noise_dev, errors_sin, errors_cos)))
# PRESENTATION

print(f'SYMBOL_NR: {SYMBOL_NR}')

print(f'DEV:  SIN,  COS')
for noise_dev, errors_sin, errors_cos in noise_dev_list:
    print(f'{noise_dev:.2f} : {errors_sin}, {errors_cos}')