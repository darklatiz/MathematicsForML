import numpy as geek
from numpy import linalg as LA
from intro.udemy.constants import *
import math
import matplotlib.pyplot as plt


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

    def outer_product(self, va, vb, type_outter_product=NUMPY_WISE):
        va_size = geek.size(va)
        vb_size = geek.size(vb)
        if va_size != vb_size:
            raise Exception("Dimension (size) must agree")

        if type_outter_product == NUMPY_WISE:
            return geek.outer(va, vb)
        elif type_outter_product == TRANSPOSE_WISE:
            vbT = geek.transpose(vb)
            F = geek.zeros((va_size, vb_size))
            # this is not vey optimal since we have two for loops
            for i in range(va_size):
                for j in range(vb_size):
                    F[i, j] = va[i] * vbT[j]
            return F

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
            sum_squared = self.dot_product(vector, vector, ELEMENT_WISE)
            return math.sqrt(sum_squared)
        elif type_dot_product == NUMPY_WISE:
            return math.sqrt(self.dot_product(vector, vector, NUMPY_WISE))
        elif type_dot_product == TRANSPOSE_WISE:
            return math.sqrt(self.dot_product(vector, vector, TRANSPOSE_WISE))
        else:
            return LA.norm(vector)

    def angle_between_vectors(self, va, vb, type_calculation=GEOMETRIC_WISE):
        if type_calculation == 'geometric':
            dot = self.__dot_product_numpy_way(va, vb)
            magv1 = self.magnitude(va)
            magv2 = self.magnitude(vb)
            pre = dot / (magv1 * magv2)
            angle_rad = math.acos(pre)
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

    def create_rand_vector(self, num_elements, data_type='default', low=1, upper=100):
        if data_type == 'int':
            return geek.random.randint(low, upper, num_elements)
        else:
            return geek.random.rand(num_elements)

    def crete_zero_vector(self, dimension):
        return geek.zeros(dimension)

    def cross_product(self, va, vb, type_calculation=ELEMENT_WISE):
        va_size = geek.size(va)
        vb_size = geek.size(vb)
        if va_size != 3 and vb_size != 3:
            raise Exception("Either va or vb is not a 3D vector")
        res = self.crete_zero_vector(3)
        if type_calculation == ELEMENT_WISE:
            res[0] = va[1] * vb[2] - va[2] * vb[1]
            res[1] = va[0] * vb[2] - va[2] * vb[0]
            res[2] = va[0] * vb[1] - va[1] * vb[0]
            return res
        elif type_calculation == NUMPY_WISE:
            return geek.cross(va, vb)

    def unit_vector(self, va):
        return self.escalar_multiplication(va, 1 / self.magnitude(va))

    def plot_vectors(self, va, vb):
        origin = [0], [0]  # origin point
        V = geek.array([va, vb])
        fig, ax = plt.subplots()
        ax.quiver(*origin, V[:, 0], V[:, 1], color=['r', 'b', 'g'], scale=18)
        ax.set_title('Ploting the unit vector')
        plt.grid()
        ax.set_aspect('equal')
        plt.show()
