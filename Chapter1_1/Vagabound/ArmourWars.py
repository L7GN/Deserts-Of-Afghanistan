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
player.body_count == 1
Punisher = False

def intro():
    print ("Chapter 1.2: ARMOUR WARS")
    time.sleep(5)
    print ("Your flying around in your iron man suit, where do you go?")
    print ("A:LA B: Barcelona")
    choice = input()
    if choice in answer_A:
        LA()
    if choice in answer_B:
        Barca()

def Barca():
    print ("You go to barcelona and run into sombra who hacks your iron man suit")
    time.sleep(3)
    print ("The suit self destructs and you die")
    print ("YOU DIED")
    time.sleep(5)
    intro()
    
def LA():
    print ("You land in los angeles and see carnage eating people and causing havoc")
    time.sleep(7)
    print ("A: Confront him B: Leave")
    choice = input()
    if choice in answer_A:
        ConfrontCarnage()
    if choice in answer_B:
        print ("You leave Carnage alone")
        time.sleep(3)
        print ("As you turn your back on him Carnage attacks you from behind and eats you")
        time.sleep(5)
        print ("YOU DIED")
        print ("TIP: Dont be a pussy")
        

def ConfrontCarnage():
    print ("You confront Carnage")
    print ("A:Activate suit B:Fight without")
    choice = input()
    if choice in answer_A:
        print ("You activate the iron man suit")
        time.sleep(3)
        print ("A:Head B:Arms C:Legs")
        choice = input()
        if choice in answer_A:
            print ("You grab his head and smash his head into a car")
            time.sleep(5)
            print ("Carnage lunges towards you and you grab him again and knock him down and throw him")
            time.sleep(7)
            print ("A rift portal appears between you both")
            time.sleep(5)
            print ("Kylo Ren steps out")
            time.sleep(3)
            print ("Kylo Ren: What? Where am i?")
            time.sleep(3)
            print ("Kylo Ren:Who are you and what is that")
            time.sleep(5)
            print ("Carnage runs towards kylo but he uses the force to disable him and reel him towards him to cut him in half with a lightsaber")
            time.sleep(10)
            print ("CARNAGE:DEAD")
            print ("Kylo runs away looking for answers")
            time.sleep(5)
            ArmourWars1()
        if choice in answer_B:
            print ("You target the arms and hold them in place so you can use your laserbeam to kill him")
            time.sleep(5)
            print ("CARNAGE:DEAD")
            player.body_count = player.body_count + 1
            print ("KILLS: ", player.body_count)
            ArmourWars1()

            
        else:
            print ("You target the legs and hit a double leg takedown")
            time.sleep(5)
            print ("You break his left leg and he screams out in pain")
            time.sleep(5)
            print ("You use your laserbeam to put a hole in his chest")
            time.sleep(5)
            print ("CARNAGE:DEAD")
            player.body_count = player.body_count + 1
            print ("KILLS: ", player.body_count)
            ArmourWars1()

    else:
        print ("You dont activate your iron man suit and have no weapons to fight Carnage with")
        time.sleep(8)
        print ("He makes an easy meal for you")
        print ("YOU DIED")
        print ("TIP: What a waste of Tony Stark technology")
        time.sleep(5)
        intro()

