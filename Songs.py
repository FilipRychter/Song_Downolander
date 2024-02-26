






for item in song_name:
    result = [video['link']
              for video in VideosSearch(item, limit=1).result()['result']]
    final_result = result[0]



    yt = YouTube(final_result)

    try:
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').last()
        print(audio_stream)
    # Pobierz plik audio

        audio_stream.download("C:\Programing\python\Song_Downolander\Playlist_downoland")
        print("Pobrano:",item)
    except KeyError:
        print(f"Nie Pobrano: {item}")
        continue

print("Pobieranie zakończone!")

#good marning usa, w