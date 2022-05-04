# Create an inventory class for use later (functions such as 'add_item()' will be added in a later version/video)
class Inventory:
    def __init__(self, name, group, description, capacity):
        self.name = name
        self.group = group # Group will be used so we can get a specific type of item. 
# Example being, if we are looking for a weapon to spawn somewhere, we can loop through all items and check if something is in the group "weapon"
# Alternatively you can make a dictionary holding all weapons.
 
        self.full = False
        self.capacity = capacity
        self.description = description
        self.items = {} # This is a dictionary so we can allow the user to pick up more than one of the same item.
        # the key will be the name attribute of the object and value is the amount of that item the user has.

    def is_full(self):
        count = 0
        for amount in self.items.values():
            count += amount
        return count >= self.capacity
    
    def __str__(self):
        return f"{self.description}, holds {self.capacity} items"
 
# Create an item class to make any items you would like to be in the game. We will be making functions such as 'use()' in a later version
class Item:
    def __init__(self, group, name, value, description, quest_item, can_sell=True):
        self.name = name
        self.group = group
        self.value = value # Used for weapons or health potions as damage amount or heal amount.
        self.worth = value # The worth of an item (how much you can sell it for) is tied to the value (such as amount of damage for a weapon).
        # You may change that if you'd like.
        self.description = description
        self.quest_item = quest_item # Use this so players can't sell an item they need for a quest.
 
    def __str__(self):
        return f"{self.name}, {self.description}, {self.value}"
 
 
# You have to have a keyword argument (such as can_sell=False) after positional arguments (such as 'Your fists') otherwise, you will get an error
fists = Item('weapon', 'Fists', 5, "Your fists", False, can_sell=False)
lesser_heal = Item('potion', 'Lesser Health Potion', 2, 'A lesser healing potion that heals for', quest_item=False)
burlap_sack = Inventory('Burlap Sack', 'inventory', 'A tattered burlap sack', 5)
 

# This will be very important for things like checking if a player has a quest item or not.
all_items = {
    'fists': fists,
    'lesser_heal': lesser_heal,
    'burlap_sack': burlap_sack
}
