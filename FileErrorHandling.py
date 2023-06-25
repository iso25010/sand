try:
    f=open('./you/youtube.txt',mode='r',encoding='UTF-8')
    print(f.read())
except FileNotFoundError:
    print('./you/youtube.txt does not exist')


