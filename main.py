from transformisi_matricu import *
from scipy.optimize import linprog

# matrice incidencije
M1= [[0,3,2,2,0,0,0,0],
    [0,0,0,0,5,1,0,0],
    [0,0,0,0,1,3,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,0,4],
    [0,0,0,0,0,0,0,0]
    ]

M2= [[0,20,60,0,0,0],
    [0,0,50,30,10,0],
    [0,0,0,35,0,10],
    [0,0,0,0,30,25],
    [0,0,0,0,0,50],
    [0,0,0,0,0,0]
    ]

M3= [[0,3,1,1,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,0,0,0,3.5,0],
    [0,0,0,0,4,4,0],
    [0,0,0,0,0,0,4],
    [0,0,0,2.5,0,0,1],
    [0,0,0,0,0,0,0]
    ]

# testiranje
print("Simulacija problema maksimalnog protoka kroz komunikacionu mrežu")
(C,A,b,Aeq,beq) = transformisi_matricu(M1)
res = linprog(C, A_ub=A, b_ub = b, A_eq = Aeq, b_eq = beq)

X = zaokruzi_vrijednosti(transformisi_u_matricu(res.x, len(M1)))
Z = zaokruzi_vrijednosti(-1 * res.fun)

print(X)
print(Z)

print("Simulacija problema maksimalnog protoka u finansijama")
(C,A,b,Aeq,beq) = transformisi_matricu(M2)
res = linprog(C, A_ub=A, b_ub = b, A_eq = Aeq, b_eq = beq)

X = zaokruzi_vrijednosti(transformisi_u_matricu(res.x, len(M2)))
Z = zaokruzi_vrijednosti(-1 * res.fun)

print(X)
print(Z)

print("Simulacija transportnog problema maksimalnog protoka")
(C,A,b,Aeq,beq) = transformisi_matricu(M3)
res = linprog(C, A_ub=A, b_ub = b, A_eq = Aeq, b_eq = beq)

X = zaokruzi_vrijednosti(transformisi_u_matricu(res.x, len(M3)))
Z = zaokruzi_vrijednosti(-1 * res.fun)

print(X)
print(Z)