from intro.udemy.matrix.matrix_operations import MatrixOperations

m_ops = MatrixOperations()

M1 = m_ops.create_random_matrix(5,5,'int')
print("M1: \n{0}".format(M1))
print("Diagonal M1: \n{0}".format(m_ops.diagonal(M1)))
print("Trace M1: \n{0}".format(m_ops.trace(M1)))

# The linearity of trace
# Determine the relationship between tr(A) + tr(B) and tr(A + B)
A = m_ops.create_random_matrix(5, 5)
B = m_ops.create_random_matrix(5, 5)
A_plus_B = m_ops.sum(A, B)
trace_A = m_ops.trace(A)
trace_B = m_ops.trace(B)

trA_plus_trB = trace_A + trace_B
tr_A_plus_B = m_ops.trace(A_plus_B)
print("tr(A) + tr(B) = {0}".format(trA_plus_trB))
print("tr(A + B) = {0}".format(tr_A_plus_B))
print("Must be zero = {0}".format(trA_plus_trB - tr_A_plus_B))

# Determine the relationship between tr(scalar * A) and scalar * tr(A)
scalar = 2.5
A_times_scalar = m_ops.scalar_multiplication(scalar, A)
tr_A_times_scalar = m_ops.trace(A_times_scalar)
print("tr(scalar * A) = {0}".format(tr_A_times_scalar))
print("scalar * tr(A) = {0}".format(scalar * trace_A))
print("Must be zero = {0}".format(tr_A_times_scalar - (scalar * trace_A)))
