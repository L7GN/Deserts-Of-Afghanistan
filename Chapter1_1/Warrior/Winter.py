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
import random


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
        choice = input("Y/N")
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
    print ("There are three dark openings in the cave")
    print ("A:LEFT B:MIDDLE C:RIGHT")
    choice = input()
    if choice in answer_A:
        LeftCave()
    if choice in answer_B:
        MiddleCave()
    if choice in answer_C:
        RightCave()

def CaveTips():
    print ("You have entered the caves")
    print ("The caves are a scary part of the new world and are very dangerous to explore")
    print ("However you may reap many rewards")
    print ("Press A to continue")
    choice = input()
    if choice in answer_A:
        print ("The further you go in the caves the more difficult it gets")
        print ("There will be dark zones of caves where you can face very difficult bosses or very easy ones")
        print ("Finding a light zone will be a safe area to save and replenish to full health but they are not common")
        print ("Caves are a very difficult part of chapter 1 of the new world")
        time.sleep(13)
        print ("You will have to travel deep thoughout the caves in order to navigate a way out")
        print ("The deeper you go the more dangerous it is from enemies and the surrounding environment")
        print ("The caves of the new world have been reborn and enemies are taking shelter in them to prepare for future wars")
        print ("BE CAREFUL")
        time.sleep(15)
        
    else:
        CaveTips()

def LeftCave():
    CaveTips()
    print ("You go down the left and you are blinded in the darkness")
    time.sleep(4)
    print ("You hear a wooshing sound all around you and rumbles in the distance")
    time.sleep(5)
    print ("You see a torch held by a skeleton, Do you grab it?")
    print ("TIP: Taking the torch may allow you to see but will also make you more vulnerable to attacks.. think carefully")
    choice = input("Y/N")
    if choice in yes:
        torch = True
        print ("You pick up the torch")
    if choice in no:
        torch = False
    print ("You carry on")
    if torch == False:
        print ("The darkness swallows you and you are blind you get stabbed")
        print ("YOU DIED")
        print ("TIP:You are in a cave why would you not take a torch")
    else:
        print ("You are walking along a wooden bridge and hear a sound from above")
        time.sleep(5)
        print ("You quickly grab a sword and prepare")
        sword = True
        time.sleep(4)
        print ("A skeleton drops from above")
        print ("It chases you")
        time.sleep(5)
        print ("You use the sword to strike at it making it collapse to bones")
        print ("The skeletons armour is on the ground do you pick it up")
        choice = input("Y/N")
        if choice in yes:
            print ("You wear the armour")
            SkeleArmour = True
        if choice in no:
            SkeleArmour = False
        print ("You cross the bridge and see bloodstains on the walls and floor")
        print ("You carry on into a DARK ZONE")
        time.sleep(10)
        print ("You see a random  survivor he runs and asks for help")
        print ("A: Kill him B: Help C:Ignore")
        choice = input(">>")
        if choice in answer_A:
            print ("You behead the survivor")
            player.body_count = player.body_count + 1
            print ("KILLS: ",player.body_count)
            Survivor = False
        if choice in answer_B:
            print ("Survivor: Help! Help!")
            time.sleep(3)
            print ("Survivor: I have been stuck down here for weeks, what has happened to the world")
            time.sleep(7)
            print ("The survivor accompanies you")
            Survivor = True
        if choice in answer_C:
            print ("Survivor: Help! Help!")
            time.sleep(3)
            print ("Survivor: I have been stuck down here for weeks, what has happened to the world")
            time.sleep(7)
            print ("You ignore him and he begs on the ground")
            Survivor = False
        print ("You carry on..")
        time.sleep(5)
        print ("A massive figure comes from the shadows")
        time.sleep(5)
        print ("A rotting corpse of osiris challenges you")
        print ("He has really become one with the dead")
        time.sleep(10)
        print ("He swings his crook and flail and charges towards you")
        time.sleep(5)
        print ("You stab him in the stomach with your sword and go for a second strike")
        time.sleep(6)
        print ("Osiris kicks you down and you roll and grab your sword")
        time.sleep(5)
        if Survivor == True:
            print ("Osiris goes to srike you but the random survivor jumps in the way and gets killed")
            time.sleep(8)
            print ("You use this time to cut Osiris' arm off")
            time.sleep(3)
            print ("You sprint into the darkness and find a ladder and go down the ladder")
            time.sleep(6)
        else:
            print ("You try to defend from Osiris and you leave a few cuts on Osiris but he batters you")
            time.sleep(5)
            print ("You are on the ground with double vision... defeated")
            time.sleep(5)
            print ("You look up and cannot see anyone")
            time.sleep(5)
            print ("You see ladders and crawl towards them")
            time.sleep(5)
            print ("You are too weak to climb down and instead fall down them")
            time.sleep(6)
            print ("The fall kills you")
            print ("YOU DIED")
            time.sleep(5)
            Caveexplore()
        print ("You are heading deeper into the dark zone")
        HP = 100
        LeftCaveOpening()


