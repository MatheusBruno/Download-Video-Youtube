from pytube import YouTube
import sys

if len(sys.argv) > 1:
    link = sys.argv[1]
    url = sys.argv[2]
else:
    link = input("Download Link: ")
    url = input("Caminho: ")

url = str(url).replace('\\','/')
YouTube(link).streams.get_highest_resolution().download(url)