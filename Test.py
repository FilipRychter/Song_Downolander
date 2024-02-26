import os
from pytube import YouTube, Search
# to jest test czy na github sie zmieni że cos zrobiłem 
# pobierz nazwe z użytkownika
query = input("Wyszukaj piosenkę na YouTube: ")

# wykonaj wyszukiwanie i pobierz linki
search_results = Search(query).results
links = [result.watch_url for result in search_results]

# pobierz informacje o filmie
try:
    video = YouTube(links)
except:
    print("Nie udało się pobrać informacji o filmie. Upewnij się, że wprowadziłeś prawidłowy link.")
    exit()

# wybierz najwyższą jakość audio
audio = video.streams.filter(only_audio=True).get_highest_resolution()

# pobierz muzykę
print("Pobieranie rozpoczęte...")
audio.download(audio)
print("Pobieranie zakończone.")


