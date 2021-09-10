from random import *

class Game:

    def _createRandomNumber()->int:
        "Return a random number between [0;100]"
        number = randint(a=0,b=100)

        return number

    def _validNumber(self, number:int)->bool:
        "Make sure that we have a valid number"
        try:
            number = int(number)
            if (number < 0):
                result = False
                print("\n[!] Tips : Number should be greater or equalt to 0")
            else:
                result = True
                print("[+] Number is conform to a typical response")
                
        except:
            print("\n[!] Only Integer number are allowed")
            result = False

        return result

    def _evaluateNumber(self, target:int, number:int)->bool:
        "Evaluate the number to the target number"
        result = False
        if (number == target) :
            print("[Warning] You have a match !")
            result = True
        elif number in range((target-50),(target+50+1)):
            print("[*] Oh no! You are so cold")
        elif number in range((target-20), (target+20+1)):
            print("[*] Continue ! You are in the right way")
        elif number in range((target-7), (target+7+1)):
            print("[*] Subarashii ! You are so hot")
        else:
            print("[ERROR] Something wrong has happened here!")

        return result
