import moviepy.editor as me
import csv

images=[]
captions=[]
timestamps=[]
positionstexts=[]
x=""
x="./video/"+input("Enter name of the video file you wanna edit:")
videopath=x
video=me.VideoFileClip(videopath)
video=video.resize((1920,1080))
x="./spreadsheets/"+input("Enter the name of the timestamp spreadsheet file you wanna use:")
with open(x, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        timestamps.append(row)
print(timestamps)
for timestamp in timestamps:
    timestamp[0]=timestamp[0].replace("\"",'')
    timestamp[1]=timestamp[1].replace("\"",'')
    timestamp[1]=int(timestamp[1])
    h, m, s = timestamp[0].split(':')
    timestamp.append(int(h) * 3600 + int(m) * 60 + int(s))


x="./spreadsheets/"+input("Enter the name of the images spreadsheet file you wanna use:")  
with open(x, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        images.append(row)      
x="./spreadsheets/"+input("Enter the name of the captions spreadsheet file you wanna use:")  
with open(x, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        captions.append(row)     
for timestamp in timestamps:
    standardornot=input("Type 'Standard' for standard positioning or 'Advanced' for non-standard positioning in time-stamp "+timestamp[0]+":")
    if standardornot=="Standard":
        x=input("How many images/texts do you want to insert?")
        positionsimages=[[0.1, 0.9],[0.5, 0.9],[0.9, 0.9],
                         [0.1, 0.5],[0.5, 0.5],[0.9, 0.5],
                         [0.1, 0.1],[0.5, 0.1],[0.9, 0.1]]
        for i in range(0,x):
            






