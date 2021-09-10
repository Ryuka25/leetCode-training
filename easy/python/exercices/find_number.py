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
