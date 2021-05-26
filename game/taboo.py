import lists

"""
    Module containing all the differents Taboos and their class
"""
class Taboo:
    def __init__(self, name, contrary=None, same=None):
        self.name = name
        if type(contrary) is Taboo or contrary is None:
            self.contrary = contrary
        else:
            print("The contrary isn't a Taboo() object")
            return
        lists.TabooList.append(self)

    def SetContrary(self, contrary):
        self.contrary = contrary
        contrary.contrary = self
