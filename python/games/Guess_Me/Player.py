class Player:

    def __init__(self, name : str = 'default') -> None:
        self.name = name;
        self.life = 10;
        self.score = 0

    def getPlayerData(self):
        "Get all Data cabout the current player"

        player = {
            'name':self.name,
            'life':self.life,
            'score': self.score
        }

        print(f"[*] The current player name is : '{player['name']}'")
        print(f"\tNumber of life\t: {player['life']}")
        print(f"\tTotal Score\t: {player['score']}")

    def upScore(self):
        "Up the score of the curent Player"
        self.score += (self.life * 5)

    def regenerateLife(self):
        "Regenerate the life of the curent Player"
        self.life += 5

    def setNewPlayer():
        " Create a new player "

        print("[!] You are about to create a new player ")
        data = {} # Data for the new player is collected here

        def allowedName(name:str)->bool:
            "Simple Name verification"
            if (len(name) >= 3):
                return True
            else:
                return False

        # set the new name
        while True:
            data['name'] = str(input("[*] Please enter a new player Name : "))
            # Verify if it's allowed Name
            if (allowedName(data['name'])):
                break
            else:
                print("[!] Name should be three chars minimum")
                pass

        # return a class with the New player data
        return Player(data['name'])