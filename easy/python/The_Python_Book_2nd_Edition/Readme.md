# The_Python_Book_2nd_Edition

This is my personnal Practises with the book : "The_Python_Book_2nd_Edition.pdf"  

## Getting Started

```bash
mkdir Python            # Creer un dossier pour les stocker les différentes scripts
cd Python               # Changer le dossier courrant vers le dossier qu'on vient de créer
touch hello_world.py    # Creer un fichier "hello_world.py"
chmod +x hello_world.py # Rendre le fichier exécutable
vim hello_world.py      # Editer le fichier
```

hello_world.py

```python
#!/usr/bin/python 
# -*- conding:Utf-8 -*-

##################
# hello_world.py #

def greatingPython():
    "This function print the python basic print"
    print("Hello World!")       # Print "Hello World" in the current shell session

def main():
    greatingPython()
    pass

if __name__ == "__main__":
    main()
```