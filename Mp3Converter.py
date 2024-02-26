import os

from moviepy.editor import VideoFileClip


def convert_mp4_to_mp3(input_file, output_file):
    video = VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    audio.close()


def batch_convert_mp4_to_mp3(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".mp4", ".mp3"))
            convert_mp4_to_mp3(input_file, output_file)


if __name__ == "__main__":
    input_folder = "C:/Programing/python/Song_Downolander/Playlist_downoland"  # Zmień na ścieżkę do folderu z plikami mp4
    output_folder = "C:/Programing/python/Song_Downolander/MP3"  # Zmień na ścieżkę do folderu, gdzie będą zapisane pliki mp3

    batch_convert_mp4_to_mp3(input_folder, output_folder)
