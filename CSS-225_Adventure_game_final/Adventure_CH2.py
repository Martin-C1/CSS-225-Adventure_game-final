import time
import main_menu

backpack =[]

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  

def enter_an_input(prompt):
    print(prompt)
    input()

enter_an_input("Press enter to continue")
def chapter_2_intro():
    print_slow("Chapter 2") #Chapter 2 begins
    print_slow("In the town, as locals gathered, a curious detective prepared to embark on the adventure that awaited them")
    CH2_options = input("Gather materials at the shop or talk to locals (M/T): ")
    if CH2_options == "M":
        print_slow("You visit the local shop and acquire several materials")
        print("You collect a map of the ancient city")
        print("You collect a set of tools")
        backpack.append("sword")
        print("You collect a sword")
        print(backpack)
        enter_an_input("Press enter to continue")
#player receives a sword from the shop. It is added to the backpack.
    elif CH2_options == "T":
        print_slow("You talk to the local townspeople")
        print_slow("You: Hello, do you know anything about this ancient city I read about?")
        print_slow("Local: Yes, unfortunately it is guarded by creatures")
        #A local informs the player that the ancient city is guarded by a monster
        print_slow("Local: Many people have attempted to locate the treasure, however, nobody has been able to find the city")
        enter_an_input("Press enter to continue")
    else:
        print("Invalid option. Enter M or T")

def begin_journey():
    print_slow("You begin your adventure")
    print_slow("You leave the town in search of the ancient city")
    enter_an_input("Press enter to continue")

chapter_2_intro()
begin_journey()