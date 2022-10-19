
import pywhatkit

with open('doc.txt',mode='r',encoding='utf-8') as s:
    str=s.read()
    
pywhatkit.text_to_handwriting(str,"doc.png")