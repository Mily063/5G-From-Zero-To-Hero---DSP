import numpy as np
from mapper_lib import symbol_to_ampl
from mapper_lib import ampl_to_symbol

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000
NOISE_DEVIATION = 2.0
SYMBOL_NR = 8
t = np.linspace(0, 2 * np.pi, TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
Ref = Carrier
noise_dev_list = list()
# TRANSMISION-RECEPTION
for noise_dev in np.linspace(0, NOISE_DEVIATION, 10):
    symbols_tx = np.random.randint(0, SYMBOL_NR, TRANSMISIONS_NR)
    symbols_rx = list()
    error_nr = 0
    for symbol in symbols_tx:
        symbol1 = symbol
        # modulation
        ampl = symbol_to_ampl(SYMBOL_NR,symbol)
        Tx = ampl * Carrier
        # real channel
        Rx = Tx + np.random.normal(0, noise_dev, TIME_VECTOR_SIZE)
        # demodulation
        ampl = (np.dot(Rx, Ref) / TIME_VECTOR_SIZE) * 2
        symbol = ampl_to_symbol(SYMBOL_NR, ampl)
        symbols_rx.append(symbol)

        if symbol != symbol1:
            error_nr += 1

    noise_dev_list.append((noise_dev, error_nr))

# PRESENTATION
symbols_rx = np.array(symbols_rx)  # list to numpy array

print('SYMBOL_NR:', SYMBOL_NR)
print('noise dev' + ' : ' + 'errors nr')
for noise_dev, error_nr in noise_dev_list:
    print(f"{noise_dev:.2f} : {error_nr}")


