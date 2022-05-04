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


player = Character.thief

def intro():
    print ("CHAPTER 1.2:BOUNTY HUNTERS")
    time.sleep(10)
    print ("You get mandalorian armour and get your first mission from Boba Fett")
    print ("They are creating their own bounty hunting clan to try and eliminate as many threats as possible")
    time.sleep(11)
    print ("NARRATOR: Alliances are being made meaning wars are becoming more likely")
    time.sleep(6)
    print ("These wars between universes are going to destroy all boundaries left between them")
    print ("I cant allow this i need to keep it together")
    time.sleep(10)
    print ("NARRATOR:But me intervening with the universe will allow HIM to come because he will know where we are")
    print ("NARRATOR:'I will get back to you")
    time.sleep(10)
    print ("QUEST UPDATE: BOUNTY: KILL THE BATMAN")
    time.sleep(5)
    print ("You go on your quest to kill batman")
    print ("TIP: YOUR CHOICES WILL AFFECT YOUR QUEST")
    time.sleep(10)
    MissionPrep()


def MissionPrep():
    print ("------------------------------------------------------------")
    print ("MISSION PREPERATION")
    print ("GEAR")
    print ("A: Mountain Climber B: Ninja C:Mandalorian")
    choice = input("Gear>>")
    if choice in answer_A:
        MountainClimber()
    if choice in answer_B:
        Ninja()
    if choice in answer_C:
        Mandalorian()
    else:
        print (required)
        choice = input()

    if choice in answer_A:
        MountainClimber()
    if choice in answer_B:
        Ninja()
    if choice in answer_C:
        Mandalorian()
    else:
        print (required)
        choice = input()

def MountainClimber():
    Gear = ("MountainClimber")
    print ("------------------------------------------------------------")
    print ("TARGETS")
    print ("--James Gordan")
    print ("--Alfred Pennyworth")
    print ("--Robin")
    print ("--Joker")
    time.sleep(15)
    print ("Where will you start?")
    print ("Gotham is where James Gordan and Alfred Pennyworth are")
    print ("New york is where Robin and the Joker are")
    print ("A:New York B:Gotham")
    choice = input()
    if choice in answer_A:
        print ("You begin in New York")
        Location = ("NYC")
        print ("Location:--",Location)
        print ("STYLE")
        print ("A:Stealth B:Guns blazing C:Interrogation")
        choice = input()
        if choice in answer_A:
            StealthNY()
        if choice in answer_B:
            RogueNY()
        if choice in answer_C:
            InformationNY()




def Ninja():
    Gear = ("Ninja")
    print ("------------------------------------------------------------")
    print ("TARGETS")
    print ("--James Gordan")
    print ("--Alfred Pennyworth")
    print ("--Robin")
    print ("--Joker")
    time.sleep(15)
    print ("STYLE")
    print ("A:Stealth B:Guns blazing C:Interrogation")
    choice = input()
    if choice in answer_A:
        StealthNY()
    if choice in answer_B:
        RogueNY()
    if choice in answer_C:
        InformationNY()


    

def Mandalorian():
    Gear = ("Mandalorian")
    print ("------------------------------------------------------------")
    print ("TARGETS")
    print ("--James Gordan")
    print ("--Alfred Pennyworth")
    print ("--Robin")
    print ("--Joker")
    time.sleep(15)
    print ("STYLE")
    print ("A:Stealth B:Guns blazing C:Interrogation")
    choice = input()
    if choice in answer_A:
            StealthNY()
    if choice in answer_B:
            RogueNY()
    if choice in answer_C:
            InformationNY()


