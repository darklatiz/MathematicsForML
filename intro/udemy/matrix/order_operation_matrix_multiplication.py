# transpose(LIVE) = transpose(E) * transpose(V) * transpose(I) * transpose(L)
from intro.udemy.matrix.matrix_operations import MatrixOperations
import numpy as geek
m_ops = MatrixOperations()
m = 20
n = 20
L = m_ops.create_random_matrix(m, n)
I = m_ops.create_random_matrix(m, n)
V = m_ops.create_random_matrix(m, n)
E = m_ops.create_random_matrix(m, n)

LIVE = L * I * V * E
LIVE_T = geek.transpose(LIVE)

ET = E.T
VT = V.T
IT = I.T
LT = L.T
EVIL_T = ET * VT * IT * LT

print("res: \n{0}".format(m_ops.subtract(LIVE_T, EVIL_T)))
