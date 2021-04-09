#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def SearchFiles(path):
    files_in_dir = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files_in_dir.append(file)
    return files_in_dir

def SearchInFile(name, file):
    file = open(file).readlines()
    chosen = []
    for line in file:
        if name in line:
            if not line.startswith("#"):
                chosen.append(line)
    return chosen

#def SearchInFile(name, file):
#    global breakline_sign, open_signs, end_signs
#    file = open(file).readlines()
#    print(file)
#    chosen = []
#    temp_chosen = []
#    for line in file:
#        temp_line = str(line).split()
#        if name in temp_line:
#            if not "".join(temp_line).startswith("#"):
#                for special_element in open_signs:
#                    if special_element in temp_line:
#                        print("special_element found:", str(special_element))
#                        x = 1
#                        while_line = line
#                        while end_signs[special_element] not in while_line:
#                            temp_chosen.append(file[file.index(line)+x])
#                            while_line = file[file.index(line)+x]
#                            print(while_line)
#                            x =+ 1
#                chosen.append(line)
#    return chosen

def ManageFileImports(file, game_path, log_path, log_name):
    modules_list = []
    imports_line = SearchInFile("import", f"{game_path}{file}")
    game_modules_path = game_path.replace("../", "").replace("/", ".")
    game_files = SearchFiles(game_path)
    game_files_module_name = [game_files_name.replace(".py", "") for game_files_name in game_files]
    modules_name_from_files = []
    for module_name in game_files:
        modules_name_from_files.append(module_name.replace(".py", ""))
    for import_statement in imports_line:
        if import_statement.startswith("from"):
            modules_list.append(import_statement.split(" import").pop(0).replace("from ", ""))
    for module in modules_list:
        try:
            exec(f"""import {game_modules_path}{module}""")
            print(f"[{log_name}] {file}'s imports checked and managed")
        except Exception as error:
            if module in game_files_module_name:
                print(f"[{log_name}] " + "{" + file + "}" + f" found {module} internal module, we pass")
            elif error == ModuleNotFoundError:
                print(f"[{log_name}] {file}, Something went wrong: {error}")
            elif error == ImportError:
                if module in modules_name_from_files:
                    open(f"{log_path}/log.txt", "w").write(f"ImportError: In-game module \"{module}\" can't be found")
                else:
                    try:
                        os.system("python -m pip install --user {}".format(module))
                    except Exception:
                        print(f"We can't import the {module} module")
