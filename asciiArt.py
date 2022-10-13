import glob
import pywhatkit

g=glob.glob('*.jpg')
for f in g:
    pywhatkit.image_to_ascii_art(f,f[:-4])

