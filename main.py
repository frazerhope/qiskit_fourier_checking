# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

## quantum fourier checking circuit

from qiskit import *
import qiskit.quantum_info as qi
from qiskit.circuit.library import FourierChecking
from qiskit.visualization import plot_histogram

import matplotlib.pyplot as plt

# functions
f = [1, -1, -1, -1]
g = [1, 1, -1, -1]

circuit = FourierChecking(f=f, g=g)

circuit.draw(output='mpl')


zero = qi.Statevector.from_label('00')
sv = zero.evolve(circuit)
probs = sv.probabilities_dict()
plot_histogram(probs)
plt.show()
