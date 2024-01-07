from pytube import YouTube, Playlist


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(save_path)
        print(f"Downloaded '{yt.title}' to {save_path}")
    except Exception as e:
        print(f"Error downloading video: {e}")


def download_playlist(playlist_url, save_path):
    try:
        pl = Playlist(playlist_url)
        for video_url in pl.video_urls:
            download_video(video_url, save_path)
    except Exception as e:
        print(f"Error downloading playlist: {e}")
