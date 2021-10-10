#! usr/bin/python3

import math as mt

print("""
/********************************************/
/*  ____   __   __  _   _   _  __     _     */
/* |  _ \  \ \ / / | | | | | |/ /    / \    */
/* | |_) |  \ V /  | | | | | ' /    / _ \   */
/* |  _ <    | |   | |_| | | . \   / ___ \  */
/* |_| \_\   |_|    \___/  |_|\_\ /_/   \_\ */
/*                                          */
/********************************************/
""")
print("This program allow user to resolve an 2nd degree function ( ax² + bx + c ) in R\n")
print("[*] Begin script ... ")

a = float(input("Enter the 'a' value \n> "))
b = float(input("Enter the 'b' value \n> "))
c = float(input("Enter the 'c' value \n> "))

print(f"Your functin is like: {a}x² + {b}x + {c} ")

delta = (pow(b,2)) - 4*(a*c)
print("[*] Calculating delta ...")
print(f"[*] Delta value is {delta}")

if (delta > 0):

    sqrtDelta = mt.sqrt(delta) # Calculate the square root of Delta

    print("[*] Delta is greater than zero")
    solutions = [
        (-b + sqrtDelta) / (2*a),
        (-b - sqrtDelta) / (2*a)
    ]

# TODO: @Ryuka25 Finish this now!

elif (delta == 0):
    
    sqrtDelta = mt.sqrt(delta) # Calculate the square root of Delta

    print("[*] Delta is equal to zero")
    solutions = [
        (-b + sqrtDelta) / (2*a)
    ]

elif (delta < 0):
    print("[*] Delta is less than zero")
    solutions = [
        "No solution in R"
    ]
else:
    print("[*] FATAL ERROR OCCURED, this programs will end!")

print(f"[*] {len(solutions)} Solution was found ...")

print("""
/*******************/
/* Begin Solutions */
/*******************/
""")

print(solutions)

print("""
/*****************/
/* End Solutions */
/*****************/
""")

print ("[*] End of script !")
