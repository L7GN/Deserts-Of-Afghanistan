answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
Continue = ["Z", "z"]
PlayerID = []




required = ("\nUse only A, B, or C\n")

def MainMenu():
  print ("You wake up in the same desert but a different world to explore")  
  print ("Welcome to the Deserts Of Afghanistan, the game where your choices impact everything")
  print ("Disclaimer: I am not responsible for any intentions this game may give you im just here to narrate the paths you go down")
  print ("Press A to accept")
  choice = input()
  if choice in answer_A:
      Startup()
  else:
      print (required)
      MainMenu()


def Startup():
    print ("Brilliant! Now that you have completed the tutorial or as we are calling the prologue into this world")
    print ("We hope you have a safe journey around the deserts of Afghanistan and the world")
    print ("I will be your tour guide, I have been called many names in my shorttime in this world.")
    print ("The Narrator is my name, but what would you like to call me")
    NarratorNickName = input("NarratorsName:")
    print ("Right, You will call me" , NarratorNickName)
    print ("So what is your name?")
    PlayerID = input("Name:")
    print ("Hello" , PlayerID)
    print ("We would like to take this time to apologise to you for the messiness of the last few minutes")
    print ("It seems like when the universes are colliding everything gets messed up")
    print ("EVERYTHING has been wiped now as the collision has ended and the worlds have been merged")
    print ("Who knows what you can come up against out there")
    print ("I bet you have been able to experience it before the reset")
    print ("All i know is this world is dangerous and you need to have good decision making skills in order to survive")
    print ("I will be here to give you tips along the way")
    print ("This is my biggest tip are you ready?")
    print ("DONT DIE")
    print ("I do not want to have to introduce myself to you again okay")
    print ("Press A for tour")
    choice = input()
    if choice in answer_A:
        BeginnersTour()
    else:
        print (required)
        print ("For being so stupid you are getting sent to the main menu")
        MainMenu()

def BeginnersTour():
    print ("Before we send you into the deserts of Afganistan we have to make sure you are prepared")
    print ("The world is as dangerous as ever before so you can not afford to lose")
    print ("Along your way you will be able to collect KNOWLEDGE")
    print ("KNOWLEDGE can be retrieved from meeting new faces. You will be able to find their strengths and weaknesses")
    print ("The more people you fight, befriend or see, the more knowledge that you shall get")
    print ("You will gain EXPERIENCE and SKILL which can be used in many different ways")
    print ("You can go down many different routes in this game and make enemies and allies so choose wisely")
    print ("Your ACTIONS dont just effect you they also effect those around you")
    print ("Press A when you are prepared to enter the deserts")
    choice = input()
    if choice in answer_A:
        PrepDeserts()
    else:
        print (required)
        BeginnersTour()

def PrepDeserts():
    print ("You shall collect many different items with strenghts and weaknesses that may effect your gameplay")
    print ("Are you ready to enter the deserts?")
    print ("When you enter there is no turning back")
    print ("PRESS A TO ENTER")
    choice = input()
    if choice in answer_A:
        import Chapter1
    else:
        print (required)
        PrepDeserts()



    
    
  





MainMenu()
