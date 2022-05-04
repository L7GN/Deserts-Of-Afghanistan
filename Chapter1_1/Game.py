answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
import sys
import time
print ("Welcome to Deserts of Afghanistan")
time.sleep(3)
print ("Before you begin on this journey i must remind you the game is not complete")
time.sleep(5)
print ("If the game tells you to use to use A,B or C")
time.sleep(5)
print ("Then please do so")
time.sleep(3)
print ("Anyway press A to begin")
choice = input(">>")
if choice in answer_A:
    import Desertsofafghanistan
else:
    print ("I asked you to enter A")
    import Desertsofafghanistan
