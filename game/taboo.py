"""
    Module containing all the differents Taboos and their class
"""
class Taboo:

    global_list = None

    def setGlobalList(list):
        Taboo.global_list = list

    def addInGlobalList(taboo):
        Taboo.global_list.append(taboo)

    def removeFromGlobalList(taboo):
        if taboo in Taboo.global_list:
            Taboo.global_list.pop(Taboo.global_list.index(taboo))
        else:
            raise KeyError("The Taboo() object given isn't in the global list, please verify")

    def __init__(self, name, contrary=None, same=None):
        Taboo.addInGlobalList(self)
        self.name = name
        if type(contrary) is Taboo or contrary is None:
            self.contrary = contrary
        else:
            print("The contrary isn't a Taboo() object")
            return

    def setContrary(self, contrary):
        self.contrary = contrary
        contrary.contrary = self

    def getContrary(self):
        if self.contrary != None:
            return self.contrary
        return None
