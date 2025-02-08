import subprocess
import sys
import os

def download_audio_to_mp3(video_url, output_filename="output.mp3", start_time=0, duration=None):
    """
    Downloads the best audio from a video URL using yt-dlp,
    optionally extracts a specific time range, and converts to MP3.
    """

    # 1. Download best audio as a single file (often M4A or WebM) with yt-dlp
    print(f"Downloading best audio from: {video_url}")
    temp_audio = "temp_audio.%(ext)s"
    subprocess.run(
        [
            "yt-dlp",
            "-f", "bestaudio",          # download best audio only
            "-o", temp_audio,           # output template (yt-dlp will pick the correct extension)
            video_url
        ],
        check=True
    )

    # Since we used an output template (temp_audio.%(ext)s), we don’t know the exact extension
    # but we can find the downloaded file by checking for "temp_audio." prefix
    downloaded_file = None
    for file in os.listdir("."):
        if file.startswith("temp_audio."):
            downloaded_file = file
            break
    
    if not downloaded_file:
        print("Could not find downloaded audio file.")
        sys.exit(1)

    print(f"Audio downloaded as: {downloaded_file}")

    # 2. Build the ffmpeg command to convert to MP3
    #    We can also use start time and duration if you only want a clip.
    #    E.g., start_time=30, duration=10 => from 30s to 40s of the audio.

    ffmpeg_cmd = [
        "ffmpeg", 
        "-y",              # overwrite output file if it exists
    ]

    # If you want to skip ahead in the audio file
    if start_time > 0:
        ffmpeg_cmd += ["-ss", str(start_time)]

    ffmpeg_cmd += ["-i", downloaded_file]

    # If you only want a certain duration (in seconds)
    if duration is not None:
        ffmpeg_cmd += ["-t", str(duration)]

    ffmpeg_cmd += [
        "-vn",            # no video
        "-acodec", "libmp3lame",
        "-q:a", "2",      # quality level; 0=best, 9=worst. Or use -b:a 192k for a fixed bitrate
        output_filename
    ]

    subprocess.run(ffmpeg_cmd, check=True)

    # 3. Cleanup
    os.remove(downloaded_file)
    print(f"Done! MP3 saved as '{output_filename}'.")

if __name__ == "__main__":

    video_url = "https://www.youtube.com/watch?v=v0YEaeIClKY"
    download_audio_to_mp3(video_url, output_filename="output.mp3", start_time=40, duration=None)
