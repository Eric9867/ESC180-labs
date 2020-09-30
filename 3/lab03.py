
## Problem 2

def sum_cubes(n):
    '''
    For all integers n > 0, computes the sum of the cubes  
    of all natural numbers up to and including n.  
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
    Compares the iterated sum from sum_cubes() to the
    value returned by the numerical formula. 
    '''
    # Ensure n is a value in the domain of this function
    if type(n) != int:
        raise(TypeError)
    if n < 1:
        raise(ValueError)

    # Boolean expression compares the step by step sum with the sum 
    # given by the formula and determines if they match
    return sum_cubes(n) == n**2 * (n + 1)**2 / 4     
    
    # NOTE: Using integer division ( // ) allows this function to 
    # continue working for much larger numbers (as great as 1 000 000)
    # return sum_cubes(n) == n**2 * (n + 1)**2 // 4     

def check_sums_up_to_n(N):
    ''' 
    The numerical formula for the sum is compared to the 
    iteratively computed sum for all values of n (where n 
    is the number of terms) from 1 to N 
    '''
    # This loop runs in reverse because the computation is very 
    # resource-intensive and False checks generally only appear 
    # for some of the upper values in a given range.

    # EXAMPLE 
        # if we were to compute check_sums_up_to_n(40000) using 
        # increasing iterations, assuming the first check fails 
        # after 13 000 to 14 000 sums were computed, somewhere on 
        # the order of 84 506 500 additionnal computations would 
        # be required to achieve the same result.
    for i in range(N, 1, -1):
        if not check_sum(i):
            return False
    # True is returned if the comparison was successfully 
    # passed for all values of n from 1 to N
    return True

def compute_pi(n):
    '''
    Computes pi using the Leibniz approximation with n terms
    '''
    if type(n) != int:
        raise(TypeError)
    if n < 0:
        raise(ValueError)

    approx_pi = 0
    for i in range(0, n):
        approx_pi += (-1)**i / (2 * i + 1)
    return 4*approx_pi

if __name__ == "__main__":
    print(sum_cubes(7))
    print(check_sum(12))
    print(check_sum(50))
    print(check_sum(15002))
    # print(check_sum(44000))
    # print(check_sum(44001))
    # CAUTION 
        # print(check_sum(1000000)) -------test passes if using integer division
        # print(check_sums_up_to_n(13000))
    print(compute_pi(1000))

    try: 
        compute_pi(err/ 3)

    except Exception as e:
        print(e)
    