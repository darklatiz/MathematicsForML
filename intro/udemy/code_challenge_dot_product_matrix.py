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

for i in range(numCols):
    dot_prodcut = dot_product_for_loop(M1[:, i], M2[:, i])
    print("Dot LOOP Method product for columns  {0} : {1}".format(i, dot_prodcut))

    dot_prodict_numpy = np.dot(M1[:, i], M2[:, i])
    print("Dot NUMPY Method product for columns {0} : {1}".format(i, dot_prodict_numpy))