def generate_random():
    new_rand = random.randint(0,8)
    return new_rand


new_number = generate_random()

def generate_random2():
    new_rand = random.randint(0,13)
    return new_rand


new_number2 = generate_random2()


def Enemy_Attack():
    new_rand = random.randint(0,3)
    return new_rand

Attack = Enemy_Attack()


def LeftCaveOpening():
    print ("You go left..")
    print ("You have your sword ready and the torch to lead your way")
    time.sleep(7)
    Scene = random.randint(0,8)
    environments = ["Wasteland" , "Desert", "Snowy" , "Volcano" , "Hell" , "Swamp", "Bliss", "Rocky" , "YetiHome"]
    Biome = (environments[Scene])
    YetiThrone = False
    if Biome == "Wasteland":
        print ("You are in a wasteland with bones spread everywhere")
    if Biome == "Desert":
        print ("Your feet get buried in the sand everytime you take a step")
        time.sleep(5)
        print ("The temperature inside is rising")
    if Biome == "Snowy":
        print ("Ice spikes point down on you from the ceiling")
        time.sleep(5)
        print ("You are beginning to freeze")
    if Biome == "Volcano":
        print ("Lava flows around you and you can hear rumbles in the distance")
    if Biome == "Hell":
        print ("The temperatures are extremely hot with heads of demons and devils everywhere")
    if Biome == "Swamp":
        print ("You step in murky water and find it hard to travel through the swamps")
    if Biome == "Bliss":
        print ("You can see glows and mysterious particles floating around glowing mushrooms light your path")
    if Biome == "Rocky":
        print ("You make your way throuh the hard rocky terrain")
    if Biome == "YetiHome":
        print ("You are beginning to get frostbite from the extreme cold")
        YetiThrone = True
        time.sleep(5)
        print ("You see paintings of a Yeti with a crown")
        time.sleep(3)
        print ("You have entered the Rulers home")
        time.sleep(8)
        print ("You see doctor stranges corpse on a rock")
        time.sleep(4)
    Boss = random.randint(0,10)
    Enemy = ["Black Knight", "Begger", "Hunter", "Swordsman", "Skeleton King", "Demon", "Demon King", "Vampire","Orc", "Ogre", "Yeti",]
    Opponent = (Enemy[Boss])
    if Opponent == "Yeti":
        print ("You spot a yeti eating the corpses of survivors")
        time.sleep(5)
        print ("It turns over to you and you ready your sword")
        if YetiThrone == True:
            print ("You face the ruler of everest")
            YetiKing = 1000
            HP = 100
            while YetiKing > 0:
                print ("Ruler of Everest: " ,YetiKing)
                print ("HP: " , HP)
                Skill = random.randint(0,5)
                Moveset = ["Claw","Bite","Icicle Throw","Blizzard", "Ice Sword", "Freeze"]
                Move = (Moveset[Skill])
                print ("The King of Everest uses his" , Move , "Move")
                if Move == "Claw":
                    print ("The Yeti uses his claws")
                    if player.defense > 5:
                        Damage = random.randint(5,40)
                        HP = HP - Damage
                    if player.defense < 5:
                        Damage = random.randint(1,20)
                        HP = HP - Damage
                if Move == "Bite":
                    print ("The King of Everest bites")
                    Damage = random.randint(15,35)
                    HP = HP - Damage
                if Move == "Icicle throw":
                    print ("With the freezing temperatures of the cave the king creates a icicle and throws it at you")
                    Damage = random.randint(40,60)
                    HP = HP -Damage
                if Move == "Blizzard":
                    print ("The ruler of everest creates a blizzard in the room")
                    Damage = random.randint(10,25)
                    HP = HP - Damage
                if Move == "Ice Sword":
                    print ("With the freezing temperatures the Yeti King forges his sword and slices it through you")
                    Damage = random.randint(50,90)
                    HP = HP - Damage
                if Move ==  "Freeze":
                    print ("The yeti freezes you")
                    Damage = random.randint(1,12)
                    HP = HP - Damage
                print ("A: Sword B: Magic")
                choice = input()
                if choice in answer_A:
                    print ("You use your sword and can get a good cut")
                    Offense = random.randint(20,50)
                    YetiKing = YetiKing - Offense
                if choice in answer_B:
                    if player.mana > 6:
                        print ("You use a fireball spell dealing immense damage")
                        Offense = random.randint(250,500)
                        YetiKing = YetiKing - Offense
                    else:
                        print ("You know no magic")
                else:
                    print ("You choose to do nothing")

                if HP < 0:
                    print ("YOU DIED")
                    time.sleep(3)
                    Caveexplore()
            print ("You have killed the ruler of everest")
            
                    
                    
                
        else:
            print ("You face the YETI")
            Yeti = 100
            HP = 100
            while Yeti > 0:
                Skill = random.randint(0,3)
                print ("Yeti: " , Yeti)
                print ("HP ", HP)
                Moveset = ["Claw","Bite","Icicle Throw","Blizzard"]
                Move = (Moveset[Skill])
                print ("The Yeti uses his" , Move , "Move")
                if Move == "Claw":
                    print ("The Yeti uses his claws")
                    if player.defense > 5:
                        Damage = random.randint(10,20)
                        HP = HP - Damage
                    if player.defense < 5:
                        Damage = random.randint(1,20)
                        HP = HP - Damage
                if Move == "Bite":
                    print ("The  yeti bites")
                    Damage = random.randint(15,35)
                    HP = HP - Damage
                if Move == "Icicle throw":
                    print ("With the freezing temperatures of the cave the yeti creates a icicle and throws it at you")
                    Damage = random.randint(40,60)
                    HP = HP -Damage
                if Move == "Blizzard":
                    print ("The yeti creates a blizzard in the room")
                    Damage = random.randint(10,25)
                    HP = HP - Damage
                print ("A: Sword B: Magic")
                choice = input()
                if choice in answer_A:
                    print ("You use your sword and can get a good cut")
                    Offense = random.randint(20,50)
                    Yeti = Yeti - Offense
                if choice in answer_B:
                    if player.mana > 6:
                        print ("You use a fireball spell dealing immense damage")
                        Offense = random.randint(250,500)
                        Yeti = Yeti - Offense
                    else:
                        print ("You know no magic")
                else:
                    print ("You choose to do nothing")

                if HP < 0:
                    print ("YOU DIED")
                    time.sleep(3)
                    Caveexplore()
            print ("You have killed the yeti")
    
    if Opponent == "Black Knight":
        BlackKnightHP = 200
        HP = 100
        while BlackKnightHP > 0:
            Skill = random.randint(0,3)
            Moveset = ["Dark Magic","Shield Attack","Shield Throw","Sword strike"]
            Move = (Moveset[Skill])
            print ("The black Knight uses his" , Move , "Move")
            if Move == "Dark Magic":
                print ("The Black Knight uses his darkness to emit a magical spell")
                if player.defense > 5:
                    Damage = random.randint(5,40)
                    HP = HP - Damage
                if player.defense < 5:
                    Damage = random.randint(1,20)
                    HP = HP - Damage
                if player.mana > 10:
                    print ("You absorb the magic")
            if Move == "Shield Attack":
                print ("The Black Knight bashes his shield at you")
                Damage = random.randint(5,10)
                HP = HP - Damage  
            if Move == "Shield Throw":
                print ("The Black Knight throws his shield at you and replaces his shield with a shadow shield")
                Damage = random.randint(10,20)
                HP = HP - Damage
            if Move == "Sword Strike":
                print ("The Black Knight swings his sword at you")
                if player.defense > 5:
                    Damage = random.randint(10,40)
                    HP = HP - Damage
                if player.defense < 5:
                    Damage = random.randint(5,20)
                    HP = HP - Damage
                if player.speed > 6:
                    print ("You dodge the attack")
            print ("Black Knight Health: ",BlackKnightHP)
            print ("Health:", HP)
            print ("A:Fight B: Surrender")
            choice = input(">>")
            if choice in answer_A:
                print ("A:Sword B: Magic")
                choice = input(">>")
                if choice in answer_A:
                    if player.strength > 7:
                        print ("You swing your sword powerfully")
                        Offense = random.randint(25,70)
                        BlackKnightHP = BlackKnightHP - Offense
                    else:
                        Offense = random.randint(10,40)
                        BlackKnightHP = BlackKnightHP - Offense
                if choice in answer_B:
                    if player.mana == 7:
                        print ("You emit a magical spell")
                        Offense = random.randint(50,150)
                        BlackKnightHP = BlackKnightHP - Offense
                    else:
                        print ("Your not magical")
            if HP < 0:
                print ("You died")
                time.sleep(3)
                Caveexplore()
        print ("You killed the black knight")
        
    if Opponent == "Begger":
        print ("You come across a begger")
        time.sleep(3)
        print ("The choice is yours")
        print ("A:KIll him B:Help C:Use as bait")
        choice = input(">>")
        if choice in answer_A:
            print ("You stab the begger in the heart with your sword")
            player.body_count = player.body_count + 1
            print ("KILLS: " , player.body_count)
            print ("You carry on in the dark zone")
        if choice in answer_B:
            print ("You offer the begger your hand")
            time.sleep(5)
            print ("He takes it too literally and tries to take your hand off")
            time.sleep(3)
            print ("Oh wait he just wants to kill you")
            time.sleep(10)
            print ("You cut through his body splitting him in two")
            player.body_count = player.body_count + 1
            print ("KILLS: " , player.body_count)
        if choice in answer_C:
            print ("You attempt to use the begger as bait")
            time.sleep(5)
            print ("Wolves arrive and eat him with them disracted you make a run")
            time.sleep(5)
    
    if Opponent == "Hunter":
        print ("You are walking around then hear a woosh")
        time.sleep(4)
        print ("A arrow zooms past you and you see a man in a hood with a bow looking at you")
        if player.speed > 8:
            print ("You are too fast for his arrows and manage to pounce at him and stab your sword in the heart")
            time.sleep(10)
            player.body_count = player.body_count + 1
            print ("KILLS: ",player.body_count)
        else:
            print ("You get shot by a arrow that is poison tipped")
            time.sleep(5)
            print ("You crawl along the floor before a dagger enters your head")
            time.sleep(5)
            print ("YOU DIED")
            print ("TIP: You need to be FAST against Hunters")
            Caveexplore()
            
    if Opponent == "Swordsman":
        print ("You see a man juggling a sword in each hand he spots you and stops")
        time.sleep(6)
        print ("He sees you and charges you down")
        SwordsManShield = 100
        HP = 100
        SwordsManHealth = 150
        while SwordsManShield > 0:
            print ("SwordsMan of Everest Health: ",SwordsManShield)
            print ("Health:", HP)
            print ("A:Fight B: Surrender")
            choice = input()
            if choice in answer_A:
                print ("A:Sword B: Magic")
            choice = input(">>")
            if choice in answer_A:
                if player.strength > 7:
                    print ("You swing your sword powerfully")
                    Offense = random.randint(25,70)
                    SwordsManShield = SwordsManShield - Offense
                else:
                    Offense = random.randint(10,40)
                    SwordsManShield = SwordsManShield - Offense
            if choice in answer_B:
                if player.mana == 7:
                    print ("You emit a magical spell")
                    Offense = random.randint(50,150)
                    SwordsManShield = SwordsManShield - Offense
                else:
                    print ("Your not magical")
            print ("SwordsMan sharpens his swords")
            if HP < 0:
                print ("You died")
                time.sleep(3)
                Caveexplore()
        print ("The SwordsMan looks wounded but then he gets ice armour and a ice sword")
        time.sleep(7)
        print ("The SwordsMan is a man of ice")
        time.sleep(3)
        print ("He throws his sword at you")
        time.sleep(4)
        print ("You duck")
        time.sleep(3)
        print ("He screams at you")
        time.sleep(3)
        print ("You go again..")
        time.sleep(2)
        print ("He turns the room to ice slowing you down")
        player.speed = 0
        SwordsManSpeed = 10
        if SwordsManSpeed > player.speed:
            print ("He throws one of his swords at you")
            print ("You dodge it")
            while SwordsManHealth > 0:
                NextMove = random.randint(0,3)
                Moves = ["Ice Shield", "Blizzard", "Ice Blast" , "Ice Sword"]
                Attack = (Moves[NextMove])
                if Attack == "Ice Shield":
                    print ("The SwordsMan gets his shield ready")
                if Attack == "Blizzard":
                    print ("The SwordsMan sends a blizard your way")
                    Damage = random.randint(25,100)
                    HP = HP - Damage
                if Attack == "Ice Blast":
                    print ("The SwordsMan creates a massive ball of ice and blasts it towards you")
                    Damage = random.randint(50,99)
                    HP = HP - Damage
                    if player.mana > 8:
                        Damage = 0
                        HP = HP - Damage
                if Attack == "Ice Sword":
                    print ("The Master SwordsMan uses his ice sword")
                    Damage = random.randint(75,100)
                    HP = HP - Damage
                print ("SwordsMan of Everest" , SwordsManHealth)
                print ("HP: ", HP)
                print ("A: Sword B: Magic")
                choice = input(">>")
                if choice in answer_A:
                    print ("You swing your sword")
                    Offense = random.randint(20,70)
                    SwordsManHealth = SwordsManHealth - Offense
                if choice in answer_B:
                    if player.mana > 8:
                        print ("You use your magic")
                        Offense = random.randint(70,120)
                        SwordsManHealth = SwordsManHealth - Offense
                    else:
                        print ("You dont know magic")
                        time.sleep(3)
                        print ("But your torch does")
                        time.sleep(2)
                        print ("It emits a fire ball")
                        Offense = random.randint(50,80)
                        SwordsManHealth = SwordsManHealth - Offense
                

                if HP < 0:
                    print ("YOU DIED")
                    print ("TIP: Magic is good against mythical creatures")
                    time.sleep(5)
                    Caveexplore()
            print ("You have killed the swordsman of everest")
    
    if Opponent == "Skeleton King":
        print ("You are walking through the cave and a massive skeletal structure breaks through the ground")
        time.sleep(7)
        print ("ITS THE SKELETON KING")
        time.sleep(3)
        print ("Skeletons start rising through the ground")
        time.sleep(5)
        print ("You fight them off and now face the ultimate challenge")
        print ("He throws a bone at you")
        time.sleep(3)
        print ("You jump over it and cut through the king")
        print ("A: CHALLENGE B: RUN C:HELP D:DUEL")
        choice = input(">>")
        if choice in answer_A:
            print ("You challenge the KING")
            print ("---FIGHTING STYLES---")
            print ("A: Counter: Speed B:Aggressive: Strength")
            choice = input(">>")
            if choice in answer_A:
                if player.speed == 10:
                    print ("You counter his attacks and dethrone the king")
                    print ("SKELETON KING:DEAD")
                else:
                    print ("You try to counter but are unable to do so and die")
                    Caveexplore()
            if choice in answer_B:
                print ("You try to be aggressive and get your spine taken out your body")
                time.sleep(7)
                print ("YOU DIED")
                Caveexplore()
        if choice in answer_B:
            print ("You go to run away but bones get dropped onto you crushing you")
            time.sleep(7)
            print ("YOU DIED")
            Caveexplore()
        if choice in answer_C:
            print ("You ask the king for help and he snaps your neck")
            time.sleep(5)
            Caveexplore()
        if choice in DUEL:
            print ("You ask for a duel and skeletons grab you and drag you to hell")
            time.sleep(5)
            Caveexplore()
    if Opponent == "Demon":
        print ("You encounter a demon")
        DemonHP = 66
        HP = 100
        
        while DemonHP > 0:
            print ("DEMON: ",DemonHP)
            print ("HP: ", HP)
            print ("Press A to attack")
            choice = input()
            if choice in answer_A:
                print ("You slice with your sword")
                Damage = random.randint (10,25)
                DemonHP = DemonHP - Damage
            else:
                print ("You do nothing")
            print ("The demon attacks you with its claws")
            Attack = random.randint (15,45)
            HP = HP - Attack
            


            if HP < 0:
                print ("YOU DIED")
                time.sleep(3)
                Caveexplore()
        print ("You killed the demon")
    if Opponent == "Demon King":
        print ("You see a large shadow cast on a wall")
        time.sleep(5)
        print ("A massive demon stares down at you, chains wrapped around its body")
        time.sleep(7)
        print ("good luck..")
        time.sleep(3)
        print ("You run towards a bag")
        bag = ["Potions" ,"DemonSlayer", "Coin" , "Stick" , "Rock", "Ring", "Cloak"]
        pick = random.randint(0,6)
        Items = (bag[pick])
        if Items == "Potions":
            print ("you pick up potions")
            Potion = True
            Potions = 7
        if Items == "DemonSlayer":
            print ("You pick up the DemonSlayer Sword")
            Demonslayer = True
        if Items == "Coin":
            print ("You pick up a coin...")
            coin = True
        if Items == "Stick":
            print ("You pick up a stick")
            Stick = True
        if Items == "Rock":
            print ("You pick up a Rock")
        if Items == "Ring":
            print ("You pick up a ring and feel eternal power run through your entire body")
            Ring = True
        if Items == "Cloak":
            print ("You pick up a cloak and wear it")
            time.sleep(3)
            print ("A strange power runs through you")
            Cloak = True
        print ("You must now decide your fate")
        DemonKingHP = 666
        HP = 100
        if Cloak == True:
            HP = 666
        if Ring == True:
            HP = 1000
        while DemonKingHP > 0:
            print ("You feel you could be facing your end...")
            print ("Demon King " , DemonKingHP)
            print ("HP", HP)
            print ("A: ATTACK B: ITEMS")
            choice = input(">>")
            if choice in answer_A:
                if Ring == True:
                    print ("A:Sword B:Wraith Attack C: Double Team")
                    choice = input(">>")
                    if choice in answer_A:
                        print ("You use your sword")
                        Damage = random.randint(20,100)
                        DemonKingHP = DemonKingHP - Damage
                    if choice in answer_B:
                        print ("You use the ring and the wraith of the bright lord attacks the demon king and you use your sword")
                        Damage = random.randint(100,177)
                        DemonKingHP = DemonKingHP - Damage
                    if choice in answer_C:
                        print ("You summon your wraith and double team the DEMON KING")
                        Damage = random.randint(10,30)
                        DemonKingHP = DemonKingHP - Damage
                if  Cloak == True:
                    print ("A:Shadow Sword B:Wraith Attack C: Shadow Ball")
                    choice = input(">>")
                    if choice in answer_A:
                        print ("You use your sword and the darkness within the cloak summons a shadow sword to attack with ")
                        Damage = random.randint(50,100)
                        DemonKingHP = DemonKingHP - Damage
                    if choice in answer_B:
                        print ("You use the cloak and a shadow attacks the demon king invisible to him")
                        Damage = random.randint(100,200)
                        DemonKingHP = DemonKingHP - Damage
                    if choice in answer_C:
                        print ("You use the darkness from within the cloak to create a shadow ball and throw it at the demon king")
                        Damage = random.randint(10,30)
                        DemonKingHP = DemonKingHP - Damage
                if Demonslayer == True:
                    print ("A:DemonSword B: Dark Laser C: Summon")
                    choice = input(">>")
                    if choice in answer_A:
                        print ("You use your demon slayer sword and leave a massive wound on the king")
                        Damage = random.randint(250,400)
                        DemonKingHP = DemonKingHP - Damage
                    if choice in answer_B:
                        print ("You use the demonslayer sword to emit a dark laser")
                        Damage = random.randint(100,200)
                        DemonKingHP = DemonKingHP - Damage
                    if choice in answer_C:
                        print ("You summon a shadow that was once the wielder of the sword he helps you attack")
                        Damage = random.randint(300,370)
                        DemonKingHP = DemonKingHP - Damage
                if choice in answer_B:
                    if Potion == True:
                        print ("A: Potions")
                        choice = input(">>")
                        if choice in answer_A:
                            print ("You use a potion")
                            HP = 100
                            Potions = Potions - 1
                            if Potions == 0:
                                Potion = False
                        else:
                            print (required)
                            print ("You choose to do nothing")
                    if Coin == True:
                        print ("A: Coin")
                        choice = input()
                        if choice in answer_A:
                            print ("You flick the coin and nothing happens")
                            time.sleep(7)
                            print ("Giant Mario appears and smashes through the KING")
                            DemonKingHP = DemonKingHP - 100
                        else:
                            print ("You choose to do nothing")

            
            print ("The Demon King swings his sword swiftly towards you")
            time.sleep(5)
            Offense =  random.randint(25,50)
            HP = HP - Offense
            if HP < 0:
                print ("YOU DIED")
                time.sleep(3)
                Caveexplore()

        print ("The Demon king drops on one knee and the looks up to see you in victory")
        time.sleep(8)
        print ("He doesnt like the idea of losing and bursts into flames")
        time.sleep(5)
        print ("You now face the Burning Demon King")
        BurningDemonKing = 150
        print ("A: FIGHT B: RUN")
        choice = input()
        if choice in answer_A:
            print ("You aim to finish what you started")
            time.sleep(3)
            print ("Against a god of fire..")
            time.sleep(6)
            print ("He throws his burning chain at you and it wraps around you and burns you")
            time.sleep(7)
            print ("You try to break free but are useless and get cut in half")
            time.sleep(5)
            print ("YOU DIED")
            time.sleep(3)
            Caveexplore()
        if choice in answer_B:
            print ("You try to run away")
            time.sleep(5)
            print ("Mount Everest is melting because of the demon")
            time.sleep(5)
            print ("You jump through a crack in the cave and escape")
        else:
            print ("YOU DID NOTHING AND DIED")
            Caveexplore()
        
        
    if Opponent == "Vampire":
        print ("You encounter the Vampire")
        time.sleep(3)
        print ("It pulls out a dagger and runs after you")
        time.sleep(4)
        print ("You have the advantage with the sword and cut the vampires hand off")
        time.sleep(6)
        print("You can: A: Execute B: Try to cure")
        choice = input()
        if choice in answer_A:
            print ("You cut the Vampires head clean off")
            player.body_count = player.body_count + 1
            print ("KILLS: ",player.body_count)
        if choice in answer_B:
            print ("You go to cure the vampire")
            if player.mana > 9:
                print ("You manage to cure the vampire and turn them into a normal human they thank you and run away")
            else:
                print ("Your magic doesnt work and more vampires arrive and devour you")
                time.sleep(6)
                print ("YOU DIED")
                time.sleep(3)
                Caveexplore()
    if Opponent == "Orc":
        if player.speed > 6:
            print ("You swing your sword and stab your sword straight through the orc")
            player.body_count = player.body_count + 1
            print ("KILLS: " , player.body_count)
        else:
            print ("You come across a orc")
            time.sleep(4)
            print ("You swing your sword and he parries and stabs you in the gut")
            time.sleep(5)
            print ("A gang of orcs appear and with you injured")
            time.sleep(4)
            print ("you struggle...")
            print ("YOU DIED")
            Caveexplore()
    if Opponent == "Ogre":
        print ("You see an ogre wielding a mace")
        if player.strength > 7:
            print ("You stab your sword and get it stuck in the ogres stomach")
            print ("You must now fight without a sword")
            time.sleep(10)
            print ("The ogre goes to smash you with a mace but you manage to hold him back with your strength")
            time.sleep(8)
            print ("You quickly grab your sword and slam it straight up through the ogres head")
            time.sleep(9)
            player.body_count = player.body_count + 1
            print ("KILLS: " , player.body_count)
        else:
            print ("The ogre picks your weak body up and tears you in half")
            time.sleep(5)
            print ("YOU DIED")
            time.sleep(3)
            Caveeplore()
    print ("After running for your life you fall through a crack in your wall into a bright room")
    print ("You have escaped the first DARK ZONE and now enter a light zone")
    time.sleep(15)
    HP = 100
    print ("HP RECOVERED")
    print ("HP: ", HP)
    time.sleep(5)
    print ("You move on and see a few orcs and can dispatch of them with no problems after being refreshed")
    player.body_count = player.body_count + 3
    print ("KILLS: ", player.body_count)
    time.sleep(11)
    print ("You see paintings of observation man on the wall and a shard of looks to be armour underneath")
    print ("You pick it up and a power fills within you")
    time.sleep(14)
    print ("A wraith of the narrator appears")
    time.sleep(4)
    print ("NARRATOR: So you have chose to bring me back")
    time.sleep(3)
    print ("NARRATOR: But as a shadow...")
    time.sleep(2)
    print ("NARRATOR: Well, i think we all deserve a last chance")
    time.sleep(6)
    print ("NARRATOR: I am proud you have made it this long without my help")
    print ("You move ahead...")
    time.sleep(8)
    print ("NARRATOR: Rifts seem to be opening everywhere")
    time.sleep(5)
    print ("NARRATOR: BEWARE! There is a dangerous man ahead")
    time.sleep(7)
    print ("NARRATOR: With nowhere else to go. You have to go ahead")
    time.sleep(8)
    print ("You encounter Sauron, the dark lord")
    time.sleep(5)
    print ("It seems like he is planning to conquer the lands")
    time.sleep(7)
    print ("You confront him and challenge him confidently")
    time.sleep(5)
    print ("You hear a massive bang and see a purple portal and outsteps general grievous")
    time.sleep(7)
    print ("He faces off with Sauron and gets destroyed")
    time.sleep(5)
    print ("Sauron cuts him limb for limb until there is nothing left")
    time.sleep(8)
    print ("General Grievous: DEAD")
    time.sleep(3)
    print ("Sauron is beginning his siege of Nepal but it seems like people are looking to defend it")
    time.sleep(10)
    print ("Knowing you do not hold enough power to take him down you run and hide")
    time.sleep(7)
    print ("You have to watch the war happen")
    BattleOfNepal()


