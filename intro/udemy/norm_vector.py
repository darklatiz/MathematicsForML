from intro.udemy.vector_operations import VectorOperations
from intro.udemy.constants import *
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
