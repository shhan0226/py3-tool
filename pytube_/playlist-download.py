import os
from pytube import YouTube
from pytube import Playlist

#p = Playlist('https://www.youtube.com/playlist?list=PLRrUisvYoUw9-cTYgkbTbr9f9CpbGdq4F')
url_list = input("url: ?")
p = Playlist(url_list)
print(f'Downloading: {p.title}')
file_name = p.title
print(file_name)

# playlist download
for video in p.video_urls:
	yt = YouTube(video)
	print(yt.title)
#	for i, stream in enumerate(yt.streams.all()):
#		print(i, " : ", stream)
	for i, stream in enumerate(yt.streams.filter(progressive=True, file_extension="mp4", type="video").all()):
		print(i, " : ", stream)
	yt.streams.get_by_itag(22).download('/data/Youtube/haru/' + file_name)

# youtube download
#yt = YouTube('url address')
#yt.streams.get_by_itag(22).download('/data')