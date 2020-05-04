import numpy as geek

from intro.udemy.matrix.matrix_operations import MatrixOperations
from intro.udemy.vector.vector_operations import VectorOperations

sigma = geek.tanh
v_ops = VectorOperations()
m_ops = MatrixOperations()

def a1(a0, w1, b1):
    return sigma(w1 * a0 + b1)


def neuronal_network():
    # First set up the network.
    sigma = geek.tanh
    W = geek.array([[-2, 4, -1],[6, 0, -3]])
    b = geek.array([0.1, -2.5])

    # Define our input vector
    x = geek.array([0.3, 0.4, 0.1])
    W_a = W @ x
    W_a1 = m_ops.dot(W, x)
    a1 = sigma(W_a + b)

    # Calculate the values by hand,
    # and replace a1_0 and a1_1 here (to 2 decimal places)
    # (Or if you feel adventurous, find the values with code!)
    return geek.array(a1)

w1 = -5
b1 = 5
print(a1(1,w1, b1))
print(a1(0,w1, b1))

print(neuronal_network())
