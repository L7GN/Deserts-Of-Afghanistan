answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
required = ("\nUse only A, B, or C\n") 
import Character
import time


player = Character.thief
player.body_count == 1
def intro():
    player.body_count == 1
    print ("------------------------------------------------------------")
    print ("You are resting in Kabul and are asking people if they have seen anything weird lately")
    print ("You exit a bar and see...")
    time.sleep(10)
    print ("THE ROCK!! HES BACK!!!")
    print ("NARRATOR:'How is he back'")
    time.sleep(5)
    print ("NARRATOR:'Im gonna have to send someone to solve this'")
    time.sleep(6)
    print ("A beam of white light hits the ground and as it fades away")
    print ("You see a giant with a massive eye in its chest")
    time.sleep(8)
    print ("NARRAOR:'I present to you THE OBSERVATION MAN'")
    print ("You watch as he fights the rock")
    time.sleep(6)
    print ("The rock stands no chance against observation man")
    print ("Observation man wipes the floor with him and beats him to an end")
    time.sleep(7)
    print ("Observation Man picks the rock up and with his giant hand snaps his neck")
    time.sleep(5)
    print ("THE ROCK:DEAD")
    time.sleep(5)
    print ("NARRATOR:'OBSERVATION MAN is a elder god for the new world")
    time.sleep(3)
    print ("NARRATOR:'His power level is on a different scale to MOST beings and variations'")
    time.sleep(5)
    print ("NARRATOR:'His powers are that he knows what his opponents are going to do before they do it making him excel in combat'")
    print ("NARRATOR:'The eye is also a weapon as it uses solar energy to emit a powerful laser known to destoy anything in an instance")
    time.sleep(10)
    print ("NARRATOR:'He is my guardian and guardian of the new world'")
    time.sleep(5)
    print ("The observation man fades away and you see a light go back up to the sky")
    time.sleep(5)
    print ("You approach the rock and see his lifeless body laying there on the ground")
    print ("You see two figures in the sky with jetpacks they get wiped out by someone on a glider")
    print ("A: Rush over B:Go the opposite way")
    print ("------------------------------------------------------------")
    choice = input()
    if choice in answer_A:
        BobaMandoGoblinFight()
    if choice in answer_B:
        StrangeEncounter()

def BobaMandoGoblinFight():
    print ("------------------------------------------------------------")
    print ("You rush over to the crash and see Boba Fett and The Mandalorian fighting Green Goblin")
    time.sleep(5)
    print ("You watch as they go into hand to hand combat")
    time.sleep(3)
    print ("The jetpacks are broken and so is the glider")
    time.sleep(3)
    print ("The goblin gets shot in the chest with a laser but he continues to fight the mandalorian")
    print ("You remember you have a golden revolver")
    print ("Do you: A:Kill The Mandalorian B:Kill Green Goblin C:Kill Boba Fett")
    choice = input()
    if choice in answer_A:
        MandoKill()
    if choice in answer_B:
        TheGoblinKill()
    if choice in answer_C:
        BobaKill()

def MandoKill():
    print ("------------------------------------------------------------")
    print ("You aim the revolver at mandalorian and shoot")
    time.sleep(5)
    print ("You forget hes wearing armour and he looks over towards you...")
    time.sleep(5)
    print ("Green goblin gets the sneak attack and stabs him in the neck")
    print ("THE MANDALORIAN:DEAD")
    time.sleep(3)
    print ("Boba Fett rushes over and gets battered by Green Goblin in a one on one")
    time.sleep(5)
    print ("Realising what you have just done you use this time to run away")
    print ("You run away and go to the docks")
    print ("You see something approaching from the water")
    time.sleep(10)
    print ("GODZILLA!!!")
    print ("The military are trying to suppress him but stand no chance")
    time.sleep(5)
    print ("You hide in a cave")
    print ("You hear voices and find a source of light")
    print ("With the light you see caesar the ape")
    time.sleep(10)
    print ("He chases you out the cave but gets blasted by godzillas beam")
    print ("CAESAR:DEAD")
    print ("You run for your life")
    time.sleep(8)
    print ("Darth Vader appears and helps you kill the apes")
    time.sleep(5)
    print ("You stay with him and he tells you about his plans to rob the millenium falcon and to create a new deathstar to destroy universes different to his own")
    print ("END OF CHAPTER1.1:THE NEW WORLD")
    

def TheGoblinKill():
    print ("------------------------------------------------------------")
    print ("You shoot the goblin but his armour is bulletproof")
    time.sleep(5)
    print ("Boba Fett and Mandalorian use the distraction to get the upperhand on the goblin")
    print ("Boba Fett uses his flamethrower and burns the Green Goblin")
    print ("GREEN GOBLIN:DEAD")
    time.sleep(7)
    print ("The bounty hunters thank you for the help and give you a reward")
    player.wallet = player.wallet + 100
    print ("You earned 100 Imperial Credits")
    print ("They ask you if you want to join us")
    time.sleep(8)
    print ("You accept..")
    time.sleep(4)
    print ("END OF CHAPTER1.1:THE NEW WORLD")

