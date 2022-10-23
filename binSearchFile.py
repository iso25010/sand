
from turtle import begin_fill


class BinSearch():
    def __init__(self,aFile):
        self.position=0
        self.file=aFile
        self.setPosition(self.position)
        self.resetBuffer()
        self.counter=0
        self.members=1000
        self.left=0,0
        self.right=self.howMany()
        self.middle=self.getRN()//2,0
        #self.look=self.inputNumber()
        self.counter=0
        self.setPosition(0)
        self.midNumber=self.findMidNum()

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
           # print(self.counter,'<= ',self.getMN())
        if self.buffer:
            index=self.counter-self.getMN()
            indexOfPosition=[i for i,x in enumerate(self.buffer) if x==';']
            print('indexPosition:{0}\n index:{1}\n buffer:{2}\n counter:{3}\n'.format(indexOfPosition,index,self.buffer,self.counter))
            if index==0:
                midNumber=self.buffer[:indexOfPosition[index]]
                #musime osetrit neuplne cislo, ktere ma kus v BackUp
                if self.backUp:
                    if self.backUp[-1] != ';':
                        beginI=self.backUp.rfind(';')
                        begin=self.backUp[beginI+1:]
                        begin+=midNumber
                        midNumber=int(begin)
                print(self.buffer)
                
            else:
                
                midNumber=int(self.buffer[indexOfPosition[index-1]+1:indexOfPosition[index]])
            return midNumber
        return -1





    def readNumbers(self):
        self.backUp=self.buffer
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
        return self.counter+1, self.file.tell()

    def inputNumber(self):
        return int(input('What number are you looking for? :'))

    



with open('set.txt',mode='rt') as f:
    bs=BinSearch(f)
    print(bs.midNumber)

    #f.seek(position-1)
    #print(f.read(1))

#print(last, ' ', number, ' ', position)