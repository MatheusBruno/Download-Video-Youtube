from pytube import YouTube
link = input("Download Link: ")
url = input("Caminho: ")
url = str(url).replace('\\','/')
YouTube(link).streams.get_highest_resolution().download(url)