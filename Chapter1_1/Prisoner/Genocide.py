
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
required = ("\nUse only A, B, or C\n") 
import Character
import time


player = Character.prisoner
player.body_count == 4
player.char_lvl == 6

def intro():
    print ("After your murdering spree you rest in Kabul")
    time.sleep(10)
    print ("You wake up feeling refreshed and bloodthirsty")
    time.sleep(5)
    player.skill = 6 
    print ("YOU HAVE a SKILL POINT, WOULD YOU LIKE TO USE THEM. Y/N?")
    choice = input(">>")
    
    if choice in yes:
        print ("Type the name of the skill you would like to upgrade")
        print (player.stats)
        choice = input()
        if choice == "Health":
            HealthUpgrade()
        if choice == "Strength":
            StrengthUpgrade()
        if choice == "Speed":
            SpeedUpgrade()
        if choice == "Intelligence":
            IntelligenceUpgrade()
        if choice == "Charisma":
            CharismaUpgrade()
        if choice == "Stealth":
            StealthUpgrade()
        if choice == "Defense":
            DefenseUpgrade()
        if choice == "Mana":
            ManaUpgrade()

            
    if choice in no:
        NewWorldGeno()


def NewWorldGeno():
    print (player.stats)
    print ("In cold blood you kill a random pedestrian and take his map")
    time.sleep(3)
    print ("You read the map and get stuck between travelling:")
    time.sleep(5)
    print ("A:North B:South")
    choice = input()
    if choice in answer_A:
        NewWorldNorth()
    if choice in answer_B:
        NewWorldSouth()

def NewWorldNorth():
    print ("You go up north but get stopped by Boba Fett")
    time.sleep(6)
    print ("BOBA FETT: Theres a huge price on your head")
    player.bounty = 1000
    print ("BOUNTY: ",player.bounty, "Imperial Credits")
    time.sleep(5)
    print ("A:Challenge to DUEL B:FIGHT C:Attempt to payoff")
    choice = input(">>")
    if choice in answer_A:
        BobaDuel()
    if choice in answer_B:
        player.body_count = 4
        print ("------------------------------------------------------------")
        print ("You attempt to fight Boba Fett and end up nearly killing each other")
        time.sleep(7)
        print ("Darth Maul EMERGES")
        time.sleep(5)
        print ("Boba Fett shoots him killing him")
        time.sleep(2)
        print ("DARTH MAUL:DEAD")
        print ("You run to grab the lightsaber")
        time.sleep(9)
        print ("You use it and slice Boba Fetts Head off")
        time.sleep(2)
        print ("BOBA FETT:DEAD")
        player.body_count = player.body_count + 1
        print ("KILLS:" , player.body_count)
        player.bounty = player.bounty + 10000
        print ("BOUNTY: ",player.bounty, "Imperial Credits")
        time.sleep(7)
        print ("NARRATOR:'Your becoming a killer and i dont like it there is no saving you now")
        print ("A GIANT WITH A MASSIVE EYE SPAWNS")
        print ("You manage to defend yourself to the best of your ability")
        time.sleep(15)
        print ("But OBSERVATION MAN is a elder god so you are outmatched")
        time.sleep(9)
        print ("Due to the dark side of the lightsaber, DARTH VADER appears as he senses you are in trouble")
        time.sleep(10)
        print ("He does some damage but can not come out on top")
        time.sleep(6)
        print ("OBSERVATION MAN picks up Darth Vader and crushes him between his giant hands")
        time.sleep(10)
        print ("DARTH VADER:DEAD")
        print ("Spiderman appears and tries to web him down but he can see this coming and counters it by grabbing the web and slamming it into the ground crushing Spiderman")
        time.sleep(12)
        print ("SPIDERMAN:DEAD")
        print ("You attempt to run away but that comes to a quick end when OBSERVATION MAN grabs you")
        time.sleep(7)
        print ("Lightning hits the ground and RAIDEN appears")
        print ("OBSERVATION MAN uses his laser whilst Raiden uses his lightning")
        time.sleep(5)
        print ("DOCTOR STRANGE appears and sends you through a portal to safety")
        time.sleep(5)
        print ("You are now in a pub in London with Doctor Strange and Iron Man")
        time.sleep(10)
        print ("Using your lightsaber you continue your genocide killing them both")
        time.sleep(5)
        print ("DOCTOR STRANGE:DEAD")
        print ("IRON MAN:DEAD")
        player.body_count = player.body_count + 2
        print ("KILLS:" , player.body_count)
        time.sleep(10)
        print ("You exit the club and see a magician..")
        time.sleep(5)
        print ("He goes by the name Mike's Magic and asks if he can do a magic trick to which you accept")
        time.sleep(10)
        print ("He grabs a deck of cards")
        time.sleep(5)
        print ("You grab your lightsaber and put it through his eye")
        time.sleep(7)
        print ("MIKE'S MAGIC:DEAD")
        player.body_count = player.body_count + 1
        print ("KILLS:" , player.body_count)
        print ("You walk down the dark alleys of London looking for people to kill")
        print ("END OF CHAPTER 1.1:THE NEW WORLD")
    if choice in answer_C:
        print ("------------------------------------------------------------")
        print ("Charisma: ",player.charisma)
        if player.charisma > 6:
            print ("Boba Fett agrees to let you off if you do a bounty mission for him")
            time.sleep(5)
            print ("As he turns his back you shoot him in the had")
            time.sleep(3)
            print ("BOBA FETT:DEAD")
            print ("END OF CHAPTER 1.1:THE NEW WORLD")
        else:
            print ("Boba Fett shoots you in the leg")
            print ("Intelligence",player.intelligence)
            if player.intelligence > 8:
                print ("You allow Boba Fett to take you in ALIVE")
                print ("You get locked up in your cells and boba fett gets his payment")
                player.bounty = 0
                print ("BOUNTY",player.bounty)
                print ("Using your intellect you manage to escape and are now the most wanted man in NewWorld")
                print ("END OF CHAPTER1.1:NEW WORLD")
            else:
                print ("BobaFett kills you")
                time.sleep(5)
                intro()
        
