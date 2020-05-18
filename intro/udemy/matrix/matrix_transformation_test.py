import numpy as geek
import matplotlib.pyplot as plt
import math

m = 4
N = geek.round( 10 * geek.random.randn(m,m) )
# 2D input vector
v = geek.array([ 3, -2])

# 2x2 transformation matrix
A = geek.array([ [1,-1], [2,1] ])

# output vector is Av (convert v to column)
w = A @ geek.matrix.transpose(v)


# plot them
plt.plot([0,v[0]],[0,v[1]],label='v')
plt.plot([0,w[0]],[0,w[1]],label='Av')

plt.grid()
plt.axis((-6, 6, -6, 6))
plt.legend()
plt.title('Rotation + stretching')
plt.show()


# with nonsymmetric matrix
N @ w    # 1
geek.matrix.transpose(N @ w) # 2
w @ N    # 3
geek.matrix.transpose(w) @ geek.matrix.transpose(N)  # 4
geek.matrix.transpose(w) @ N   # 5