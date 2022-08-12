class Reverse:
    def __init__(self):
        self.stack=list()
    def push(self,anObject):
        self.stack.append(anObject)
    def pop(self):
        return self.stack.pop(-1)
    def pushStack(self,inFile):
        with open(inFile, mode='r') as inF:
            for char in inF:
                self.push(char)
    def emptyStack(self,outFile):
        with open(outFile,mode='w') as outF:
            while self.stack:
                aChar= self.pop()
                outF.write(aChar)
        
    def printStack(self):
        print(self.stack)



r=Reverse()
aFile='c:\\Users\\zd004868\\Documents\\git\\array.py'
r.pushStack(aFile)
r.printStack()
r.emptyStack('c:\\Users\\zd004868\\Documents\\git\\meat.txt')
r.printStack()

