import time
import main_menu
import Adventure_CH1
import Adventure_CH2
import Adventure_CH3
import Adventure_CH4
from threading import Timer

player_HP = 100
boss_HP = 150
sword_attack = 20
special_attack = 35
boss_attack = 15

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  

def enter_an_input(prompt):
    print(prompt)
    input()

def chapter_5_intro():
    print_slow("Chapter 5") #Chapter 5 begins
    print_slow("After overcoming the obstacles and a lengthy journey, the detective encountered the ancient city")

def treasure():
    print_slow("Upon entering the ancient city you find the treasure") #Player finds treasure chest and collects items.
    print("You collect gold and valuable materials")
    enter_an_input("Press enter to continue")

def creature():
    print_slow("After collecting the treasure a large monster appears")
    if "sword" in Adventure_CH2.backpack:
        enter_an_input("Press enter to continue")
        boss_fight() #If player has sword in their backpack, they must fight the monster.
    else:
        run_away()
        #If they don't have a sword, the only option will be to run.
    
# This is the boss fight sequence. It will continue to loop until player or boss health reaches zero.
def boss_fight():
    global boss_HP
    global player_HP
    print("You have a sword. You must defeat the monster to win!")
    print("Objective: You must defeat the monster to win the game")
    enter_an_input("Press enter to continue")
    while player_HP > 0 and boss_HP > 0:
        print(F"Player HP: {player_HP}, Boss HP: {boss_HP}")
        print(F"Sword attack is {sword_attack} damage, Special attack is {special_attack} damage")
        attack = input("Choose an attack(sword/special): ") #player attacks first.
        if attack == "sword":
            print("You use a sword attack. It deals 20 damage.")
            boss_HP -= sword_attack
            print("The boss attacks you. It deals 15 damage.")
            player_HP -= boss_attack
        elif attack == "special":
            print("You use a special attack. It's very effective! You deal 35 damage.")
            boss_HP -= special_attack
            print("The boss attacks you. It deals 15 damage.") #Boss attacks for 15 damage after the player's turn.
            player_HP -= boss_attack
        else:
            print("Invalid input")
    if player_HP <= 0:
        print("Game Over. You have been defeated") #If player health reaches zero, the player loses and the game ends.
        print("Thank you for playing!")
    elif boss_HP <= 0:
        print("You Win! The boss has been defeated") #If boss health reaches zero, the player wins and the game ends.
        print("Thank you for playing!")

def run_away():
    print_slow("You don't have a sword to fight! The only option is to run.")
    print("Objective: You must run away before the monster catches you to win the game")
    print("You have 10 seconds to make each choice.")
    enter_an_input("Press enter to continue")
    Successful_choices = 0
    win_choices = 4 #user needs to make four choices within the time limit to win.
    while Successful_choices < win_choices:  #Will loop until successful choices = 4
        t = Timer(10, lambda: print("\nYou did not make a decision. The monster has caught you!"), )#Game will end if  the player does not chose within 10 seconds.
        t.start()
        decision = input("make a choice: hide or run? ")
        t.cancel()
        if decision == "run":
            print("You run away quickly")
            Successful_choices += 1
        elif decision == "hide":
            print("You hide behind a pillar")
            Successful_choices += 1
    if Successful_choices == 4:
        print("Congratulations you successfully escaped!") #If the player  makes 4 successful choices within the time limit, they successfully escape.
        print("Thank you for playing!")
#After the player successfully defeats the monster or runs away the game will be over.
def main():
    chapter_5_intro()
    treasure()
    creature()

main()
#After the player successfully defeats the monster or runs away the game will be over.


