from random import randint
import os

class Player :
    " Handle the Player "
    __score = 0
    life = 7

    def __init__(self,name):
        self.name = name
    
    def upScore(self, upper):
        self.__score = self.__score + upper
    
    def getScore(self):
        return self.__score

run = True

while run:
    os.system("clear")

    print("\n\t\t🤨️ GUESS ME - Challenge ⁉️\n")

    print("\n\t=============[BEGIN GAME]=============\n\n")

    ################################
    #        INITIALIZATION        #
    ################################

    playerList = [] # Handle the player list
    scoreList = []

    # GET INFORMATION ABOUT A SET:

    numberOfPlayer = int(input('How Many Player For this set (1/2) ? > '))

    ############################
    #        BEGIN GAME        #
    ############################

    for i in range(numberOfPlayer):

        # Get a new player data and store it to the player List
        playerName = str(input('Enter Player Name: '))
        player = Player(playerName)
        playerList.append(player)

        # Set a target number for the curent player
        target = randint(0,100)

        # Handle the match between user Input
        match = False

        # Loop for the query
        while (player.life != 0):

            # Show current player life / attempt
            print(f"\n{player.name} Life = ", end="")
            for i in range(player.life):
                print("❤️ ", end="")

            # GET USER INPUT
            userIn = int(input(f"\n[?]  Input your number here : "))

            # TEST USER INPUT
            if (userIn == target):

                print("\n[*]  🎉️ There is a match\n")
                match = True
                player.upScore(player.life+10)

                # Break the query loop
                break
            
            # In this block of case, the player don't match...
            elif (userIn > target):
                print("[*] ⏬️ Might choose a low number\n")
            elif (userIn < target):
                print("[*] ⏫️ Might choose a great number\n")

            player.life -= 1

        # In this case, the player is game over
        if (not match):
            difference = (abs(userIn - target))
            if ((difference) < 10):
                player.upScore(10)
            elif ((difference) < 20):
                player.upScore(5)

            print(f"\nGAME OVER 💀️")

        # Show the correct number
        print(f"The correct number has been: {target}")

        # Store the curent player score in the score list:
        scoreList.append(player.getScore())

        print("\n\n\t\tThe player {} score is {}".format(player.name, player.getScore()))
        print("\n\t=============[END OF THE CURENT SET]=============\n")

    # Handle the winner at the end of the set

    if (len(playerList) == 1):
        winner = playerList[0]
    
    elif (len(playerList) == 2):
        if (playerList[0].getScore() > playerList[1].getScore()):
            winner = playerList[0]
        elif (playerList[0].getScore() < playerList[1].getScore()):
            winner = playerList[1]
        else:
            winner = Player("none 🙄️ of booth")

    else:
        winner = Player("none ! We haven't handle this number of player before!")

    print(f"\n 🏆️ The winner is {winner.name}")

    reRun = str(input('\nWould you like to reRun the game ? (y/n) > '))

    if reRun == 'y' :
        run = True
    elif reRun == 'n': 
        run = False

os.system("clear")
print("\n... You just exit the GUESS ME CHALLENGE ...")