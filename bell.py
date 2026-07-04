from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Bell state: entangle two qubits
qc = QuantumCircuit(2)
qc.h(0)          # Hadamard on qubit 0
qc.cx(0, 1)      # CNOT: entangles qubit 1 with qubit 0
qc.measure_all()

sim = AerSimulator()
result = sim.run(qc, shots=1000).result()
print(result.get_counts())