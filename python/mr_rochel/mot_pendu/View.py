import os

from Player import Player


class View:

    def showBanner():
        os.system('clear')
        print("\n")
        os.system('figlet "MOT_P*NDU"')

    def inputName():
        return "\nInput your name here : "

    def showWinningScreen():
        View.showBanner()
        print("\n Congratulations you are the : \n")
        os.system('figlet " _WINNER_ "')
        print("\n")

    def showExitScreen():
        os.system("clear")
        print("\n")
        os.system('cowsay "GOOD BYE MY FRIEND"')

    def playerStatus(player:Player):
        playerStatus = f"\n Name : {player.getName()} \t\t Number Of Correct Answer : {player.getNumberOfCorrectAnswer()}"
        return playerStatus

    def guessWord(hiddenWord, indice):
        guessMyWord = f"\nGuess the following Word : {hiddenWord}\t\tIndices : {indice}"
        return guessMyWord
    
    def inputAnswer():
        return "Answer : "

    def correctWord():
        return "\n Your answer has been exact"
    
    def wrongWord(correctWord):
        return f"\nOh no, the correct answer is : {correctWord}"

    def continueGame():
        return f"\nWould you like to continue the game ? (y/n)"

    def reviewAnswer():
        return f"We don't understand your answer! Please review it ..."

    def menu():
        View.showBanner()
        print("\n Copyright © 2021 - Ryuka")
        print("\n [*] What would you like to do ?")
        print("\n\t\t1 - Start a new Game\n\t\t99 - Exit the game")