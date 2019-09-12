import numpy as np
import math

def simplex(A,b,c,Aeq,beq):
    m=len(A)
    n=len(A[0])
    m1=len(Aeq)
    n1=len(Aeq[0])
    baza=[]
    for i in range(0,m1):
        b.append(beq[i])
        A.append(Aeq[i])
    print(b)
    print(A)
    for i in range(1,m+m1+1):
        baza.append(n+i)
        A[i-1].insert(0,b[i-1])
        for j in range(n+1,n+m+m1+1):
            A[i-1].append(0)
        A[i-1][n+i]=1
    x=c
    M=999999
    Z=0
    for i in range(0,m1):
        Z=Z-M*beq[i]
    x.insert(0,Z)
    for j in range(n+1,n+m+1):
        x.append(0)
    for j in range(n+m+1,n+m+m1+1):
        x.append(-M)
    #print(x)
    A.insert(0,x)
    print(A)


    optimal=False
    while not optimal:
        cmax=-1
        q=0
        p=0
        for j in range(1,m+n+m1+1):
            if A[0][j]>0 and A[0][j]>cmax:
                cmax=A[0][j]
                q=j
            if cmax==-1:
                optimal=True
            else:
                tmax=math.inf
                for i in range(1,m+m1+1):
                    if A[i][q]>0:
                        if A[i][0]/A[i][q]<tmax:
                            tmax=A[i][0]/A[i][q]
                            p=i
                if tmax==math.inf:
                    return print("Rjesenje je neograniceno")
                baza[p-1]=q
                pivot=A[p][q]
                for j in range(0,m+n+m1+1):
                    A[p][j]=A[p][j]/pivot
                for i in range(0,m+m1+1):
                    if i!=p:
                        faktor=A[i][q]
                        for j in range(0,m+n+m1+1):
                            A[i][j]=A[i][j]-faktor*A[p][j]
        print("____")
        print(A)
    x=[]
    for j in range (1,m+n+m1+1):
        x.append(0)
    for i in range(1,m+m1+1):
        x[baza[i-1]-1]=A[i][0]
    Z=-1*A[0][0]
    x=x[0:n]
    return [x,Z]



A=[[1,2],[3,4]]
b=[15, 30]
c=[3,3]
beq=[10]
Aeq=[[6, 7]]
print("**********************")

print(simplex(A,b,c,Aeq,beq))