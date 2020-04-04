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

        print(self.row_vectors)
        print(self.column_vectors)

    def __str__(self):
        return "Matrixx: {0}".format(self.matrixx)

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

