import math
from vectors.vector import Vector

class Matrixx(object):
    '''
        This class tries to impalement the main operations of Matrix (linear algebra) concepts.
    '''
    def __init__(self, data):
        super().__init__()
        self.row_count = len(data)
        self.column_count = len(data[0])
        self.row_vectors = []
        self.column_vectors = []
        self.matrixx = data

        for i in range(self.row_count):
            self.row_vectors.append(Vector(data[i]))

        for j in range(self.column_count):
            nums = []
            for i in range(self.row_count):
                nums.append(data[i][j])
            self.column_vectors.append(Vector(nums))

    def __str__(self):
        '''
        :return: String representation of the matrix
        '''

        str_cols = [str(vc) for vc in self.column_vectors]
        str_rows = [str(vr) for vr in self.row_vectors]
        str_matrix = ''
        for vrow in self.row_vectors:
            str_matrix = str_matrix + str(vrow) + "\n"
        str1 = "Matrix:\n{0}\nRow Vectors: {1}\nColumn Vectors: {2}"
        return str1.format(str_matrix, str_rows, str_cols)

    def __eq__(self, other):
        if self.row_count != other.row_count or self.column_count != other.column_count:
            return False

        for row in range(self.row_count):
            if self.row_vectors[row] != other.row_vectors[row]:
                return False

        #This loop for might not be needed
        for col in range(self.column_count):
            if self.column_vectors[col] != other.column_vectors[col]:
                return False

        return True

    def __add__(self, other):
        if self.row_count != other.row_count or self.column_count != other.column_count:
            raise Exception("Both Matrices MUST have same dimension")

        m_result = []
        for row in range(self.row_count):
            r_result = []
            for col in range(self.column_count):
                r_result.append(self.row_vectors[row].coordinates[col] + other.row_vectors[row].coordinates[col])
            m_result.append(r_result)

        return Matrixx(m_result)

    def scalar_multiplication(self, scalar):
        m_result = []
        for vector_row in self.row_vectors:
            r_result = []
            for col in range(self.column_vectors):
                r_result.append(vector_row[col] * scalar)
            m_result.append(r_result)

        return Matrixx(m_result)

    def __mul__(self, other):
        '''
        The number of columns of the 1st matrix must equal the number of rows of the 2nd matrix.
        And the result will have the same number of rows as the 1st matrix, and the same number of columns as the 2nd matrix.

        To multiply an M x N matrix by an N x P matrix, the ns must be the same,
        and the result is an M x P matrix.

        ie:
        1 x 3 matrix by 3 x 4   --> 3 ara the same result is 1 x 4 matrixx

        :param other: matrix
        :return: The resultant matrix
        '''

        if self.column_count != other.row_count:
            raise Exception("The dimension of both matrices do not check")
        matrixx_result =[]
        for row_vector in self.row_vectors:
            result = []
            for col_vector in other.column_vectors:
                result.append(row_vector.dot_product(col_vector))
            matrixx_result.append(result)

        return Matrixx(matrixx_result)

