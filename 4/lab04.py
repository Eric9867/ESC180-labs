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
            print(str(n//div)+"/"+str(m//div))

            print(simplified_fraction_check(n, m, n/div, m/div))

            return ((n/div), (m/div), div)

def simplified_fraction_check(n,m,n_simpl, m_simpl):
    return n/m == n_simpl/m_simpl

## PROBLEM 5:



if __name__ == "__main__":

    lst1 = [1,2,3,4,5,6,7,8,9,0]
    lst2 = [1,2,3,4,5,6,7,8,9,0,1]
    print(count_evens(lst))
    print(list_to_str(lst))
    print(lists_are_the_same(lst1,lst2))
    print(simplify_fraction(16,24))