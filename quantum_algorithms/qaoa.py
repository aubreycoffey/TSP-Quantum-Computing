import numpy as np
from qiskit import BasicAer
from qiskit.algorithms import QAOA
from qiskit.tools.jupyter import *
from qiskit.providers.aer import QasmSimulator
from qiskit.algorithms.optimizers import COBYLA
from qiskit.providers.basicaer import QasmSimulatorPy  # local simulator
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.utils.algorithm_globals import algorithm_globals
from qiskit.utils import QuantumInstance
import random
from qiskit.circuit import QuantumCircuit

def qaoa(n,qubo,p,param_seed):
    optimizer = COBYLA(maxiter=1000, tol=0.0001)
    algorithm_globals.random_seed = 123
    quantum_instance = QuantumInstance(
        BasicAer.get_backend('qasm_simulator'),
        seed_simulator=123,
        seed_transpiler=123,
    )
    nqubits=n**2
    random.seed(param_seed)
    theta=[]
    for i in range(2*p):
        x=random.uniform(0, 1)
        if i%2==0:
            x=x*np.pi
        else:
            x=x*2*np.pi
        theta.append(x)
    #run qaoa
    qc_0 = QuantumCircuit(nqubits)
    for i in range(0, nqubits):
        qc_0.h(i)
       
    qaoa_mes = QAOA(optimizer = optimizer, quantum_instance =quantum_instance, initial_point=theta,initial_state=qc_0,reps=p)
    qaoa = MinimumEigenOptimizer(qaoa_mes)
    qaoa_result = qaoa.solve(qubo)
    f_theta=qaoa_result.min_eigen_solver_result.optimal_point

    return qaoa_result,f_theta



