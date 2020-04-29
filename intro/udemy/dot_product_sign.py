from intro.udemy.vector_operations import VectorOperations

ops = VectorOperations()

# Generate two vectors R3

v1 = ops.create_vector([-3, 4, 5])
v2 = ops.create_vector([3, 6, -3])

es1 = 2
es2 = 3

# Compute dot product
dot = ops.dot_product(v1, v2, 'numpy')
dot_transpose_way = ops.dot_product(v1, v2, 'transpose_wise')

# Compute dot product between scaled vectors
v1_scaled = ops.escalar_multiplication(v1, es1)
v2_scaled = ops.escalar_multiplication(v2, es2)
dot_scaled = ops.dot_product(v1_scaled, v2_scaled)

print("Dot Product = {0}, Dot product scaled vectors: {1}".format(dot_transpose_way, dot_scaled))

v1 = ops.create_vector([-3, 4, 6])
v2 = ops.create_vector([3, 6, -3])
dot = ops.dot_product(v1, v2, 'numpy')
dot_transpose_way = ops.dot_product(v1, v2, 'transpose_wise')

# Compute dot product between scaled vectors
v1_scaled = ops.escalar_multiplication(v1, es1)
v2_scaled = ops.escalar_multiplication(v2, es2)
dot_scaled = ops.dot_product(v1_scaled, v2_scaled)

print("Dot Product = {0}, Dot product scaled vectors: {1}".format(dot_transpose_way, dot_scaled))