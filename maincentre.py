#import
game_list = ["game","I want to play a game","i want play game","i want game play","play a game","i want to play a game","i wanna play a game"]
paperscissorsrock = ["paper scissors rock","psr"]
horror_story = ["horror story","game story","horror game","horror","horror story game"]
bearbot_list = ["bearbot", "Bearbot"]
chatterbot_list = ["chatterbot","Chatterbot"]
quit_list = ["quit","quit code","quit all code","end code"]
back_list = ["back","go back"]


def gameoptions():
    whatgame = input("What game would you like to play? Paper, scissors, rock, or a horror story game?")
    if whatgame in horror_story:
        import gamestory
    elif whatgame in paperscissorsrock:
        import paperscissorsrockgame
    elif whatgame in quit_list:
        quit()
    elif whatgame in back_list:
        choices()
    else:
        print("Please enter a valid response")
        gameoptions()
print("Would you like to talk to Bearbot or play a Game? Please answer in lowercases.")
def choices():
    choice = input()
    if choice in bearbot_list:
        import berabot
    elif choice in game_list:
        gameoptions()
    elif choice in quit_list:
        quit()
    else:
        print("Please enter a valid response")
        choices()

choices()








