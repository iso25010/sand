from pytube import YouTube

with open('./you/youtube.txt',mode='r',encoding='utf-8') as f:
    for aVideo in f:
        yt = YouTube(aVideo)
        videos=yt.streams.filter(only_audio=True)
        for aSong in videos.order_by('abr'):
            aSong.download('./you/')

        

