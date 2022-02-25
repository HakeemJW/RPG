class Cleric(object):
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.atk = 5
        self.res = 10
        self.stats = {"Level": self.level,"Attack": self.atk,"Resistance": self.res,"Experience" : self.exp}