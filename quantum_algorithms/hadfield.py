#used - https://lucaman99.github.io/new_blog/2020/mar16.html
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
import math
import random
from qiskit.circuit import QuantumCircuit
from qiskit.opflow import I, X, Z,Y


def mixer_unitary(nqubits):
    vs=int(math.sqrt(nqubits))
    st=np.array([I])
    for m in range(1,nqubits):
        st=np.append(st, [I])
    H=0
    for i in range(0, vs):
        nt=np.copy(st)
        nt[i*vs]=X
        nt[(i*vs)+1]=X
        nh=nt[0]
        for p in range(1,len(nt)):
            nh=nh^nt[p]
        H=H+nh 
                    
        nt=np.copy(st)
        nt[(i*vs)+1]=X
        nt[(i*vs)+2]=X
        nh=nt[0]
        for p in range(1,len(nt)):
            nh=nh^nt[p]
        H=H+nh 
        
        nt=np.copy(st)
        nt[i*vs]=Y
        nt[(i*vs)+1]=Y
        nh=nt[0]
        for p in range(1,len(nt)):
            nh=nh^nt[p]
        H=H+nh 
        
        nt=np.copy(st)
        nt[(i*vs)+1]=Y
        nt[(i*vs)+2]=Y
        nh=nt[0]
        for p in range(1,len(nt)):
            nh=nh^nt[p]
        H=H+nh        
    return H

def hadfield(n,qubo,p,param_seed,sp):
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
    if sp=='0213':
        qc_0.initialize('1000001001000001', qc_0.qubits)# -0213
    if sp=='0123':
        qc_0.initialize('1000010000100001', qc_0.qubits) #-0123
    if sp=='0231':
        qc_0.initialize('1000000101000010', qc_0.qubits)# -0231
    mix=mixer_unitary(nqubits)
    qaoa_mes = QAOA(optimizer = optimizer, quantum_instance =quantum_instance, initial_point=theta,initial_state=qc_0,mixer=mix,reps=p)
    qaoa = MinimumEigenOptimizer(qaoa_mes)
    qaoa_result = qaoa.solve(qubo)
    f_theta=qaoa_result.min_eigen_solver_result.optimal_point
    
    
    return qaoa_result,f_theta