def ArmourWars1():
    print ("-------------------------------------")
    print ("You run into punisher")
    print ("A: Challenge him B:ALLY")
    choice = input(">>")
    if choice in answer_A:
        print ("You challenge the punisher")
        print ("He grabs his rifle and shoots a full mag at you")
        time.sleep(7)
        print ("You charge up your laserbeam and shoot it at punisher")
        time.sleep(5)
        print ("He dodges out the way and charges at you")
        time.sleep(3)
        print ("Strength" , player.strength)
        if player.strength > 8:
            print ("You brawl with the punisher and get a few good blows on him")
            time.sleep(5)
            print ("You suplex him onto a rock")
            time.sleep(3)
            print ("Your strength pulls you through and you knock him down with a overhand")
            time.sleep(5)
            print ("You see a sword do you grab it?")
            choice = input("Yes/No?")
            if choice in yes:
                print ("You grab the sword and behead punisher")
                time.sleep(5)
                player.body_count = player.body_count + 1
                print ("KILLS: " ,player.body_count)
                print ("PUNISHER:DEAD")
                ArmourWars2()
            if choice in no:
                print ("You dont grab the sword and offer punisher mercy")
                time.sleep(5)
                print ("You go to help punisher up but he is evaporated by OBSERVATION MAN")
                time.sleep(7)
                print ("PUNISHER:DEAD")
                print ("The narrator teleports you into space")
                time.sleep(4)
                print ("NARRATOR: This new world is already doomed")
                time.sleep(3)
                print ("NARRATOR: There are too many supernatural beings that managed to get through this new world")
                time.sleep(5)
                print ("NARRATOR: I tried to stop this...")
                time.sleep(3)
                print ("NARRATOR: My purpose was to keep this world safe from these threats but it was already too late")
                time.sleep(7)
                print ("NARRATOR:I had to reset the world")
                time.sleep(2)
                print ("NARRATOR:That didnt work")
                time.sleep(3)
                print ("NARRATOE: So i had to stop it from getting worse")
                time.sleep(5)
                print ("NARRATOR: My powers are now useless")
                print ("NARRATOR: The orb was my source of power and it has exploded")
                time.sleep(7)
                print ("NARRATOR: The orb of all was a orb present in every universe they are all interconnected if one goes so do they all")
                time.sleep(10)
                print ("NARRATOR: The orb was exploded accidentally in this universe because of these threats that made their way through")
                time.sleep(7)
                print ("NARRATOR: They all was fighting for this orb so they could tie their universe with this one")
                time.sleep(8)
                print ("NARRATOR: Because i reset the world i also reset the hierarchy")
                time.sleep(7)
                print ("NARRATOR: Noone is in control anymore and everyone is fighting for control of this world now")
                time.sleep(7)
                print ("NARRATOR: Now i have failed in keeping this world safe")
                time.sleep(5)
                print ("NARRATOR: Just know that from here onwards its not going to be easy its gonna be quite ugly")
                time.sleep(10)
                print ("NARRATOR: There is going to be a lot of fights, a lot of wars")
                time.sleep(5)
                print ("NARRATOR: A lot of death....")
                time.sleep(6)
                print ("NARRATOR: ANYONE COULD ARRIVE IN THIS WORLD NOW")
                time.sleep(5)
                print ("NARRATOR: This all started bacause SOMEONE got powerhungry and started travelling through universes absorbing powers")
                time.sleep(7)
                print ("NARRATOR: This left holes in the universe which would then lead to cracks which let people travel to our world")
                time.sleep(9)
                print ("NARRATOR: But now.. Anyone can travel anywhere meaning universes will collapse and worlds will be destroyed")
                time.sleep(7)
                print ("NARRATOR: I wish you good fortune")
                ArmourWars2()
        else:
            print ("You are too weak to challenge the punisher and get destroyed")
            print ("YOU DIED")
            print ("TIP: Remember how strong you are")
            intro()
    if choice in answer_B:
        SuitUp()


def ArmourWars2():
    print ("You are now in greenland fighting against T-51b Power Armour")
    print ("You charge up your laser beam and shoot it at the power armour damaging it heavily")
    time.sleep(12)
    print ("The power armour shuts off and you prevail")
    time.sleep(7)
    print ("SPIDERMAN: Should we split up or stick together?")
    ArmourWars3()

