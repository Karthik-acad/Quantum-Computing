from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator # The most common simulator
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2, 2)

qc.h(0)

qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

simulator = AerSimulator()

compiled_circuit = transpile(qc, simulator)

job = simulator.run(compiled_circuit, shots=1024)

result = job.result()
counts = result.get_counts(qc)

# Results
print("\nQuantum Circuit:")
print(qc) # Draw the circuit
print("\nSimulation Results:")
print(counts)
plot_histogram(counts)
