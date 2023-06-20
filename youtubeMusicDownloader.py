import pafy

url = 'https://youtu.be/Q6tlxZUt14A'

video=pafy.new(url)



streams = video.audiostreams

for i in streams:
    print(i.extension, ' ', i.get_filesize)
    


