#! python3

print("""
  ____      _            _       _             
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | (__| |_| | | (_| | || (_) | |   
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

                    - by Ryuka (2021)
 """)
 
class calculator:

    def getOperator(self):
        choosing = True
        while choosing:
            self.operator = int(input("Please enter a number for the operation: "))
            if (self.operator == 1):
                self.operatorSign = "+"
                break
            elif (self.operator == 2):
                self.operator = "-"
                break
            elif (self.operator == 3):
                self.operatorSign = "*"
                break
            elif (self.operator == 4):
                self.operatorSign = "/"
                break
            else:
                print("[*] ERROR ! Please choose a correct number for the operation ...")
                pass

    def getNumbers(self):
        self.number1 = float(input("Enter the first number\t: "))
        self.number2 = float(input("Enter the second number\t: "))

    def addition(self):
        self.result = self.number1 + self.number2

    def subtraction(self):
        self.result =  self.number1 - self.number2

    def multiplication(self):
        self.result = self.number1 * self.number2

    def division(self):
        self.result = self.number1 / self.number2

    def showResult(self):
        print(f"[*] Result of operation : ' {self.number1} {self.operatorSign} {self.number2} = {self.result}' ")

    def execute(self):
        if (self.operator == 1):
            self.addition()
        elif (self.operator == 2):
            self.subtraction()
        elif (self.operator == 3):
            self.multiplication()
        elif (self.operator == 4):
            self.division()

class programmsBanner:

    def __init__(self):
        self.content = "[*] This programms allows user to make a binary operations with:\n\t1- Addition\n\t2- Subtraction\n\t3- Multiplication\n\t4- Division"

    def show(self):
        print(self.content)

def main():
    banner = programmsBanner()
    calc = calculator()
    run = True

    print("[*] Begin of script")

    banner.show()
    while run:
        calc.getNumbers()
        calc.getOperator()
        calc.execute()
        calc.showResult()
        reRun = (input("[!] Would you like to re-use this calculator ? (y/n): ")).lower()
        if (reRun in ["yes", "y"]):
            pass
        elif (reRun in ["no","n"]):
            break

    print("[*] End of script")
    
# Cette bout de code permet de choisir la fonction main()
# Comme étant une fonction principale

if __name__ == "__main__":
    main()