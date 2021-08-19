
def check_win(board):
    for i in range(6):
        for j in range(4):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]and board[i][j] in ['X','O']:
                print(f"{board[i][j]} wins.")
                return True
    for j in range(7):
        for i in range(3):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]and board[i][j] in ['X','O']:
                print(f"{board[i][j]} wins.")
                return True
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]and board[i][j] in ['X','O']:
                print(f"{board[i][j]} wins.")
                return True
    for i in range(3,6):
        for j in range(4):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]and board[i][j] in ['X','O']:
                print(f"{board[i][j]} wins.")
                return True
    return False

board1 = [
        [' ',' ',' ',' ',' ','O','O'],
        [' ',' ',' ',' ',' ','O',' '],
        [' ',' ',' ','O','O',' ',' '],
        [' ',' ','O','O',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        ['O','-','-','-','-','-','-']
        ]

board2 = [
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ','O'],
        [' ',' ',' ',' ',' ',' ','O'],
        [' ',' ',' ',' ',' ',' ','O'],
        [' ',' ',' ',' ',' ',' ','O'],
        [' ',' ',' ',' ','-','-','-']
        ]
board3 = [
        [' ',' ',' ',' ',' ',' ',' '],
        ['X',' ',' ',' ',' ',' ',' '],
        [' ','X',' ',' ',' ',' ',' '],
        [' ',' ','X',' ',' ',' ',' '],
        [' ',' ',' ','X',' ',' ',' '],
        ['-','-','-','-',' ','-','-']
        ]

board4 = [
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        ['X',' ','X','X','X','X',' '],
        ['X',' ',' ',' ',' ',' ',' '],
        [' ','X',' ',' ',' ',' ',' '],
        ['X','-','-','-','-','-','-']
        ]

assert(check_win(board1))
assert(check_win(board2))
assert(check_win(board3))
assert(check_win(board4))
