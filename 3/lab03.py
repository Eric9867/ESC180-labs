
## Problem 2

def sum_cubes(n):
    '''
    For all n > 0, computes the sum of the cubes of all natural 
    numbers up to and including n.  
    '''
    # Ensure n is a value in the domain of this function
    if type(n) != int:
        raise(TypeError)
    if n < 1:
        raise(ValueError)

    # Calculate the sum step by step
    sum = 0
    for i in range(1, n + 1):
        sum += i**3
    return sum

def check_sum(n):
    '''

    '''
    # Ensure n is a value in the domain of this function
    if type(n) != int:
        raise(TypeError)
    if n < 1:
        raise(ValueError)

    # Boolean expression compares the step by step sum with the sum 
    # given by the formula and determines if they match
    return sum_cubes(n) == n**2 * (n + 1)**2 / 4


if __name__ == "__main__":
    print(sum_cubes(5))
    print(sum_cubes(7))