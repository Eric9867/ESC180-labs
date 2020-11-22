
# PROBLEM 1
def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n-1)

# PROBLEM 2
def interleave(L1, L2):
    if len(L2) == 0:
        return L1
    L1.append(L1[0])
    L1.append(L2[0])
    return interleave(L1[1:],L2[1:])    
    

# PROBLEM 3
def reverse_rec(L):

    L[0], L[-1] = L[-1], L[0]
    
    if len(L) > 2:
        L[1:-1] = reverse_rec(L[1:-1])

    return L

# PROBLEM 4    
def zigzag(L):
    if len(L) == 0:
        return
    elif len(L) == 1:
        print(L[0], end = " ")
        return
    zigzag(L[1:-1])
    print(L[-1], L[0], end=" ")        

def zigzag1(L):
    if len(L) == 0:
        print("")
    elif len(L) == 1:
        print(L[0], end = " ")
    else:
        print(L[0], L[-1], end = " ")
        zigzag1(L[1:-1])

    #print('\n',len(L))

# PROBLEM 5
def simple_is_balanced(a):

    pass

if __name__ == "__main__":
    print(power(9, 10))
    L1 = [1,2,3,4,5,6]
    L2 = [9,8,7,6,5,4]
    L1 = interleave(L1,L2)
    print(L1)
    print(reverse_rec(L1))

    zigzag(L1)
    print("")
    zigzag1(L1)
