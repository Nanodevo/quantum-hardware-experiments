from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

service = QiskitRuntimeService()
backend = service.least_busy(operational=True, simulator=False)
print(f"Running on: {backend.name}")

# Adapt the circuit to the real chip's native gates and layout
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)

sampler = Sampler(mode=backend)
job = sampler.run([isa_circuit], shots=1000)
print(f"Job ID: {job.job_id()}")

result = job.result()
counts = result[0].data.meas.get_counts()
print(counts)