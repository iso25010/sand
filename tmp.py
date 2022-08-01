l=[[i + j*10 for i in range(10)] for j in range(10)]

for x in range(len(l)):
    print([i for i in l[x] if i<3])

