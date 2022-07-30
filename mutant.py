class Mutant:
    def __init__(self):
        self.aSet={i for i in 'Hi Mutant'}
        self.aList=[x for x in 'Ahoj']
    def getS(self):
        return(self.aSet)
    def getL(self):
        return(self.aList)
    def getCopyL(self):
        return(self.aList.copy())
    def getCopySasL(self):
        return(list(self.getS()))

m=Mutant()

print(m.getS())
print(id(m.getL()))
cL=m.getCopyL()
cL.reverse()
print(m.getL())
print(id(cL))
m.getCopySasL().reverse()
print(m.getS())