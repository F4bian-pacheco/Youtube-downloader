
import pafy
import os


class Downloader:
    def __init__(self,url):
        self.url = url

    def track(self,total,rcvd,a,b,c):
        print(total,rcvd)


    def get_audio(self,path):
        try:
            audio = pafy.new(self.url)
            audio.getbestaudio("m4a").download(path)
            print(audio.audiostreams)
            return True
        except Exception:
            print("algo malo sucedio en el audio")
            return False

    def get_video(self,path):
        try:
            video = pafy.new(self.url)
            video.getbest("mp4").download(path)
            print(video.streams)
        except Exception:
            print("algo malo sucedio en el video")
            return False

# url = "https://www.youtube.com/watch?v=qZHxUy5ZpZE"
# path = os.getcwd() + "/downloads"
# mp3(url,path)

