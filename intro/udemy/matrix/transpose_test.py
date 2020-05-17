from intro.udemy.matrix.matrix_operations import MatrixOperations

m_ops = MatrixOperations()

M = [[1,2,3],[4,5,6],[7,8,9]]
M_eror = [[1,2,3],[6],[7,8]]

print("M Transpose: \n{0}".format(m_ops.transpose(M)))

transpose_err = m_ops.transpose(M_eror)
print("Type error: {0}".format(type(transpose_err)))
print("Type[0] error: {0}".format(type(transpose_err[0])))
print("M Transpose error: \n{0}".format(transpose_err))
