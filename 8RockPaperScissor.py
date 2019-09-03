import random
moves = ["rock", "paper", "scissor"]
keep_playing = True
while keep_playing:
    cmove = random.choice(moves)
    pmove = input("You are about to start Rock, Paper and Scissor game. Please enter your input: ")
    if cmove == pmove:
        print('Tie')
    elif pmove == 'rock' and cmove == 'scissor':
        print("Player wins!!")
    elif pmove == 'scissor' and cmove == 'paper':
        print("Player wins!!")
    elif pmove == 'paper' and cmove == 'rock':
        print("Player wins!!")
    elif cmove == 'rock' and pmove == 'scissor':
        print("Computer wins!!")
    elif cmove == 'scissor' and pmove == 'paper':
        print("Computer wins!!")
    elif cmove == 'paper' and pmove == 'rock':
        print("Computer wins!!")
    else:
        print("Please enter a valid input next time!!")
    print(cmove, 'and ', pmove)
    option = print(input("Do you want to continue the game. If no, please enter N: "))
    if option == 'N':
        keep_playing = False
        print('GoodBye!!')
        break
    else:
        print("Enter a valid input")
