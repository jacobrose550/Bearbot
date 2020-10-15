import time
import random
from random import randint
from random import randrange
import time, os
import sys
##50 percent chance
fifty_chance = randint(0, 1)
##33 percent chance
thirty_chance = randint(0, 2)
# lists
main_centre_list = ["main centre","go back to main centre","selection","go back to selection"]
items_in_class = ["Computer", "Ladder", "Printer"]
yes_list = ["yes", "Yes", "Ye", "ye", "y", "Y"]
no_list = ["no", "No", "N", "n"]
teachers = ["Mr. Walker", "Mr Wilson", "Mr Simpson", "Mr Macown"]
weapons_list = ["bat", "knife", "hammer", "boulder", "rock"]
animals = ["Pig", "Rat", "Sheep", "Snake", "Chicken"]
run_list = ["Run", "run"]
walk_list = ["walk", "Walk"]
rocktrip_finddoor = ["go back", "Go Back", "go Back", "Go Back", "GO BACK", "find another door", "find door",
                     "Find Door", "find Door", "Find Door", "FIND DOOR", "door", "Door", "find a door"]
rocktrip_keeprunning = ["keep running", "Keep running", "keep Running", "Keep Running", "KEEP RUNNING"]
hit_door_open = ["hit", "Door", "Hit", "door", "hit door open", "hit the door open", "hit door", "hit the door",
                 "hit the door please"]
subjects = ["art", "english", "digital science"]
foward_list = ["foward", "step foward"]
go_back_list = ["go back", "back"]
move_list = ["move", "move now"]
stay_list = ["stay", "stay in net", "stay in the net"]
dont_move_list = ["dont move", "dont", "dont move please"]
throw_something = ["throw something", "throw", "get something"]
vent_list = ["vent", "Go to the vent", "go through the vent", "the vent"]
enter_vent = ["enter vent", "enter the vent", "go in the vent", "go into the vent", "go vent", "vent"]
play_again_list = ["play again", "again", "play again please"]

print("This is inspired by Eva")
time.sleep(1)
print("Please use lower cases while entering your response.")
time.sleep(1)


########################################################################
def art_storyline():
    global wyd
    print("You are about to leave your class, but the moon suddenly rises and it's night.")
    art_storyline2()


def art_storyline2():
    time.sleep(1)
    print("Do you run or walk?")
    art_storyline3()


def art_storyline3():
    wyd = input("")
    if wyd in walk_list:
        time.sleep(1)
        weapon = random.choice(weapons_list)
        teacher = random.choice(teachers)
        time.sleep(1)
        print("You walk outside the class, but you're hit by " + teacher + " with a " + weapon)
        time.sleep(2)
        playagain()
    if wyd in run_list:
        time.sleep(1)
        weapon = random.choice(weapons_list)
        teacher = random.choice(teachers)
        print("You run as fast as you can but sadly you trip over a bag")
        time.sleep(1)
        stillrunning()
    while wyd not in walk_list and wyd not in run_list:
        print("Please enter a valid response")
        art_storyline3()


############################################################################

def stillrunning():
    print("What do you do? Go back and find another door or keep running?")
    stillrunning2()


def stillrunning2():
    rocktrip = input("")
    if rocktrip in rocktrip_keeprunning:
        weapon = random.choice(weapons_list)
        teacher = random.choice(teachers)
        print("You get up and keep running, but you are hit by " + teacher + " with a " + weapon)
        playagain()
    elif rocktrip in rocktrip_finddoor:
        nearly_out_of_door()
    else:
        valid_response()
        time.sleep(1)
        stillrunning2()


###################################################################################################

def nearly_out_of_door():
    time.sleep(1)
    print("You find another door, but it's locked!")
    time.sleep(2)
    print("You hear a weird noise coming from afar...")
    time.sleep(1)
    print("What was that?? ")
    time.sleep(2)
    weapon = random.choice(weapons_list)
    teacher = random.choice(teachers)
    print("Ahhh its " + teacher + " with a " + weapon)
    time.sleep(1)
    throwhitdoor()


###################################################################################################

def throwhitdoor():
    print("Do you throw something at them or do you try to hit the door open?")
    throwhitdoor2()


def throwhitdoor2():
    teacher = random.choice(teachers)
    pickupitem = random.choice(items_in_class)
    throw_or_hit_door = input("")
    if throw_or_hit_door in hit_door_open:
        print("You take your chances and try and hit the door open")
        time.sleep(2)
        if fifty_chance == 0:
            print("You successfully hit the door down and run!!")
            time.sleep(1)
            ##run out of door code
            out_of_door()
        elif fifty_chance == 1:
            print("Oh no :( The door doesn't break and you're stuck in the class!")
            time.sleep(1)
            deathtoteacher()
    elif throw_or_hit_door in throw_something:
        print("You pick up a " + pickupitem + " and throw it at them")
        ###########################
        time.sleep(2)
        ##0 = miss
        ##1 = hits
        dodge_chance = randint(0, 1)
        if dodge_chance == 0:
            print("Your accuracy sucks and you throw it the wrong way")
            time.sleep(2)
            hitdooragain()
        elif dodge_chance == 1:
            print("You successfully hit them!")
            ###############################REOCCURING THING
            time.sleep(2)
            print("They are bleeding, but are not dead.")
            time.sleep(1)
            print("This spares you some time to try and escape the classroom.")
            time.sleep(2)
            print("Do you go through the vent that you previously saw? Or do you try and hit the door open again?")
            ventordoor1()
    else:
        valid_response()
        throwhitdoor2()


