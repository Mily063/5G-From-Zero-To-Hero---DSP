import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = 3.25

# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)

Ref = np.sin(t)
Shifted = np.sin(t+PHASE_SHIFT)
Ref_mult_Shifted = Ref*Shifted
dot_product = np.sum(Ref_mult_Shifted) #use Ref_mult_Shifted

# PLOTS (HINT: use separate plots, not one with grid)

# components
plt.plot(t, Ref, '-p', color='blue')
plt.plot(t, Shifted, '-p', color='green')
plt.legend(["Ref", "Shifted"])
plt.title("Components")
plt.grid()
plt.axhline(y=0, color='black')
plt.show()
# multiplication, HINT: use "stem" function for ploting
plt.title("Components")
plt.stem(t, Ref_mult_Shifted, markerfmt='darkorange')
plt.legend(["Ref_mult_Shifted"])
plt.grid()
plt.axhline(y=0, color='red')
plt.ylim([-1,1])
plt.show()
# print phase shift and dot product value
print(f' phase shift = {PHASE_SHIFT:0.2f}','\n',f'dot product = {dot_product:0.2f}',)

