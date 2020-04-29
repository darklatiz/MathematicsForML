import numpy as geek
from numpy import linalg as LA
from intro.udemy.constants import *
import math


class VectorOperations(object):

    def __init__(self):
        print("Vector operations initialized")

    def dot_product(self, va, vb, type_dot_product=ELEMENT_WISE):
        if type_dot_product == ELEMENT_WISE:
            return self.__dot_product_for_loop(va, vb)
        elif type_dot_product == TRANSPOSE_WISE:
            return geek.transpose(va) @ vb
        else:
            return self.__dot_product_numpy_way(va, vb)

    def outter_product(self, va, vb, type_outter_product=NUMPY_WISE):
        if type_outter_product == NUMPY_WISE:
            return geek.outer(va, vb)
        elif type_outter_product == TRANSPOSE_WISE:

    def __dot_product_for_loop(self, vector, other_vector):
        res = 0
        if len(vector) != len(other_vector):
            raise Exception("Both Matrices MUST have same dimension")

        for col in range(geek.size(vector)):
            res += vector.item(col) * other_vector.item(col)
        return res

    def __dot_product_numpy_way(self, vector, other_vector):
        return vector @ other_vector

    def magnitude(self, vector, type_dot_product=ELEMENT_WISE):
        if type_dot_product == ELEMENT_WISE:
            sum_squared = self.__dot_product_for_loop(vector, vector)
            return math.sqrt(sum_squared)
        elif type_dot_product == NUMPY_WISE:
            return math.sqrt(self.__dot_product_numpy_way(vector, vector))
        else:
            return LA.norm(vector)

    def angle_between_vectors(self, va, vb, type_calculation=GEOMETRIC_WISE):
        if type_calculation == 'geometric':
            dot = self.__dot_product_numpy_way(va, vb)
            magv1 = self.magnitude(va)
            magv2 = self.magnitude(vb)
            pre = dot/(magv1 * magv2)
            angle_rad =  math.acos(pre)
            angle_degrees = math.degrees(angle_rad)
            return angle_rad, angle_degrees

    def is_orthogonal(self, va, vb):
        dot = self.__dot_product_numpy_way(va, vb)
        if dot == 0:
            return True
        else:
            return False

    def escalar_multiplication(self, v1, scalar):
        return v1 * scalar


    def create_vector(self, data):
        if type(data) is list:
            return geek.array(data)
        else:
            raise Exception("Vector cannot be created, we need a list to do it [a,b,c,d,...]")

    def create_rand_vector(self, num_elements):
        return geek.random.rand(num_elements)



if __name__ == '__main__':
    ops = VectorOperations()
    v = ops.create_vector([1, 2, 3, 4])
    print("Norm ||v|| = {0}".format(ops.magnitude(v, ELEMENT_WISE)))
    print("Norm ||v|| = {0}".format(ops.magnitude(v, NUMPY_WISE)))
    print("Norm ||v|| = {0}".format(ops.magnitude(v, LA_NORM_WISE)))

    v1 = ops.create_vector([16, -2, 4])
    v2 = ops.create_vector([.5, 2, -1])
    rad, degress = ops.angle_between_vectors(v1, v2)
    print("Rad = {0} , Degrees= {1}".format(rad, degress))
    print("Dot product = {0}".format(ops.dot_product(v1, v2)))
    print("Are orthogonal: {0}".format(ops.is_orthogonal(v1, v2)))


    print("***************************** Angles ****************")
    print("*****************************************************")
    va = ops.create_vector([1, -2])
    vb = ops.create_vector([2, 3])
    vc = ops.create_vector([0, 2])

    print("va Vs vb")
    print("Dot Product vaTvb = {0}".format(ops.dot_product(va, vb)))
    rad, ang = ops.angle_between_vectors(va, vb)
    print("Angle va Vb = {0}".format(ang))

    print("va Vs vc")
    print("Dot Product vaTvc = {0}".format(ops.dot_product(va, vc)))
    rad, ang = ops.angle_between_vectors(va, vc)
    print("Angle va Vb = {0}".format(ang))

    print("vb Vs vc")
    print("Dot Product vaTvb = {0}".format(ops.dot_product(vb, vc)))
    rad, ang = ops.angle_between_vectors(vb, vc)
    print("Angle va Vb = {0}".format(ang))