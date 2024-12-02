# Originally Created on 10/29/2024
## Created as an asset for Bits-and-Bytes
### DO NOT COPY THIS PROJECT WITHOUT CREDITS TO BROCLLY

import time

defDir = "assets/saves/"

def saveLocator():
        fileName = input("What was the name of the file? (don't add .txt at the end)")

        print("\nData Retrieved!\n")
        print(saveDataRetrive(fileName,defDir))

def saveDataRetrive(fileName, savesDir):
    try:
        saveFile = open(savesDir + fileName + ".txt","r")
    except:
        print("An error has occured!")
    else:
        saveData = saveFile.read()
        return saveData

def newSave(username, savesDir):
    try:
        saveFile = open(savesDir + username + ".txt", "x")
    except:
        print("This file already exists!")
        time.sleep(1/2)
        print("Retrieving save file instead...")
        saveDataRetrive(username, defDir)
    else:
         saveFile = open(savesDir + username + ".txt", "a")
         saveFile.write("Save File Initalized!\n\n\n")
         saveFile.write("Username:" + username + "\n")

def saveToFile(username, savesDir, newData):
    try:
        saveFile = open(savesDir + username + ".txt", "a")
    except:
        print("An error occured")
    else:
        saveFile.write(newData)