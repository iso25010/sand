import os
from pprint import pprint


top=input('Input top dir: ')
ls=list()

for dirPath,dirs,files in os.walk(top):
    try:
        splitPath=dirPath.split('/')
        parent=splitPath[-2]       
    except IndexError:
        parent='' #bloody root
    ls.append({'parent':parent,'dirPath': dirPath, 'dirs':dirs,'files':files})

pprint(ls)

