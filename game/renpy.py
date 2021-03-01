
class Renpy:
    def __init__(self):
        pass

    def say(self, who="Dev", what="nothing"):
        print(who, "said", what)

    def jump(self, label):
        print("We jumped into", label)

    def show(self, who, position="left"):
        print(who, "is showed at", position)


    def Character(self, name, color="#ffffff", *args, **kwargs):
        pass

    def log(self, text):
        print("LOG:", text)

renpy = Renpy()
