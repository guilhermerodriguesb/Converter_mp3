import yt_dlp

def download_video_as_mp3(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download e conversão para MP3 concluídos!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    url = input("Digite o URL do vídeo do YouTube: ")
    download_video_as_mp3(url)
