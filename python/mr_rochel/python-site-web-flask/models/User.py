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

    def getPassword(self):
        return self.__password

    def getEmail(self):
        return self.__email

    def getId(self):
        return self.__id

    def getAllUser():
        "Retourne une liste contenant tout les utilisateurs"
        stmt = Database.getCursor()
        sql = "SELECT * FROM users"
        stmt.execute(sql)

        userList = []
        allUserData = stmt.fetchall()

        for userData in allUserData:
            userList.append(User(userData))

        return userList
    
    def getUserByUsername(username):
        "Retourne l'utilisateur dont l'username est spécifiée!"

        myCursor = Database.getCursor()
        sql = "SELECT * FROM users WHERE username = '%s' ;" %username
        myCursor.execute(sql)
        myResult = myCursor.fetchone()
        
        user = User(myResult)

        return user        

    def checkMatch(inputUsername:str, inputPassword:str):
        "Test si le nom d'utilisateur donée en paramètre correspond au mot de passe entrée!"
        testedUser = User.getUserByUsername(inputUsername)
        if (testedUser == 0):
            result = False
        else:
            if (testedUser.getPassword() == inputPassword):
                result = True
            else:
                result = False

        return result
            
    def normalize(string):
        "Normalise la chaine de caractère pour les différentes utilisations"
        return str(string).lower()