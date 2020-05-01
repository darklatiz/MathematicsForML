import numpy as geek
import math
from intro.udemy.constants import *


class MatrixOperations(object):
    def __init__(self):
        print("Matriz operations initialized")

    def create_random_matrix(self, m_rows, n_cols, data_type='default', low=1, upper=100):
        if data_type == 'int':
            return geek.random.randint(low, upper, size=(m_rows, n_cols))
        else:
            return geek.random.rand(m_rows, n_cols)

    def create_matrix(self, data):
        if type(data) is list and type(data[0]) is list:
            return geek.array(data)
        else:
            raise Exception("Data {0} seems not to be a Matrix".format(data))

    def sum(self, M_1, M_2):
        """

        :param M_1: Matrix 1
        :param M_2: Matrix 2
        :return: The sume of M_1 + M_2
        """
        m1_is_not_ndarray = self.__is_data_an_nd_array(M_1)
        m2_is_not_ndarray = self.__is_data_an_nd_array(M_2)

        if m1_is_not_ndarray:
            M_1 = self.create_matrix(M_1)

        if m2_is_not_ndarray:
            M_2 = self.create_matrix(M_2)
        return M_1 + M_2

    def subtract(self, M_1, M_2):
        """
        Method to subtract Matrix1 - Matrix2
        :param M_1: Matrix 1
        :param M_2: Matrix 2
        :return: Subtracted Matrix
        """
        m1_is_not_ndarray = self.__is_data_an_nd_array(M_1)
        m2_is_not_ndarray = self.__is_data_an_nd_array(M_2)

        if m1_is_not_ndarray:
            M_1 = self.create_matrix(M_1)

        if m2_is_not_ndarray:
            M_2 = self.create_matrix(M_2)
        return M_1 - M_2

    def __is_data_an_nd_array(self, data):
        return type(data) is not geek.ndarray
    
    def identity_matrix(self, size):
        return geek.identity(size)
    
    def shift(self, M, scalar):
        return self.sum(M, scalar * self.identity_matrix(M.shape[0]))


if __name__ == '__main__':
    m_ops = MatrixOperations()
    M1 = m_ops.create_random_matrix(2, 2)
    M2 = m_ops.create_random_matrix(3, 2, INT_TYPE)
    print("M1 = {0}".format(M1))
    print("M2 = {0}".format(M2))

    # lower and upper plus int
    M4 = m_ops.create_random_matrix(4, 5, INT_TYPE, -100, 100)
    print("M4 = {0}".format(M4))

    # Incorrect data
    try:
        MM = m_ops.create_matrix([1, 2, 3, 5, 6, 7])
    except Exception as ex:
        print("Error detected: {0}".format(ex))

    MM4 = m_ops.create_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("MM4= {0}".format(MM4))

    # usiong list of list
    M_res = m_ops.sum([[1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]])

    #numpy array
    K = m_ops.create_random_matrix(5, 5, INT_TYPE, -100, 100)
    K1 = m_ops.create_random_matrix(4, 5)
    M_res01 = m_ops.sum(K, K)
    M_res02 = m_ops.subtract(K, K)
    print("Sum: {0}".format(M_res01))
    print("Sub: {0}".format(M_res02))

    shift = m_ops.shift(K, 2)
    print("Shift: {0}".format(shift))
