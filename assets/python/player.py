# Originally Created on 11/14/2024
## Created as an asset for Bits-and-Bytes
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random
import time 

class player():

    def __init__(self) -> None:
        self.cryptix = 0
        self.username = "ERROR"
        self.health = 5
        self.inspiration = 1
        self.level = 1
    
    def player_turn(self): # Action selection for user's turn
        print("Choose an action for your turn!\n")
        print("1. Attack")
        print("2. Defend")
        temp = int(input("What action shall you choose? (enter #): "))
        return temp
    
    def player_defend(self, block_spam):
        temp = random.randint(1,2*block_spam)
        if temp == 1:
            print(f"You held up your guard...")
            time.sleep(2)
            print(f"* Your blocking skills fill you with determination")
            print(f"You regenerated for {self.inspiration} health!")
            return 1
        else:
            print(f"You held up your guard...")
            time.sleep(2)
            return 0