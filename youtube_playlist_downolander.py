from pytube import Playlist

link = input("Enter YouTube Playlist URL:")

yt_playlist = Playlist(link)

#dada

for video in yt_playlist.videos:
    video.streams.get_lowest_resolution().download("C:\Programing\python\Song_Downolander\Playlist_downoland")
    print("Vdeo Downoland:",video.title)

print("\nDone!")
