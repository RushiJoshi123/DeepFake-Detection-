import yt_dlp 

with yt_dlp.YoutubeDL({"format":"bv*+ba/best"}) as ytl : 
    ytl.download(["https://www.youtube.com/watch?v=UDBSkUu71Jo"])