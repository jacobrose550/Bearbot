#Imports
from chatterbot.trainers import ListTrainer #way to train the chatbot
from chatterbot import ChatBot # import the chatbot
from chatterbot.logic import LogicAdapter
from chatterbot import filters
import time
import random
import gamestory
import paperscissorsrockgame
game_list = ["game","I want to play a game","i want play game","i want game play"]
paperscissorsrock = ["paper scissors rock"]
horror_story = ["horror story","game story"]
def bearbot():
    #lists innit
    #first run
    no_list = ["no","No","n","N","No thx", "no thx", "Ummm no", "ummm no"]
    yes_list = ["Yes","yes","Y","y","Yez","yez","Yeah","yeah"]
    bye_list = ["bye","Bye","bai","Bai","Byee","byee","cya","Cya","see ya", "See ya","see Ya","See you later", "see you later"]
    game_list = ["I want to play a game","I want game","I want play game", "I game want to play","Paper scissors rock"]
    #age
    def ageask():
        age = int(input("How old are you? Please answer in digits."))
        if age == str:
            print("Please answer in digits...")
        if age == no_list:
            print("It is needed for future development.")

    #name and age
    name = input("What is your name?").capitalize()
    time.sleep(1)

    print("Hey "+ name + "!")
    time.sleep(1)
    ageask()

    #letting user know to talk in lowercase
    print("Please use lowercases while talking. This helps Bearbot understand what you are talking about.")

    chatbot = ChatBot('Bearbot') # create the chatbot

    trainer = ListTrainer(chatbot)

    conv = open('get_to_know','r').readlines()

    conv = open('sad','r').readlines()

    conv = open('hi','r').readlines()

    conv = open('swearing and rude','r').readlines()

    trainer = ListTrainer(chatbot) # set the trainer

    trainer.train(conv)

    while True:
        request = input('You: ')
        response = chatbot.get_response(request)
##remove confidence if dfont work
        if chatbot.confidence > 0.80:    #remove if dont work
            print('Bearbot: ' + response)
        if chatbot.confidence < 0.80:    #remove if dont work
            print("Bearbot: Sorry, i don't quite understand.")

        print('Bot: ', response)

def chatterbot():
    import chatterbot
    from chatterbot.trainers import ChatterBotCorpusTrainer
    from chatterbot.trainers import ChatterBotCorpusTrainer
    from chatterbot import ChatBot # import the chatbot
    from chatterbot.logic import LogicAdapter
    from chatterbot import filters
    import time
    import random
    '''
    This is an example showing how to create an export file from
    an existing chat bot that can then be used to train other bots.
    '''

    chatbot = ChatBot('Chatterbot')

    # First, lets train our bot with some data
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

    # Now we can export the data to a file
    trainer.export_for_training('./my_export.json')

    while True:
        request = input('You: ')
        response = chatbot.get_response(request)

        if chatbot.confidence > 0.80:    #remove if dont work
            print('Chatterbot: ' + response)
        if chatbot.confidence < 0.80:    #remove if dont work
            print("Chatterbot: Sorry, i don't quite understand.")


bearbot_list = ["bearbot", "Bearbot"]

chatterbot_list = ["chatterbot","Chatterbot"]


####FIX THIS LATER
choice = input("Would you like to talk to Bearbot, Chatterbot or play a Game? Bearbot is designed to have semi-realistic conversations while chatterbot has alot more responses but is unrealistic.")
if choice in bearbot_list:
    bearbot()
elif choice in chatterbot_list:
    chatterbot()
elif choice in game_list:
    whatgame = input("What game would you like to play? Paper, scissors, rock, or a horror story game?")
    whatgame.split(" ")
    if whatgame in horror_story:
        gamestory
    elif whatgame in paperscissorsrock:
        paperscissorsrockgame
    else:
        print("Please enter a valid response")






