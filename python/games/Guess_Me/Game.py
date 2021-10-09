class Game:

    def gameBanner():
        "Print the banner of the game"
        print("=== [ GUESS ME ] ===")

    def gameContinue()->bool:
        "The game will keep running"
        reply = str(input("[?] Would you like to continue the game ? (y/n)\n> ")).lower

        if (reply=='y' or reply=='yes'):
            return True
        elif (reply=='n' or reply=='no'):
            print("no")
            return False

    def gameOver():
        "Appear if the game is over"
        print("=== [ GAME OVER ] ===")
        query = str(input("Would you like to try again ? (y/n)\n> "))
        if (query == 'y'):
            Game.execute()
        elif(query == 'n'):
            Game.gameExit()

    def gameExit():
        "Exit this program"
        print("[!] Good Bye ! ")
        try:
            exit()
        except:
            SystemExit

    def execute(gameSet):
        gameSet.configNewSet()
        gameSet.getSetData()
        match = False
        while (not match):
            if (gameSet.player.life > 0):
                gameSet.getPlayerReply()
                if (gameSet.evaluteMatch()):
                    gameSet.player.upScore()
                    continueGame = Game.gameContinue()
                    if (continueGame == True):
                        print("pass")
                        Game.execute(gameSet)
                    else:
                        break
                else:
                    pass
            else:
                gameSet.getSetData()
                Game.gameOver()
        Game.gameExit()