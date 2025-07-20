import numpy as np
from objective import tsp_objective
from objective import tsp_objective_ws
from qaoa import qaoa
from hadfield import hadfield
from wsqaoa import wsqaoa
from gsaoa import gsaoa
from vqe import vqe
n=4


insfils=['neuc_shape1','neuc_shape2','neuc_shape3','euc_shape1','euc_shape2','euc_shape3']

paramseedvals=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#only if initial param varies



#sa
from sa import sa
numreads=[1,100,1000,10000]
for ins in insfils:
    for j in numreads:    
        D = np.loadtxt('instances/'+ins+'.txt',  delimiter=',') 
        sol=sa(D,j)
        filestr='results/sa/sa_'+ins+'_numreads-'+str(j)+'.txt'
        file1 = open(filestr,"a")
        L = [str(sol)+'\n ||'] 
        file1.writelines(L)
        file1.close()


#vqe
for ins in insfils:
    D = np.loadtxt('instances/'+ins+'.txt',  delimiter=',') 
    qubo=tsp_objective(D)
    for j in paramseedvals:
        for p in range(1,21):
            filestr='results/vqe/vqe_'+ins+'_paramseed-'+str(j)+'_p-'+str(p)+'.txt'
            file1 = open(filestr,"a")
            sol,theta=vqe(n,qubo,p,j)
            L = [str(sol)+'\n ||',str(theta)+'\n ||'] 
            file1.writelines(L)
            file1.close()

#gsaoa
#sp=['none','shape1','shape2','shape3']
for ins in insfils:
    D = np.loadtxt('instances/'+ins+'.txt',  delimiter=',') 
    for i in sp:
        for j in paramseedvals:
            for p in range(1,21):
                filestr='results/gsaoa/gaaoa_'+ins+'_paramseed-'+str(j)+'_sp-'+str(i)+'_p-'+str(p)+'.txt'
                file1 = open(filestr,"a")
                edges,obj,thetas=gsaoa(D,p,j,i)
                L = [str(edges)+'\n ||',str(obj)+'\n ||',str(thetas)+'\n ||'] 
                file1.writelines(L)
                file1.close()


#hadfield
sp=['0213','0231','0123']
for ins in insfils:
    D = np.loadtxt('instances/'+ins+'.txt',  delimiter=',') 
    qubo=tsp_objective(D)
    for i in sp:
        for j in paramseedvals:
            for p in range(1,21):
                filestr='results/hadfield/hadfield_'+ins+'_paramseed-'+str(j)+'_sp-'+str(i)+'_p-'+str(p)+'.txt'
                file1 = open(filestr,"a")
                qaoa_result,f_theta=hadfield(n,qubo,p,j,i)
                L = [str(qaoa_result)+'\n ||',str(f_theta)+'\n ||'] 
                file1.writelines(L)
                file1.close()

#wsqaoa
for ins in insfils:
    D = np.loadtxt('instances/'+ins+'.txt',  delimiter=',') 
    qubo,H=tsp_objective_ws(D)
    for j in paramseedvals:
        for p in range(1,21):
            filestr='results/wsqaoa/wsqaoa_'+ins+'_paramseed-'+str(j)+'_p-'+str(p)+'.txt'
            file1 = open(filestr,"a")
            qaoa_result,f_theta,method=wsqaoa(n,qubo,H,p,j)
            L = [str(qaoa_result)+'\n ||',str(f_theta)+'\n ||',str(method)+'\n ||'] 
            file1.writelines(L)
            file1.close()
    

#qaoa
for ins in insfils:
    D = np.loadtxt('instances/'+ins+'.txt',  delimiter=',') 
    qubo=tsp_objective(D)
    for j in paramseedvals:
        for p in range(1,21):
            filestr='results/qaoa/qaoa_'+ins+'_paramseed-'+str(j)+'_p-'+str(p)+'.txt'
            file1 = open(filestr,"a")
            qaoa_result,f_theta=qaoa(n,qubo,p,j)
            L = [str(qaoa_result)+'\n ||',str(f_theta)+'\n ||'] 
            file1.writelines(L)
            file1.close()











            
        
