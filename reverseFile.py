class Reverse:
    def __init__(self):
        self.stack=list()

    def push(self,anObject):
        self.stack.append(anObject)

    def pop(self):
        return self.stack.pop(-1)

    def pushStack(self,inFile):
        with open(inFile, mode='rt') as inF:
            char=inF.read(1)
            while char!='':
                self.push(char)
                char=inF.read(1)  

    def emptyStack(self,outFile):
        with open(outFile,mode='wt') as outF:
            while self.stack:
                aChar= self.pop()
                outF.write(aChar)
        
    def printStack(self):
        print(self.stack)



r=Reverse()

aFile=str(input('Input a source file: '))

try:
    r.pushStack(aFile)
    try:
        aFile=str(input('Input an output file: '))
        r.emptyStack(aFile)
    except:
        print('Problem with the output file')
except:
    print('Problem with the input file')


