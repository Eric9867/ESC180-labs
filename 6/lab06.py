'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random, copy


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# PROBLEM 1:

# Part (a):
def board_coord(square_num):
    return [(square_num -1)//3, (square_num-1) % 3]

# Part (b):
def put_in_board(board, mark, square_num):
    coord = board_coord(square_num)
    board[coord[0]][coord[1]] = mark
    return board

# Part (c):

def check_free_square(square_num, board):
    return board_coord(square_num) in get_free_squares(board)

def input_counter(board, comp = False):
    global counter
    square_num = -1
    if not counter % 2:
        current_mark = 'X'
    else:
        current_mark = 'O'
    while not check_free_square(square_num, board) and not comp:
        try:
            square_num = int(input("Please enter coordinate (between  1 and 9) for {}: ".format(current_mark)))
        except:
            continue
    counter+=1
    return current_mark, square_num


# PROBLEM 2:

# Part (a):
def get_free_squares(board):
    empty_slots = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                empty_slots.append([i,j])
    return empty_slots

# Part (b):
def make_random_move(board, mark):
    free_tiles = get_free_squares(board)
    rnd_tile = free_tiles[int(len(free_tiles)*random.random())]
    board[rnd_tile[0]][rnd_tile[1]] = mark
    return board

# Part (c):
def simple_comp_game(board):
    while len(get_free_squares(board)) != 0:
        mark_pos_player = input_counter(board)
        put_in_board(board, mark_pos_player[0], mark_pos_player[1])
        print_board_and_legend(board)
        player_win = is_win(board, mark_pos_player[0])

        if player_win:
            print("Player wins!")
            break

        if len(get_free_squares(board)) == 0:
            print("Tie game.")
            break

        input("Computer's move, press enter to continue...")
        mark_pos_comp = input_counter(board, True)
        #make_random_move(board,mark_pos[0])
        cpu_move(board, mark_pos_comp[0], mark_pos_player[0])
        print_board_and_legend(board)
        comp_win = is_win(board, mark_pos_comp[0])

        if comp_win:
            print("Computer wins!")
            break

#3a
def is_row_all_marks(board, row_i, mark):
    return all([tile == mark for tile in board[row_i]])

#3b
def is_col_all_marks(board, col_i, mark):
    return all([tile == mark for tile in [board[j][col_i] for j in range(3)]])

#3c
def are_diag_all_marks(board, mark):
    return (
        all(tile == mark for tile in [board[i][i] for i in range(3)]) or
        all(tile == mark for tile in [board[i][2-i] for i in range(3)])
    ) 
    
def is_win(board, mark):   
    for i in range(3):
        if(
            is_row_all_marks(board, i, mark) or 
            is_col_all_marks(board, i, mark)
          ):
            return True
    return are_diag_all_marks(board, mark)

#4a
def win_con(board,mark):
    options = get_free_squares(board)
    test_board = copy.deepcopy(board)
    for tile in options:
        test_board[tile[0]][tile[1]] = mark
        if is_win(test_board,mark):
            return tile
        else:
            test_board[tile[0]][tile[1]] = ' '
    return False

def cpu_move(board, mark_cpu, mark_player):
    win_tile = win_con(board, mark_cpu)
    if win_tile:
        board[win_tile[0]][win_tile[1]] = mark_cpu
    else:
        lose_tile = win_con(board, mark_player)
        if lose_tile:
            board[lose_tile[0]][lose_tile[1]] = mark_cpu
        else:
            make_random_move(board,mark_cpu)
    return None
    

if __name__ == '__main__':
    global counter
    counter = 0
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    # board = [["O", "X", "X"],
    #          [" ", "X", " "],
    #          [" ", "O", " "]]
    
    # print_board_and_legend(board)  
    # board = make_empty_board()
    simple_comp_game(board)          