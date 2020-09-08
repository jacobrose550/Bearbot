import time
import random
from random import randint
from random import randrange
###IMPORTANT !ij@io#uo!@i#y
##50 percent chance
fifty_chance = randint(0,1)
##33 percent chance
thirty_chance = randint(0,2)
items_in_class = ["Computer","Ladder","Printer"]
yes_list = ["yes","Yes","Ye","ye","y","Y"]
no_list = ["no","No","N","n"]
teachers = ["Mr. Walker","Mr Wilson","Mr Simpson","Mr Macown"]
weapons_list = ["Bat","Knife","Hammer","Boulder","Rock","Jesus"]
animals = ["Pig","Rat","Sheep","Snake","Chicken",]
run_list = ["Run","run"]
walk_list = ["walk","Walk"]
rocktrip_finddoor = ["go back","Go Back","go Back","Go Back","GO BACK","find door","Find Door","find Door","Find Door","FIND DOOR","door","Door","find a door"]
rocktrip_keeprunning = ["keep running","Keep running","keep Running","Keep Running","KEEP RUNNING"]
hit_door_open = ["hit","Door","Hit","door","hit door open","hit the door open",]
subjects = ["art","english","digital science"]
foward_list = ["foward","step foward"]
go_back_list = ["go back","back"]
print("This is inspired by Eva")
time.sleep(1)
########################################################################
def art_storyline():
    global wyd
    print("You are about to leave art class, but the moon suddenly rises and it's night.")
    art_storyline2()
def art_storyline2():
    global wyd
    wyd = input("Do you run or walk?")
    if wyd in walk_list:
        weapon = random.choice(weapons_list)
        teacher = random.choice(teachers)
        print("You walk outside the class, but you're hit by " +teacher+ " with a "+ weapon)
        playagain()
    if wyd in run_list:
        weapon = random.choice(weapons_list)
        teacher = random.choice(teachers)
        print("You run as fast as you can but sadly you trip over a rock")
        time.sleep(1)
        stillrunning()
    while wyd not in walk_list and wyd not in run_list:
        print("Please enter a valid response")
        art_storyline2()
############################################################################

def stillrunning():
    rocktrip = input("What do you do? Go back and find another door or keep running?")
    if rocktrip in rocktrip_keeprunning:
        weapon = random.choice(weapons_list)
        teacher = random.choice(teachers)
        print("You get up and keep running, but you are hit by "+teacher+" with a "+weapon)
        playagain()
    elif rocktrip in rocktrip_finddoor:
        nearly_out_of_door()
    else:
        print("Please enter a valid response")
        stillrunning()

def nearly_out_of_door():
    print("You find another door, but it's locked!")
    time.sleep(1)
    print("You hear a weird noise coming from afar...")
    #playsound
    print("What was that?? ")
    time.sleep(1)
    weapon = random.choice(weapons_list)
    teacher = random.choice(teachers)
    print("Ahhh its " +teacher+ " with a " +weapon)
    time.sleep(1)
    throw_or_hit_door = input("Do you throw something at them or do you try to hit the door open?")

    if throw_or_hit_door in hit_door_open:
        print("You take your chances and try and hit the door open")
        if fifty_chance == 0:
            print("You successfully hit the door down and run!!")
            out_of_door()
        if fifty_chance == 1:
            print("Oh no :( The door doesn't break and you're stuck in the class!")
            time.sleep(1)
            deathtoteacher()


def out_of_door():
    print("You think to yourself, Wow! This is such a nice place!")
    time.sleep(1)
    step_foward = input("Do you step foward to see more?")
    if step_foward in yes_list or step_foward in foward_list:
        inside_the_room()
    elif step_foward in no_list or step_foward in go_back_list:
        print("You get pushed into the room by a mysterious figure...")
        inside_the_room()


def inside_the_room():
    print("It's surrounded by water and plants you've never seen before...")
    time.sleep(1)
    ##make first person color text different
    print("While admiring this new place, you step forward and fall down a hole")
    time.sleep(2)
#normal defs that can happena nytiem
def deathtoteacher():
    print("You get hit, and bleed out. Tha tsucks !")
def playagain():
    play = input("Would you like to play again?")
    if play in yes_list:
        art_storyline()
    else:
        print("Thanks for playing!")




##def the art storyline.


####run the code
art_storyline()
