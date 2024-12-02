# Originally Created on 11/20/2024
## Created as an asset for Bits-and-Bytes
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time

class enemy():
    def __init__(self) -> None:
        self.current_enemy = "ERROR!"
        self.enemy_health = 0
        self.enemy_damage = 0
        self.enemy_alive = False
        self.boss = False

    def generate_enemy(self): # Random enemy generation, Fixed enemy attribute assignment
        temp = random.randint(0,(len(enemies)) - 1)

        self.current_enemy = enemies[temp]["name"]
        self.enemy_health = enemies[temp]["health"]
        self.enemy_damage = enemies[temp]["damage"]
        self.enemy_alive = True
    
    def enemy_encounter(self): # Cool little swag intro for enemies (i'll probably update this)
        print("Negative energy gathers and discharges...")
        time.sleep(1)
        print(self.current_enemy + " formed! Take it out!")
    
    def enemy_turn(self, block): # Randomly generates whether or not the shot hits
        temp = random.randint(0,1)
        if temp == 1:
            temp2 = self.enemy_damage * block
            print(f"{self.current_enemy} hit you for", str(temp2), "damage!")
            return temp2
        else:
            print(f"{self.current_enemy} missed!")
            return 0
    
    def enemy_defeated(self):
        print("The negative energy calms down...")
        print(f"You defeated the {self.current_enemy}!")

    def generate_boss(self):
        temp = random.randint(0,(len(boss)) - 1)

        self.current_enemy = boss[temp]["name"]
        self.enemy_health = boss[temp]["health"]
        self.enemy_damage = boss[temp]["damage"]
        self.enemy_alive = True
        self.boss = True

    def boss_encounter(self):
        print("Negative energy swirls in a hurricane-like storm...")
        time.sleep(1)
        print("!!BOSS APPEARS!!")
        print(f"{self.current_enemy} rampages, destroy it at all costs!!")
    
    def boss_defeated(self):
        print("The whirlwind subsides...")
        print(f"You defeated the {self.current_enemy}!")

enemies = [{"name" : "malware", "health" : 3, "damage" : 2}, {"name" : "trojan", "health" : 7,"damage" : 1}]
boss = [{"name" : "virus", "health" : 5, "damage" : 4, "boss" : True},{"name" : "ERR CORRUPTED", "health" : 10, "damage" : 6, "boss" : True}]
