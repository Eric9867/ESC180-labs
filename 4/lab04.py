import math
## EXAMPLE FUNCTIONS

def sum_nums(L):
    s = 0
    for num in L:
        s += num
    return s


## PROBLEM 1: Writing count_evens(L)

def count_evens(L):
    num_even = 0

    for num in L:
        if num % 2 == 0:
            num_even += 1
    return num_even

## PROBLEM 2:

def list_to_str(lis):
    ''' DOC STRING '''

    string = "["
    for num in lis:
        string += str(num)
        string += ", " if num != lis[-1] else "]"

    return string

## PROBLEM 3:

def lists_are_the_same(list1, list2):
    # I feel like tge code style could be improved
    if len(list1) != len(list2):
        return False

    for index in range(len(list1)):
        if list1[index] != list2[index]:
            return False
    return True

## PROBLEM 4:

def simplify_fraction(n, m):

    min_num_checks = math.ceil(min(n,m))

    for div in range(min_num_checks, 0, -1):
        if n % div == 0 and m % div == 0:
            #print(str(n//div)+"/"+str(m//div))

            #print(simplified_fraction_check(n, m, n/div, m/div))

            return ((n/div), (m/div), div, min_num_checks)

def simplified_fraction_check(n,m,n_simpl, m_simpl):
    return n/m == n_simpl/m_simpl

## PROBLEM 5: Sum more Pi

""" find number of elements n (output) required for approximation with s_d sig digs (input) """

def required_num_terms(s_d):
    pi = int(math.pi*(10**(s_d-1)))
    quarter_approx_pi = 0
    i=0
    while(pi != int(4*quarter_approx_pi*(10**(s_d-1)))):
        #print(int(4*quarter_approx_pi*(10**(s_d-1))), pi)
        quarter_approx_pi += (-1)**i / (2 * i + 1)
        i+=1
    return i+1

## PROBLEM 6: Euclid's Algorithm

'''
DOC-STRING
if a/b has a remainder r, it runs itself with new inputs euclids_algorithm(b,r) and returns its results
when a/b has no remainder, returns b

Parameters:
    arg1 a (int): original numerator
    arg2 b (int): original denomenator

Returns:
    int: returns gdc(a,b) using euclids algorithm

'''
def euclids_algorithm(a,b, iter = 0):
    iter += 1
    if a%b == 0:
        return b, iter

    return euclids_algorithm(b, a%b, iter)

def frac_simplifier(a,b):
    factor, iter = euclids_algorithm(a,b)
    return a/factor, b/factor, factor, iter


if __name__ == "__main__":

    lst1 = [1,2,3,4,5,6,7,8,9,0]
    lst2 = [1,2,3,4,5,6,7,8,9,0,1]
    print(count_evens(lst1))
    print(list_to_str(lst1))
    print(lists_are_the_same(lst1,lst2))
    print(required_num_terms(4),"\n")
    a,b = 132409240389000044,2343424
    #print("Brute force:       ",simplify_fraction(a,b))
    print("Euclid's Algorithm:",frac_simplifier(a,b))






