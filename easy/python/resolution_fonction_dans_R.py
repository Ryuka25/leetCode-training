#! usr/bin/python3

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
print("\nThis program allow user to resolve an 2nd degree function ( ax^2 + bx + c ) in R\n")
print("\n[*] Begin script ... ")

a = float(input("\nEnter the 'a' value \n> "))
b = float(input("\nEnter the 'b' value \n> "))
c = float(input("\nEnter the 'c' value \n> "))

delta = (b*b) - 4*(a*c)
print("[*] Calculating delta ...")
print(f"[*] Delta value is {delta}")

if (delta > 0):
    print("[*] Delta is greater than zero")

# TODO: @Ryuka25 Finish this now!

print ("\n[*] End of script !")
