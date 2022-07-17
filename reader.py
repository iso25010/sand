from glob import glob
class Reader:
    def __init__(self,aMask):
        self.mask=aMask

    def getMask(self):
        return(self.mask)
    
    def getContent(self):
        g=glob(self.getMask())
        return(g)




