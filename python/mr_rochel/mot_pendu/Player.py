class Player:

    def __init__(self,data):
        self.name = data['name']
        self.level = "easy"
        self.numberOfCorrectAnswer = 0
    
    def evaluatePlayerLevel(self):
        if (self.numberOfCorrectAnswer <= 10):
            self.level = 'easy'