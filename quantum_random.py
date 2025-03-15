# Import necessary libraries
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer.backends import QasmSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram

import matplotlib.pyplot as plt

# Quantum Circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Hadamard gates to put qubits in superposition
qc.h(range(3))

# Measuring qubits
qc.measure(range(3), range(3))

# Show Quantum Circuit (Fancy Visualization)
qc.draw("mpl")  
plt.show()

# Aer QasmSimulator
backend = QasmSimulator()
compiled_circuit = transpile(qc, backend)

# Executing quantum circuit
job = backend.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts()

print("Quantum Random Number Generator Results:", counts)

# Result as Histogram
plot_histogram(counts)
plt.show()
