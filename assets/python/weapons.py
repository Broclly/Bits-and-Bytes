# Originally Created on 11/20/2024
## Created as an asset for Bits-and-Bytes
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import assets.python.enemy

enemy = assets.python.enemy.enemy()

class weapon():

    def __init__(self):
        self.current_weapon = "ERROR"
        self.weapon_damage = 0
        self.hit_chance = 0

    def weapons_check(self,weapon_choice):
        for i in weapons:
            if i["id"] == weapon_choice:
                self.current_weapon = i["name"]
                self.weapon_damage = i["damage"]
                self.hit_chance = i["hit_chance"]
            
    def weapons_list(self):
        temp = 0
        for i in weapons:
            print(f"{str(temp + 1)}. " + i["name"] + " (Hit Chance: " + str(i["hit_chance"]) + ", Damage: " + str(i["damage"]) + ")") 
            temp += 1
    def player_attack(self,currentEnemy):
        temp = random.randint(1,self.hit_chance)
        temp = 1
        if temp == 1:
            print(f"You hit the {currentEnemy} for", str(self.weapon_damage), "damage!")
            return self.weapon_damage
        else:
            print("You missed your attack!")
            return 0

weapons = [{"name" : "Bug Spray", "damage" : 2, "hit_chance" : 2, "id": 1},{"name" : "Pocket Firewall", "damage" :  4, "hit_chance" : 5, "id": 2}, {"name" : "Binary Knuckles", "damage" : 1, "hit_chance" : 1, "id": 3}]