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

def Intro():
    print ("Chapter 1.2: RED DEAD")
    time.sleep(5)
    print ("Your on a horse riding around the outskirts of New York")
    time.sleep(6)
    print ("Arthur Morgan:We are gonna attack that train")
    time.sleep(3)
    print ("Arthur Morgan:I want you to attack the back of the train")
    time.sleep(5)
    print ("You attack the train ")
    time.sleep(3)
    print ("Press A to open door")
    choice = input()
    if choice in answer_A:
        TrainHeist()
    else:
        print (required)
        Intro()



def TrainHeist():
 #map
    dungeonMap = [["0","0","0","0","0","0","0","0","E"],
                  ["0",".",".","1",".",".",".",".","V"],
                  ["0",".",".",".",".",".",".",".","7"],
                  ["0",".",".","4",".",".",".",".","."],
                  ["0","2","3",".","1","..",".",".","0"],
                  ["0","0","0","1",".",".",".","*","0"],
                  ["0","8",".",".",".",".",".","5","0"],
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
        BlackPanther = False

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
                print("Thats a wall")
                x = previousX
                y = previousY
                position = mapChoice[y][x]

            if position == ".":
                print("This area is clear")

            if position == "*":
                print("In the darkness you see a dull glint..")
                print("You go over to inspect and realise that the object is a gun")
                print("You pick it up and holster it in you belt")
                gun = True

            if position == "2":
                print ("You see starlord who shoots at you, you hide behind a box")
                time.sleep(3)
                if gun == False:
                    print ("You dont have a weapon to fight back so John Marston comes to your aid and kills him")
                    time.sleep(7)
                    print ("STARLORD:DEAD")
                else:
                    print ("You use your gun and shoot Starlod in the hand")
                    time.sleep(5)
                    print ("Starlord is disarmed by this and you shoot him in the head")
                    time.sleep(4)
                    print ("STARLORD:DEAD")
                    player.body_count = player.body_count + 1
                    print ("KILLS:" , player.body_count) 
                

                    
                    position = mapChoice[y][x]
                    
            if position == "3":
                print ("You continue through the train and see Kung Fu Panda fighting Conor Mcgregor")
                time.sleep(5)
                print ("Kung Fu Panda judo throws conor off the train and looks for someone else to fight")
                time.sleep(6)
                print ("Doomfist tries to punch Kung Fu Panda but gets countered with a punch in the eye stunning him")
                time.sleep(7)
                print ("Kung Fu Panda snaps his neck")
                time.sleep(5)
                print ("DOOMFIST:DEAD")
                print ("You use this time to continue on while he is distracted")
                
                        
                position = mapChoice[y][x]

                    
            if position == "4":
                print ("Obi wan: Hello There!")
                time.sleep(2)
                print ("McCree appears and begins shooting at Obi-Wan")
                time.sleep(5)
                print ("Obi-Wan deflects the bullet back at McCree killing him")
                time.sleep(3)
                print ("MCCREE: DEAD")
                print ("Obi-Wan goes to strike you down but roadhog hooks him off the train")

            if position == "5":
                print ("You find a chest and go to open it")
                time.sleep(3)
                print ("Sea Raider: Thats a nice head you have on your shoulders")
                time.sleep(5)
                if gun == True:
                    print ("You shoot the Sea Raider and collect his sword")
                    sword = True
                else:
                    print ("The sea raider takes your head off")
                    time.sleep(3)
                    print ("YOU DIED")
                    print ("TIP:Try stopping the sea raider from taking your head off your shoulders")
                    time.sleep(10)
                    Intro()
                    


            if position == "7":
                print ("You are heading towards the front of the train but as you are heading into the next section of the train Black Panther appears")
                time.sleep(10)
                print ("He runs towards you but some random guy called Mikes Magic appears between you")
                time.sleep(5)
                print ("Mikes magic: Can i spare a second of your time")
                time.sleep(1)
                print ("Mikes magic and black panther disappear")
                time.sleep(5)
                print ("You stand confused with what has happened")
                time.sleep(5)
                print ("Out of respect you take the black panther suit")
                BlackPanther = True
                

            if position == "V":
                print ("You are running towards the exit and Kung Fu Panda stands in your way")
                if BlackPanther == True:
                    print ("Using your claws you scratch at Kung Fu Panda and catch him a couple times")
                    time.sleep(5)
                    print ("NARRATOR:What is so important for everyone to be here?")
                    time.sleep(3)
                    print ("Kung Fu Panda charges at you")
                    if sword == True:
                        print ("You put the sword through his chest")
                        print ("KUNG FU PANDA:DEAD")
                    else:
                        print ("YOU DIED")
                        intro()
                else:
                    print ("YOU DIED")
                    Intro()

                
                        
                    

            

            if position == "8":
                print("You find a small rusty key on the floor, you pick it up and put it in your pocket")
                key = True


            
            
        print("you made it out alive!!!")
        time.sleep(5)
        print ("You enter the next room to see Arthur Morgan holding a purple orb")
        time.sleep(5)
        print ("NARRATOR: thats the orb of all, An orb present in all universes")
        time.sleep(7)
        print ("NARRATOR: This orb connects to the orbs in the universes creating a portal")
        time.sleep(3)
        print ("NARRATOR: Are they using it to bring people from there universes to fight alongside them?")
        time.sleep(5)
        print ("NARRATOR:They are trying to fight for superiority")
        print ("NARRATOR:They're gonna extinct one another")
        time.sleep(7)
        print ("A white light hits the sky from outside")
        print ("OBSERVATION MAN IS BACK")
        time.sleep(10)
        print ("OBSERVATION MAN shoots a beam at the bus and it hits the orb exploding it")
        print ("The ORB explodes creating a massive blackhole")
        time.sleep(17)
        print ("You open yur eyes to see a massive purple blackhole with people charging out of it")
        time.sleep(5)
        print ("You close your eyes")
        time.sleep(3)
        print ("CHAPTER 1.2: Red Dead")
        
            


            
    main(mapChoice, playerMap, position)                           































Intro()
