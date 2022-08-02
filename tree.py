def tree(aString):
    if aString:
        tree(aString[:-1])
        print(aString)

def tree1(aChar,aNumber):
    for x in range(aNumber):
        print(aChar*x)



tree('*****')
tree1('*',6)
