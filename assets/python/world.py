# Originally Created on 11/04/2024
## Created as an asset for Bits-and-Bytes
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import random

class Room:
    exits = 1
    items = 0
    boss = False
    roomData = []

    def room_gen(self):

        bossGen = random.randint(0,2)
        if bossGen == 2:
            bossGen = True
        else:
            bossGen = False

        self.roomData.insert(2, bossGen)

        if self.boss == True:
            self.exits = 0
            self.items = 0
        else:
            self.exits = random.randint(1,3)
            self.roomData.insert(0, self.exits)
            self.items = random.randint(0,1)
            self.roomData.insert(1, self.items)