from chatterbot.trainers import ListTrainer #way to train the chatbot
from chatterbot import ChatBot # import the chatbot
from chatterbot import logic

import time

#lists innit
#first run
quit_list = ["quit","close","close program","quit now"]
no_list = ["no","No","n","N","No thx", "no thx", "Ummm no", "ummm no"]
yes_list = ["Yes","yes","Y","y","Yez","yez","Yeah","yeah"]
bye_list = ["bye","Bye","bai","Bai","Byee","byee","cya","Cya","see ya", "See ya","see Ya","See you later", "see you later"]
#age
def ageask():
    age = int(input("How old are you? Please answer in digits."))
    if age == str:
        print("Please answer in digits...")
        ageask()
    if age == no_list:
        print("It is needed for future development.")
        ageask()

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
    if response.confidence > 0.80:    #remove if dont work
        print('Bearbot: ' + response)
    elif response.confidence < 0.80:    #remove if dont work
        print("Bearbot: Sorry, i don't quite understand.")

    elif request in quit_list:
        quit()
