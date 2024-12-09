import time
import main_menu
from threading import Timer

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  

def enter_an_input(prompt):
    print(prompt)
    input()

def chapter_4_intro():
    print_slow("Chapter 4") #Chapter 4 begins
    print_slow("Treacherous obstacles blocked the path, a challenge for the detectives decision making and resolve")
    print("You come across several obstacles requiring quick decision making")
    enter_an_input("Press enter to continue")

def evade_traps():
    print_slow("There is a boulder rolling towards you!")
    print("You have 10 seconds to make a choice or you will be crushed")
    enter_an_input("Press enter to continue")
    t = Timer(10, lambda: print("\nThe boulder crushed you. Game Over"), ) #Game will end if  the player does not jump fast enough.
    t.start()
    trap = input("enter jump: ")
    t.cancel()
    if trap == "jump":
        print("You successfully evaded the boulder")
    else:
        print("You did not jump. Game Over") #If the player does not jump away from the boulder the game ends.
    enter_an_input("Press enter to continue")

def navigate_terrain():
    print_slow("You must navigate through rough terrain to move on")
    print_slow("A tree blocks the path")
    print("1. cut down the tree with an axe from your backpack")
    print("2. climb over the tree")

    while True:
        try:
            choice = int(input(("choose an option (1 or 2): "))) #Player chooses to cut down the tree or climb over it.
            if choice == 1:
                print("You successfully cut the tree. The path is now cleared")
                break
            elif choice == 2:
                print("You climbed over the tree. You can now continue on the path")
                break
        except ValueError:
            print("enter a valid option")
    enter_an_input("Press enter to continue")

def unstable_bridge():
    print_slow("You must cross an unstable bridge to move on")
    print("You have 10 seconds to make a choice or the bridge will collapse")
    enter_an_input("Press enter to continue")
    t = Timer(10, lambda: print("\nThe bridge crumbled beneath you. Game Over"), )#Game will end if  the player does not cross the bridge fast enough.
    t.start()
    bridge = input("make a choice: run over the bridge or jump across (run/jump)? ")
    t.cancel()
    if bridge == "run":
        print("You run across the bridge")
    elif bridge == "jump":
        print("You jump over the pit avoiding the bridge")
    else:
        print("Invalid choice") 

chapter_4_intro()
evade_traps()
navigate_terrain()
unstable_bridge()