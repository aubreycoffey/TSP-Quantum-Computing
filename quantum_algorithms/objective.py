from docplex.mp.model import Model
from qiskit_optimization.translators import from_docplex_mp
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo
import numpy as np

def tsp_objective(dmat):
    #xv,i, where v represents the vertex and i represents its order in a prospective cycle.
    mdl = Model()
    l=len(dmat)
    varlist=[]
    for i in range(0,l):
        for m in range(0,l):
            varlist.append('x_'+str(i)+'_'+str(m))
    for i in varlist:
        locals()[i] = mdl.binary_var(i)
        

    #create our hamiltonian
    #for our A and B values we want 0< B*max(Wuv)< A
    B=1
    A=dmat.max()+10
    #we need three terms in our hamiltonian 
    #first term is A* the sum over the vertices * (1-sum over order)^2
    H1=0
    for v in range(0,l):
        s=1
        for j in range(0,l):
            s=s-eval('x_'+str(v)+'_'+str(j))
        s=s**2
        H1=H1+s
    H1=A*H1
    #second term is A* the sum over the order * (1-sum over vertices)^2
    H2=0
    for j in range(0,l):
        s=1
        for v in range(0,l):
            s=s-eval('x_'+str(v)+'_'+str(j))
        s=s**2
        H2=H2+s
    H2=A*H2
    #third term is B* sum over all possible edges(uv in E) W(weight of uv) *the sum over order of x_u_j*x_v_j+1
    H3=0
    for u in range(0,l):
        for v in range(0,l):
            w=dmat[u,v]
            if w!=0:
                s=0
                for j in range(0,l):
                    s=s+(eval('x_'+str(u)+'_'+str(j))*eval('x_'+str(v)+'_'+str((j+1)%l)))
                s=w*s
                H3=H3+s
    H3=B*H3
    H=H1+H2+H3
    
    objective=H
    mdl.minimize(objective)
    qp = QuadraticProgram()
    qp=from_docplex_mp(mdl)
    qubo_converter = QuadraticProgramToQubo()
    qubo = qubo_converter.convert(qp)

    return qubo

def tsp_objective_ws(dmat):
    #xv,i, where v represents the vertex and i represents its order in a prospective cycle.
    mdl = Model()
    l=len(dmat)
    varlist=[]
    for i in range(0,l):
        for m in range(0,l):
            varlist.append('x_'+str(i)+'_'+str(m))
    for i in varlist:
        locals()[i] = mdl.binary_var(i)
        

    #create our hamiltonian
    #for our A and B values we want 0< B*max(Wuv)< A
    B=1
    A=dmat.max()+10
    #we need three terms in our hamiltonian 
    #first term is A* the sum over the vertices * (1-sum over order)^2
    H1=0
    for v in range(0,l):
        s=1
        for j in range(0,l):
            s=s-eval('x_'+str(v)+'_'+str(j))
        s=s**2
        H1=H1+s
    H1=A*H1
    #second term is A* the sum over the order * (1-sum over vertices)^2
    H2=0
    for j in range(0,l):
        s=1
        for v in range(0,l):
            s=s-eval('x_'+str(v)+'_'+str(j))
        s=s**2
        H2=H2+s
    H2=A*H2
    #third term is B* sum over all possible edges(uv in E) W(weight of uv) *the sum over order of x_u_j*x_v_j+1
    H3=0
    for u in range(0,l):
        for v in range(0,l):
            w=dmat[u,v]
            if w!=0:
                s=0
                for j in range(0,l):
                    s=s+(eval('x_'+str(u)+'_'+str(j))*eval('x_'+str(v)+'_'+str((j+1)%l)))
                s=w*s
                H3=H3+s
    H3=B*H3
    H=H1+H2+H3
    
    objective=H
    mdl.minimize(objective)
    qp = QuadraticProgram()
    qp=from_docplex_mp(mdl)
    qubo_converter = QuadraticProgramToQubo()
    qubo = qubo_converter.convert(qp)


    return qubo,H





