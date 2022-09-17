class cTree():

    Width=0
    Iteration = 0

    
    def __init__(self,String):
        self.aString=String
        if cTree.Iteration==0:
            cTree.Width=len(self.aString)
            
        cTree.Iteration+=1
        if self.aString:
            cTree(self.aString[:-1])
        print(self)
           

    def __str__(self):
        
        return(self.aString.center(cTree.Width))
        

cTree(input('Input a string for christmas tree: '))

