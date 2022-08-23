def tree(aString):
    if aString:
        tree(aString[:-1])
        print(aString)





tree('*****')
