from Player import Player
from Word import Word
from View import View
import os

class GameSet: 

    def start(self):
        View.menu()
        while True:
            run = str(input(' > '))
            if (run == '99'):
                GameSet.end()
            elif (run == '1'):
                while True:
                    View.showBanner()
                    data = {}
                    data['name'] = input(f"{View.inputName()}")
                    player = Player(data)

                    continueGame = 'y'
                    while continueGame == 'y':
                        self.configSetForPlayer(player)
                        View.showBanner()
                        print(f"{View.playerStatus(player)}")               
                        print(f"{View.guessWord(self.getHiddenWord(), self.getCorrectWordIndice())}")
                        answer = str(input(f"{View.inputAnswer()}")).lower()

                        if (answer == self.getCorrectWordWord()):
                            print(f"{View.correctWord()}")
                            player.upNumberOfCorrectAnswer()
                        elif (answer == 'exit'):
                            break
                        else:
                            print(f"{View.wrongWord(self.getCorrectWordWord())}")
                        
                        while True:
                            continueGame = str(input(f"{View.continueGame()}")).lower()
                            if continueGame in ['y','n']:
                                break
                            else :
                                print(f"{View.reviewAnswer()}")
                                pass
                        
                        if (player.getNumberOfCorrectAnswer() == 10):
                            View.showWinningScreen()
                            break
                    
                    input('Press Enter to continue ...')
                    View.menu()
                    reRun = str(input(' > '))
                    if (reRun == '99'):
                        GameSet.end()
                    elif (run == '1'):
                        pass
                    
            else:
                print(f"{View.reviewAnswer()}")
                pass
        return 0

    def end():
        View.showExitScreen()
        exit(0)
  
  #* Setters & Getters about Word in the curent GameSet
    def setHiddenWord(self, hiddenWord):
        self.__hiddenWord = hiddenWord
    
    def setCorrectWordData(self,correctWord):
        self.__correctWord = correctWord
    
    def getHiddenWord(self):
        return self.__hiddenWord

    def getCorrectWord(self):
        return self.__correctWord
    
    def getCorrectWordWord(self):
        return self.__correctWord['word']

    def getCorrectWordIndice(self):
        return self.__correctWord['indice']
  
  #* Methods about GameSet
    def configSetForPlayer(self, player:Player):

        player.evaluatePlayerLevel()

        if player.getLevel() == "easy":
            self.__correctWord = Word.getWordFromLevel(player.getLevel())
            self.__hiddenWord = Word.getHiddenWordFromWord(self.getCorrectWordWord(), 3)
