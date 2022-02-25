class Fighter(object):
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.atk = 10
        self.res = 5
        self.stats = {"Level": self.level,"Attack": self.atk,"Resistance": self.res,"Experience" : self.exp}