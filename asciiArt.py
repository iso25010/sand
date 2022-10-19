import glob
import pywhatkit

g=glob.glob('*.jpg')
for f in g:
    pywhatkit.image_to_ascii_art(f,f[:-4])
    s=open(f[:-4]+'.txt',mode='r')
    print(s.read())
    s.close()

with open('doc.txt',mode='r',encoding='utf-8') as s:
    str=s.read()
    pywhatkit.text_to_handwriting(str,"doc.png")


