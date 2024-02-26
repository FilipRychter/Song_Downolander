from youtubesearchpython import VideosSearch
from pytube import YouTube,Search
import subprocess

with open('lista_piosenek.txt', 'r') as f:
    lines = f.readlines()
    song_name = [line.strip() for line in lines]


for item in song_name:
    result = [video['link']
              for video in VideosSearch(item, limit=1).result()['result']]
    final_result = result[0]


    yt = YouTube(final_result)

    try:
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()

    # Pobierz plik audio

        audio_stream.download("C:\Programing\python\Song_Downolander\RANDOM")
        print("Pobrano:",item)
    except KeyError:
        print(f"Nie Pobrano: {item}")
        continue

print("Pobieranie zakończone!")
subprocess.run(['C:\\Users\\filop\\.pyenv\\pyenv-win\\versions\\3.11.1\\python3.11.exe','C:\Programing\python\Song_Downolander\Mp3Converter.py'], check=True)
#good marning usa, wenamechuindasama