def NewWorldSouth():
    print ("------------------------------------------------------------")
    print ("You go South and meet LAKAKA")
    print ("you shoot him with Cad Banes pistol but he eats it")
    print ("You decide to run")
    time.sleep(5)
    print ("You bump into captain america who fights LAKAKA to protect you")
    time.sleep(5)
    print ("LAKAKA eats his shield then eats him")
    print ("CAPTAIN AMERICA:DEAD")
    NewWorldNorth()
        

def BobaDuel():
    print ("------------------------------------------------------------")
    print ("(D)UEL")
    choice = input()
    if choice in DUEL:
        print ("Boba Fett stares you down")
        if player.speed > 7:
            print ("Boba Fett Shoots you")
            time.sleep(4)
            print ("But you shot him first and you barely escape with your life")
            time.sleep(9)
            print ("BOBA FETT: DEAD")
            player.bounty = player.bounty + 10000
            print ("BOUNTY: ",player.bounty, "Imperial Credits")
            print ("NARRATOR:'Your becoming a killer and i dont like it there is no saving you now")
            print ("A GIANT WITH A MASSIVE EYE SPAWNS")
            time.sleep(8)
            print ("OBSERVATION MAN HP:1000000000000000000000")
            print ("Press A to attack")
            choice = input()
            if choice in answer_A:
                print ("------------------------------------------------------------")
                print ("You try to fight OBSERVATION MAN but he knows what you are doing beforehand")
                print ("You stand no chance and get your arms ripped off")
                time.sleep(12)
                print ("He picks you up and starts punching you endlessly")
                print ("Press A for mercy B:Fight back")
                if choice in answer_A:
                    print ("------------------------------------------------------------")
                    print ("You beg for mercy but OBSERVATION MAN doesnt know what MERCY is")
                    time.sleep(7)
                    print ("The narrator intervenes and stops him")
                    print ("The narrator gives you a chance of redemption and wipes your memory and takes you to a brighter path")
                    time.sleep(11)
                    import NewWorld
                else:
                    print ("------------------------------------------------------------")
                    print ("OBSERVATION MAN uses his laser and kills you")
                    print ("YOU DIED")
                    print ("TIP:Dont try anything stupid against a elder god")
                    time.sleep(5)
                    intro()
                    
                    
            
            


def HealthUpgrade():
    player.stats['Health'] += 1
    player.health = player.health + 1
    print ("HEALTH UPGRADED")
    print ('Health:' ,player.health)
    NewWorldGeno()
    



def StrengthUpgrade():
    player.stats['Strength'] += 1
    player.strength = player.strength + 1
    print ("STRENGTH UPGRADED")
    print ('Strength:' ,player.strength)
    NewWorldGeno()

def SpeedUpgrade():
    player.stats['Speed'] += 1
    player.speed = player.speed + 1
    print ("SPEED UPGRADED")
    print ('Speed:' ,player.speed)
    NewWorldGeno()

def IntelligenceUpgrade():
    player.stats['Intelligence'] += 1
    player.intelligence = player.intelligence + 1
    print ("INTELLIGENCE UPGRADED")
    print ('Intelligence:' ,player.intelligence)
    NewWorldGeno()

def CharismaUpgrade():
    player.stats['Charisma'] += 1
    player.charisma = player.charisma + 1
    print ("CHARISMA UPGRADED")
    print ('Charisma:' ,player.charisma)
    NewWorldGeno()

def StealthUpgrade():
    player.stats['Stealth'] += 1
    player.stealth = player.stealth + 1
    print ("STEALTH UPGRADED")
    print ('Stealth:' ,player.stealth)
    NewWorldGeno()

def DefenseUpgrade():
    player.stats['Defense'] += 1
    player.defense = player.defense + 1
    print ("DEFENSE UPGRADED")
    print ('Defense:' ,player.defense)
    NewWorldGeno()

def ManaUpgrade():
    player.stats['Mana'] += 1
    player.mana = player.mana + 1
    print ("MANA UPGRADED")
    print ('Mana:' ,player.mana)
    NewWorldGeno()





intro()
