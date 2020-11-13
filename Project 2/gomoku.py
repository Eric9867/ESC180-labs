"""
Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 26, 2020
"""

def is_empty(board):
    return all([all([square == ' ' for square in row]) for row in board])
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    bounded_before = False
    bounded_after = False

    try:
        bounded_after = (board[y_end + d_y][x_end + d_x] != ' ')
    except IndexError:
        bounded_after = True
    try:
        bounded_before = (
            (board[y_end - (length) * d_y][x_end - (length) * d_x] != ' ') or 
            (y_end - (length) * d_y) < 0 or 
            (x_end - (length) * d_x) < 0
        )
    except IndexError:
        bounded_before = True

    if bounded_before and bounded_after:
        return 'CLOSED'
    elif bounded_before or bounded_after:
        return 'SEMIOPEN'
    else: # essentially: not bounded_before and not bounded_after
        return 'OPEN'
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x, check_win=False):
    board_width = len(board[0]) # 8
    board_height = len(board) # 8 
    # the current "row" or sequence being analyzed
    
    # THIS ASSUMES YOUR LOOKING AT THE LONGEST ROW THAT FITS IN THE TABLE GIVEN THE PARAMETERS
    seq = [board[y_start + i * d_y][x_start + i * d_x] for i in range(min(board_height - y_start * d_y, board_width - x_start * d_x if d_x >= 0 else x_start + 1))]

    # Instead, we specify the length.... why tho?
    # seq = [board[y_start + i * d_y][x_start + i * d_x] for i in range(length)]
    # print(seq, 'dy', d_y, 'dx', d_x, 'yst', y_start, 'xst', x_start)
    #start_points = []
    end_points = []
    lengths = []
    is_in_color_seq = False
    cur_length = 0

    for i in range(len(seq)):
        if seq[i] == col:
            cur_length += 1
            is_in_color_seq = True
        elif is_in_color_seq:
            if cur_length == length:
                end_points.append((y_start + (i - 1) * d_y, x_start + (i - 1) * d_x))
                lengths.append(cur_length)
            cur_length = 0
            is_in_color_seq = False
    if is_in_color_seq and cur_length == length:
        end_points.append((y_start + (i - 1) * d_y, x_start + (i - 1) * d_x))
        lengths.append(cur_length)

    seq_count = {
        'OPEN': 0,
        'CLOSED': 0,
        'SEMIOPEN': 0
    }
    for sub_seq in range(len(end_points)):
        seq_count[is_bounded(board, *end_points[sub_seq], lengths[sub_seq], d_y, d_x)] += 1

    return (max(val for val in seq_count.values()), 0) if check_win else (seq_count['OPEN'], seq_count['SEMIOPEN'])

def detect_rows(board, col, length, check_win = False):
    ####CHANGE ME
    dy_dx = [(0,1),(1,0),(1,1),(1,-1)]
    open_seq_count, semi_open_seq_count = 0, 0

    y = 0
    for x in range(len(board[0])):
        for inc in [(1,0), (1,1), (1,-1)]:
            counts = detect_row(board, col, y, x, length, inc[0], inc[1], check_win)
            open_seq_count += counts[0]
            semi_open_seq_count +=  counts[1] 
    x = 0
    # x = 0, y = 0
    counts = detect_row(board, col, y, x, length, 0, 1, check_win)
    open_seq_count += counts[0]
    semi_open_seq_count +=  counts[1]

    for y in range(1, len(board)):
        for inc in [(0,1), (1,1)]:
            counts = detect_row(board, col, y, x, length, inc[0], inc[1], check_win)
            open_seq_count += counts[0]
            semi_open_seq_count += counts[1]

    x = len(board[0]) - 1
    for y in range(1, len(board)):
        for inc in [(1,-1)]:
            counts = detect_row(board, col, y, x, length, inc[0], inc[1], check_win)
            open_seq_count += counts[0]
            semi_open_seq_count += counts[1]

    return open_seq_count, semi_open_seq_count
    
# def search_max(board):
#     max_score = 0
#     move_y, move_x = -1, -1
  
#     for y in range(len(board)):
#         for x in range(len(board[y])):
#             tmp_board = copy.deepcopy(board)
#             cur_score = score(tmp_board[y][x])
#             if cur_score > max_score: 
#                 move_y, move_x = y, x
#                 max_score = score

#     return move_y, move_x

def search_max(board):
    max_score = -100001
    cur_score = None
    move_y = None
    move_x = None
  
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == ' ':
                board[y][x] = 'b'
                cur_score = score(board)
                board[y][x] = ' '

                if cur_score > max_score: 
                    move_y, move_x = y, x
                    max_score = cur_score
    
    # assert move_y != None and move_x != None
    if move_y != None and move_x != None:
        return move_y, move_x
    else:
        return 0, 0

def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    # Check win
    # print(detect_rows(board, 'b', 5, True)[0])
    # print(detect_rows(board, 'w', 5, True)[0])
    # print(all(all(square != ' ' for square in row) for row in board))
    if detect_rows(board, 'b', 5, True)[0] > 0:
        return "Black won"
    if detect_rows(board, 'w', 5, True)[0] > 0:
        return "White won"
    # Check Tie
    if all(all(square != ' ' for square in row) for row in board):
        return "Draw"
    else:
        return "Continue playing"


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_row2():
    board = make_empty_board(8)
    x = 6; y = 5; d_x = -1; d_y = 1; length = 2
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", y-1,x+1,length,d_y,d_x) == (0,1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_detect_rows2():
    board = make_empty_board(8)
    x = 6; y = 3; d_x = -1; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE #2 for detect_rows PASSED")
    else:
        print("TEST CASE #2 for detect_rows FAILED")


def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def test_score():
    board = make_empty_board(8)
    x = 7; y = 0; d_x = 1; d_y = 0; length = 1; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    # x = 7; y = 0; d_x = 0; d_y = 1; length = 1; col = 'b'
    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    print(score(board))    

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    #play_gomoku(8)
    # board = [
    #     [' ', ' ', ' '],
    #     [' ', 'w', ' '],
    #     [' ', ' ', 'w']
    # ]
    # print((board, *(2,2), 2, 1, 1))
    # board = [
    #     ['w', ' ', ' '],
    #     ['w', 'w', ' '],
    #     [' ', ' ', 'w']
    # ]
    # print(detect_row(board, 'w', 0, 0, 3, 1, 1))

    # some_tests()
    # test_is_empty()
    # test_is_bounded()
    # test_detect_row2()

    
    # test_detect_rows()
    # test_detect_rows2()
    # easy_testset_for_main_functions()
    print('\n\n', play_gomoku(3), '!')
    #some_tests()