def StealthNY():
    print ("------------------------------------------------------------")
    print ("You begin in New York")
    Location = ("NYC")
    print ("Location:--",Location)
    print ("You climb on the rooftops and search for the targets")
    print ("You will use these targets to try and get to the batman")
    time.sleep(10)
    print ("You see the hulk destroying New York, he seems to have gone rogue")
    time.sleep(7)
    print ("You see Joker going up to challenge the hulk")
    time.sleep(10)
    print ("The hulk throws a car at him crushing him")
    time.sleep(5)
    print ("JOKER:DEAD")
    time.sleep(3)
    print ("You see robin on the roofs hiding")
    time.sleep(5)
    print("You sneak over and go in for a stealth kill")
    time.sleep(5)
    print ("You go to kill Robin but he sees you coming and fights you")
    print ("You push him off the roofs and he crashes to the ground")
    time.sleep(5)
    print ("ROBIN:DEAD")
    player.body_count = player.body_count + 1
    print ("KILLS:" ,player.body_count)
    print ("BOBA FETT: Damn good job you have killed all the targets")
    time.sleep(7)
    print ("You stand confused as you had 2 targets remaining")
    time.sleep (5)
    print ("NARRATOR:I have released the OBSERVATION MAN")
    print ("NARRATOR:The new world needs protection so i needed to release 1 of the gods")
    time.sleep(10)
    print ("NARRATOR:HE is probably going to enter, shattering the walls between all universes allowing everything to merge")
    print ("My Time Is Up....")
    time.sleep(10)
    print ("BREAKING NEWS: Alfred Pennyworth and James Gordan found dead. UNKNOWN ENTITY SAID TO BE RESPONSIBLE")
    time.sleep(7)
    print ("You see two figures fall from the sky")
    time.sleep(4)
    print ("NARRATOR: That ia him, Ultimate Andy")
    print ("Ultimate Andy combats OBSERVATION MAN")
    time.sleep(8)
    print ("The Batman glides onto the scene and lands on the rooftop with you")
    print ("He goes to fight you to avenge Robin")
    print ("#####BOSS FIGHT#####")
    BatmanBoss()

def BatmanBoss():
    print ("#####################################################")
    player.health = 100
    BatmanHealth = 1000
    print ('HP:' , BatmanHealth)
    print ("A:Attack B:CALL C:Items")
    choice = input()
    if choice in answer_A:
        print ("------------------------------------------------------------")
        print ("You throw a overhand at the Batman and connect it")
        BatmanHealth = BatmanHealth - 100
        print ("BATMAN HP:",BatmanHealth)
        print ("The Batman then beats you up because your useless")
        player.health = player.health - 99
        print ("HP:",player.health)
        time.sleep(10)
        print ("NARRATOR: I cant risk you die along with me")
        print ("The narrator comes down from the sky and fights Batman")
        time.sleep(10)
        print ("The narrator freezes the batman in time then beats him up")
        BatmanHealth == 1
        print ("BATMAN HP:",BatmanHealth)
        time.sleep(5)
        print ("Ultimate Andy approaches me and uses his powers from out this world to bring me to atoms")
        time.sleep(5)
        print ("NARRATOR:DEAD")
        print ("With me destroyed i do not have control over what happens next")
        print ("You look for observation man who you see is injured and disabled")
        time.sleep(10)
        print ("The narrator uses his last wish to teleport you to safety")
        print ("You are now in LA")
        print ("The narrators soul lives within you so that it can narrate your story")
        print ("END OF CHAPTER1.2")
        
            
    if choice in answer_B:
        print ("------------------------------------------------------------")
        print ("You call for help and the OBSERVATION MAN turns towards you and grabs Batman and devours him")
        time.sleep(10)
        print ("The Batman and Observation Man merge into one")
        print ("The body and mind of Batman remain however the powers of OBSERVATION MAN remains")
        time.sleep(12)
        print ("With this merge they challenge Ultimate Andy")
        print ("But his power level is too high")
        print ("Observations powers allow him to see what he is doing but they cant do anything to counter it")
        time.sleep(20)
        print ("I teleport into the way of Andys powers and get demolished")
        time.sleep(5)
        print ("NARRATOR:DEAD")
        print ("With me destroyed i do not have control over what happens next")
        time.sleep(7)
        print ("A rift opens and you run through it")
        print ("END OF CHAPTER 1.2")
    if choice in answer_C:
        print ("------------------------------------------------------------")
        print ("You reach into your pockets and cant find any items")
        print ("The Batman KOs you")
        time.sleep(10)
        print ("You wake up to Observarion Man standing over you he gives you the option to merge into one")
        print ("A: Accept B;Decline")
        choice = input()
        if choice in answer_A:
            print ("------------------------------------------------------------")
            print ("You merge into one and become a GOD")
            print ("NARRATOR: My time has come it is time for me to go")
            time.sleep(7)
            print ("You watch as the narrator fades away knowing you are safe with OBSERVATION MAN")
            print ("END OF CHAPTER 1.2")
        if choice in answer_B:
            print ("You decline and he teleports away")
            time.sleep(3)
            print ("You have just declined to become a god and you stand there looking stupid")
            time.sleep(3)
            print ("I am that sick of your shit that i dont want to do this anymore")
            time.sleep(5)
            print ("NARRATOR:DEAD")
            print ("With me destroyed i do not have control over what happens next")
            time.sleep(10)
            print ("Boba Fett and Mandalorian return to save you")
            time.sleep(3)
            print ("Mandalorian: We have bad news")
            time.sleep(3)
            print ("Boba Fett: The world has expanded and rifts are opening")
            print ("Mandalorian: The rifts have allowed more characters to get into this world meaning more enemies")
            time.sleep(10)
            print ("Boba Fett; We have got to defend ourselves we dont know who we can encounter")
            time.sleep(5)
            print ("You watch from the window as you see rifts opening from everywhere allowing universes to connect with ours")
            time.sleep(5)
            print ("You need to find out how this is happening")
            print ("END OF CHAPTER 1.2")
                
