nome_do_site = "MetaCogni"
from pytube import YouTube

# youtube_downloader.py

class YouTubeDownloader:
    
    
    @staticmethod
    def download_video(video_url, output_path='video.mp4'):
        
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            stream.download(filename=output_path)
            return output_path
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")
            raise e