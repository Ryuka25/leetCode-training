#! /usr/bin/env python
# -*- coding:utf-8 -*-
import random # Used for random number
import re # Used for regex expression
import os

class Player:
    " Class for the player in the Game "
    __numberOfCorrectAnsw = 0
    __level = "easy"

    def __init__(self, name):
        self.__name = name

    def evaluate(self):
        " Sync number of correct answer to level "
        if ( self.__numberOfCorrectAnsw < 4 ):
            self.__level = "easy"
        elif ( self.__numberOfCorrectAnsw < 7):
            self.__level = "intermediate"
        elif ( self.__numberOfCorrectAnsw < 10):
            self.__level = "hard"
    
    def correctAnsw(self):
        self.__numberOfCorrectAnsw += 1
    
    def getLevel(self):
        return self.__level

    def getName(self):
        return self.__name

    def getNumberOfCorrectAnsw(self):
        return self.__numberOfCorrectAnsw

class Game:
    " Class for the Game it self "

    def run(self, player: Player):
        print ("===[ Compare-Me ] ===")

        player.evaluate()
        # Get New Set Data
        setData = Game.getDatabyLevel(player.getLevel())
        
        # Print question and info about set:
        print(f"\n👤️ Name : {player.getName()}\nLevel : {player.getLevel()}\t💡️Number Of correct answer : {player.getNumberOfCorrectAnsw()}\n")
        print(f"\n🤨️ {setData['quest']}")

        # Get userResp
        userResp = str(input("\nYour answer : "))

        # Format userResp
        userResp = userResp.lower()

        #! Evaluate userResp
        # In case where we exit the game
        if (userResp == "exit"):
            quit()
        # In case where the game is still running
        else:
            match = re.search(setData["resp"], userResp)
            if match:
                print(" You have a match 😎️")
                player.correctAnsw()
            else:
                print(f" 😓️ Wrong answer! The correct has : {setData['resp']}")

    def getDatabyLevel(level: str)->dict:
        " Return a question and the correct response according to level"
        
        #! FILE HANDLER

        myDataFile = open("data.txt", "r")
        myRespFile = open("resp.txt", "r")

        data = myDataFile.readlines() # Store all data lines in a list
        resp = myRespFile.readlines() # Store all resp lines in a list
        if (level == "easy"):
            line = random.randint(0,9)
        elif (level == "intermediate"):
            line = random.randint(11,19)
        elif (level == "hard"):
            line = random.randint(21,31)

        # Format correctResp
        correctResp = resp[line]
        correctResp = correctResp.split()

        set = {
            "quest":data[line],
            "resp":correctResp[0]
        }

        myDataFile.close()
        myRespFile.close()

        return set

#! CONFIGURATION
run = True

print ("🎊️ Welcome to the game ")

while run:
    # Store players Data
    game = Game()
    playerName = str(input("Enter Your Name 👤️ : "))
    player = Player(playerName)

    # Launch a set of game
    continueGame = True
    while continueGame:
        os.system("clear")
        game.run(player)
        input("\n... Press Enter to continue ...")
        os.system("clear")

        if (player.getNumberOfCorrectAnsw() > 15):
            os.system("clear")
            os.system("echo 'Winner 🏆️ ! You have finished the game' | cowsay")
            reRun = str(input("Would you like to reRun ? (y/n) : "))
            if (reRun == "y"):
                run = True
            elif (reRun == "n"):
                run = False
            break
