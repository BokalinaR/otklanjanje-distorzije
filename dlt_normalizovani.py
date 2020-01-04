import numpy as np
from numpy import linalg as la
import math

def matrica_2X9(t1, t2):
    M = np.matrix(
        [ [0, 0, 0, -t2[2]*t1[0], -t2[2]*t1[1], -t2[2]*t1[2], t2[1]*t1[0], t2[1]*t1[1], t2[1]*t1[2]],
         [t2[2]*t1[0], t2[2]*t1[1], t2[2]*t1[2], 0, 0, 0, -t2[0]*t1[0], -t2[0]*t1[1], -t2[0]*t1[2]]
        ])
    return M

def dlt_algoritam(v1, v2, n):
    A = []
    for i in range(n):
        a = matrica_2X9(v1[i], v2[i])
        
        if(i > 0):
            A = np.concatenate((A, a), axis = 0)
        else:
            A = a
    #print(A)
    U, D, Vt = la.svd(A, full_matrices=True)
    V = np.transpose(Vt)
    # P je poslednja kolona V
    V = V[:, -1]
    P = V.reshape(3,3)
    
    return P

def normalizacija_tacaka(v, n):
    
    #Teziste
    G = []
    tmp = [] # mesto gdecuvamo tacke u afinim koordinatama
    for i in range(n):
        A = np.array(v[i])
        # Afine koordinate
        A = np.array([A[0]/A[2], A[1]/A[2]])
        tmp.append(A)
        if(i > 0):
            G += A
        else:
            G = A
    n1 = 1/n # ono cime delimo koordinate tezista
    G = G * np.array([n1, n1])
    # print(G)
    
    # Matrica translacije
    T = np.matrix([ [1, 0, -G[0]],
                    [0, 1, -G[1]],
                    [0, 0, 1] ])
    
    lamb = 0
    for i in range(n):
        A = tmp[i] # trenutna tacka u njenim afinim koordinatama
        lamb += math.sqrt(A[0]*A[0] + A[1]*A[1])
    lamb = lamb / n
    
    # koeficijent homotetije
    k = math.sqrt(2) / lamb
    # Matrica homotetije
    S = np.matrix([[k, 0, 0],
                   [0, k, 0],
                   [0, 0, 1]
                   ])
    # Matrica normalizacije
    N = S @ T
    return N

# Unos podataka
n = int(input("Unesite zeljeni broj tacaka: "))
v1 = []
for i in range(n):
    print('Unesite koordinate originalne tacke', i+1)
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    A = [a1, a2, a3]
    v1.append(A)
print(v1)

v2 = []
for i in range(n):
    print('Unesite koordinate tacke slike', i+1)
    ap1 = int(input())
    ap2 = int(input())
    ap3 = int(input())
    Ap = [ap1, ap2, ap3]
    v2.append(Ap)
print(v2)  
###############################################

T = normalizacija_tacaka(v1, n)
Tp = normalizacija_tacaka(v2, n)

# Normalizovane originalne tacke i tacke slike
v1_novo = []
v2_novo = []
for i in range(n):
    A = np.matrix(v1[i])
    An = T @ A.T
    An = [An[0, 0], An[1, 0], An[2, 0]]
    
    Ap = np.matrix(v2[i])
    Apn = T @ Ap.T
    Apn = [Apn[0, 0], Apn[1, 0], Apn[2, 0]]
    
    v1_novo.append(An)
    v2_novo.append(Apn)
    
print()
# P nadvuceno
Pn = dlt_algoritam(v1_novo, v2_novo, n)
# T prim inverzna
Tp_inv = la.inv(Tp)
# Matrica preslikavanja
P = Tp_inv @ Pn @ T
print()
print("Matrica preslikavanja: ")
print(np.around(P, 5))
print()