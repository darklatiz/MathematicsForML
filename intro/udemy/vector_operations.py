import numpy as geek
from numpy import linalg as LA
import math


class VectorOperations(object):

    def __init__(self):
        print("Vector operations initialized")

    def __dot_product_for_loop(self, vector, other_vector):
        res = 0
        if len(vector) != len(other_vector):
            raise Exception("Both Matrices MUST have same dimension")

        for col in range(geek.size(vector)):
            res += vector.item(col) * other_vector.item(col)
        return res

    def __dot_product_numpy_way(self, vector, other_vector):
        return geek.dot(vector, other_vector)

    def magnitude(self, vector, type_dot_product='element_wise'):
        if type_dot_product == 'element_wise':
            sum_squared = self.__dot_product_for_loop(vector, vector)
            return math.sqrt(sum_squared)
        elif type_dot_product == 'numpy_dot_way':
            return math.sqrt(self.__dot_product_numpy_way(vector, vector))
        else:
            return LA.norm(vector)

    def create_vector(self, data):
        if type(data) is list:
            return geek.array(data)
        else:
            raise Exception("Vector cannot be created, we need a list to do it [a,b,c,d,...]")


if __name__ == '__main__':
    ops = VectorOperations()
    v = ops.create_vector([1, 2, 3, 4])
    print("Norm ||v|| = {0}".format(ops.magnitude(v, 'element_wise')))
    print("Norm ||v|| = {0}".format(ops.magnitude(v, 'numpy_dot_way')))
    print("Norm ||v|| = {0}".format(ops.magnitude(v, 'LA-norm')))
