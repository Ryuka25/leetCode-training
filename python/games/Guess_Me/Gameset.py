from random import *
from Player import *

class GameSet:

    def __init__(self) -> None:
        self.targetNumber = -99
        self.firstLaunch = True

    def _setTargetNumber(self):
        "Set a new target Number"
        self.targetNumber = randint(0,100)

        return True

    def _configNewPlayer(self)->bool:
        "Config a new player"
        self.player = Player.setNewPlayer()

        return True

    def getTargetNumber(self)->bool:
        "Show the curent Target Number"
        print(f"[*] The target Number in this set is : {self.targetNumber}")

        return True

    def getSetData(self):
        "get the current state of the running set"
        self.player.getPlayerData()
        self.getTargetNumber()

        return True

    def configNewSet(self)->bool:
        "Config a new set"

        # Config the player
        if (self.firstLaunch):
            self._configNewPlayer()
            self.firstLaunch = False
        else:
            self.player.upLife()

        # Config the target number
        self._setTargetNumber()

        return True

    def getPlayerReply(self)->bool:
        "Get reply by Player"

        while True:
            reply = str(input("[?] Input the target number here > ")).lower()
            if (reply in ['quit','exit'] ):
                quit
            else:
                try:
                    reply = int(reply)
                    break
                except:
                    print(f"[!] Guess_ME don't understand '{reply}'")
                    pass

        self.userInput = reply
        return True

    def evaluteMatch(self)->bool:
        "Evaluate if there is a match betwenn the target number and "

        userIn = self.userInput
        target = self.targetNumber

        match = False

        self.player.life -= 1

        ###############################

        if (userIn == target):
            print("[*]  🎉️ There is a match ")
            self.player.life += 2
            match = True
        elif (userIn in range(target-50, target+50+1)):
            print("[*] Grrr ! It's so cold ☃️")
        elif (userIn in range(target-20, target+20+1)):
            print("[*] Keep Moving, you are one the right way 💧️")
        elif (userIn in range(target-5, target+5+1)):
            print("[*] It's Hot 🔥️")
        else:
            print("[*] Give Up 💀️")

        ###############################

        if (userIn > target):
            print("[*] Choose a low number",end="\t\t")
        elif (userIn < target):
            print("[*] Choose a great number",end="\t\t")

        ###############################

        print(f"[!] Life ♥️ : {self.player.life}")

        return match