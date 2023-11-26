def fob(f,fn=[0,1]):
    if f==1:
        print ('F({0}) -> {1}'.format(len(fn)-1,fn))
        return 
    if f==0:
        print([0])
        return 
    if f<0:
        return
    fn.append(fn[-1]+fn[-2])
    #print (fn)
    fob(f-1,fn)

fob(int(input('Enter a number: ')))
