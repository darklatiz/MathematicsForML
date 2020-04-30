from intro.udemy.vector.vector_operations import VectorOperations
from intro.udemy.constants import *

ops = VectorOperations()

va = ops.create_vector([-3, 2, 5])
vb = ops.create_vector([4, -3, 0])

print("Cross Product = {0}".format(ops.cross_product(va, vb)))
print("Cross Product Numpy wise = {0}".format(ops.cross_product(va, vb, NUMPY_WISE)))