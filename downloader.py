import os
import yt_dlp  # or youtube_dl if you prefer

def download_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join('songs', '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # If you want to download the whole playlist, ensure noplaylist is False (or simply omit it)
        'noplaylist': False,
        'quiet': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    # Use the playlist URL directly
    playlist_url = "https://www.youtube.com/playlist?list=OLAK5uy_nCawb3VyvHzAuYpZWFnvIKNh5lZlC6o3I"
    os.makedirs('songs', exist_ok=True)
    
    print(f"\nDownloading audio from playlist: {playlist_url}")
    try:
        download_mp3(playlist_url)
    except Exception as e:
        print(f"Error downloading from {playlist_url}: {e}")

if __name__ == "__main__":
    main()
