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

def left_path():
    print_slow("You take the left path hoping to find the ancient city faster")
    print("You move on to chapter 4")
    enter_an_input("Press enter to continue")
    #When the player chooses the left path, they move to chapter 4

def right_path():
    print_slow("You take the right path being more cautious")
    print_slow("You move on to chapter 5")
    enter_an_input("Press enter to continue")
    #When the player chooses the right path, they move to chapter 5

def chapter_3_intro():
    print_slow("Chapter 3") #Chapter 3 begins
    print_slow("As the detective set off on their adventure an unexpected obstacle compelled them to make a crucial choice")
    print_slow("You encounter a fork in the path")

    print("1. Take the left path which is faster but dangerous")
    print("2. Take the right path which is slower and safer")

    while True:
        try:
            choice = int(input(("choose an option (1 or 2): "))) #Player chooses left or right
            if choice == 1:
                left_path()
                break
            elif choice == 2:
                right_path()
                break
        except ValueError:
            print("enter a valid option")

chapter_3_intro()
 


