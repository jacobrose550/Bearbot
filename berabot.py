#Imports
from chatterbot.trainers import ListTrainer #way to train the chatbot
from chatterbot import ChatBot # import the chatbot
from chatterbot import logic
import time
import random
import sys, os

#lists innit
#first run
no_list = ["no","No","n","N","No thx", "no thx", "Ummm no", "ummm no"]
yes_list = ["Yes","yes","Y","y","Yez","yez","Yeah","yeah"]
quit_list = ["quit","close"]
#age

#name and age
name = input("What is your name?").capitalize()
print("Hey "+ name + "!")
time.sleep(1)

#letting user know to talk in lowercase
print("Please use lowercases while talking. This helps Bearbot understand what you are talking about.")
time.sleep(2)
print("Some responses may be odd, or Bearbot may not understand as many responses haven't been made.")
time.sleep(3)

chatbot = ChatBot('Bearbot') # create the chatbot

trainer = ListTrainer(chatbot)

conv = open('allzetext','r').readlines()


trainer = ListTrainer(chatbot) # set the trainer

trainer.train(conv)

while True:
    request = input('You: ')
    response = chatbot.get_response(request)
    if response.confidence > 0.80:
        print('Bot: ', response)
    elif response.confidence < 0.80:
        print("Bot: I dont quite understand...")
## prints response and then the print (not sure why that happens)
    elif request in quit_list:
        print("Bot: Aww okay, byee")
        quit()