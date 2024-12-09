import time
import main_menu

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  

def enter_an_input(prompt):
    print(prompt)
    input()
# Chapter 1 begins
enter_an_input("Press enter to continue")
def chapter_1_intro():
    print_slow("Chapter 1")
    print_slow("It was a quiet and gloomy night, mysterious sounds reverberated from the library")
    enter_an_input("Press enter to continue")

def enter_library():
    print_slow("You enter the library")
    enter_an_input("Press enter to continue")

def search_library():
    print_slow("You look around for clues")
    enter_an_input("Press enter to continue")

def read_book():
    print_slow("You find a book")
    print_slow("You open the book and read about an ancient city full of treasure")
    keep_exploring = input("Would you like to continue exploring?(Y/N) ")
    #Asks the player to continue to chapter 2 or keep exploring the library.
    if keep_exploring == "Y":
        explore_more()
    elif keep_exploring == "N":
        print("moving to chapter 2")
    else:
        print("Invalid input")

def explore_more():
    print("You decide to keep exploring the library.")
    print("You find a hint: Follow the path to the town. A sword awaits in the shop.")
    # Informs players that a sword is located in the town's shop and will be useful to have during the adventure.

chapter_1_intro()
enter_library()
search_library()
read_book()

