from pytube import YouTube

link = input("Link musica: ")
yt = YouTube(link)

yt.streams.filter(only_audio=True).first().download(r"C:\Users\Matheus\Documents\_Jogo in Python")