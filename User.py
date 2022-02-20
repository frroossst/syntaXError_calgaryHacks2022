class User: 
    def __init__(self, name="", WOF=0, minTime=0):
        self.name = name 
        self.WOF = WOF 
        self.minTime = minTime

    def get_name(self):
        return self.name

    def get_WOF(self): 
        return self.WOF

    def get_minTime(self): 
        return self.minTime 

