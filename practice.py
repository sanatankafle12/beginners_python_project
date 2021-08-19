boards = [
        ['X','X','X','X','X','X','X'],
        ['X','X','X','O','X','X','X'],
        ['X','X','X','X','X','X','X'],
        ['X','O','X','X','X','X','X'],
        ['X','X','X','O','X','X','O'],
        ['X','X','X','X','X','X','X'],
]
def check_draw():
    for i in range(6):
        for j in range(7):
            if(boards[i][j] != 'X' and boards[i][j] != 'O'):
                return False
    return True


print(check_draw())