def BobaKill():
    print ("------------------------------------------------------------")
    print ("You aim your gun at Boba Fett..")
    time.sleep(5)
    print ("The goblin batters Boba Fett knocking him down and destorying his mask")
    time.sleep(3)
    print ("In this instance you shoot Boba in the head killing him")
    print ("BOBA FETT:DEAD")
    player.body_count = player.body_count + 1
    print ("KILLS: ", player.body_count)
    time.sleep(5)
    print ("The goblin kills the mandalorian and approaches you")
    print ("THE MANDALORIAN:DEAD")
    time.sleep(7)
    print ("The goblin gives you the opportunity to team up with him")
    print ("Do you accept?")
    print ("A: Accept B: Reject C:Suprise attack")
    choice = input()
    if choice in answer_A:
        AcceptGoblinDeal()
    if choice in answer_B:
        RejectGoblinDeal()
    if choice in answer_C:
        SupriseGreenGoblin()


def AcceptGoblinDeal():
    print ("------------------------------------------------------------")
    print ("You accepted the goblins deal and shake hands")
    print ("Spiderman swings in and attacks green goblin")
    time.sleep(3)
    print ("Spiderman gets the better of both of you and webs you up")
    time.sleep(5)
    print ("Spiderman sends you to a New York Prison")
    print ("You go into a cell with Green Goblin,Venom,Electro,Doctor octavius and the lizard")
    print ("The goblin is planning on making a team to take down spiderman and then to conquer the world")
    time.sleep(5)
    print ("A plane crashes into the prison giving you the opportunity to escape")
    print ("The six of you take the opportunity")
    time.sleep(6)
    print ("Goblin has requested for you to cause mayhem in the city to boost the reputation of the team and to lure the spiderman")
    print ("You see deathstroke roaming the streets")
    print ("You Challenge him and he tears you apart")
    time.sleep(5)
    print ("He slices your right hand off and goes to chop your head off")
    print ("Venom appears and finishes him")
    print ("DEATHSTROKE:DEAD")
    time.sleep(5)
    print ("You black out and then wake up to see the green goblin staring at you")
    time.sleep(3)
    print ("He calls you a failure and asks for your abilities")
    print ("Do you: A:Say nothing B:Lie")
    choice = input(">>")
    if choice in answer_A:
        print ("------------------------------------------------------------")
        print ("Goblin:'Nothing, thats what i thought'")
        print ("Green goblin throws you out of the group and now you lie in the streets of New York")
        time.sleep(5)
        print ("You have no money, no house, no nothing")
        print ("A:Rob someone")
        choice = input()
        if choice in answer_A:
            print ("------------------------------------------------------------")
            print ("You rob someone but enter a dark alley in your escape")
            time.sleep(5)
            print ("The batman appears and you run the opposite way")
            time.sleep(3)
            print ("Then daredevil appears")
            time.sleep(3)
            print ("They fight with you in the middle")
            time.sleep(3)
            print ("You take a few blows but then punisher appears and guns you all down")
            print ("YOU DIED")
            print ("TIP:Siding with the goblin never goes well")
            intro()
        if choice in answer_B:
            print ("------------------------------------------------------------")
            print ("You try to find help and come across Arthur Morgan")
            print ("He asks if you need a job and you accept")
            print ("END OF CHAPTER1.1 - THE NEW WORLD")
            import RedDead

def RejectGoblinDeal():
    print ("------------------------------------------------------------")
    print ("GOBLIN:But you cant do this to me")
    print ("The goblin attacks you but you manage to counter with a sweet uppercut")
    time.sleep(7)
    print ("You are still to weak to kill the goblin")
    print ("Spiderman swings in and helps you out")
    print ("Spiderman gets the goblin arrested and tells you to come with him")
    print ("You go with spiderman and end up at Stark tower")
    time.sleep(8)
    print ("You meet Tony Stark and he tells you he has something for you")
    time.sleep(7)
    print ("You get your very own version of an iron man suit")
    print ("END OF CHAPTER1.1:THE NEW WORLD")
    import ArmourWars


def SupriseGreenGoblin():
    print ("------------------------------------------------------------")
    print ("You try to use the element of suprise on Green Goblin so he gives you the element of death")
    print ("YOU DIED")
    print ("TIP:Your too weak to beat the green goblin")

