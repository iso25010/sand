
class BinSearch():
    def __init__(self,aFile):
        #starting position where the reading of a file starts from
        self.position=0
        #the file with a sequence of numbers
        self.file=aFile
        #initial setUp for the reading
        self.setPosition(self.position)
        self.resetBuffer()
        #a current number of the field of numbers
        self.counter=0
        #how many members contains the buffer
        self.members=1000
        #left interval ... counter, position
        self.left=[0,0]
        #self.counter, self.file.tell() .... counting how manny numbers has the sequence
        self.right=self.howMany()
        #reset counter and setUp 0 position of the file
        self.counter=0
        self.setPosition(0)
        #a middle of the interval
        self.middle=[0,0]
        #the number we are looking for ...
        self.look=self.inputNumber()
        
        
    def search(self):
        #middle of the interval, position ... initial setUp
                
        while self.getLN()<=self.getRN():
            self.resetBuffer()
            #self.middle=[self.getRN()//2,0]
            self.setMN((self.getLN()+self.getRN())//2)
            #set counter at the left interval    
            self.counter=self.getLN()    
            #set position in the file
            if self.getLN() != 0:
                self.position=self.getLP()+1
            else:
                self.position=self.getLP()
            self.setPosition(self.position)
            self.midNumber=self.findMidNum()
            if self.look==self.midNumber:
                #we found the number
                return self.midNumber,self.getMN(),self.getMP()
            #looking number > middle number -> shift the interval to the right
            if self.look>self.midNumber:
                self.setLN(self.getMN())
                self.setLP(self.getMP())
               
            #looking number < middle number -> shift the interval to the left
            if self.look<self.midNumber:
                self.setRN(self.getMN())
                self.setRP(self.getMP())
        return 0
            
            
        


    def setPosition(self,p):
        self.file.seek(self.position)

    def getRN(self):
        return self.right[0]
    def getRP(self):
        return self.right[1]

    def getLN(self):
        return self.left[0]
    def getLP(self):
        return self.left[1]
    
    def getMN(self):
        return self.middle[0]
    def getMP(self):
        return self.middle[1]

    def setRN(self,r):
        self.right[0]=r
    def setRP(self,p):
        self.right[1]=p

    def setLN(self,l):
        self.left[0]=l
    def setLP(self,p):
        self.left[1]=p
    
    def setMN(self,l):
        self.middle[0]=l
    def setMP(self,p):
        self.middle[1]=p

    def resetBuffer(self):
        self.buffer=None
        self.backUp=None

    def findMidNum(self):
        #within the current interval finds the middle number
        
        check=True
        while (self.counter < self.getMN()) and check:
            check=self.readNumbers()
        if self.buffer: 
            indexOfPosition=[i for i,x in enumerate(self.buffer) if x==';']
            index=len(indexOfPosition) -1 - (self.counter-self.getMN())
            if index==0:
                midNumber=self.buffer[:indexOfPosition[index]]
                #doplnit neuplne cislo, ktere ma kus v BackUp
                if self.backUp:
                    if self.backUp[-1] != ';':
                        beginI=self.backUp.rfind(';')
                        begin=self.backUp[beginI+1:]
                        begin+=midNumber
                        midNumber=begin             
            else:          
                midNumber=self.buffer[indexOfPosition[index-1]+1:indexOfPosition[index]]
            #a position for the middle number in the interval
            self.setMP(indexOfPosition[index]+self.backCounter)
            
            return int(midNumber)
        return -1

    def readNumbers(self):
        self.backUp=self.buffer
        self.backCounter=self.file.tell()
        self.buffer=self.file.read(self.members)
        self.counter += self.buffer.count(';')
        if self.buffer:
            return True
        else:
            return False

    def howMany(self):
        while self.readNumbers():
            pass
        #last=self.backUp.split(';')[-2]
        return [self.counter, self.file.tell()]

    def inputNumber(self):
        return int(input('What number are you looking for? :'))

    

fSet='/media/zed/NTB/Dev/set.txt'
fs='set.txt'
t='testBin.dat'

with open(t,mode='rt') as f:
    bs=BinSearch(f)
    t=bs.search()
    print(' self.midNumber {0},self.getMN(){1},self.getMP(){2}'.format(t[0],t[1],t[2]))
    
   