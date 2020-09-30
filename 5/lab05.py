
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

if __name__ == "__main__":
    print("1. List 1 starts with list 2: ", list1_start_with_list2([1,2,3,4,5,6],[1,2,3,4,5,6,7]))
    print("2. List 2 in list 1: ", match_pattern([1,2,3,4,5,6,7,8,9,10,11],[5,6,7]))
    print("3. List0 repeats: ", repeats([0,1,2,3,4,5,6,7]))
    print("4. a) Matrix dimensions: ", print_matrix_dim([[1,2,3],[4,5,6],[7,8,9]]))
    print("4. b)")
    print("4. c)")