from intro.udemy.vector.vector_operations import VectorOperations
from intro.udemy.constants import *
import math

ops = VectorOperations()
# create two random integers vector
va = ops.create_rand_vector(2, 'int')
vb = ops.create_rand_vector(2, 'int')

# get magnitude and dot product
va_mag = ops.magnitude(va, NUMPY_WISE)
vb_mag = ops.magnitude(vb, NUMPY_WISE)
va_dot_magnitude_vb = abs(ops.dot_product(va, vb, TRANSPOSE_WISE))


# normalize the vectors (get the unit vectors)
va_unit = ops.unit_vector(va)
vb_unit = ops.unit_vector(vb)
va_unit_mag = ops.magnitude(va_unit)
vb_unit_mag = ops.magnitude(vb_unit, TRANSPOSE_WISE)

# get the dot product of thw normalized vectors
vau_dot_magnitude_vbu = abs(ops.dot_product(va_unit, vb_unit))