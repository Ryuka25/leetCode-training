from .Database import *

class User :

    def __init__(self, data) -> None:
        User.__hydrate(self,data)
        pass

    def __hydrate(self,data):

        self.__id = data[0]
        self.__username = data[1]
        self.__password = data[2]
        self.__email = data[3]
    
    def getUsername(self):
        return self.__username

    def __getPassword(self):
        return self.__password

    def getEmail(self):
        return self.__email

    def getId(self):
        return self.__id

    def getAllUser():
        "Retourne une liste contenant tout les utilisateurs"
        stmt = Database.getInstance()
        sql = "SELECT * FROM users"
        stmt.execute(sql)

        userList = []

        for userData in stmt:
            userList.append(User(userData))

        return userList

    def getUserByID(id):
        "Retourne l'utilisateur dont l'ID est spécifiée!"
        users = User.getAllUser()
        for user in users:
            if str(user.getId() == str(id)):
                return user
        
        return 0
    
    def getUserByUsername(username):
        "Retourne l'utilisateur dont l'username est spécifiée!"
        users = User.getAllUser()
        username = User.normalize(username)
        for user in users:
            currentUsername = User.normalize(user.getUsername())
            if  currentUsername == username:
                return user
            
        return 0

    def checkMatch(inputUsername:str, inputPassword:str):
        "Test si le nom d'utilisateur donée en paramètre correspond au mot de passe entrée!"
        testedUser = User.getUserByUsername(inputUsername)
        if (testedUser == 0):
            result = False
        else:
            if (testedUser.__getPassword() == inputPassword):
                result = True
            else:
                result = False

        return result
            
    def normalize(string):
        "Normalise la chaine de caractère pour les différentes utilisations"
        return str(string).lower()