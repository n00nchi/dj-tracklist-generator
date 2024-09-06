# tracklist_generator.py

# Import necessary libraries
from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video(url, output_path='downloads'):
    """
    Downloads a YouTube video and extracts the audio.
    :param url: YouTube video URL
    :param output_path: Directory to save the video/audio
    :return: Path to the downloaded audio file
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    print(f"Downloading video from {url}...")
    yt = YouTube(url)
    video_stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = os.path.join(output_path, yt.title + ".mp4")
    
    # Download the audio
    video_stream.download(output_path=output_path, filename=yt.title + ".mp4")
    print(f"Downloaded video as audio file: {audio_file_path}")

    # Convert mp4 audio to mp3 using pydub
    mp3_audio_path = os.path.join(output_path, yt.title + ".mp3")
    audio = AudioSegment.from_file(audio_file_path, format="mp4")
    audio.export(mp3_audio_path, format="mp3")
    print(f"Converted to MP3: {mp3_audio_path}")
    
    return mp3_audio_path

if __name__ == "__main__":
    # Example YouTube video URL
    video_url = "https://www.youtube.com/watch?v=example_video"
    
    # Call the download function
    mp3_file = download_youtube_video(video_url)
