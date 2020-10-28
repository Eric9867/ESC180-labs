
## Problem 1
def list1_start_with_list2(list1, list2):
    '''
    Checks if the elements of list2 are the first elements of list1 in the same order.
    '''
    if not len(list1) > len(list2):
        return False
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            return False
    return True

## Problem 2
def match_pattern(list1, list2):
    '''
    Checks if the elements of list2 appear anywhere in list1, in the same order
    ''' 
    if not len(list1) > len(list2):
        return False
    for i in range(len(list1) - len(list2)):
        if list1[i : i + len(list2)] == list2:
            return True
    return False

## Problem 3
def repeats(list0):
    '''
    Checks if any adjacent values in list0 are equal
    '''
    for i in range(len(list0) - 1):
        if list0[i] == list0[i+1]:
            return True
    return False

## Problem 4 :: Matrices

# Matrix in format:
# M = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
def print_matrix_dim(M):
    '''
    returns (number of rows)x(number of columns)
    '''
    row_length = len(M[1])
    for row in M:
        if len(row) != row_length:
            raise TypeError
    return str(len(M)) + "x" + str(len(M[1]))

def dot_product(v, u):
    '''
    Returns the dot product of vector v with vector u
    '''
    try:
        product = 0
        for i in range(len(v)):
            product += v[i]*u[i]
    except: # IndexError
        return False
    else:
        return product

def matrix_multiply(A, B):
    # Verify that 
    for row in A:
        if len(row) != len(A[0]):
            raise TypeError
    for row in B:
        if len(row) != len(B[0]):
            raise TypeError

    # Transpose B for more convenient value access
    temp_matrix_B = B
    B = [[0] * len(B)] * len(B[0])
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = temp_matrix_B[j][i]

    if len(A[0]) != len(B[0]):
        raise ValueError    # Could also be an index error

    # Given matrix (m x n)
    # and matrix (n x p)
    # Resulting matrix is (m x p)

    C = [[None] for i in range(len(B)) for j in range(len(A))]

    # C = [[[0][:] * len(B])]*len(A)
    #C = []
    #for i in range(len(A)): 

    #    C.append([0] * len(B))
    for i in C:
        for j in i:
            j = None

    for row_of_A in range(len(A)):
        for column_of_B in range(len(B)):
            # Entry i,j of resultant matrix C
            C[row_of_A][column_of_B] = dot_product(A[row_of_A], B[column_of_B])
    
    # (optional) If it is a single column matrix, converts it to a simple list
    for i in range(len(C)):
        if len(C[i]) == 1:
            C[i] = C[i][0]
    return C

### Matrix Multiplication ###
import numpy as np


def mult_M1_M2(M1, M2):
    ''' Return the matrix multiplication of an (m x n) & an (n x p) matrix '''
    cur_ind = 0
    if len(M1[0]) != len(M2):
        raise IndexError("M1 column size != M2 row size [not (m x n) & (n x p) matrices]")

    res_matrix = [[] for j in range(len(M1))]
    for m in range(len(M1)):
        for p in range(len(M2[0])):
            cur_ind = 0
            for n in range(len(M2)):
                cur_ind += M1[m][n]*M2[n][p]
            res_matrix[m].insert(p, cur_ind)
    return res_matrix


if __name__ == "__main__":
    print("1. List 1 starts with list 2: ", list1_start_with_list2([1,2,3,4,5,6],[1,2,3,4,5,6,7]))
    print("2. List 2 in list 1: ", match_pattern([1,2,3,4,5,6,7,8,9,10,11],[5,6,7]))
    print("3. List0 repeats: ", repeats([0,1,2,3,4,5,6,7]))
    print("4. a) Matrix dimensions: ", print_matrix_dim([[1,2,3],[4,5,6],[7,8,9]]))
    
    print("4. b) matrix u by vector v")
    v = [[1], 
        [2], 
        [3]]
    u = [[1,2,5],
        [6,4,1],
        [1,4,2]]
    for i in u:
        print(i)
    print()
    print(v)
    print(matrix_multiply(u, v))
    print("4. c)")

    z = [[8 , 9 , 1],
        [4 , 7 , 2],
        [8 , 1 , 3]]

    print(matrix_multiply(u, z))
    matrix1 =  [[2 ,1 ,0 ,7 ,4 ,1 ,5 ,0 ,6 ,9],
                [4 ,8 ,6 ,7 ,0 ,5 ,7 ,8 ,3 ,7],
                [2 ,7 ,9 ,6 ,5 ,0 ,1 ,6 ,8 ,2],
                [2 ,2 ,1 ,0 ,3 ,5 ,0 ,0 ,6 ,0],
                [2 ,4 ,2 ,8 ,7 ,1 ,2 ,8 ,5 ,8],
                [4 ,2 ,3 ,8 ,5 ,1 ,7 ,0 ,8 ,3]]

    matrix2 =  [[6 ,6 ,2 ,3],
                [3 ,9 ,1 ,8],
                [0 ,8 ,9 ,4],
                [4 ,2 ,1 ,4],
                [1 ,5 ,5 ,9],
                [7 ,9 ,8 ,9],
                [3 ,5 ,7 ,8],
                [4 ,3 ,5 ,4],
                [2 ,8 ,2 ,7],
                [9 ,1 ,8 ,8]]
    # np.matrix(matrix1)
    # np.matrix(matrix2)

    print("M1:\n", np.matrix(matrix1), "\n", sep = "")
    print("M2:\n", np.matrix(matrix2), "\n", sep = "")

    results = mult_M1_M2(matrix1, matrix2)
    results = np.matrix(mult_M1_M2(matrix1, matrix2))
    print("Results:\n", results, sep ="")
    results = np.matrix(mult_M1_M2(u,v))
    print("Results:\n", results, sep ="")    
    results = np.matrix(mult_M1_M2(matrix1,matrix2))
    print("Results:\n", results, sep ="")    


