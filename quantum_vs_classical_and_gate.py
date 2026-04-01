from qiskit import QuantumCircuit
from qiskit.primitives import Sampler # Qiskit's modern simulator interface

# 1. The Classical Experiment

def classical_and(a, b):

    if a == 1 and b == 1:
        return 1
    else:
        return 0

# 2. The Quantum Simulation

def quantum_and(a, b):

    # We need 3 qubits (2 for input, 1 for output)
    # We need 1 classical bit to store the measured result
    qc = QuantumCircuit(3, 1)


    if a == 1:
        qc.x(0)  # Flip q0 to |1⟩
    if b == 1:
        qc.x(1)  # Flip q1 to |1⟩
        
    # Add a barrier for visualization
    qc.barrier()

    # Step 2: Apply the logic gate
    # Use a Toffoli (CCX) gate.

    qc.ccx(0, 1, 2)
    
    qc.barrier()

    qc.measure(2, 0)
    

    # shots=1 is enough because this circuit is deterministic. but we can use more to check if it is deterministic, if there is les number of unexpected results it might be due to errors in Quantum computer
    sampler = Sampler()
    job = sampler.run(qc, shots=1)
    result = job.result()
    

    counts = result.quasi_dists[0].binary_probabilities()
    
    # Return the measured bit (as an integer)
    measured_result = int(list(counts.keys())[0])
    return measured_result, qc # Return the result and the circuit

# 3. Compare the Results

inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
print("--- Classical vs. Quantum Simulation ---")
print("----------------------------------------")

for a, b in inputs:
    classical_result = classical_and(a, b)
    quantum_result, quantum_circuit = quantum_and(a, b)
    
    print(f"Input: ({a}, {b})")
    print(f"  Classical Result: {classical_result}")
    print(f"  Quantum Result:   {quantum_result}")
    print("----------------------------------------")

print("\nExample Quantum Circuit for (1, 1):")
_, qc_example = quantum_and(1, 1)
print(qc_example)