def ventordoor1():
    teacher = random.choice(teachers)
    vent_or_door = input("")
    if vent_or_door in hit_door_open:
        print("You take your chances and try and hit the door open")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("You successfully hit the door down and run!!")
        out_of_door()
    elif vent_or_door in vent_list:
        print("You run to the vent, and grab a ladder")
        time.sleep(1)
        waiting_animated()
        print(teacher + " tries to grab you, but you kick them in the face")
        time.sleep(1)
        waiting_animated()
        print("They bleed out and die!")
        waiting_animated()
        print("You open the vent, and crawl in")
        waiting_animated()
        the_vent()
    else:
        valid_response()
        ventordoor1()


##################################################################################################
def hitdooragain():
    teacher = random.choice(teachers)
    pickupitem = random.choice(items_in_class)
    print("Do you throw something or try to hit the door open again?")
    throworhit()


def throworhit():
    throw_or_hit_door = input("")
    if throw_or_hit_door in hit_door_open:
        print("You take your chances and try and hit the door open")
        if fifty_chance == 0:
            time.sleep(1)
            print("You successfully hit the door down and run!!")
            ##run out of door code
            time.sleep(1)
            out_of_door()
        elif fifty_chance == 1:
            time.sleep(1)
            print("Oh no :( The door doesn't break and you're stuck in the class!")
            time.sleep(1)
            deathtoteacher()
    elif throw_or_hit_door in throw_something:
        print("You throw it at them again, but you sadly miss.")
        time.sleep(2)
        deathtoteacher()
    else:
        valid_response()
        throworhit()


##################################################################################################

###################################################################################################
def the_vent():
    print("You're about to enter the vent")
    time.sleep(1)
    print("Before you go in, you smell an odd smell. It smells like a rotting body...")
    time.sleep(3)
    print("You hear the teacher get up, but they are wounded")
    print("Do you enter the vent? ")
    enterventorno()


def enterventorno():
    go_in = input("")
    if go_in in yes_list or go_in in enter_vent:
        time.sleep(2)
        print("You enter the vent...")
        time.sleep(1)
        not_finished()
    elif go_in in no_list:
        not_finished()
    else:
        valid_response()
        enterventorno()


###################################################################################################

def valid_response():
    print("Please enter a valid response.")


def waiting_animated():
    for i in range(9):
        time.sleep(0.2)
        x = i % 2
        sys.stdout.write("." * x)
        sys.stdout.flush()


def out_of_door():
    print("You think to yourself, Wow! This is such a nice place!")
    time.sleep(2)
    print("Do you step foward to see more?")
    stepfowardorstay()


def stepfowardorstay():
    step_foward = input("")
    if step_foward in yes_list or step_foward in foward_list:
        time.sleep(1)
        inside_the_room()
    elif step_foward in no_list or step_foward in go_back_list:
        time.sleep(1)
        print("You get pushed into the room by a mysterious figure...")
        time.sleep(1)
        inside_the_room()
    else:
        valid_response()
        stepfowardorstay()


def inside_the_room():
    print("It's surrounded by water and plants you've never seen before...")
    time.sleep(1)
    ##make first person color text different
    print("While admiring this new place, you step forward and fall down a hole...")
    time.sleep(2)
    down_the_hole()


# normal defs that can happena nytiem

##net with 1 in 5 chance of not breaking
def down_the_hole():
    print("After falling for about 20 seconds, you land in a net")
    time.sleep(2)
    print("But if you move, the net only has a 2 in 5 chance of breaking.")
    time.sleep(3)
    print("What do you do? Stay there or move?")
    moveorstay()


def moveorstay():
    weapon = random.choice(weapons_list)
    teacher = random.choice(teachers)
    moveorstay = input("")
    if moveorstay in dont_move_list or moveorstay in stay_list:
        print("You stay in the net, and see " + teacher + " looking at you from above")
        time.sleep(2)
        print("""You scream, "Why are you here?!" """)
        time.sleep(1)
        not_finished()
    else:
        not_finished()


def deathtoteacher():
    print("You get hit by them, and bleed out.")
    time.sleep(1)
    playagain()


def playagain():
    print("Would you like to play again? Or go back to the main selection?")
    playagain2()


def playagain2():
    play = input("")
    if play in yes_list or play in play_again_list:
        art_storyline()
    elif play in no_list:
        print("Thanks for playing!")
        quit()
    elif play in go_back_list or play in main_centre_list:
        import maincentre
    else:
        print("Please enter a valid response.")
        playagain2()


##def the art storyline.

def not_finished():
    print("This part of the story isn't finished yet, but thank you for playing!")
    time.sleep(2)
    playagain()


####run the code
art_storyline()
