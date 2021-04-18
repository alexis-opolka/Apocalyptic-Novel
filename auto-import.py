import sys
import os
import random
### Import our modules
import packages.files as fme ### fme for file module of me


def main():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:] # First element of args is the file name
    global path

    if len(args) == 0:
        print('You have not passed any commands in!')
    else:
        for a in args:
            if a == '--help':
                print('Basic command line program')
                print('Options:')
                print(' --help -> show this basic help menu.')
                print(' --handle-imports -> launch script to handle imports.')

            elif a == '--handle-imports':
                files_dir = fme.SearchFiles("game/")
                for file in files_dir:
                    fme.ManageFileImports(file, "game/", ".", "auto-import.py")

            elif a == '--handle-imports-dev':
                files_dir = fme.SearchFiles("game/")
                for file in files_dir:
                    fme.ManageFileImports(file, "game/", ".")
                    print(f"(DEV)[auto-import.py] {file}'s imports checked and managed")
                os.system("py game/__dev__.py")

            elif a == '--handle-imports-testrun':
                files_dir = fme.SearchFiles("game/")
                for file in files_dir:
                    fme.ManageFileImports(file, "game/", ".", "[auto-import.py]")
                    print(f"[auto-import.py] {file}'s imports checked and managed'")
                print("We're going to run the main.py file to ensure the well importation of libs...")

                try:
                    os.system("py game/main.py")
                    os.system("cls")
                    print("Apparently, the importation went well.")

                except Exception:
                    print(f"Something went wrong, error code:\n{Exception}")

            elif a == "--testrun":
                os.system(f"py {path}main.py")

            else:
                print('Unrecognised argument, try --help for more informations about commands.')
path = r"game/"
files_dir = []
if __name__ == '__main__':
    main()
