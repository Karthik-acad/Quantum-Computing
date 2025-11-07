from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator # The most common simulator
from qiskit.visualization import plot_histogram

# --- 1. Build the Circuit ---

# Create a circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Step A: Put the first qubit (q0) into superposition
# q0 is now 50% |0⟩ and 50% |1⟩
qc.h(0)

# Step B: Create the entanglement
# q0 is the control, q1 is the target
# - If q0 is |0⟩, do nothing to q1 (it stays |0⟩) -> Result: |00⟩
# - If q0 is |1⟩, flip q1 (from |0⟩ to |1⟩) -> Result: |11⟩
qc.cx(0, 1)

# --- 2. Measure the Qubits ---
# We measure both qubits to see the correlated result
qc.measure([0, 1], [0, 1])

# --- 3. Run the Simulation ---

# Use the Aer simulator
simulator = AerSimulator()

# Prepare the circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Run the experiment 1024 times
job = simulator.run(compiled_circuit, shots=1024)

# Get the results
result = job.result()
counts = result.get_counts(qc)

# --- 4. Display Results ---
print("\nQuantum Circuit:")
print(qc) # Draw the circuit
print("\nSimulation Results:")
print(counts)
plot_histogram(counts)
