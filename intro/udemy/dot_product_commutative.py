from intro.udemy.vector_operations import VectorOperations
# Is the dot product commutative
# a*b = b*a ??

# Generate 2 100 vector element

v_ops = VectorOperations()
v1 = v_ops.create_rand_vector(100)
v2 = v_ops.create_rand_vector(100)

# Compute the dot product
print("Dot Product v1 T v2 = {0}".format(v_ops.dot_product(v1, v2)))
print("Dot Product v2 T v1 = {0}".format(v_ops.dot_product(v2, v1, "transpose_wise")))

# Generate 2 element vectors and repeat
v3 = v_ops.create_vector([1,2])
v4 = v_ops.create_vector([3,4])
print("Dot Product v3 T v4 = {0}".format(v_ops.dot_product(v3, v4)))
print("Dot Product v4 T v3 = {0}".format(v_ops.dot_product(v4, v3, "transpose_wise")))