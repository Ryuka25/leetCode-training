#! python3

print("""
       _                                       
 _ __ | |__     ___  __ _ _   _  __ _ _ __ ___ 
| '_ \| '_ \   / __|/ _` | | | |/ _` | '__/ _ \\
| | | | |_) |  \__ \ (_| | |_| | (_| | | |  __/
|_| |_|_.__/___|___/\__, |\__,_|\__,_|_|  \___|
          |_____|      |_|                     
                    
                    - by Ryuka (21/08/21)
""")

#Ecrire un programme qui demande un nombre à l’utilisateur, puis qui calcule et affiche le carré de ce nombre.

def squareNumber(number):
    print("[*] Process squareNumber")
    return pow(number,2)
    print("[*] Process Finished")

def main():
    print("[*] Begin of script")
    
    number = float(input("Enter the number please\t: "))
    
    squaredNumber = squareNumber(number)
    
    print("[*] Process Finished")
    print(f"[*] The square of the number {number} is {squaredNumber}")
    print("[*] End of script")

if __name__ == "__main__":
    main()
