from random import *

class Word:

#* Methods to get the correct Word Data
    def getWordFromLevel(level):
        " Return a word from the specifed"
      # Get All word and choose a random word Data from the list
        allWord = Word.__getAllWordForLevel(level)
        randomNumber = randint(0,(len(allWord)-1))
        randomWord = allWord[randomNumber]
      # Return the random word
        return randomWord

    def __getAllWordForLevel(level):
        " Return a list of all word according to the specified level in a list form "
      # Read the file and get all lines
        if (level == "easy"):
            myWordFile = open("mot_pendu/word.easy.txt", "r")
            allWord = myWordFile.readlines()
            myWordFile.close()
        else :
            myWordFile = open("word.txt", "r")
            allWord = myWordFile.readlines()
            myWordFile.close()
      # Store lines in a list of ["word", "indice"]
        allWordData = []
        for data in allWord:
            data = str(data).casefold()
            data = data.split()

            wordData = {
                'word':data[0],
                'indice':data[1]
            }
            allWordData.append(wordData)
      # Return the list of all word with their indices
        return allWordData

#* Methods to get the hidden Word according to the correct word Data
    def getHiddenWordFromWord(correctWord, numberOfHiddenChar:int)->str:
        " Return a hidden word from a WordData withe numberOfHIddenChar "
        hiddenWord = correctWord
      # Set a list of random index to change
        listOfRandomIndex = Word.__getListOfRandomNumber(numberOfHiddenChar,len(correctWord))
      # Create the finnal hiddenWord
        hiddenWord = Word.__replaceCharInWord(hiddenWord, listOfRandomIndex)   

        return hiddenWord

    def __getListOfRandomNumber(numberOfRandomNumber, maxNumberOfRandomNumber):
        " Return a list of different Random Number to replace in a word"
      # Get the list of random number
        listOfRandomNumber = []
        if (numberOfRandomNumber < maxNumberOfRandomNumber):
            while (len(listOfRandomNumber) != numberOfRandomNumber):
                randomNumber = randint(0,maxNumberOfRandomNumber-1) # range = [a,b] with a,b included

        # Test if the number is already in the list of random number
                if (not (randomNumber in listOfRandomNumber)):
                    listOfRandomNumber.append(randomNumber)
                else:
                    next
      # Sort the list of Random Number
            listOfRandomNumber.sort()
      # Return the list of random number
        return listOfRandomNumber

    def __replaceCharInWord(word:str,listOfRandomIndex:list):
        "Change 'indexedChar' to '*'"

        listedWord = list(word)
        for index in listOfRandomIndex:
            listedWord[index] = '*'

        # replacedWord = ""
        # for char in listedWord:
        #     replacedWord = f"{replacedWord}{char}"

        replacedWord = ''.join([char for char in listedWord])

        return replacedWord