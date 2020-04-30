from intro.udemy.vector.vector_operations import VectorOperations
from intro.udemy.constants import *

ops = VectorOperations()

va = ops.create_rand_vector(2)
vb = ops.create_rand_vector(2)

MM1 = ops.outer_product(va, vb)
MM2 = ops.outer_product(va, vb, TRANSPOSE_WISE)

print("MM1 = {0}".format(MM1))
print("MM2 = {0}".format(MM2))