from intro.udemy.vector.vector_operations import VectorOperations
from intro.udemy.constants import *

ops = VectorOperations()
va = ops.create_vector([-3, 6])
va_unit = ops.unit_vector(va)
print("Unit vector va = {0}".format(va_unit))
ops.plot_vectors(va, va_unit)

vb = ops.create_vector([3,-3])
vb_unit = ops.unit_vector(vb)
ops.plot_vectors(vb, vb_unit)
