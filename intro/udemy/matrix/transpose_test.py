from intro.udemy.matrix.matrix_operations import MatrixOperations

m_ops = MatrixOperations()

M = [[1,2,3],[4,5,6],[7,8,9]]
M_eror = [[1,2,3],[6],[7,8]]

print("M Transpose: \n{0}".format(m_ops.transpose(M)))

transpose_err = m_ops.transpose(M_eror)
print("Type error: {0}".format(type(transpose_err)))
print("Type[0] error: {0}".format(type(transpose_err[0])))
print("M Transpose error: \n{0}".format(transpose_err))


# let's see what happens with compex numbers

M_complex = [[1 + 2j, -2 -3.5j, 1 + 1j],[101j, -123-3.3j, 12+45.5j],[1 -1j, 2 -2j, 3+3j]]
print("M_complex: \n{0}".format(m_ops.create_matrix(M_complex)))
M_complex_T = m_ops.transpose(M_complex)
M_complex_TH = m_ops.transpose(M_complex, hermitian=True)
print("M_complex Transpose: \n{0}".format(M_complex_T))
print("M_complex Hermitian Transpose: \n{0}".format(M_complex_TH))
