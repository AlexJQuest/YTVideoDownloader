##YT Video Downlodser

from pytube import YouTube
from sys import argv

#link = argv[1]
#filesize = argv[2]

link = input("please enter the video link:")
ytvid = YouTube(link)


print("Title: ", ytvid.title)
print("Channel: ", ytvid.channel_id)
print("Length: ",ytvid.length)
print("Views: ", ytvid.views)



checkvid =  input("Is this correct? (y/n): ")

if checkvid == "y": 
    filesize = input("Please select file size (144p, 240p, 360p, 480p,720p, 1080p): ")
    ytdownload = ytvid.streams.get_by_resolution(filesize)
    if ytdownload == None:
        filesize = input("Sorry, that quality is not available. Please select file size again (144p, 240p, 360p, 480p,720p, 1080p): ")
        ytdownload = ytvid.streams.get_by_resolution(filesize)
    else:
        ytdownload.download('C:/Users/alex/Desktop/YTdowload')
    
    
    
else:
    link = input("please enter the video link:")
    ytvid = YouTube(link)
    print("Title:", ytvid.title)
    print("Length: ",ytvid.length)
    print("Views:", ytvid.views)