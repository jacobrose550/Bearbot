#imports
import berabot
import gamestory
import paperscissorsrockgame
game_list = ["game","I want to play a game","i want play game","i want game play"]
paperscissorsrock = ["paper scissors rock"]
horror_story = ["horror story","game story"]
bearbot_list = ["bearbot", "Bearbot"]
chatterbot_list = ["chatterbot","Chatterbot"]

choice = input("Would you like to talk to Bearbot or play a Game?")
if choice in bearbot_list:
    berabot
elif choice in game_list:
    whatgame = input("What game would you like to play? Paper, scissors, rock, or a horror story game?")
    if whatgame in horror_story:
        gamestory
    elif whatgame in paperscissorsrock:
        paperscissorsrockgame
    else:
        print("Please enter a valid response")






