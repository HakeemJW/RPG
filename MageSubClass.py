class Mage(object):
    def __init__(self):
        self.level = 1
        self.exp = 0
        self.atk = 15
        self.res = 0
        self.stats = {"Level": self.level,"Attack": self.atk,"Resistance": self.res,"Experience" : self.exp}
