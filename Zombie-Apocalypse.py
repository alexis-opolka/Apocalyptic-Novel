import os
import sys

def Arguments():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:] # First element of args is the file name
    global larg

    if len(args) == 0:
        os.system("python3 auto-import.py --handle-imports")
    else:
        for a in args:
            if a == "-dev":
                os.system("python3 auto-import.py --handle-imports-dev")
            if a == "-i":
                larg = a
            else:
                larg = ""

larg = None

if __name__ == "__main__":
    Arguments()
    os.chdir("game/")
    os.system(f"python3 {larg} main.py")

r = "test"
