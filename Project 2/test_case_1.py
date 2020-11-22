from gomoku import *

def test_detect_rows3():
    board = [[" "," "," ","b"," "," ","w","w"],
             [" "," ","b"," "," "," ","w","w"],
             ["w","b","b"," "," ","b","b","b"],
             ["w","w"," "," "," "," "," ","b"],
             ["b","b","b","b","b","b"," ","b"],
             ["w","b"," "," "," "," ","w","b"],
             ["b"," "," "," "," "," ","w","b"],
             ["b"," "," "," "," "," ","w"," "]]

    print_board(board)
    for col in ['b','w']:
        for length in range(2, 5):
            detect_rows(board, col,length)

if __name__ == "__main__":
    test_detect_rows3()