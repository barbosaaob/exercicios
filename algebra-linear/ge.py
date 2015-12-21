import numpy as np


def ge(A, eps=1e-8):
    m, n = A.shape
    print "initial:\n", A
    for k in range(min(m, n) - 1):
        # print "row =", k+1, ", k =", k
        # print "before:\n", A
        if (np.abs(A[k, k]) < eps):
            # Find the k-th pivot
            idx = find_pivot(A, k, eps)
            if idx:
                swap_rows(A, k, idx)
                print "L_" + str(idx+1) + " <--> L_" + str(k+1)
                print "after:\n", A
            else:
                continue

        # Do for all rows below pivot:
        for i in range(k+1, m):
            c = - float(A[i, k]) / float(A[k, k])
            if (c != 0):
                s = "L_" + str(i+1) + " <-- L_" + str(i+1) + " + ("
                s += str(c) + ") * L_" + str(k+1)
                print s

            # Do for all remaining elements in current row
            for j in range(k+1, n):
                A[i, j] = A[i, j] + c * A[k, j]

            # Fill lower triangular matrix with zeros:
            A[i, k] = 0.0

        print "after:\n", A


def find_pivot(A, k, eps=1e-8):
    # m = A.shape[0]
    # idx = np.argmax(np.abs(A[k:m, k]))
    # if (np.abs(A[idx, k]) < eps):
    #     print "### Matrix is singular!"
    m = A.shape[0]
    idx = None
    for i in range(k, m):
        if (np.abs(A[i, k]) >= eps):
            idx = i
            break

    return idx


def swap_rows(A, i, j):
    if (i != j):
        aux = np.copy(A[i, :])
        A[i, :] = A[j, :]
        A[j, :] = aux


if (__name__ == "__main__"):
    M = np.array([[1., 2., 3., 4.],
                  [5., 6., 7., 8.],
                  [9., 10., 11., 12.],
                  [13., 14., 15., 17.],
                  [17., 18., 19., 20.]])
    # M = np.array([[0., 1., 2., 3.],
    #               [2., 1., 3., 0.],
    #               [3., 4., 2., 0.],
    #               [4., 2., 0., 1.]])
    # M = np.array([[1., 2., -3., 4.],
    #               [2., 3., 4., 5.],
    #               [4., 7., -2., 12.]])
    # M = np.array([[0., 2., 2.],
    #               [1., 1., 3.],
    #               [3., -4., 2.],
    #               [2., -3., 1.]])
    ge(M)
