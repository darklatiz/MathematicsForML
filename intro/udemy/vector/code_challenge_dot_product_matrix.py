import numpy as np


def dot_product_for_loop(v1, v2):
    res = 0
    for col in range(np.size(v1)):
        res += v1.item(col) * v2.item(col)
    return res


M1 = np.random.rand(4, 6)
M2 = np.random.rand(4, 6)

print(M1)
print(M2)

# rows
numRows = np.size(M1, 0)

# cols
numCols = np.size(M1, 1)

r1 = np.zeros(numCols)
r2 = np.zeros(numCols)

for i in range(numCols):
    dot_prodcut = dot_product_for_loop(M1[:, i], M2[:, i])
    r1[i] = dot_prodcut
    print("Dot LOOP Method product for columns  {0} : {1}".format(i, dot_prodcut))

    dot_prodict_numpy = np.dot(M1[:, i], M2[:, i])
    r2[i] = dot_prodict_numpy
    print("Dot NUMPY Method product for columns {0} : {1}".format(i, dot_prodict_numpy))

print("DEtecting different values from method 1 and method 2 \n\n")
for i in range(numCols):
    if r1[i] != r2[i]:
        print("{0} is not equal to {1} the difference is {2}".format(r1[i], r2[i], r1[i]-r2[i]))