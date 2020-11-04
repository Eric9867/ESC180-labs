import numpy as np
import copy


# Problem 1
def print_matrix(M):
    print(np.array(M))

# Problem 2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row) - 1

# Problem 3
def get_row_to_swap(M, start_row):
    min_index = len(M)
    selected_row = 0
    for row_i in range(start_row,len(M)):
        if get_lead_ind(M[row_i]) < min_index:
            min_index = get_lead_ind(M[row_i])
            selected_row = row_i
    return selected_row

# Problem 4
def add_rows_coefs(r1, c1, r2, c2):
    sum_list = []
    for i in range(len(r1)):
        sum_list.append(c1*r1[i] + c2*r2[i])
    return sum_list

# Problem 5
def eliminate(M, row_to_sub, best_lead_ind):
    lead_val = M[row_to_sub][best_lead_ind]
    
    M_elim = copy.deepcopy(M)

    for row in range(row_to_sub+1, len(M)):
        if lead_val:
            row_lead_val = M[row][best_lead_ind]
            factor = -row_lead_val/lead_val
            row_elim = add_rows_coefs(M[row], 1, M[row_to_sub], factor)
            M_elim[row] = row_elim
    
    return M_elim

# Problem 6
def forward_step(M):
    for row_i in range(len(M)):
        cur_swap = get_row_to_swap(M, row_i)
        M[row_i], M[cur_swap] = M[cur_swap], M[row_i]
    print('Rows swapped')
    print_matrix(M)
    print()
    for row_i in range(len(M)):
        if M[row_i][get_lead_ind(M[row_i])]:
            M = eliminate(M, row_i, get_lead_ind(M[row_i]))
            print('Eliminate: row ' + str(row_i))
            print_matrix(M)
            print()
        else:
            pass
        #if [0 for i in M[row_i]] in [M[row] for row in range(row_i,len(M))]:

    for row_i in range(len(M)):
        try:
            M[row_i] = add_rows_coefs(M[row_i], 1/M[row_i][get_lead_ind(M[row_i])], [0 for i in M[row_i]], 0)
        except ZeroDivisionError:
            M.append(M[row_i])
            M.pop(row_i)

    print('Rows divided by leading coefficient')
    print_matrix(M)
    print()
    return M

# Problem 7
def flip_rows(M):
    for row in range(len(M)//2):
        M[row], M[len(M)-1-row] = M[len(M)-1-row], M[row]
    return M
        
def backward_step(M):
    M = flip_rows(M)
    
    for row in range(len(M)):
        M = eliminate(M, row, get_lead_ind(M[row]))
    
    M = flip_rows(M)
    return M

# Problem 8
def solve_vec(M,b):
    '''
    Solve equation M x = b for x
    '''
    x = []
    for row_i in range(len(M)):
        M[row_i].append(b[row_i])
    M = backward_step(forward_step(M))
    for row in M:
        x.append(row[-1])
    print_matrix(M)
    if all([row[get_lead_ind(row[:-1])] for row in M]):
        print_matrix(x)
    elif all([row[get_lead_ind(row)] for row in M]):
        print('0 not equal to n: NO SOLUTIONS')
    else:
        print('Solutions may exist: Examine matrix')
    



if __name__ == "__main__":
    # M = [
    #     [5, 6, 7, 8],
    #     [0, 4, 0, 1],
    #     [1, 0, 5, 2],
    #     [4, 1, 0, 5]
    # ]
    M = [
        [1,2,3,4],
        [5,6,7,8],
        [3,3,3,3],
        [9,3,1,2],
        [1,5,3,2]
    ]
    solve_vec(M,[1,2,3,4,5])