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


def ManageFileImports(file, game_path, log_path):
    modules_list = []
    imports_line = SearchInFile("import", f"{game_path}{file}")
    game_modules_path = game_path.replace("../", "").replace("/", ".")
    game_files = SearchFiles(game_path)
    modules_name_from_files = []
    for module_name in game_files:
        modules_name_from_files.append(module_name.replace(".py", ""))
    for import_statement in imports_line:
        if import_statement.startswith("from"):
            modules_list.append(import_statement.split(" import").pop(0).replace("from ", ""))
    for module in modules_list:
        try:
            exec(f"""import {game_modules_path}{module}""")
        except ModuleNotFoundError:
            pass
        except ImportError:
            if module in modules_name_from_files:
                open(f"{log_path}/log.txt", "w").write(f"ImportError: In-game module \"{module}\" can't be found")
            else:
                try:
                    os.system("python -m pip install --user {}".format(module))
                except Exception:
                    print(f"We can't import the {module} module")
