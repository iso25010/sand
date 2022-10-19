def search(x,y):
    l=0
    r=len(x)-1
    while l<=r:
        s=int((l+r)/2)
        if y==x[s]:
            return(x[s],s)
        if y>x[s]:
            l=s+1
        else:
            r=s-1
    return(0,0)

r=int(input('Zadej pocet: '))
x=[i for i in range(r)]
y=int(input('Zadej cislo: '))
a,b=search(x,y)
print(a,b)

