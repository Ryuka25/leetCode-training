#!/usr/bin/python 
# -*- conding:Utf-8 -*-

##############################################
# The_python_Book_2nd_Edition/hello_world.py #

def greatingPython():           # Creating a new function
    "This function print the python basic print"
    print("Hello World!")   # Print "Hello World" in the current shell session

def main():                     # Creating the principal function
    greatingPython()            # Calling the greatingPython() function into the main()
    pass                        # Pass to the next thread

if __name__ == "__main__":      # compare the current function name to '__main__'
    main()                      # Calling the main() function