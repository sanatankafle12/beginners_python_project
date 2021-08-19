import random
#declaring the board
board = [
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        ['-','-','-','-','-','-','-']
        ]
        
#showing board with proper formating
def display():
    print("   0 1 2 3 4 5 6 ")
    print("0 |"+board[0][0]+"|"+board[0][1]+"|"+board[0][2]+"|"+board[0][3]+"|"+board[0][4]+"|"+board[0][5]+"|"+board[0][6]+"|")
    print("1 |"+board[1][0]+"|"+board[1][1]+"|"+board[1][2]+"|"+board[1][3]+"|"+board[1][4]+"|"+board[1][5]+"|"+board[1][6]+"|")
    print("2 |"+board[2][0]+"|"+board[2][1]+"|"+board[2][2]+"|"+board[2][3]+"|"+board[2][4]+"|"+board[2][5]+"|"+board[2][6]+"|")
    print("3 |"+board[3][0]+"|"+board[3][1]+"|"+board[3][2]+"|"+board[3][3]+"|"+board[3][4]+"|"+board[3][5]+"|"+board[3][6]+"|")
    print("4 |"+board[4][0]+"|"+board[4][1]+"|"+board[4][2]+"|"+board[4][3]+"|"+board[4][4]+"|"+board[4][5]+"|"+board[4][6]+"|")
    print("5 |"+board[5][0]+"|"+board[5][1]+"|"+board[5][2]+"|"+board[5][3]+"|"+board[5][4]+"|"+board[5][5]+"|"+board[5][6]+"|")

'''
Check for the win:
-> the first loop checks horizontal win
-> the second loop checks vertical win
-> the third loop checks download diagonal
-> the forth loop checks upward diagonal
'''
def check_draw():
    for i in range(6):
        for j in range(7):
            if(board[i][j] == 'X' and board[i][j]=='O'):
                return False
    return True


def check_win():
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

#for computer's move
def computer_move():
    while(True):
        choice1 = random.choice([0,1,2,3,4,5])
        choice2 = random.choice([0,1,2,3,4,5,6])
        if(valid(choice1,choice2,'O')):
            return(choice1,choice2)

#this checks for valid position and sets X or O if position is valid
def valid(x,y,player):
    if board[x][y] == '-':
        return True
    else:
        return False

if __name__ == "__main__":
    checkwin = False
    display()
    n=1
    vs = input("Press 1 to play one on one and press2 to play with computer. ")
    draw = False
    while(checkwin==False or draw==False):
        if(int(vs)==1):
            if(n%2==0):
                player = 'X'
            else:
                player = 'O'
            x,y = input(f"{player}'s turn. Use column and row simultaniusly to place {player}: ").split()
            x = int(x)
            y = int(y)
            if valid(x,y,player) == True:
                board[x][y] = player
                if(x!=0):
                    board[x-1][y] = '-'
                checkwin = check_win()
                draw =check_draw() 
                n+=1      
            else:  
                print("Invalid Input.. Please input valid coordinate.")
            display()

        elif(int(vs)==2):
            if(n%2==0):
                player = 'X'
                x,y = input(f"{player}'s turn. Use column and row simultaniusly to place {player}: ").split()
                x = int(x)
                y = int(y)
            else:
                player = 'O'
                (x,y) = computer_move()
            if valid(x,y,player) == True:
                board[x][y] = player
                if(x!=0):
                    board[x-1][y] = '-'
                checkwin = check_win() 
                draw = check_draw()
                n+=1      
            else:  
                print("Invalid Input.. Please input valid coordinate.")
            display()
        else:
            print("Invalid Option.")
            vs = input("Press 1 to play one on one and press2 to play with computer. ")
            
