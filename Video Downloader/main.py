from yt_dlp import YoutubeDL

# link = YouTube("https://www.youtube.com/watch?v=9kk7VJAul8U")
#
# video = link.streams.get_highest_resolution()
#
# video.download()

link = 'https://www.youtube.com/watch?v=-x2pLPHSkD0'
bestvideo = {'format':'bestvideo+bestaudio/best',
         'merge_output_format': 'mkv'}

with YoutubeDL(bestvideo) as ydl:
    ydl.download([link])