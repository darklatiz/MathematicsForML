from intro.udemy.matrix.matrix_operations import MatrixOperations

# test for random M x N matrices whether s(A + B) = sA + sB
m_ops = MatrixOperations()
A = m_ops.create_random_matrix(3, 3, 'int')
B = m_ops.create_random_matrix(3, 3, 'int')
s = 11.432

# calculating s(A + B)
AB = m_ops.sum(A, B)
sAB = m_ops.scalar_multiplication(s, AB)
print("sA_plus_B: \n{0}".format(sAB))

# Calculating sA + sB
sA = m_ops.scalar_multiplication(s, A)
sB = m_ops.scalar_multiplication(s, B)
sA_plus_sB = m_ops.sum(sA, sB)
print("sA_plus_B: \n{0}".format(sA_plus_sB))

print("s(A + B) = sA + sB ? \n{0}".format(m_ops.equality(sAB, sA_plus_sB)))

print("Identity = \n{0}".format(m_ops.subtract(sAB, sA_plus_sB)))

print("It is not the Identity matriz but those values are too small")