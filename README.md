# Master's Thesis
This repository contains the code for my Master's thesis in mathematics (see [thesis_final.pdf](https://github.com/aubreycoffey/TSP-Quantum-Computing/blob/main/thesis_final.pdf)) “Quantum algorithms for variants of the Traveling Salesperson Problem (TSP)”. In this work, I introduce two new quadratic unconstrained binary optimization formulations for the capacitated vehicle routing problem and a new quantum algorithm for the TSP based on graph states, the graph state alternating operator ansatz (GSAOA). We also benchmark some existing quantum algorithms against the GSAOA. 
## Implementation
As part of this thesis, we implemented several quantum algorithms to benchmark against our own algorithm. Those algorithms are the quantum alternating
operator ansatz (AOA) from Hadfield (hadfield.py), the quantum approximate optimization algorithm (QAOA) (qaoa.py), warm-start QAOA (wsqaoa.py). There
are two additional algorithms, simulated annealing (sa.py) and the variational quantum eigensolver (vqe.py) that can be found in the folder 
quantum_algorithms, but did not make it to the final benchmarking in the thesis. Our original algorithm is the GSAOA (gsaoa.py) which can be found in the 
same folder and the theory behind the algorithm is detailed in chapter 6 of the thesis, (thesis_final.pdf). 
