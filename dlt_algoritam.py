import numpy as np
from numpy import linalg as la

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
    print(A)
    
    U, D, Vt = la.svd(A, full_matrices=True)
    V = np.transpose(Vt)
    # P je poslednja kolona V
    V = V[:, -1]
    P = V.reshape(3,3)
    
    return P
    
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

P = dlt_algoritam(v1, v2, n)

print()
print("Matrica preslikavanja: ")
print(np.around(P, 5))
