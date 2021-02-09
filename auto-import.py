import sys
import os
import random
### Import our modules
import packages.files as fme ### fme for file module of me

def main():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:] # First element of args is the file name

    if len(args) == 0:
        print('You have not passed any commands in!')
    else:
        for a in args:
            if a == '--help':
                print('Basic command line program')
                print('Options:')
                print(' --help -> show this basic help menu.')
                print(' --monty -> show a Monty Python quote.')
                print(' --veg -> show a random vegetable')
            elif a == '--monty':
                print('He’s not the Messiah—he’s a very naughty boy')
            elif a == '--veg':
                print(random.choice(['Tomato','Reddis','Carrot', 'Potato', 'Turnip']))
            elif a == '--manage-imports':
                files_dir = fme.SearchFiles("game/")
                for file in files_dir:
                    fme.ManageFileImports(file, "game/", ".")
                    print(f"[auto-import.py] {file}'s imports checked and managed")
            else:
                print('Unrecognised argument.')
path = r"game/"
files_dir = []
if __name__ == '__main__':
    main()
