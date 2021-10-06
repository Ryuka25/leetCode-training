class Player:

    def __init__(self,data):
        self.__name = data['name']
        self.__level = "easy"
        self.__numberOfCorrectAnswer = 0
    
    def evaluatePlayerLevel(self):
        if (self.__numberOfCorrectAnswer <= 10):
            self.__level = 'easy'

    def getLevel(self):
        return self.__level

    def getNumberOfCorrectAnswer(self):
        return self.__numberOfCorrectAnswer

    def getName(self):
        return self.__name

    def setNumberOfCorrectAnswer(self, value:int):
        self.__numberOfCorrectAnswer = value
    
    def upNumberOfCorrectAnswer(self):
        self.setNumberOfCorrectAnswer((self.getNumberOfCorrectAnswer() +1 ))