def StrangeEncounter():
    print ("------------------------------------------------------------")
    print ("You run the opposite way and encounter doctor strange")
    print ("A:Challenge him B:Ask for help C:Stay with him")
    choice = input()
    if choice in answer_A:
        print ("------------------------------------------------------------")
        print ("You challenge doctor strange")
        if player.mana > 7:
            print ("You manage to defend yourself against Doctor Strange and he is impressed")
            time.sleep(5)
            print ("He sends you to Kamar-Taj and you get to train in Mystic Arts")
            print ("END OF CHAPTER1.1 - THE NEW WORLD")
        else:
            print ("Doctor Strange sends you through a portal and you are now tumbling down Mount Everest")
            print ("YOU DIED")
            print ("TIP:Why challange Doctor Strange with no magical skills")
    if choice in answer_B:
        print ("------------------------------------------------------------")
        print ("You ask Doctor Strange to help with getting the rock back")
        print ("DOCTOR STRANGE:'Look he is dead, now come with me'")
        print ("Doctor Strange then gets a idea and opens up a portal")
        time.sleep(5)
        print ("DWAYNE 'THE ROCK' JOHNSON steps out")
        print ("THE NARRATOR:'Thats the strongest version of the rock'")
        print ("THE NARRATOR:'His battles have caused some of this damage, he has universal power")
        print ("A white beam enters and OBSERVATION MAN appears")
        time.sleep(10)
        print ("OBSERVATION MAN, HP:9999999")
        print ("Press A to Attack")
        choice = input()
        if choice in answer_A:
            print ("------------------------------------------------------------")
            print ("You punch the eye, HP:9999998")
            time.sleep(3)
            print ("Doctor Strange attacks OBSERVATION MAN")
            print ("OBSERVATION MAN punches Doctor Strange into the sky, he creates a portal and gets the sneak attack on him")
            print ("You have realised his weakness")
            time.sleep(7)
            print ("THE NARRATOR;'LISTEN! You do not understand that Rock variants power'")
            print ("The narrator enters to help Observation man")
            print ("You shoot me with your gun")
            print ("I Die..")
            time.sleep(10)
            print ("my ability to narrate lives on but my soul has gone to a deeper place")
            print ("you do not know what you have now caused")
            print ("This new world has no control now")
            time.sleep(8)
            print ("THE NARRATOR:DEAD")
            player.body_count = player.body_count + 1
            print ("KILLS:" , player.body_count)
            time.sleep(3)
            print ("Dwayne Johnson has a gauntlet with a galactic amount of power")
            print ("He Smashes OBSERVATION MAN in the eye, it shows cracks and he falls onto his knees")
            time.sleep(5)
            print ("A meteor enters the atmosphere and its coming towards you")
            time.sleep(3)
            print ("As the flame approaches you can see a manly figure in the meteor")
            time.sleep(3)
            print ("It crashes into the ground")
            time.sleep(3)
            print ("DWAYNE:...")
            time.sleep(1)
            print ("DWAYNE: Is that..")
            time.sleep(2)
            print ("DWAYNE: Andy?")
            time.sleep(1)
            print ("Ultimate Andy enters the realm at the top of his powers")
            print ("He results to attacking DWAYNE")
            print ("You try to help, but he sends you into space and brings you back down")
            print ("At terminal velocity you crash into the ground")
            print ("You should be dead but Andy keeps you alive to uppercut you into a portal")
            time.sleep(7)
            print ("You are now on Mount Everest but you can see the fight happening through the portal")
            print ("Doctor Stranges power gets absorbed by Andy")
            time.sleep(5)
            print ("and his life...")
            time.sleep(4)
            print ("DOCTOR STRANGE:DEAD")
            print ("The portal closes...")
            print ("END OF CHAPTER 1.1:THE NEW WORLD")
        else:
            print ("He vapourises you")
            intro()

    if choice in answer_C:
        print ("------------------------------------------------------------")
        print ("You decide to stay with strange")
        print ("He takes you through a portal to London")
        print ("You go to a pub in London..")
        time.sleep(4)
        print ("Carnage and Venom are fighting in the pub")
        print ("You try to intervene but Carnage grabs hold of you")
        print ("You bite him and turn into your own symbiote and kill Carnage")
        print ("CARNAGE:DEAD")
        player.body_count = player.body_count + 1
        print ("KILLS:" ,player.body_count)
        time.sleep(7)
        print ("A:Kill Venom B:Team")
        choice = input()
        if choice in answer_A:
            print ("------------------------------------------------------------")
            print ("You kill venom and look to find Doctor Strange but he is nowhere to be seen")
            print ("VENOM:DEAD")
            player.body_count = player.body_count + 1
            print ("KILLS:" ,player.body_count)
            print ("END OF CHAPTER1.1: THE NEW WORLD")
        if choice in answer_B:
            print ("------------------------------------------------------------")
            print ("You tell Venom that we can be allies and he agrees")
            time.sleep(3)
            print ("Doctor Strange also wants to help you both in getting the evil out the city and any other CARNAGE that might be left")
            print ("END OF CHAPTER1.1:THE NEW WORLD")
        else:
            print ("VENOM eats you")
            intro()



intro()