def ArmourWars3():
    print ("A:Split up B: Together")
    choice = input()
    if choice in answer_A:
        Spiderman = False
        print ("A: LEFT B: RIGHT")
        choice = input()
        if choice in answer_A:
            print ("You go left and see wolverine")
            if Spiderman == True:
                print ("He goes to stab you but spiderman appears and webs him to a tree")
                time.sleep(3)
                print ("SPIDERMAN: This world is not safe but its our job to try and make it")
                time.sleep(5)
                print ("Ezio lands on spiderman from above and tries to stealth kill him")
                time.sleep(6)
                print ("He throws a throwing knife at you which you catch")
                print ("Ezio wields his sword in a fast motion and cuts spiderman across the stomach making him kneel in pain")
                time.sleep(7)
                print ("Ezio turns towards you")
                time.sleep(3)
                print ("EZIO: You killed Boba Fett..")
                print ("EZIO: You will pay on behalf of the clan")
                print ("A to throw knife")
                choice = input()
                if choice in answer_A:
                    if player.speed > 7:
                        print ("You throw the knife at Ezios throat")
                        time.sleep(4)
                        print ("EZIO:DEAD")
                        player.body_count = player.body_count + 1
                        print ("KILLS: ",player.body_count)
                        print ("You run to spiderman but see that he has bled out")
                        print ("SPIDERMAN :DEAD")
                        print ("END OF CHAPTER 1.2: ARMOUR WARS")
                    else:
                        print ("You throw the knife but he catches it and cuts your right leg clean off")
                        time.sleep(6)
                        print ("You are in visible pain and he knocks you out")
                        time.sleep(10)
                        print ("You wake up in a holding cell not knowing where you are")
                        time.sleep(3)
                        print ("You try to stand up but realise you have one leg")
                        print ("END OF CHAPTER 1.2: ARMOUR WARS")
                else:
                    print ("You stand still and Ezio slices your throat")
                    print ("YOU DIED")
                    time.sleep(4)
                    intro()
                
            else:
                print ("He runs towards you and desroys your iron man armour leaving you open to a stab which he takes")
                time.sleep(7)
                print ("Spiderman appears and tries to help but stands no chance and gets stabbed 11 times")
                time.sleep(6)
                print ("SPIDERMAN:DEAD")
                print ("Black Panther pounces onto the scene and talks wolverine into being alies to help his universe take over")
                time.sleep(8)
                print ("Masterchief appears and shoots at them both, they run away")
                time.sleep(5)
                print ("Masterchief helps you up and takes you to his ship")
                print ("END OF CHAPTER 1.2: ARMOUR WARS")

    if choice in answer_B:
        Spiderman = True
        print ("A: LEFT B: RIGHT")
        choice = input()
        if choice in answer_A:
            print ("You go left and see wolverine")
            if Spiderman == True:
                print ("He goes to stab you but spiderman appears and webs him to a tree")
                time.sleep(3)
                print ("SPIDERMAN: This world is not safe but its our job to try and make it")
                time.sleep(5)
                print ("Ezio lands on spiderman from above and tries to stealth kill him")
                time.sleep(6)
                print ("He throws a throwing knife at you which you catch")
                print ("Ezio wields his sword in a fast motion and cuts spiderman across the stomach making him kneel in pain")
                time.sleep(7)
                print ("Ezio turns towards you")
                time.sleep(3)
                print ("EZIO: You killed Boba Fett..")
                print ("EZIO: You will pay on behalf of the clan")
                print ("A to throw knife")
                choice = input()
                if choice in answer_A:
                    if player.speed > 7:
                        print ("You throw the knife at Ezios throat")
                        time.sleep(4)
                        print ("EZIO:DEAD")
                        player.body_count = player.body_count + 1
                        print ("KILLS: ",player.body_count)
                        print ("You run to spiderman but see that he has bled out")
                        print ("SPIDERMAN :DEAD")
                        print ("END OF CHAPTER 1.2: ARMOUR WARS")
                    else:
                        print ("You throw the knife but he catches it and cuts your right leg clean off")
                        time.sleep(6)
                        print ("You are in visible pain and he knocks you out")
                        time.sleep(10)
                        print ("You wake up in a holding cell not knowing where you are")
                        time.sleep(3)
                        print ("You try to stand up but realise you have one leg")
                        print ("END OF CHAPTER 1.2: ARMOUR WARS")
                else:
                    print ("You stand still and Ezio slices your throat")
                    print ("YOU DIED")
                    time.sleep(4)
                    intro()
                
            else:
                print ("He runs towards you and desroys your iron man armour leaving you open to a stab which he takes")
                time.sleep(7)
                print ("Spiderman appears and tries to help but stands no chance and gets stabbed 11 times")
                time.sleep(6)
                print ("SPIDERMAN:DEAD")
                print ("Black Panther pounces onto the scene and talks wolverine into being allies to help his universe take over")
                time.sleep(8)
                print ("Masterchief appears and shoots at them both, they run away")
                time.sleep(5)
                print ("Masterchief helps you up and takes you to his ship")
                print ("END OF CHAPTER 1.2: ARMOUR WARS")
        else:
            print ("You walk into a room with savitar who grabs you and sprints around at superspeed which your body cant handle and you begin to fall apart limb by limb")
            time.sleep(14)
            print ("YOU DIED")
    else:
        ArmourWars2()



