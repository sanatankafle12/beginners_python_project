HUMAN = -1
COMP = +1
grid=['0','1','2','3','4','5','6','7','8']

def draw_board():
    print(grid[0], "|" , grid[1], "|" ,grid[2])
    print("__  __  __")
    print(grid[3], "|" , grid[4], "|" ,grid[5])
    print("__  __  __")
    print(grid[6], "|" , grid[7], "|" ,grid[8])


def evaluate(board):
    if wins(board, COMP):
        score = +1
    elif wins(board, HUMAN):
        score = -1
    else:
        score = 0

    return score


def check_win(board,player):
    if grid[0]==grid[1]==grid[2] ==player or grid[3]==grid[4]==[5] ==player or grid[6]==grid[7]==grid[8]==player or grid[0]==grid[4]==grid[8]==player or grid[2]==grid[4]==grid[6] ==player or grid[0]==grid[3]==grid[6] ==player or grid[1]==grid[4]==grid[7] ==player or grid[2]==grid[5]==grid[8]==player :
        return True
    return False

def game_over(board):
    return check_win(grid, HUMAN) or wins(grid, COMP)

def check_valid(number):

    if number not in [0,1,2,3,4,5,6,7,8]:
        return False

    if grid[number] == "X" or grid[number] == "Y":
        return False
    else:
        return True




