answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
required = ("\nUse only A, B, or C\n") 
import Character
import time
import sys


player = Character.warrior
YetiHead = False

def intro():
    print ("Chapter 1.2: Winter")
    print ("You are freezing on mount everest and find a cave")
    time.sleep(7)
    print ("In the cave is a yeti")
    print ("A: FIGHT B:RUN")
    choice = input()
    if choice in answer_A:
        FightYeti()
    if choice in answer_B:
        Caveexplore()

def FightYeti():
    if player.strength > 5:
        print ("You snap the Yeti's head off, do you keep it?")
        choice = input()
        if choice in yes:
            print ("You store the head in your rucksack")
            YetiHead = True
            Caveexplore()
        if choice in no:
            YetiHead = False
            Caveexplore()
        else:
            print ("You stare at it waiting for something to happen")
            time.sleep(10)
            print ("You keep staring")
            time.sleep(3)
            print (".....")
            time.sleep(2)
            print ("Bit odd now..")
            time.sleep(5)
            print ("ok thats enough...")
            Caveexplore()
    else:
        print ("The Yeti mauls uou")
        print ("YOU DIED")
        print ("TIP: Stop fighting things when you are so weak")
        intro()

def Caveexplore():
    print ("You are exploring the cave and come across a peasant i guess its like looking in a mirror for you")
    time.sleep(10)
    print ("You approach him and he pulls out a knife and runs at you turns out he is as crazy as you too")
    time.sleep(10)
    print ("You bang him on the nose and he falls to the ground and turns to ash")
    time.sleep(4)
    
            
intro()
