import pytube
from instagrapi import Client
cl = Client()
cl.login("chikku_v2023", "Pranavkd44#")

cap = "https://youtube.com/shorts/eTaQmbqxZsU"


def downloadvid(url):
  youtube = pytube.YouTube(url)
  video_stream = youtube.streams.filter().get_highest_resolution()
  video_stream.download(filename="reel.mp4")
  print("Video Title:", youtube.title)
  global cap
  cap = youtube.title
  
  

def instaup():
  global cap
  
  media = cl.clip_upload(
    "reel.mp4",
    cap,
    extra_data={
        "like_and_view_counts_disabled": 0,
        "disable_comments": 0,
    })
  media.dict()

print("hshah")