def RogueNY():
    print ("------------------------------------------------------------")
    print ("You arrive in New York and see some thugs do you:")
    print ("A:Beat them up B:Ignore")
    choice = input()
    if choice in answer_A:
        print ("------------------------------------------------------------")
        print ("You walk up to the gang of thugs")
        time.sleep(3)
        print ("They pull out knives and run at you")
        time.sleep(3)
        print ("You take them on one on one")
        time.sleep(5)
        print ("You find the hideout for the thugs")
        time.sleep(3)
        print ("You see Robin dead on the floor with Joker next to him holding the gun")
        time.sleep(7)
        print ("ROBIN DEAD")
        print ("3 TARGETS REMAIN")
        time.sleep(5)
        print ("NARRATOR: Breaking down this gang may be enough to bring out the BATMAN")
        time.sleep(5)
        print ("You walk into the hideout")
        Hideout()
    if choice in answer_B:
        print ("------------------------------------------------------------")
        print ("You get shot by the thugs and die")
        RogueNY()

def Hideout():
    #map
    dungeonMap = [["0","0","0","0","0","0",".","3","E"],
                  ["0",".",".","1",".",".",".","7","."],
                  ["0",".",".","2",".",".",".","1","."],
                  ["0",".",".","4",".",".",".","5","."],
                  ["0",".","V","7","1",".7","7","7","0"],
                  ["0","7",".7","1","*",".",".",".","0"],
                  ["0","8",".",".",".",".","7",".","0"],
                  ["0","0","0","0","0","0","0","0","0"]]

    playerMap  = [[".",".",".",".",".",".",".",".","E"],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  ["S",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."],
                  [".",".",".",".",".",".",".",".","."]]


    #Displaying the map
    def displayMap(maps):
        for x in range(0,8):
            print(maps[x])

    #selecting a map
    mapChoice = dungeonMap

    displayMap(playerMap)

    #initialising the players position
    position = mapChoice[0][0]

    def main(mapChoice, playerMap, position):
        #players starting position
        x = 0
        y = 3
        #players inventory
        key = False
        gun = False
        sword = False

        print(mapChoice[y][x])
        position = 0
        while position != "E":
            
            previousX = x
            previousY = y

            movement = input("N,S,E,W,MAP").upper()

            if movement == "N":
                y = y-1

            if movement == "S":
                y = y+1

            if movement == "E":
                x = x+1

            if movement == "W":
                x = x-1

            if movement == "MAP":
                displayMap(playerMap)

            position = mapChoice[y][x]
            playerMap[y][x] = "X"
            
            if position == "0" or position == "1":
                print("You hit a wall, you stumble in the darkness back to your previous position...")
                x = previousX
                y = previousY
                position = mapChoice[y][x]

            if position == ".":
                print("You sneak through the dark corners of the hideout.")

            if position == "*":
                print("In the darkness you see a dull glint..")
                print("You go over to inspect and realise that the object is a gun")
                print("You pick it up and holster it in you belt")
                gun = True

            if position == "2":
                print("You enter a room with the riddler at a table....")
                print("They tell you that in order to pass, you will need to answer their riddle...")
                print("What has a bed but does not sleep, and a mouth but does not eat?")
                guess = input().upper()
                if guess != "RIVER":
                    print("You anger the riddler, He slices your throat")
                    x = previousX
                    y = previousY
                    print("YOU DIED")
                    print ("TIP: Riddler begins with R")
                    Hideout()
                    
                    position = mapChoice[y][x]

                else:
                    print("You may pass through my room....")
                    
            if position == "3":
                if key == False:
                    print("you come across a door, but do not have a key for it...")
                    x = previousX
                    y = previousY
                    print("You go back to the previous room")
                    position = mapChoice[y][x]
                else:
                    print("you come across a dimly lit door...")
                    print("fumbling around in the dark, you find the keyhole...")
                    print("You open the door, and walk through into the darkness....")
                    
                    
            if position == "4":
                print("You find a small crack in the wall...You could easily squeeze through...")
                print("as you squeeze through the gap you feel a rip and your inventory falls out of the rip")
                print("You have lost everything...is it worth going back?")
                print("You are the other side of the gap now...its up to you if you should continue on...")
                key = False
                sword = False

            if position == "5":
                print("You can see the exit up ahead, but one final challenge remains...")
                print(" appears before you, in order to leave you must present the code...")
                print("Did you find any letters on your travels?")
                guess = input().upper()
                if guess != "ZORK":
                    print("The troll is seriously unimpressed, it makes a grab for you, but you dive back into the previous room")
                    x = previousX
                    y = previousY
                    position = mapChoice[y][x]
                else:
                    print("The troll is even more annoyed you got his password right")
                    print("He makes a grab for you...")
                    if sword == True:
                        print("Using the sword you slash at the troll who recoils in horror!")
                        print("The troll flees, leaving you to exit in peace...")
                    else:
                        print("You dive out of his grasp and back into the last room")
                        print("Something tells me that troll isnt going to let you out without a fight!")
                        x = previousX
                        y = previousY
                        position = mapChoice[y][x]
            if position == "7":
                print ("You find a group of bandits")
                if sword == True:
                    print ("You use your dragonbane to slice through the bandits")
                if gun == True:
                     print ("You shoot the bandits from range")
                if sword == True and gun == True:
                    print ("You put your draggon bane through two bandits and shoot the others")
                if sword == False and gun == False:
                    print ("You get ganged up on and get stabbed")
                    print ("YOU DIED")
                    print ("TIP: probably time for a career change")
                    StealthNY()
            if position == "V":
                print ("You walk into a room with a dragon")
                time.sleep(3)
                print ("The dragon has a dragonbane through its head")
                print ("You pick it up")
                sword = True
                time.sleep(7)
                print ("NARRATOR: So the dragons have made their way into this world")
                
                        
                    

            

            if position == "8":
                print("You find a small rusty key on the floor, you pick it up and put it in your pocket")
                key = True


            
            
        print("you made it out alive!!!")
        time.sleep(5)
        print ("You are about to enter the final room")
        print ("ARE YOU READY, Y/N")
        choice = input()
        if choice in yes:
            JokersFinale()
        else:
            print ("You get shot through the door")
            print ("YOU DIED")
            Hideout()
            


            
    main(mapChoice, playerMap, position)                           


def JokersFinale():
    print ("------------------------------------------------------------")
    print ("You enter the room and see the Joker with Batman, Alfred and Gordon dead on the ground")
    time.sleep(7)
    print ("JOKER: Look at what i have done.")
    time.sleep(3)
    print ("JOKER: I have done your job for you")
    time.sleep(3)
    print ("JOKER: So that only leaves me")
    time.sleep(5)
    print ("JOKER: How about...")
    time.sleep(5)
    print ("JOKER: We make a deal??")
    time.sleep(3)
    print ("JOKER: Now i had been talking to this goblin guy")
    time.sleep(5)
    print ("JOKER:But he has been executed recently")
    time.sleep(3)
    print ("JOKER: We had plans to rule this new world")
    time.slseep(3)
    print ("JOKER: BUT YOU KILLED HIM!")
    time.sleep(5)
    print ("JOKER: So my deal..")
    time.sleep(7)
    print ("JOKER: You can join me and replace the goblin guy and we have no problems")
    time.sleep(7)
    print ("JOKER: OR you face DEATH")
    time.sleep(4)
    print ("JOKER: Time is ticking")
    choice = input("Deal? Y/N")
    if choice in yes:
        print ("------------------------------------------------------------")
        print ("JOKER: Good.. GOOD")
        tine.sleep(3)
        print ("JOKER: Me an you are gonna cause CARNAGE")
        time.sleep(3)
        print ("JOKER:*Laughs sinisterly")
        time.sleep(5)
        print ("END OF CHAPTER 1.2:Bounty Hunters")
    if choice in no:
        print ("------------------------------------------------------------")
        print ("JOKER: Fine.. ")
        time.sleep(5)
        print ("A rocket explodes knocking you and the joker down to the ground")
        time.sleep(5)
        print ("You look as you see Boba Fett aiming his gun at Joker who surrenders")
        time.sleep(7)
        print ("Boba Fett shows no remorse and kills joker")
        time.sleep(3)
        print ("JOKER:DEAD")
        print ("BOBA FETT: We need to move quickly")
        print ("END OF CHAPTER 1.2:BOUNTY HUNTERS")

    else:
        print ("You try to pull a sneak on joker and he shoots you through the skull")
        print ("YOU DIED")
        time.sleep(3)
        RogueNY()


def InformationNY():
    print ("------------------------------------------------------------")
    print ("You walk into the interrogation room with the captive tied up with a bag on their head")
    time.sleep(5)
    print ("A to remove bag")
    choice = input()
    if choice in answer_A:
        print ("You remove the bag to reveal alexios the assassin")
        time.sleep(5)
        print ("Alexios: Listen i had a encounter with this The Batman")
        time.sleep(5)
        print ("Alexios: He was not easy for me to take down")
        time.sleep(5)
        print ("Alexios: He is currently in the place you call New York?")
        time.sleep(3)
        print ("Alexios: I got battered by an angry green giant there")
        time.sleep(3)
        print ("Alexios: I am going to reunite with my creed and get them on board with this bounty hunting clan to take over the new world")
        time.sleep(9)
        print ("Alexios: I shall speak with you soon")
        time.sleep(5)
        StealthNY()

    else:
        print ("------------------------------------------------------------")
        print ("You dont remove the bag and exit the room")
        print ("You see Boba Fett who asks you why you did not do your job")
        time.sleep(10)
        print ("You get knocked out by the mandalorian who hits you on the back of the head")
        time.sleep(11)
        print ("You wake up in the deserts of afghanistan...")
        print ("End of Chapter 1.2")
        


intro()
