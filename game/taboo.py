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






### We initialize the taboos
taboo_nude = Taboo("Nudity")
taboo_wear = Taboo("Wearing")
taboo_sex = Taboo("Sex")
taboo_nosex = Taboo("No Sex")
taboo_bj = Taboo("Blowjob")
taboo_nobj = Taboo("No Blowjob")
taboo_kill = Taboo("Killing")
taboo_save = Taboo("Saving")
taboo_egality = Taboo("Equality")
taboo_slavery = Taboo("Slavery")
taboo_capitalism = Taboo("Capitalism")
taboo_socialism = Taboo("Socialism")
taboo_test = Taboo("test")

### We set the contraries
taboo_nude.SetContrary(taboo_wear)
taboo_sex.SetContrary(taboo_nosex)
taboo_bj.SetContrary(taboo_nobj)
taboo_kill.SetContrary(taboo_save)
taboo_egality.SetContrary(taboo_slavery)
taboo_capitalism.SetContrary(taboo_socialism)