def SuitUp():
    print ("You and punisher become allies")
    time.sleep(3)
    print ("You meet up with iron man and war machine")
    time.sleep(2)
    print ("IRON MAN: There has been disturbances in Paris about some robots causing destruction")
    time.sleep(7)
    print ("You land in Paris and see megatron destroying buildings")
    time.sleep(5)
    print ("Iron Man flies at him but megatron picks up the eiffel tower and smashes him with it sending him crashing to the ground")
    time.sleep(10)
    print ("You fly upwards and are ready to fight Megatron")
    time.sleep(3)
    print ("A tail smashes into the back of Megatron")
    time.sleep(5)
    print ("Its Slattern the category V Kaiju")
    time.sleep(5)
    print ("The size advantage Slattern has allows him to beat megatron with ease")
    time.sleep(6)
    print ("Slattern uses his tail to impale Megatron ")
    time.sleep(4)
    print ("MEGATRON: DEAD")
    print ("The autobots appear and challenge Slattern")
    print ("You fly and find a safe with a nuclear weapon inside")
    key = input("Enter Key Here>> - - - -")
    if key == "1954":
        LongLiveTheKing()
    else:
        print ("First hint: The king and he will claim this world also")
        key = input("Enter Key Here>> - - - - ")
        if key == "1954":
            LongLiveTheKing()
        else:
            print ("Second hint: Its a year")
            key = input("Enter Key Here>> - - - - ")
            if key == "1954":
                LongLiveTheKing()
            else:
                print ("Final Hint: I believe they call him... the KING OF MONSTERS")
                key = input("Enter Key Here>> - - - - ")
                while key != "1954":
                    print ("Incorrect.. try again")
                    key = input("Enter Key Here>> - - - - ")
                LongLiveTheKing()
    
