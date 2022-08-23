def cTree(aBase):
    for x in range(1,aBase):
        if x %2:
           
            print('{:^{}}'.format('*'*x,aBase))


cTree(int(input('Base : ')))
