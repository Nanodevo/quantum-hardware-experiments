# Bell State: Simulation vs. Real Quantum Hardware

First hands-on experiment comparing an ideal Bell state on the Qiskit Aer
simulator against execution on IBM's `ibm_fez` (156-qubit Heron QPU).

## Results (1000 shots)
| Outcome | Simulator | ibm_fez |
|---------|-----------|---------|
| 00      | 472       | 510     |
| 11      | 528       | 427     |
| 01      | 0         | 28      |
| 10      | 0         | 35      |

The ~6.3% population in forbidden states (01/10) on real hardware reflects
gate errors, decoherence, and readout error — absent in ideal simulation.

## Files
- `bell.py` — Bell state on the local Aer simulator
- `bell_real.py` — same circuit on real IBM hardware via Qiskit Runtime
- `bell_hardware_vs_sim.ipynb` — visualization and error analysis