def LongLiveTheKing():
    print ("You open the safe and grab the nuclear weapon")
    Nuke = True
    print ("NARRATOR: WAIT!!!")
    time.sleep(5)
    print ("NARRATOR: Doing this will give GODZILLA a signal, infact it will give everyone a signal")
    print ("NARRATOR: YOU ARE GOING TO CAUSE A LOT OF DEATH AND A WAR")
    choice = input("USE NUCLEAR WEAPON Y/N?")
    if choice in yes:
        if Nuke == True:
            print ("You shoot the nuke at Slattern he can see it coming but cannot move out the way")
            time.sleep(9)
            print ("SLATTERN:DEAD")
            print ("OPTIMUS PRIME:DEAD")
            print ("RATCHET:DEAD")
            print ("ARCEE:DEAD")
            print ("BUMBLEBEE:DEAD")
            print ("BULKHEAD:DEAD")
            print ("SMOKESCREEN:DEAD")
            print ("ULTRAMAGNUS:DEAD")
            player.body_count = player.body_count + 8
            print ("KILLS : " ,player.body_count)
            Nuke = False
            time.sleep(10)
            print ("Godzilla rises from the ocean attacking everyone and everything with its atomic breath")
            time.sleep(8)
            print ("There are news articles appearing everywhere about a massive purple rift that has opened with characters from other universes running out of it")
            time.sleep(10)
            print ("Interstellar spaceships enter the atmosphere and shoot at godzilla he roars at them and outsteps predator skydiving")
            time.sleep(9)
            print ("PARIS  is entering its end...")
            time.sleep(5)
            print ("GREEN GOBLIN has escaped and has joined in the mayhem, killing the innocent")
            time.sleep(7)
            print ("Everywhere you look there are different characters fighting from different universes")
            time.sleep(10)
            print ("The nuclear alarm rings and fallout shelters have opened around France and the world will probably open them all as precaution")
            time.sleep(11)
            print ("You run to the nearest fallout shelter and take a look behind you to the see the mosasaurus grab GODZILLA by the neck and takes him underwater")
            time.sleep(9)
            print ("You watch as Warmachine fights away different characters and runs towards you before a milkvan hits him")
            time.sleep(9)
            print ("A psychopath exits the van and stabs Warmachine to death and takes his body into the van")
            time.sleep(8)
            print ("WARMACHINE:DEAD")
            print ("Punisher shoots at the van but it accelerates away")
            time.sleep(5)
            print ("Predator slowly approaches you both, you look at punisher before you enter combat with him")
            time.sleep(6)
            print ("He swings his sword at you both before sidekicking punisher away and focusing on you")
            time.sleep(8)
            print ("YOU ARE NOW ENTERING A FIGHT OF YOUR LIFE")
            time.sleep(5)
            print ("---------------FIGHTING STYLES-----------------")
            print ("Fighting styes allow you more freedom in your fights on using your strengths to beat opponents")
            print ("However you must be careful that you are nout outmatched in your fighting styles as that will result in well... Death")
            print ("Your Fighting Style choice will take character stats into consideration so CHOOSE WISELY")
            print (player.stats)
            print ("A: Aggressive: Strength")
            print ("B: Counter: Defense and Intelligence")
            print ("C: Talk out of it: Charisma")
            print ("D: DUEL : Speed")
            choice = input()
            if choice in answer_A:
                print ("You charge at predator with aggression")
                if player.strength > 7:
                    print ("You hit hard at Predator and give him no time to make an attack you disarm him and take his sword")
                    time.sleep(8)
                    print ("You stab the predator through the chest and run into the fallout shelter")
                    print ("END OF CHAPTER 1.2: ARMOUR WARS")
                else:
                    print ("You throw your strongest punch at Predator and he does not flinch")
                    print ("He rips your head off")
                    print ("YOU DIED")
                    time.sleep(7)
                    intro()
            if choice in answer_B:
                if player.defense > 5:
                    print ("You play on the counter and allow Predator to throw punches and to swing his sword at you")
                    time.sleep(5)
                    print ("He loses his patience and a laserbeam eventually connects harming predator you knock him down")
                    time.sleep(6)
                    print ("You do not have the strength to keep him knocked down for long and he gets back up")
                    if player.intelligence > 5:
                        print ("You attack whilst he is recovering and with no time to recover you uppercut his head off")
                        print ("You run into the fallout shelter")
                        print ("END OF CHAPTER 1.2: ARMOUR WARS")
                    else:
                        print ("Your not smart enough to know how to keep him down and he rips your legs off and smashing your head into bits")
                        print ("YOU DIED")
                        time.sleep(6)
                        intro()
                else:
                    print ("Your defence is no match and he guts you")
                    print ("YOU DIED")
                    time.sleep(5)
                    intro()
                
            if choice in answer_C:
                print ("You try talking to something that does not know english and it splits you into two")
                print ("YOU DIED")
                time.sleep(5)
                intro()

            if choice in DUEL:
                print ("You stare down the predator")
                if player.speed > 6:
                      print ("You shoot a fully charged laserbeam at predator turning his head to dust")
                      print ("his headless body falls to the ground")
                      time.sleep(5)
                      player.body_count = player.body_count + 1
                      print ("KILLS: " ,player.body_count)
                      print ("You run into the shelter")
                      print ("END OF CHAPTER 1.2: ARMOUR WARS")
            else:
                print ("You stand there and get obliterated")
                intro()
    if choice in no:
        print ("You leave the nuclear bomb and watch the fight from afar")
        time.sleep(7)
        print ("There are news articles appearing everywhere about a massive purple rift that has opened with characters from other universes running out of it")
        time.sleep(9)
        print ("You go to find shelter")
        print ("There are news articles appearing everywhere about a massive purple rift that has opened with characters from other universes running out of it")
        print ("END OF CHAPTER 1.2: ARMOUR WARS")              
            
                   
            

intro()