def BattleOfNepal():
    print ("CHAPTER 1.2.2: The battle of Nepal")
    time.sleep(4)
    print ("NARRATOR: We stand here today useless and incapable of the destruction that is to come")
    time.sleep(6)
    print ("NARRATOR: But we may aswell stay to see a glorious battle")
    time.sleep(5)
    print ("Saurons armies have built up all over the himalayas and are ready to draw the first blood in the war")
    time.sleep(11)
    print ("I mean.. who else was you expecting it to be...")
    time.sleep(5)
    print ("In the town of Arkhale, the avengers are seen to be protecting the town")
    time.sleep(6)
    print ("A horn is sounded to fill the silence and the warcries can be heard from the charging orcs")
    time.sleep(8)
    print ("Volunteers from Nepal also join in the defence and charge towards them for their country")
    time.sleep(8)
    print ("The orcs can kill them with ease and progress towards the avengers")
    time.sleep(6)
    print ("Sauron watches as hulk smashes through his forces")
    time.sleep(5)
    print ("The hulk is outnumbered and cannot recover from the amount of orcs stabbing him from all over and falls...")
    time.sleep(8)
    print ("He gets back up but is met by a olog who rips his head off")
    time.sleep(6)
    print ("HULK:DEAD")
    time.sleep(2)
    print ("The avengers are swarmed and taken apart by the orcs because of their numbers")
    time.sleep(6)
    print ("Saurons armies are stong and are looking to take Nepal with ease")
    time.sleep(8)
    print ("A rift opens and stormtroopers storm the battlefield")
    time.sleep(3)
    print ("Vader appears and has a staredown with Sauron")
    time.sleep(8)
    print ("Vader fights his way up towards mount everest killing hundreds of orcs on his way out of rage")
    time.sleep(9)
    print ("He faces a olog but using the force flings him off the mountain killing it")
    time.sleep(7)
    print ("Vader and Sauron begin a fight of the ages, the fight for Nepal")
    time.sleep(6)
    print ("THE FIGHT OF THE DARK LORDS")
    time.sleep(7)
    print ("Sauron blocks and tries to counter Vaders swings with the lightsaber")
    time.sleep(5)
    print ("Sauron punches vader to the ground and goes to smack him with the mace")
    time.sleep(6)
    print ("Vader uses the force to keep Sauron from crushing his skull with the mace")
    time.sleep(7)
    print ("Sauron tilts his head knowing Vader cant hold him here forever")
    time.sleep(5)
    print ("Meanwhile, The Storm troopers are wiping out the orcs but they still have the numbers advantage")
    time.sleep(6)
    print ("Vader lets go and Sauron smashes him with his mace and grabs him by the throat")
    time.sleep(7)
    print ("Sauron uses his one ring to break Vader and to try to get him to submit to the true dark lord")
    time.sleep(7)
    print ("Sauron with vader broken and on his kness smashes his skull with his mace")
    time.sleep(5)
    print ("Again..")
    time.sleep(2)
    print ("Again..")
    time.sleep(2)
    print ("and Again...")
    time.sleep(3)
    print ("Darth Vader has been defeated by Sauron")
    time.sleep(3)
    print ("His power reigns supreme over him and he continues his conquest")
    time.sleep(5)
    print ("Captain America rises and helps the clone troopers in fighting the orcs")
    time.sleep(6)
    print ("Vader rises and Sauron orders him to join him")
    time.sleep(4)
    print ("The clone troopers switch and shoot at Captain America")
    time.sleep(4)
    print ("Captain America protects himself with his shield from the blasts")
    time.sleep(5)
    print ("He forgets about the orcs and gets stabbed from behind")
    time.sleep(6)
    print ("CAPTAIN AMERICA:DEAD")
    time.sleep(2)
    print ("Hawkeye tries to run but gets picked up by a olog")
    time.sleep(3)
    print ("The olog hangs him upside down and then squeezes and twists him around causing him to scream in agony")
    time.sleep(8)
    print ("HAWKEYE:DEAD")
    time.sleep(3)
    print ("The troopers and orcs storm Arkhale")
    time.sleep(5)
    print ("They take control of the town in ease and you watch as the armies march towards the other towns of Nepal")
    time.sleep(7)
    print ("A rift portal opens which looks like the country of Calradia")
    time.sleep(5)
    print ("Swadian Horses stampede through the portal and you see King Harlaus emerge with his Swadian Banner on his horse")
    time.sleep(8)
    print ("King Harlaus gets off his horse and faces Sauron to rule the town of Arkhale")
    time.sleep(5)
    print ("Harlaus uses his shield to block Saurons mace then slices through Saurons gut wounding him")
    time.sleep(7)
    print ("Sauron looks with rage and swings his mace powerfully five times shattering his shield")
    time.sleep(8)
    print ("Harlaus parries for survival and stabs Sauron in the chest")
    time.sleep(4)
    print ("Sauron looks to see his orc army all dead in Arkhale and the Swadian horses chasing down the rest")
    time.sleep(6)
    print ("Harlaus has beat Sauron at his game but now has to defeat him")
    time.sleep(8)
    print ("Harlaus circles around Sauron..")
    time.sleep(3)
    print ("Harlaus lunges and gets his jaw broke by Saurons mace")
    time.sleep(5)
    print ("The wounded Sauron wants to finish him but he decides to leave him and teleports away")
    time.sleep(6)
    print ("Vader breaks away from Saurons magic gaining his sanity again")
    time.sleep(5)
    print ("Vader knowing the cost of his defeat walks away miserably")
    time.sleep(5)
    print ("King Harlaus gets back up and rides his horse into Arkhale")
    time.sleep(6)
    print ("You walk down to Arkhale and look at the damage that has been done")
    time.sleep(6)
    print ("King Harlaus: Traveller!!")
    time.sleep(3)
    print ("King Harlaus: Would you care to join me and the Kingdom Of Swadia in conquering this realm?")
    choice = input("Y/N")
    if choice in yes:
        print ("You accept his offer and join up with Harlaus")
        time.sleep(4)
        print ("He tells you to get some rest and you do so")
        print ("END OF CHAPTER 1.2")
        import SecondShot
    if choice in no:
        print ("King Harlaus: Very well then.")
        time.sleep(2)
        print ("King Harlaus: You have until dark to leave this town")
        time.sleep(4)
        print ("King Harlaus: I will see you around..")
        time.sleep(3)
        print ("You get your rucksack ready and walk down the roads")
        print ("END OF CHAPTER 1,2")
        import TheDarkLords
    
    
    
    
    
    
    
    
    
    
    
        
        
            
            
        
    
        


        
            
            
        
        
    
    
            
        
        
            

def RightCave():
    CaveTips()
    print ("You find a torch and use it to light your way")
    Torch = True
    print ("A:Left B: Right")
    choice = input(">>")
    if choice in answer_A:
        print ("You go left and come across a activated spike trap that has killed someone")
        time.sleep(6)
    if choice in answer_B:
        print ("You see a shadow in the distance")
        time.sleep(4)
        print ("Its a bear with a top hat")
        print ("A: Challange B: Run")
        choice = input(">>")
        if choice in answer_A:
            print ("You challange Freddy Fazbear and he screams at you and everything goees dark")
            import FNAF1
        if choice in answer_B:
            print ("You run away as fast as you can")
            time.sleep(4)
            print ("You slide under a rock and escape Freddy Fazbear")
            time.sleep(4)
            print ("For now..")
            time.sleep(3)
            print ("

def MiddleCave():
    CaveTips()
            
intro()
