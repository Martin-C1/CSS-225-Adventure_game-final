import time

def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  

def exit_game():
    print("Quitting the game")
    exit()

def start_game(): 
    print("beginning the adventure")
    player_name = input("Enter player name, detective: ")
    return player_name  


def menu():
    options = [start_game, exit_game]
    

    print("1. Start Game")
    print("2. Exit Game")
    
    
    choice = input("Choose an option (1 or 2): ").strip()
    if choice == '1':
        player_name = options[0]()  
        print_slow(f"Hello detective {player_name}!")
    elif choice == '2':
        options[1]() 
    else:
        print("Invalid choice. Please enter either 1 or 2.")
menu()
#Players will be shown a menu where they decide if they want to start a game or exit.
#Then the player will be asked for their detective name.