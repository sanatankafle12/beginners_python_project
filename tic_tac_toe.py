
grid=['0','1','2','3','4','5','6','7','8']


def draw_board():
    print(grid[0], "|" , grid[1], "|" ,grid[2])
    print("__  __  __")
    print(grid[3], "|" , grid[4], "|" ,grid[5])
    print("__  __  __")
    print(grid[6], "|" , grid[7], "|" ,grid[8])


def check_win():
    if grid[0]==grid[1]==grid[2] =="X" or grid[3]==grid[4]==[5] =="X" or grid[6]==grid[7]==grid[8]=="X" or grid[0]==grid[4]==grid[8]=="X" or grid[2]==grid[4]==grid[6] =="X" or grid[0]==grid[3]==grid[6] =="X" or grid[1]==grid[4]==grid[7] =="X" or grid[2]==grid[5]==grid[8]=="X" :
        return 0
    if grid[0]==grid[1]==grid[2] =="O" or grid[3]==grid[4]==[5] =="O" or grid[6]==grid[7]==grid[8]=="O" or grid[0]==grid[4]==grid[8]=="O" or grid[2]==grid[4]==grid[6] =="O" or grid[0]==grid[3]==grid[6] =="O" or grid[1]==grid[4]==grid[7] =="O" or grid[2]==grid[5]==grid[8]=="O" :    
        return 1


def check_valid(number):

    if number not in [0,1,2,3,4,5,6,7,8]:
        return 0

    if grid[number] == "X" or grid[number] == "Y":
        return 0
    else:
        return 1


def main():
    print("Play with X as player 1 and O with player 2. \n")
    n=1
    draw_board()
    while n<10:
        if n%2!=0:
            input_1 = int(input("Player1 turn.\nEnter Number you want to put X in: "))
            if check_valid(input_1) == 1:
                grid[input_1] = 'X'
            else:
                print("Invalid Space.. use other space")
                draw_board()
                continue
        else:
            input_2 = int(input("Player2 turn.\nEnter Number you want to put O in: "))
            if check_valid(input_2) == 1:
                grid[input_2] = "O"
            
            else:
                print("Invalid Space.. use other space")
                draw_board()
                continue
        n+=1

        if check_win()==0:
            print("Congrats player 1 won!!!")
            draw_board()
            break
        if check_win()==1:
            print("Congrats player 2 won!!")
            draw_board()
            break
        draw_board()


main()