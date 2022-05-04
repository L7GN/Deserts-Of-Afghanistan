import os,sys
import os.path
import Character# Import character to access character types
import time
import Items
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
DUEL = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

        


required = ("\nUse only A, B, or C\n") 


# Assign character objects to the name (a string)
char_types = {
    "mage": Character.mage,
    "thief": Character.thief,
    "gamer": Character.gamer,
    "prisoner":Character.prisoner,
    "vagabound":Character.vagabound,
    "warrior":Character.warrior,
    
}
 
def char_select():
    """
    Allows the player to choose the type of character they would like to be
    """
    #Pull in the list 'char_types'
    global char_types
    print("Please choose a character type\n")
    
    #Loop through the dictionary 'char_types' to list the character types and stats assigned to them
    for char in char_types:
        print(char.title()) #print the name of the character type in title case (Which capitalizes the first letter of each word in a line)
        # Just to make it look better, print a line of dashes
        print("------------------------------------------------------")
        # loop through the character type stats for printing
        for stat in char_types[char].stats.keys():
            #list the stats assigned to the character type
            print(stat, ":", char_types[char].stats[stat])
        
        # Seperate character types and their stats with an empty line
        print("\n")
 
    # Prompt the player to chose a character by entering its name
    Class = input("Please choose a character by typing its name\n")



    
 
    # Loop through char_types to check which character the player chose
    for char in char_types.keys():
 
        # If their choice is equal to the current key (Iteration 1 is "mage") then assign that character object to 'player'
        if Class.lower() == char:
            
            # Assign the character object to the variable 'player'
            player = char_types[char]
            
            # Allow them to give their character a name
            name = input("Please give your character a name\n")

            
            # Confirm that they entered their desired name correctly
            conf = input(f"You entered {name}, is this correct? y/n \n")
            
            # If they are satisfied with the name they entered the first time, assign the name to the attribute 'name' of the character object (which is assigned to 'player' on line 40)
            if conf.lower() == 'y':
                player.name = name
                print(f"You are now {name} the {char}")
                return player            
            
            # If they did not enter the name correctly, use a while loop to ask until they are satisfied with their entry
            while conf.lower() == 'n':
                name = input("Please give your character a name\n")
                conf = input(f"You entered {name}, is this correct? y/n \n")
                
                #If they are satisfied with the name they gave, assign the name to the attribute 'name' of the character object (which is assigned to 'player' on line 40)
                if conf.lower() == 'y':
                    player.name = name
                    print(f"You are now {name} the {char}")

                    # Return the complete player object

                    return player

 
            
# Assign the return of char_select() to the player variable
# Note: When assigning a function call to a variable, we are actually assigning the return of the function to the variable
player = char_select() 
 
# If there is no return from char_select() the player variable is set to None.
# So we use a while loop to keep prompting them to select a character until char_select() has a return value
while player == None:
    # Tell them that they didn't enter a listed character type or they had a typo
    print("!!!You did not enter a listed character name or had a typo, please try again!!!")
    
    # Give them 2 seconds to read the warning
    time.sleep(2)
    
    # Assign the return of char_select() to the player variable (which will call the function)
    player = char_select()





def Chapter1Intro():
    answer_A = ["A", "a"]
    answer_B = ["B", "b"]
    answer_C = ["C", "c"]
    yes = ["Y", "y", "yes"]
    no = ["N", "n", "no"]
    print ("Welcome to the deserts of afganistan")
    print ("A:North")
    print ("B:West")
    choice = input()
    if choice in answer_A:
        North()
    if choice in answer_B:
        West()


def West():
    print ("You go west and see a figure in the distance")
    time.sleep(3)
    print ("ITS LAKAKA")
    print ("He eats you")
    print ("YOU DIED")
    time.sleep(4)
    Chapter1Intro()

