import numpy as np

def transformisi_matricu(M):
    n = len(M)
    A = np.identity(n**2)
    b = [0] * (n**2)
    Aeq = np.zeros((n, n**2))
    beq = np.zeros((n-2,1))
    C = np.zeros((1,n**2))

    for i in range(n):
        for j in range(n):
            b[i*n + j] = M[i][j]

            if M[i][j] != 0:
                Aeq[i][i*n + j] = -1
                Aeq[j][i*n + j] = 1

    for i in range(n):
        if M[0][i] != 0:
            C[0][i] = -1

    Aeq = np.delete(Aeq, (0, n-1), axis=0)
    return (C,A,b,Aeq,beq)


def transformisi_u_matricu(A,n):
    M = np.zeros((n,n))
    for i in range(n):
        M[i] = A[(n*i):(n*i+n)]
    return M

def zaokruzi_vrijednosti(M):
    return np.around(M, 2)