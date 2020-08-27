from random import randint
#rock paper or scissors optios
t = ["rock", "paper", "scissors"]
#bearbot random
bearbot = t[randint(0,2)]

#set player to False
player = False

print("Again, please answer in lowercase")
while player == False:
#set player to True
    player = input("paper, scissors, or rock?")
    if player == bearbot:
        print("It's a tie!")
    elif player == "rock":
        if bearbot == "paper":
            print("You lose!", bearbot, "covers", player)
        else:
            print("You win!", player, "smashes", bearbot)
    elif player == "paper":
        if bearbot == "scissors":
            print("You lose!", bearbot, "cut", player)
        else:
            print("You win!", player, "covers", bearbot)
    elif player == "scissors":
        if bearbot == "rock":
            print("You lose...", bearbot, "smashes", player)
        else:
            print("You win!", player, "cut", bearbot)
    else:
        print("That is an incorrect answer, please input either rock, paper or scissors!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    bearbot = t[randint(0,2)]


