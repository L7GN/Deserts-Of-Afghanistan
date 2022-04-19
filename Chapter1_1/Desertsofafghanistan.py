


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]




required = ("\nUse only A, B, or C\n") 

def MainMenu():
  print ("Welcome to the Deserts Of Afghanistan, the game where your choices impact everything")
  print ("press A to begin")
  choice = input()
  if choice in answer_A:
    intro()
def intro():
  print ("STARTING GAME...")
  print ("You are in the deserts of Afghanistan, do you want to go:")
  print ("""  A. North
  B. West""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_north()
  elif choice in answer_B:
    option_west()
  else:
      print (required)
      intro()

def option_north():
    print ("You step on a landmine and have lost your legs")
    print ("You crawl to kazakhstan")
    print ("You encounter Dwayne Johnson, Do you? A: Challenge Him B:Ask for Help C:Crawl away")
    choice = input(">>> ")
    if choice in answer_A:
        challenge_rock()
    elif choice in answer_B:
        help_rock()
    elif choice in answer_C:
        Rock_crawl()
def option_west():
    print ("You reach the borders of China")
    print ("You encounter Genghis Khan")
    print ("You run away and Kim jong un finds you and takes you to North Korea")
    print ("You encounter Agent 47, KSI and Benjamin Mendy")
    print ("Benjamin Mendy chases you and KSI gets shot by agent 47, Genghis Khan finds agent 47 and snaps his neck")
    print (" A: LEFT B:RIGHT")
    choice = input()
    if choice in answer_A:
      NorthKorea_Left()
    elif choice in answer_B:
      NorthKorea_Right()
      

def NorthKorea_Left():
  print ("You go left but Benjamin Mendy is still chasing you, do you:")
  print ("A: LEFT B: RIGHT C:UP")
  choice = input()
  if choice in answer_A:
    NorthKorea_LeftLeft()
  elif choice in answer_B:
    NorthKorea_LeftRight()
  elif choice in answer_C:
    NorthKorea_LeftUp()

def NorthKorea_LeftLeft():
  print ("You go left again and fall to your death")
  print ("Tip: Why do you go the same direction twice idiot")
  intro()

def NorthKorea_LeftRight():
  print ("You go right and Genghis Khan is fighting Shao Kahn")
  print ("They stop fighting and punt kick you to death")
  intro()

def NorthKorea_LeftUp():
  print ("You go up and press a button")
  print ("You just nuked a whole country")
  print ("Tip: Dont press random buttons")
  intro()


  
def NorthKorea_Right():
  print ("You go right and reach a dead end do you:")
  print ("A:UP B:Challenge him C:Accept Fate")
  choice = input()
  if choice in answer_A:
    NorthKorea_RightUp()
  elif choice in answer_B:
    NorthKorea_RightChallenge()
  elif choice in answer_C:
    NorthKorea_RightFate()

def NorthKorea_RightUp():
  print ("You go up and encounter Genghis Khan he pops your head")
  print ("You died")
  print ("Tip:Dont mess with genghis khan")
  intro()

def NorthKorea_RightChallenge():
  print ("You challenge Mendy and he ****s you and makes an easy meal with you")
  print ("You died")
  print ("Tip:Dont challenge a convict")
  intro()

def NorthKorea_RightFate():
  print ("You are ready to offer yourself to mendy but somebody grabs you from above its Genghis Khan")
  print ("Benjamin Mendy chases you upwards and assaults Genghis Khan")
  print ("A: Run away B: Help Mendy C: Help Genghis Khan")
  choice = input()
  if choice in answer_A:
    NorthKorea_RightFateRun()
  elif choice in answer_B:
    NorthKorea_RightFateMendy()
  elif choice in answer_C:
    NorthKorea_RightFateKhan()

def NorthKorea_RightFateRun():
  print ("You run away")
  option_north()

def NorthKorea_RightFateMendy():
  print ("You help mendy and kill genghis khan, Mendy takes you to london")
  London()
def NorthKorea_RightFateKhan():
  print ("Genghis Khan kills mendy with your help, but he still wants to kill you")
  print ("Genghis Khan challenges you but the rock fights him away")
  help_rock()


def challenge_rock():
    print ("You have no legs and dwayne johnson curb stomps your head into the ground")
    print ("You died")
    print ("Tip: Dont fight someone with no legs you idiot")
    intro()

def help_rock():
    print ("Dwayne johnson gives you a home and new legs")
    print ("Dwayne johnson gives you a plane. Will you fly to: A:New York B:London?")
    choice = input()
    if choice in answer_A:
        New_York()
    elif choice in answer_B:
        London()

def New_York():
    print ("Your plane crashes and you die")
    print ("Tip: Dont fly with Dwayne Johnson")
    intro()  

def London():
    print ("The plane crashes")
    print ("But you survive")
    print ("You are now roaming the streets of London at night do you: A: Find shelter B: Find Someone C:Search for The Rock")
    choice = input()
    if choice in answer_A:
        London_Shelter()
    elif choice in answer_B:
        PostRock_Help()
    elif choice in answer_C:
        LondonCrash_RockSearch()

def LondonCrash_RockSearch():
  print ("You search for the rock and find him, Shao Kahn finds the rock and has Genghis Khans head")
  print ("Shao Kahn grabs his hammer and smashes the rock into the ground and crushes him")
  print ("You fight shao kahn and defeat him, so he banishes you to north korea")
  option_west()
      

        

def London_Shelter():
    print ("You shelter in a pub for the night")
    print ("The owner wants you to pay for accomodation do you: A: Fight him B:Run away")
    choice = input()
    if choice in answer_A:
        PubOwner_Fight()
    if choice in answer_B:
        PubOwner_Run()
    

def PubOwner_Fight():
    print ("You deform his face with your powerful punches and leave the pub")
    print ("You go outside and get shot")
    print ("They shoot you in the metal legs and you dropkick them both to hell")
    PubOwner_Run()


def PubOwner_Run():
  print ("You run away and encounter Dwayne Johnson do you A:Challenge Him B:Run away  C: Hide in a alley")
  choice = input()
  if choice in answer_A:
    Rock_Fight()
  if choice in answer_B:
    Rock_run()
  if choice in answer_C:
    London_Alley()

def London_Alley():
  print ("You hide in an alley")
  PostRock_Help()
         
def Rock_Fight():
  print ("You try to fight the rock but he rips your legs off")
  print ("Tip: he made your legs you idiot")
  print ("A:Challenge him B:Crawl away C:Surrender")
  choice = input()
  if choice in answer_A:
    challenge_rock()
  if choice in answer_B:
    Rock_crawl()
  if choice in answer_C:
    rock_surrender()

def Rock_run():
  print ("You run away from Dwayne Johnson, What do you do now?")
  print ("A: Find help B:Rob store C: Kill Someone for no reason")
  choice = input()
  if choice in answer_A:
    PostRock_Help()
  if choice in answer_B:
    LondonStore_Rob()
  if choice in answer_C:
    London_Kill01()

def PostRock_Help():
  print ("You try to find help and find Mr beast he kidnaps you flies you to LA and you take part in one of his videos, do you:")
  print ("A: Try to escape B:Take Part")
  choice = input()
  if choice in answer_A:
    Escape_MrBeast()
  if choice in answer_B:
    MrBeast_Video()

def Escape_MrBeast():
  print ("You try to escape Mr beast and he kills you. Mr beast goes to prison and gets cancelled but that does not matter because you was stupid enough to die")
  print ("Tip: Test your might and go for the bag")
  intro()

def MrBeast_Video():
  print ("You enter the Mr beast challenge video")
  BeastLuck = ["You fall 100 stories", "You win the challenge successfully", "You win trial by combat", "You get destroyed in trial by combat and leave with half a face", "You fight a bear and leave with one hand", "You burn half of your body", "You win against the kangaroo"]
  print (BeastLuck[new_number])
  print ("A: Go to a casino with your new funds B:Go to a pub")
  choice = input()
  if choice in answer_A:
    Casino()
  if choice in answer_B:
    GoToLondonPub()

def GoToLondonPub():
  print ("You enter the pub and see dwayne johnson hes been waiting for you")
  print ("The mandalorian blasts through the window and fights the rock")
  print ("You get to help one and one only, who do you choose? A: Mandalorian B: The Rock")
  choice = input()
  if choice in answer_A:
    MandalorianSave_LondonPub()
  if choice in answer_B:
    TheRockSave_LondonPub()

def TheRockSave_LondonPub():
  print ("You help the rock, the mandalorian uses his jetpack to his advantage")
  print ("He shoots the rock in the head")
  print ("The rock falls to the ground and dies")
  print ("You chase the mandalorian who flies away but gets attacked by the green goblin on his glider who knocks him out of the air into the ground")
  print ("End of prologue")
  Chapter1()

def MandalorianSave_LondonPub():
  print ("You help the mandalorian take down the rock")
  print ("He rips off your legs as you fight him and you stand there like the useless prat you are")
  print ("The mandalorian gives you a jetpack and you fly away")
  print ("You crash onto Tatooine and you are met by Boba Fett")
  print ("He asks where the mandalorian is")
  print ("Do you say A: I dont know B: Hes dead")
  choice = input()
  if choice in answer_A:
    CluelessChoice()
  if choice in answer_B:
    DeadChoice()

def DeadChoice():
  print ("You tell the bounty hunter that he is dead and the rock comes from out of nowhere and gives boba fett a rock bottom through the ground never to be seen again")
  print ("You turn around and see a zombified mandalorian staring you down and it shoots you, killing you in the process")
  print ("You died")
  print ("Tip:Do not go around spreading false rumours")
  intro()

def CluelessChoice():
  print ("You tell the bounty hunter that you do not know where he is")
  print ("He thinks your lying and locks you up")
  print ("You stay in your cell but Boba brings you company")
  print ("Boba Fett tells you that the mandalorian is dead and leaves")
  print ("He burns you in the cell thinking you was responsible")
  print ("You crawl out of the cell with your legless body half burnt and skin melting")
  print ("You pass out...")
  print ("....")
  print ("You wake up and Boba Fett is flying above you")
  print ("He fires a rocket at you and you deflect it back at him, exploding Boba Fett")
  print ("You see a object do you collect it Y/N")
  choice = input()
  if choice in yes:
    print ("You collected the darksaber")
    print ("Boba Fett challenges you and you accept")
    print ("The bounty hunter stares you down as you wield the darksaber in your hand")
    BobaFettBoss()
    print ("You strike down Boba Fett with the darksaber and take his ship and fly back to london")
    print ("End of prologue")
    Chapter1()
  if choice in no:
    print ("You dont collect the item and Boba Fett stands behind you, half of his mask missing and no left arm")
    print ("He burns you with his flamethrower and cuts your head off")
    print ("You died...")
    print ("Tip: Why are you trying to fight a bounty hunter unarmed")
    intro()
    
  
  


  

def generate_random():
    import random
    new_rand = random.randint(1,6)
    return new_rand
new_number = generate_random()


def LondonStore_Rob():
  print ("You rob the store, do you:")

  print ("A: Kill the cashier B: Kidnap him C:Leave store")
  choice = input()
  if choice in answer_A:
    Cashier_Kill()
  if choice in answer_B:
    Cashier_Kidnap()
  if choice in answer_C:
    London_LeaveStore()

def Cashier_Kill():
  print ("You gut the cashier")
  London_LeaveStore()

def Cashier_Kidnap():
  print ("You kidnap cashier and go back to the pub and kill the owner for no witnesses")
  print ("You hide in the pub")
  GoToLondonPub()

def London_LeaveStore():
  print ("You leave the store do you")
  print ("A: Go to a casino with your new funds B:Go to a pub C:Explore")
  choice = input()
  if choice in answer_A:
    Casino()
  elif choice in answer_B:
    GoToLondonPub()
  elif choice in answer_C:
    London_Explore()


def London_Explore():
  print ("You explore london but encounter the green goblin who flies towards you")
  print ("You dodge the glider but he turns around and laughs")
  print ("He gets off his glider and you fight he destroys you to the point you become paralysed")
  print ("The Goblin returns to his glider throwing a bomb at you that explodes")
  print ("You died")
  print ("Tip: Its the green goblin did you really expect to win?")
  intro()


def London_Kill01():
  print ("You kill someone do you:")
  print ("A: Search Body B:Hide body C:Run")
  choice = input()
  if choice in answer_A:
    London_Searchbody()
  if choice in answer_B:
    London_Hidebody()
  if choice in answer_C:
    London_Run()

def London_Searchbody():
  print ("You search the body and collect a knife that is no suprise as you are in London")
  print ("A:Challenge The Rock the final time B: Search London for shelter C: Kill someone else")
  choice = input()
  if choice in answer_A:
    print ("You challenge the rock for the final time he stares you down as you pull out a knife")
    TheRockBoss()
    print ("By killing the drive and power your destiny in this new universe is fulfilled")
    print ("You then go on a murdering spree killing everyone")
    print ("I have tried to reach out but you are too far gone")
    print ("There is only one thing left to be done")
    print ("A:Kill narrator")
    choice = input()
    if choice in answer_A:
      NarratorFight()
      print ("You have defeated the narrator and have caused a genocide in the universe")
      print ("You see a portal open and go through it")
      Chapter1()
    else:
      print ("Fine ill do it myself")
      print ("Thanos destroys all of life")
      print ("GAME OVER")
      print ("TIP:You must finish what you started")
      intro()
  if choice in answer_B:
    print ("You search london for shelter but you encounter roadman you pull out a knife")
    print ("Doctor Strange appears and makes easy work of them, he tells you every universe has managed to collide leading to wars between universes out of confusion")
    print ("Godzilla shows up and Doctor Strange sends you into a portal")
    print ("End of prologue")
    Chapter1()
  if choice in answer_C:
    print ("You go to kill someone else and see someone emerge from the shadows...")
    print ("Its the batma oh wait its someone pretending to be batman as you kill them instantly")
    print ("The rock finds you but before he can hit you everything turns to black")
    Chapter1()


def London_Hidebody():
  print ("You hide the body and then encounter Logan Paul who records the body, your cover is blown due to his loud behaviour")
  print ("A:Challenge Him B: Run")
  choice = input()
  if choice in answer_A:
    print ("You challenge logan paul and with your limited fighting skills you get battered")
    print ("Tip: You just lost to logan paul and for that you are getting sent to the start screen")
    MainMenu()
  if choice in answer_B:
    print ("You try to run but encounter spiderman fighting green goblin")
    print ("With evil brewing inside you, you help the goblin to take down spiderman")
    print ("you get killed by spiderman but goblin kills him")
    print ("Tip:Dont be a maniac yet its the literal prologue")
    intro()

def London_Run():
  print ("You run out of london but encounter Zouma do you:")
  print ("A:Challenge him")
  choice = input()
  if choice in answer_A:
    Zouma_Challenge()

def Zouma_Challenge():
  print ("He kicks you like he did to his cat you stood no chance")
  print ("Tip: Dont challenge aggressive people unprepared")
  print ("You now go to prison and rot in a cell")
  MainMenu()

    
def rock_surrender():
  print ("The rock grabs your legless body and throws you to the bottom of the ocean")
  print ("You drown")
  print ("Tip: The rock is merciless")
  intro()
  
def Rock_crawl():
    print ("Dwayne Johnson grabs you and throws you on a boat with somali pirates")
    print ("You enter somalia and explore, will you go, A:East B:South")
    choice = input()
    if choice in answer_A:
      Somalia_East()
    if choice in answer_B:
      Somalia_South()

def Somalia_East():
  print ("You go east and get spotted by somali pirates do you..")
  print ("A:Challenge Them")
  print ("B:Crawl away")
  choice = input()
  if choice in answer_A:
    Challenge_SomaliPirates()
  if choice in answer_B:
    Run_SomaliPirates()

def Somalia_South():
  print ("You go south and find Lakaka")
  print ("He eats you")
  print ("Tip: LAKAKA")
  MainMenu()

def Challenge_SomaliPirates():
  print ("You challange the somali pirates but you have no legs so they aim there guns at you but they dont shoot you?")
  print ("Instead they bash your skull in with their guns")
  print ("You died...")
  print ("Tip:Stop challenging people when you have no legs")
  MainMenu()

def Run_SomaliPirates():
  print ("You try to run but realise you have no legs they grab your legless body and take you hostage")
  print ("Luke Skywalker comes from out of nowhere but gets RKO'D by Randy Orton")
  print ("Randy Orton batters all the somali pirates and escorts you to safety")
  print ("Do you...")
  print ("A:Challenge him")
  print ("B:Crawl Away")
  print ("C:Stay with him")
  choice = input()
  if choice in answer_A:
    ChallengeTheViper()
  if choice in answer_B:
    CrawlSomalia()
  if choice in answer_C:
    StayTheViper()

def ChallengeTheViper():
  print ("You challenge the viper who laughs at you and leaves you but then comes back to throw you in the air and RKO you")
  print ("You died")
  print ("Tip:You challenged the viper with no legs what a idiot")
  MainMenu()

def CrawlSomalia():
  print ("You crawl away from the randy orton he allows you to crawl")
  print ("You crawl as far as you can but find yourself in a sandstorm which kills you")
  print ("Tip:Please accept help")
  MainMenu()

def StayTheViper():
  print ("You stay with Randy Orton but realise hes a viper and when your not looking he RKO's you off a cliff")
  print ("End of prologue")
  Chapter1()
  

def Casino():
  casinoOn = True
  import random
  from random import randint
  userMoney = 10000
  #MAIN MENU
  while casinoOn == True:
          gameNumber = int(input("Welcome to the Casino.\n" + "Your current balance is " + str(int(userMoney)) + " dollars" + "\nPlease select which game you'd like to play. (Type 1, 2, or 3) \n \n 1. Blackjack \n \n 2. High or Low \n \n 3. Slots \n \n 4.Exit \n \n"))
          #Blackjack Game
          while gameNumber == 1:
                  print("\n \n Welcome to Blackjack!\n You will now be dealt two cards. \n \n")
                  blackjack_cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
                  import random
                  from random import randint
                  #defining variables
                  cardOneRan = random.randint(0, 12)
                  cardTwoRan = random.randint(0, 12)
                  cardOne = blackjack_cards[cardOneRan]
                  cardTwo = blackjack_cards[cardTwoRan]
                  #shows card values to player
                  userBJBet = input("How much would you like to bet?     ")
                  print("You were dealt a " + str(cardOne) + " and a " + str(cardTwo))
                  #ask for player move
                  bjMove = int(input("\n \n Would you like to:\n 1. Hit (Ask the dealer for another random card) \n 2. Stand (You do not want to change your cards) \n \n"))
                  while bjMove == 1:
                  #hit
                                  if bjMove == 1:
                                          playerScore = int(input("\n \n What is your score?   \n "))
                                          cardThreeRan = random.randint(0,12)
                                  cardThree = blackjack_cards[cardThreeRan]
                                  if cardThreeRan >= 10:
                                          cardThreeScore = 10
                                  else:
                                          cardThreeScore = cardThreeRan + 1
                                          print("\n \n You were dealt a " + str(cardThree))
                                          playerScore = cardThreeScore + playerScore
                                          print("\n \n Your sum is currently " + str(playerScore) + "\n \n ")
                                  if playerScore > 21:
                                          input("\n Sadly, you struck out with a card sum above 21. \n You lost " + str(userBJBet) + "\n Play again to win! \n")
                                          break
                                  if playerScore < 21:
                                          bjMove = int(input("\n \n Would you like to:\n 1. Hit (Ask the dealer for another random card) \n 2. Stand (You do not want to change your cards) \n \n"))
                  if bjMove == 2:
                          playerScore = int(input("\nWhat is your score?   \n "))
                          cardDealOneRan = random.randint(0, 12)
                          cardDealTwoRan = random.randint(0, 12)
                          cardDealOne = blackjack_cards[cardDealOneRan]
                          cardDealTwo = blackjack_cards[cardDealTwoRan]
                          cardDealOneRan = cardDealOneRan + 1
                          cardDealOneRan = cardDealOneRan + 1
                          cardDealSum = cardDealOneRan + cardDealTwoRan
                          cardDealAce = 21-cardDealSum
                          while cardDealSum <= 15:
                                          cardDealSum = int(float(cardDealSum) + float(random.randint(1,10)))
                          if cardDealAce <= 10 and cardDealOneRan == 1:
                                  cardDealSum = cardDealSum + 10
                          if playerScore >= cardDealSum:
                                  print("\n \n You won with a score of " + str(playerScore) + "! \n The dealer only had " + (str(cardDealSum)) + "\n \n")
                                  input("You won " + str(userBJBet) + " dollars! Play Again!")
                                  userMoney = float(userMoney) + float(userBJBet)
                          if cardDealSum > playerScore:
                                  if cardDealSum > 21:
                                          print("\n \n The dealer struck out! You won with a score of " + str(playerScore) + "!     Play again! \n \n ")
                                          input("You won " + str(userBJBet) + " dollars! Play Again!")
                                          userMoney = float(userMoney) + float(userBJBet)
                                  print("\n \n Sadly, the dealer won with a score of " + str(cardDealSum) + "        Press 1 to play again! \n")
                                  input("You lost " + str(userBJBet) + " dollars. Play Again to Win!")
                                  userMoney = float(userMoney) - float(userBJBet)
                          break
                  print("\n" * 50)
                  break
          while gameNumber == 2:
                  #establishes the possibilities for a card in a deck
                  card_ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
                  card_suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
                  #finds a random card
                  cardRanRank = random.randint(0, 12)
                  cardRanSuit = random.randint(0, 3)
                  cardRank = str(card_ranks[cardRanRank])
                  cardSuit = str(card_suits[cardRanSuit])
                  #asks the player if they think the next card will be higher or lower
                  print(" \n \n Welcome to High or Low. Your card is the " + str(cardRank) + " of " + str(cardSuit) + "\n \n")
                  highLow = int(input("\n \n Do you think the dealer's card will be higher or lower than yours? \n \n 1.Higher \n \n 2.Lower \n \n"))
                  userCardBet = input("How much would you like to bet?        ")
                  #draws the next card
                  card2RanRank = random.randint(0, 12)
                  card2RanSuit = random.randint(0, 3)
                  card2Rank = str(card_ranks[card2RanRank])
                  card2Suit = str(card_suits[card2RanSuit])
                  #tells the player what the card was
                  print(" \n \n The card drawn was a " + str(card2Rank) + " of " + str(card2Suit) + "\n \n ")
                  #calculates who won
                  if highLow ==1:
                          if int(cardRanRank) > int(card2RanRank):
                                  print(" \n \n Sadly, you were incorrect. The dealer's card was lower than yours. You lost " + str(userCardBet ) + " dollars.... \n Play Again to Win! \n \n ")
                                  userMoney = float(userMoney) - float(userCardBet)
                          else:
                                  print("\n \n You were correct. The dealer's card was higher than yours! You won " + str(userCardBet ) +" dollars! Play Again! \n \n ")
                                  userMoney = float(userMoney) + float(userCardBet)
                  if highLow == 2:
                          if int(cardRanRank) > int(card2RanRank):
                                  print("\n \n You were correct. The dealer's card was lower than yours! You won " + str(userCardBet ) +" dollars! Play Again! \n \n ")
                                  userMoney = float(userMoney) + float(userCardBet)

                          else:
                                  print("\n \n Sadly, you were incorrect. The dealer's card was higher than yours. You lost " + str(userCardBet ) + " dollars.... \n Play Again to Win! \n \n ")
                                  userMoney = float(userMoney) - float(userCardBet)
                  break
          while gameNumber == 3:
                  #this is where we set up the three slot rolls
                  slotSymbolsOne = ["BAR", "Grapes", "Orange", "Lemon", "Seven",	"Cherries", "Triple Sevens", "Plum", "Watermelon", "CASH", "WIN", "★★★"] #first slot array
                  slotSymbolsTwo = ["BAR", "Grapes", "Orange", "Lemon", "Seven",	"Cherries", "Triple Sevens", "Plum", "Watermelon", "CASH", "WIN", "★★★"] #2nd slot array
                  slotSymbolsThree = ["BAR", "Grapes", "Orange", "Lemon", "Seven",	"Cherries", "Triple Sevens", "Plum", "Watermelon", "CASH", "WIN", "★★★"] #3rd slot array
                  slotNum1 = random.randint(0, 11) #rng 1-12. there's 3 of these for the three slots
                  slotNum2 = random.randint(0, 11)
                  slotNum3 = random.randint(0, 11)
                  slotOne = slotSymbolsOne[slotNum1] #takes the rng and applies it to the arrays to find three slot rolls
                  slotTwo = slotSymbolsTwo[slotNum2]
                  slotThree = slotSymbolsThree[slotNum3]
                  if slotNum1 != slotNum2 and slotNum1 != slotNum3 and slotNum2 != slotNum3: #this is if none of the slots are equal
                          slotMatch1 = True
                  else:
                          slotMatch1 = False
                  if slotNum1 == slotNum2 or slotNum1 == slotNum3 or slotNum2 == slotNum3: #this is if two of the slots are equal
                          slotMatch2 = True
                  else:
                          slotMatch2 = False
                  if slotNum1 == slotNum2 and slotNum2 == slotNum3: #this is if all the slots are equal
                          slotMatch3 = True
                  else:
                          slotMatch3 = False
                  userSlotBet = int(float(input("\n \n How much would you like to bet?\n \n ")))
                  print("\n \nYou have decided to bet " + str(userSlotBet) + " dollars in the slots\n \n Get ready to roll!")
                  print("\n \n You rolled: \n \n" + str(slotOne) + "        " + str(slotTwo) + "        " + str(slotThree) + "\n \n")
                  if slotMatch3 == True:
                          input("Wow!!! You rolled three " + str(slotOne) + " \n " + str(userSlotBet) + " dollars have been added to your balance! Play Again!")
                          userMoney = float(userMoney) + float(userSlotBet)
                          print("\n" * 30)
                          break
                  if slotMatch2 == True:
                          input("Wow!!! You rolled two of the same kind! \nYour balance has not been lowered or highered. Play Again!")
                          userMoney = float(userMoney)
                          print("\n" * 30)
                          break 
                  if slotMatch1 == True:
                          input("Sadly, you rolled three different slots \n " + str(userSlotBet) + " dollars have been removed from your balance. Play Again!")
                          userMoney = float(userMoney) - float(userSlotBet)
                          print("\n" * 30)
                          break
          while gameNumber == 4:
            London_LeaveStore()

def TheRockBoss():
  import random, time
  class Action():
      def __init__(self, owner, opponent):
          self.owner = owner
          self.opponent = opponent

      def execute(self):
          pass


  class Attack(Action):
      def __init__(self, owner, opponent):
          super().__init__(owner, opponent)

      def execute(self):
          self.owner.defending = False
          if self.opponent.defending:
              hit = random.randrange(10,20)
          else:
              hit = random.randrange(5,7)
          self.opponent.health -= hit
          print('{} is hit! (-{})'.format(self.opponent.name, hit))


  class Defend(Action):
      def __init__(self, owner, opponent):
          super().__init__(owner, opponent)

      def execute(self):
          self.owner.defending = True
          print(self.owner.name, 'is defending!')


  class Player():
      players = []

      def __init__(self, name, inputmethod):
          self.name = name
          self.inputmethod = inputmethod
          self.health = 100
          self.defending = False
          self.players.append(self)

      def __str__(self):
          description = "Player: {}\n{}\nHealth = {}\nDefending = {}\n".format(
              self.name,
              '-' * (8 + len(self.name)),
              self.health,
              self.defending
          )
          return(description)

      @classmethod
      def get_next_player(cls, p):
          # get the next player still in the game
          current_index = cls.players.index(p)
          current_index = (current_index + 1) % len(cls.players)
          while cls.players[current_index].health < 1:
              current_index = (current_index + 1) % len(cls.players)
          return cls.players[current_index]

      def choose_action(self):
          print(self.name, ': [a]ttack or [d]efend?')
          action_choice = self.inputmethod(['a', 'd'])
          if action_choice == 'a':
              print('Choose an opponent')
              # build up a list of possible opponents
              opponent_list = []
              for p in self.players:
                  if p != self and p.health > 0:
                      print('[{}] {}'.format(self.players.index(p), p.name))
                      opponent_list.append(str(self.players.index(p)))
              # use input to get the opponent of player's action
              opponent = self.players[int(self.inputmethod(opponent_list))]
              return Attack(self, opponent)
          else:
              return Defend(self, None)


  def human_input(choices):
      choice = input()
      while choice not in choices:
          print('Try again!')
          choice = input()
      return choice

  def computer_input(choices):
      time.sleep(2)
      choice = random.choice(choices)
      print(choice)
      return choice

  # add 2 players to the battle, with their own input method
  hero = Player('Player', human_input)
  enemy = Player('The Rock', computer_input)

  # the hero has the first turn
  current_player = Player.players[0]
  playing = True

  # game loop
  while playing:

      # print all players with health remaining
      for p in Player.players:
          if p.health > 0:
              print(p, end='\n\n')

      # current player's action executed
      action = current_player.choose_action()
      time.sleep(2)
      action.execute()

      # continue only if more than 1 player with health remaining
      if len([p for p in Player.players if p.health > 0]) > 1:
          current_player = Player.get_next_player(current_player)
          time.sleep(2)
      else:
          playing = False

  for p in Player.players:
      if p.health > 0:
          print('**', p.name, 'wins!')

def BobaFettBoss():
  import random, time

  class Action():
      def __init__(self, owner, opponent):
          self.owner = owner
          self.opponent = opponent

      def execute(self):
          pass


  class Attack(Action):
      def __init__(self, owner, opponent):
          super().__init__(owner, opponent)

      def execute(self):
          self.owner.defending = False
          if self.opponent.defending:
              hit = random.randrange(100,200)
          else:
              hit = random.randrange(100,200)
          self.opponent.health -= hit
          print('{} is hit! (-{})'.format(self.opponent.name, hit))


  class Defend(Action):
      def __init__(self, owner, opponent):
          super().__init__(owner, opponent)

      def execute(self):
          self.owner.defending = True
          print(self.owner.name, 'is defending!')


  class Player():
      players = []

      def __init__(self, name, inputmethod):
          self.name = name
          self.inputmethod = inputmethod
          self.health = 100
          self.defending = False
          self.players.append(self)

      def __str__(self):
          description = "Player: {}\n{}\nHealth = {}\nDefending = {}\n".format(
              self.name,
              '-' * (8 + len(self.name)),
              self.health,
              self.defending
          )
          return(description)

      @classmethod
      def get_next_player(cls, p):
          # get the next player still in the game
          current_index = cls.players.index(p)
          current_index = (current_index + 1) % len(cls.players)
          while cls.players[current_index].health < 1:
              current_index = (current_index + 1) % len(cls.players)
          return cls.players[current_index]

      def choose_action(self):
          print(self.name, ': [a]ttack or [d]efend?')
          action_choice = self.inputmethod(['a', 'd'])
          if action_choice == 'a':
              print('Choose an opponent')
              # build up a list of possible opponents
              opponent_list = []
              for p in self.players:
                  if p != self and p.health > 0:
                      print('[{}] {}'.format(self.players.index(p), p.name))
                      opponent_list.append(str(self.players.index(p)))
              # use input to get the opponent of player's action
              opponent = self.players[int(self.inputmethod(opponent_list))]
              return Attack(self, opponent)
          else:
              return Defend(self, None)


  def human_input(choices):
      choice = input()
      while choice not in choices:
          print('Try again!')
          choice = input()
      return choice

  def computer_input(choices):
      time.sleep(2)
      choice = random.choice(choices)
      print(choice)
      return choice

  # add 2 players to the battle, with their own input method
  hero = Player('Player', human_input)
  enemy = Player('Boba Fett', computer_input)

  # the hero has the first turn
  current_player = Player.players[0]
  playing = True

  # game loop
  while playing:

      # print all players with health remaining
      for p in Player.players:
          if p.health > 0:
              print(p, end='\n\n')

      # current player's action executed
      action = current_player.choose_action()
      time.sleep(2)
      action.execute()

      # continue only if more than 1 player with health remaining
      if len([p for p in Player.players if p.health > 0]) > 1:
          current_player = Player.get_next_player(current_player)
          time.sleep(2)
      else:
          playing = False

  for p in Player.players:
      if p.health > 0:
          print('**', p.name, 'wins!')

def NarratorFight():
  print ("The Narrator stares down knowing your sins")
  print ("As you step closer fear builds inside")
  print ("I stabbed the narrator and watch his last moments")
  print ("You may think this is the end but it is only the beginning")
  print ("You press a button and it does nothing")

  
def Chapter1 ():
  import Reboot
  
    

MainMenu()
