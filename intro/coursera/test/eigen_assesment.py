import numpy as np


if __name__ == '__main__':
    # Eigenvalues
    M = np.array([[1, 0, 0],
                  [0, 2, 0],
                  [0, 0, 3]])
    vals, vecs = np.linalg.eig(M)
    print(vals)

    # Eigenvectors - Note, the eigenvectors are the columns of the output.
    M = np.array([[1, 0, 0],
                  [0, 2, 0],
                  [0, 0, 3]])
    vals, vecs = np.linalg.eig(M)
    print("Eigen Vectors: {0} ".format(vecs))

    matrix = np.array([[4, -5, 6],
                      [7, -8, 6],
                      [3/2, -1/2, -2]])

    vals, vecs = np.linalg.eig(matrix)
    print(vecs)

    matrix = np.array([[0, 0, 0, 1],
                       [1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0]])
    vals, vecs = np.linalg.eig(matrix)
    print("****************")
    print(vals)
    print(vecs)

    matrix = np.array([[0.1, 0.1, 0.1, 0.7],
                       [0.7, 0.1, 0.1, 0.1],
                       [0.1, 0.7, 0.1, 0.1],
                       [0.1, 0.1, 0.7, 0.1]])
    vals, vecs = np.linalg.eig(matrix)
    print("<><><><><><><><<<><<><><<><><><><><<<<><><><><<><<<><><<<><><<<><<")
    print(vals)
    print(vecs)
