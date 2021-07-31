import random

while True:
    user_input = input("Enter your choice (s for Scissors, r for Rock and p for papers)")
    user_input.lower()

    lists = ["s","r","p"]
    computer_choice = random.choice(lists)
    if computer_choice == user_input:
        print("You chose the same option as computer. Please try again.")
    elif user_input == "s":
        if computer_choice == "r":
            print("Computer Wins as he chose rock and it broke your scissor.")
        else:
            print("You Win as you chose scissor and it cuts paper.")
    elif user_input == "r":
        if computer_choice == "s":
            print("You Win as computer chose scissors which broke due to your rock.")
        else:
            print("Computer Wins as his paper stopped your rock.")
    elif user_input == "p":
        if computer_choice == "s":
            print("computer Wins as he chose scissors which cut your paper")
        else:
            print("You Win as your paper stopped computer's rock")
    else:
        print("Please Enter valid input..")
        continue
    choice = input("type 'n' to quit and anything else to play again. \n" )
    if choice == 'n':
        print("Thanks for playing")
        break
