
import youtube_dl
import os


print('[Info] Simple video-to-audio converter \n')

video_url = input('Enter the youtube URL of the video or playlist: ')
print('[Info] You have entered:', video_url)


def createFolder(dirName):
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
        return dirName
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")

    return dirName

if video_url is not "":
    print('[Info] Conversion in progress...')

    folder = createFolder('./audio/')

    ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': folder+'%(title)s.%(etx)s' ,
    'quiet': False
}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_list=[video_url])

    print("[Info] Done!")
else:
    raise ValueError ('[Error] Please enter a valid URL')
