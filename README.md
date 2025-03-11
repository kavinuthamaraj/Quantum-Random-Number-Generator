# Quantum Random Number Generator

This project implements a Quantum Random Number Generator (QRNG) using Qiskit. It utilizes quantum superposition to generate truly random numbers based on quantum mechanics.

## 📌 Features

- Uses a 3-qubit quantum circuit to generate random 3-bit numbers.
- Uses Hadamard gates to create equal probability distributions.
- Runs on the Qiskit Aer simulator.
- Displays a histogram of the generated numbers.

## 🛠️ Requirements

Ensure you have the following installed:
- Python (>=3.8)
- Qiskit (>=1.0)
- Matplotlib (for visualization)

To install dependencies, run:
pip install qiskit matplotlib

🚀 How to Run

Clone this repository:

git clone https://github.com/yourusername/Quantum-RNG.git
cd Quantum-RNG

Run the script:

python3 quantum_random.py

View the histogram output showing the random numbers generated.

📜 Code Explanation

Quantum Circuit Creation:

A 3-qubit, 3-classical-bit circuit is created.

Each qubit is placed into superposition using Hadamard gates.

Measurement: The qubits are measured and converted into binary numbers.

Execution: The circuit runs on the Qiskit Aer simulator.

Visualization: The results are plotted using a histogram.

📊 Sample Output

The output histogram will look something like this:

Quantum Random Number Generator Results: {'000': 120, '001': 138, '010': 126, ...}

🏗️ Future Enhancements

Increase the number of qubits for higher-bit random numbers.

Implement a GUI for better user interaction.

Use a real quantum computer instead of a simulator.

📜 License

This project is licensed under the MIT License.

