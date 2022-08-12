def tree(aString):
    if aString:
        tree(aString[:-1])
        print(aString)

def tree1(aChar,aNumber):
    aParagraph=''
    for x in range(aNumber):
        aParagraph += (aChar*x) +'\n'
    return aParagraph



tree('*****')
aText=tree1('*',6)

print(aText)
