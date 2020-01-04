# Radjeno prema resenju sa predavanja PPGR
import numpy as np
from numpy import linalg as la

def naivni_algoritam(v):
    A = v[0]
    B = v[1]
    C = v[2]
    D = v[3]
    
    A0 = (1, 0, 0)
    B0 = (0, 1, 0)
    C0 = (0, 0, 1)
    D0 = (1, 1, 1)
    
    delta = [ [A[0], B[0], C[0]],
              [A[1], B[1], C[1]],
              [A[2], B[2], C[2]] ]
    
    delta1 = [ [D[0], B[0], C[0]],
               [D[1], B[1], C[1]],
               [D[2], B[2], C[2]] ]
    
    
    delta2 = [ [A[0], D[0], C[0]],
               [A[1], D[1], C[1]],
               [A[2], D[2], C[2]] ]
    
    delta3 = [ [A[0], B[0], D[0]],
               [A[1], B[1], D[1]],
               [A[2], B[2], D[2]] ]
    
    delta_det = la.det(delta)
    delta1_det = la.det(delta1)
    delta2_det = la.det(delta2)
    delta3_det = la.det(delta3)
    
    lambda1 = delta1_det/delta_det
    lambda2 = delta2_det/delta_det
    lambda3 = delta3_det/delta_det
    
    
    P = [[lambda1*x for x in A],
         [lambda2*x for x in B],
         [lambda3*x for x in C]]
    
    
    return np.transpose(P)
    
n = 4
v1 = []
for i in range(n):
    print('Unesite koordinate originalne tacke', i+1)
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    A = [a1, a2, a3]
    v1.append(A)
    
#print(v1)
v2 = []
for i in range(n):
    print('Unesite koordinate tacke slike', i+1)
    ap1 = int(input())
    ap2 = int(input())
    ap3 = int(input())
    Ap = [ap1, ap2, ap3]
    v2.append(Ap)
#print(v2)    

P1 = naivni_algoritam(v1)
P2 = naivni_algoritam(v2)

P1_inv = la.inv(P1)
P = np.matmul(P2, P1_inv)

print()
print("Matrica preslikavanja: ")
print(P)