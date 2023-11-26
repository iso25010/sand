li=['Karel','Petr','Jana','Honza','Zuzka','Pavel','Jirka','Klara','Ondra','Eva']
para=[[name,len(name)] for name in li]
print(para)
sortedPara=sorted(para,key=lambda x:x[1])
print(sortedPara)