def North():
    print ("------------------------------------------------------------")
    print ("You see someone get blown up by a landmine in the distance")
    print ("You decide to move on and you see a tornado")
    print ("Theres a shadow in the tornado")
    time.sleep(3)
    print (".........")
    time.sleep(5)
    print ("Its...")
    time.sleep(2)
    print ("THE ROCK")
    time.sleep(3)
    print ("")
    RockBattle()
    print ("------------------------------------------------------------")
    print ("You knock the rock down but he gets back up and grabs you by the legs and drags you to the edge of a cliff")
    print ("He picks you up and is about to drop you off")
    print ("The ROCK:Where am i? What is happening? TELL ME NOW!")
    time.sleep(10)
    print ("A:FIGHT")
    print ("B:TRUTH")
    print ("C:...")
    choice = input()
    if choice in answer_A:
        print ("------------------------------------------------------------")        
        print ("You stick your fingers in the rocks eyes and with him blinded you push him off the cliff")
        print ("You watch as he falls down colliding with rocks on the way")
        player.body_count = player.body_count + 1
        print ("KILLS" , player.body_count)
        print ("THE ROCK:DEAD")
        print ("Green goblin flies towards you")
        time.sleep(3)
        print ("You grab his glider and smash it into the ground")
        time.sleep(3)
        print ("The goblin begs for forgiveness, You stab him with the glider")
        player.body_count = player.body_count + 1
        print ("GREEN GOBLIN:DEAD")
        print ("KILLS:" , player.body_count)
        print ("You use the goblin glider and fly to Kabul")
        time.sleep(11)
        print ("You spot Cad Bane...")
        time.sleep(5)
        print ("He goes to shoot but you grab his gun and headbutt him. You kill him with your fist")
        player.body_count = player.body_count + 1
        time.sleep(7)
        print ("CAD BANE:DEAD")
        print ("KILLS:" , player.body_count)
        time.sleep(9)
        print ("John Marston appears and aims his gun at you")
        time.sleep(3)
        print ("You grab Cad Banes laser pistol and with no remorse shoot him dead")
        time.sleep(6)
        player.body_count = player.body_count + 1
        print ("JOHN MARSTON:DEAD")
        print ("KILLS:" , player.body_count)
        time.sleep(5)
        print ("You have become a cold blooded killer," , player.name)
        time.sleep(3)
        print ("You still  have time to save yourself")
        time.sleep(7)
        print ("END OF CHAPTER 1.0")
        time.sleep(3)
        print ("Welcome to the multiverse, a place with endless possibilities")
        time.sleep(2)
        print ("Killing all of them people has inspired you to get stronger")
        player.xp = player.xp + 500
        print ("YOU gained" , player.xp , "XP")
        player.char_lvl = player.char_lvl + 5
        print ("YOU are LEVEL",player.char_lvl)
        Genocide()

        
        
    if choice in answer_B:
        print ("------------------------------------------------------------")   
        print ("You tell the rock everything you know")
        print ("He tells you that its everyman for himself")
        print ("The green goblin appears and attacks the rock")
        print ("You use this time to run away")
        print ("You run as far as you can")
        print ("You enter the city of Kabul")
        time.sleep(5)
        print ("You see a figure in the distance")
        time.sleep(2)
        print ("ITS CAD BANE")
        print ("He challenges you to a duel")
        print ("(D)UEL")
        choice = input()
        if choice in DUEL:
            CadBaneDuel()
        else:
            print ("------------------------------------------------------------")
            print (required)
            print ("You stand still and dont draw out your weapon")
            print ("Cad Bane slaughters you")
            Chapter1Intro()
            
    if choice in answer_C:
        print ("------------------------------------------------------------")
        print ("The rock drops you and you fall to your inevitable death")
        print ("YOU DIED")
        print ("TIP: Try speaking you idiot")
        print ("Press A")
        choice = input()
        if choice in answer_A:
            North()
        else:
            print (required)
            print ("Press A")
            choice = input()
            if choice in answer_A:
                North()
            else:
                print (required)
                print ("Get sent back to the beginning for your stupidity")
                import Desertsofafghanistan




def CadBaneDuel():
    print ("------------------------------------------------------------")
    print ("You shout you dont have a weapon")
    print ("A random pedestrian gives you a golden revolver")
    time.sleep(7)
    print ("You stare down Cad Bane")
    time.sleep(3)
    print ("Speed:" , player.speed)
    if player.speed > 6:
        print ("------------------------------------------------------------")
        print ("{You are likely to win the duel}")
        time.sleep(10)
        print ("You quickdraw and shoot five bullets")
        time.sleep(3)
        print ("You approach his body and watch as he fades away, shocked by your reflexes")
        player.body_count = player.body_count + 1
        print ("CAD BANE:DEAD")
        print ("KILLS:" , player.body_count)
        time.sleep(2)
        print ("You explore the city of kabul")
        print ("END OF CHAPTER 1.0")
        time.sleep(3)
        print ("Welcome to the multiverse, a place with endless possibilities")
        Continue()
        
    else:
        print ("------------------------------------------------------------")
        print ("{Your screwed basically}")
        time.sleep(10)
        print ("You are too slow in reaching your revolver and get obliterated by Cad Bane")
        print ("TIP: CHOOSE your class and path wisely")
        time.sleep(5)
        print ("You only just manage to survive")
        Continue()


def Genocide():
    if player.char_type == "mage":
        from Mage import Genocide
    if player.char_type == "thief":
        from Thief import Genocide
    if player.char_type == "prisoner":
        from Prisoner import Genocide
    if player.char_type == "gamer":
        from Gamer import Genocide
    if player.char_type == "vagabound":
        from Vagabound import Genocide
    if player.char_type == "warrior":
        from Warrior import Genocide
        
def Continue():
    if player.char_type == "mage":
        from Mage import NewWorld
    if player.char_type == "thief":
        from Thief import NewWorld
    if player.char_type == "prisoner":
        from Prisoner import NewWorld
    if player.char_type == "gamer":
        from Gamer import NewWorld
    if player.char_type == "vagabound":
        from Vagabound import NewWorld
    if player.char_type == "warrior":
        from Warrior import NewWorld


    
def RockBattle():
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
              hit = random.randrange(10,35)
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
  hero = Player(player.name, human_input)
  enemy = Player('The ROCK', computer_input)

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


def do_action(self, action, **kwargs):
    action_method = getattr(self, action.method.__name__)
    if action_method:
        action_method(**kwargs)


def equip(self, item):
    try:
        for key in self.inventory.items.keys():
            if item.name == key:
                self.equipped = items.all_items[item.name]
                name = self.equipped.name
                return print(f"You have equipped {name}")
        return print("\n!!!You do not have that item!!!\n")
    except Exception as e:
        print("Debug line 126 character.py Error:", e)

def has_item(self, item):
    try:
        amount = self.inventory.items[item.name]
        return True
    except:
        return False

def add_item(self, item):
    if not self.has_item(item):
        self.inventory.items[item.name] = 1
        return print(f"You've added {item.name} to your inventory!")
    elif self.has_item(item):
        ans = input(f"You already have {item.name}, would you like to pick it up anyway?")
        if ans.lower() == 'y':
            self.inventory.items[item.name] += 1
            return print(f"You've added another {item.name}! You now have {self.inventory.items[item.name]} {item.name}s!")
        elif ans.lower() == 'n':
            return print(f"You put the {item.name} back where you found it.")
        else:
            print("Please choose 'y' or 'n'")
            return self.add_item(item) 

Chapter1Intro()





