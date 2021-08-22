#! python3

print("""
  ____      _            _       _             
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | (__| |_| | | (_| | || (_) | |   
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

                    - by Ryuka (2021)
 """)

def getNumbers():
    global number1
    global number2
    number1 = float(input("Enter the first number\t: "))
    number2 = float(input("Enter the second number\t: "))

def addition(number1, number2):
    print("[*] Process addition")
    global result
    result = number1 + number2
    print ("[*] Result Found ")

def subtraction(number1, number2):
    print("[*] Process soustraction")
    global result
    result = number1 - number2
    print ("[*] Result Found ")

def multiplication(number1, number2):
    print("[*] Process multiplication")
    global result
    result = number1 * number2
    print ("[*] Result Found ")

def division(number1, number2):
    print("[*] Process division")
    global result
    result = number1 / number2
    print ("[*] Result Found ")


def main():
    print("[*] Begin of script")
    print("[*] This programms allows user to make a binary operations with:\n\t1- Addition\n\t2- Subtraction\n\t3- Multiplication\n\t4- Division")
    operator = int(input("Please enter a number for the operation: "))

    getNumbers()

    if (operator == 1):
        addition(number1, number2)
    elif (operator == 2):
        subtraction(number1, number2)
    elif (operator == 3):
        multiplication(number1, number2)
    elif (operator == 4):
        division(number1, number2)
    else:
        print("[*] ERROR ! Please choose a correct number for the operation ...")
        exit()

    print("[*] Process finished")
    print(f"[*] Result of operation between {number1} and {number2} is {result}")
    print("[*] End of script")
    
# Cette bout de code permet de choisir la fonction main()
# Comme étant une fonction principale

if __name__ == "__main__":
    main()
