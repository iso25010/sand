from types import NoneType


class Array:
    def __init__(self,y,x):
        self.pole=[[None for j in range(y)]  for i in range(x)]
        
    def getPole(self):
        return(self.pole)

    def getCell(self,a,b):
        return(self.getPole()[a][b])

    def setCell(self,a,b,aValue):
       try:
        self.pole[a][b]=aValue
       except IndexError:
        print('out of range') 
    
c=int(input('Velost pole x: '))
d=int(input('Velost pole y: '))

a=Array(c,d)
z=0
while z != 'stop':
    x=int(input('x: '))
    y=int(input('y: '))
    v=input('a value: ')
    a.setCell(x,y,v)
    print(a.getPole())
    z=input('Next action? stop=>end of the program')


