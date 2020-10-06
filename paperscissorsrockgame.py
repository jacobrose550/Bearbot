from random import randint
back_list=["back","go back","selection"]
def game():
    #rock paper or scissors optios
    t = ["rock", "paper", "scissors"]
    #bearbot random
    bearbot = t[randint(0,2)]

    #set player to False
    player = False

    print("Again, please answer in lowercase")
    while player == False:
    #set player to True
        player = input("paper, scissors, or rock? Or do you want to go back to the selection")
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
        elif player in back_list:
            import maincentre
        else:
            print("That is an incorrect answer, please input either rock, paper or scissors!")
        player = False
        bearbot = t[randint(0,2)]

game()

