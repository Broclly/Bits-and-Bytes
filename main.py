# Originally Created on 10/25/2024
## Main code for Bits-and-Bytes
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time
import os
import assets.python.enemy
import assets.python.player
import assets.python.save
import assets.python.world
import assets.python.weapons

save = assets.python.save
room = assets.python.world.Room()
player_data = assets.python.player.player()
enemy = assets.python.enemy.enemy()
weapon_data = assets.python.weapons.weapon()

save_confirmation = 0
def_dir = "assets/saves/"
current_version = 1.0

def ctpd(): # Locates where the script is currently running, and then changes to parent directory of the file
    directory_location = os.path.realpath(__file__)
    file_name = os.path.basename(__file__)
    os.chdir(directory_location[0:-(len(file_name))])
ctpd()

def welcome(): # A warm welcome
    print("=========================")
    print("Welcome to Bits and Bytes!")
    print("A solo project created by Broclly!")
    print(f"Current Version: {current_version}")
    print("=========================")
    time.sleep(1/2)
    input("Press enter to continue...")
    os.system('cls')
    start_menu()

def start_menu(): # Start menu CLI
    print("Main Menu:")
    print("1. Begin!")
    print("2. Options")
    print("3. Credits")
    print("4. Quit")
    temp = input("Select an option ")

    if temp == "1":
        time.sleep(1/2)
        os.system('cls')
        game_setup()
    elif temp == "2":
        time.sleep(1/2)
        os.system('cls')
        options()
    elif temp == "3":
        time.sleep(1/2)
        os.system('cls')
        credits()
    elif temp == "4":
        print("Bye!")
        time.sleep(1/2)
        quit()

def game_setup(): # Runs a setup for username and weapon selection data (not currently used)
    player_data.username = input("What is your username? ")
    weapon_data.weapons_list()
    global weapons_choice 
    weapons_choice = int(input("What's your weapon choice? (enter #): "))
    
    os.system('cls')
    gameplay()

def options():
    print("This menu is currently unavailable, I'll send you back to the menu for now..")
    time.sleep(3)
    os.system('cls')
    start_menu()

def credits():
    print("Credits:")
    print("\nCreated by Broclly")
    print("Inspired by Coin-op Vice")
    input("\n\nPress enter to go back...")
    os.system('cls')
    start_menu()

def gameplay(): # Gameplay loop
    block_spam = 1
    while player_data.health > 0: # Checks for if you are alive
        if enemy.enemy_alive == False: # Runs if an enemy has not been generated yet
            if (player_data.level % 5) != 0: # Checks if level is a multiple of 5
                enemy.generate_enemy() # Generates enemy
                enemy.enemy_encounter() # Runs cool message
            else:
                enemy.generate_boss() # Generates boss
                enemy.boss_encounter() # Runs epic message
        
        weapon_data.weapons_check(weapons_choice) # Checks your current weapon equipped, used for damage calculation
        turn_type = player_data.player_turn() # Input thingy to check which attack is used
        os.system('cls')

        if turn_type == 1:
            player_damage = weapon_data.player_attack(enemy.current_enemy) # Runs hit checker
            enemy.enemy_health = enemy.enemy_health - player_damage # Runs damage calculation on enemies health
            block_spam = 1 # Set block spam to default, that way spam doesn't accumulate, and instead resets when another attack is used
            block_inactive = 1 # Sets block to inactive, so then player takes damage
        elif turn_type == 2:
            player_data.health += player_data.player_defend(block_spam)
            block_inactive = 0
            block_spam += 1
        else:
            print(f"{player_data.username} passed their turn! ")


        enemy_damage = enemy.enemy_turn(block_inactive)
        player_data.health = player_data.health - (enemy_damage)
        print(f"\n{enemy.current_enemy} currently has {enemy.enemy_health} hit points left!")
        print(f"{player_data.username} currently has {player_data.health} hit points left!")
        time.sleep(3)
        os.system('cls')
        if enemy.enemy_health > 0:
            os.system('cls')
        else:
            if player_data.health < 0:
                print("When the dust settles, you curse your enemy with your last breath, and close your eyes...")
                time.sleep(3)
                return
            
            if enemy.boss == True:
                enemy.boss_defeated()
            else:
                enemy.enemy_defeated()

            enemy.enemy_alive = False
            time.sleep(3)
            os.system('cls')
            player_data.level += 1
    print("You died! Oh no try again!")
    time.sleep(3)
    quit()
        
    
welcome()