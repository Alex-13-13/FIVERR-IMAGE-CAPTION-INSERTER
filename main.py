import moviepy.editor as me
from moviepy.video.compositing.concatenate import concatenate_videoclips
import csv
import numpy as np
from moviepy.editor import clips_array
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"})
images=[]
captions=[]
timestamps=[]
positionstexts=[]
image_clips=[]
voidclips=[]
positionsimages=[(0.1, 0.9),(0.5, 0.9),(0.9, 0.9),
                 (0.1, 0.5),(0.5, 0.5),(0.9, 0.5),
                 (0.1, 0.1),(0.5, 0.1),(0.9, 0.1)]
positionsimagesstandard=[(0.5, 0.5),(0.1, 0.9),(0.9, 0.9),(0.1, 0.1),(0.9, 0.1)]
while True:
    try:
        x="./video/"+input("Enter name of the video file you wanna edit:")
        videopath=x
        video=me.VideoFileClip(videopath)
        break
    except OSError:
        print("File not found")
video=video.resize((1920,1080))
while True:
    try:
        x="./spreadsheets/"+input("Enter the name of the timestamp spreadsheet file you wanna use:")
        with open(x, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                timestamps.append(row)
        break
    except OSError:
        print("File not found")
for timestamp in timestamps:
    timestamp[0]=timestamp[0].replace("\"",'')
    timestamp[1]=timestamp[1].replace("\"",'')
    timestamp[1]=int(timestamp[1])
    h, m, s = timestamp[0].split(':')
    timestamp.append(int(h) * 3600 + int(m) * 60 + int(s))


while True:
    try:
        x="./spreadsheets/"+input("Enter the name of the images spreadsheet file you wanna use:")  
        with open(x, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                images.append(row)  
        break
    except OSError:
        print("File not found")    
while True:
    try:
        x="./spreadsheets/"+input("Enter the name of the captions spreadsheet file you wanna use:")  
        with open(x, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                captions.append(row) 
        break
    except OSError:
        print("File not found")   
i=0
if timestamps[0][2]!=0:
    voidclips.append(video.subclip(0,timestamps[0][2]))
voidbegin=[]
for timestamp in timestamps:
    voidbegin.append(timestamp[2]+timestamp[1])
print(voidbegin)
for index,timestamp in enumerate(timestamps):
    if index==0:
        continue
    voidclips.append("")
    voidclips.append(video.subclip(voidbegin[i],timestamp[2]))
    i=i+1
i=0
voidclips.append("")
if timestamps[len(timestamps)-1][2]+timestamps[len(timestamps)-1][1]<video.duration:
    voidclips.append(video.subclip(timestamps[len(timestamps)-1][2]+timestamps[len(timestamps)-1][1],video.duration))
print(voidclips)
for timestamp in timestamps:
    standardornot=""
    while(not standardornot==("Cross" or "3x3")):
        standardornot=input("Type 'Cross' for Cross positioning or '3x3' for 3x3 positioning in time-stamp "+timestamp[0]+":")
        if(not standardornot==("Cross" or "3x3")):
            print("Invalid input")
    if standardornot=="Cross":
        while True:
            x=input("How many images/texts do you want to insert?")
            if x>"5":
                print("Can't insert more than 5 images in Cross positioning. Insert number again")
                continue
            if x=="1":
                if images[i]==[]:
                    image=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                else:
                    image=me.ImageClip("./images/"+images[i][0])
                    if image.size[1]<=image.size[0]:
                        image=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.5*1920-225,0.5*1080-image.size[1]/2))
                    else:
                        image=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450)
                        image=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450).set_position((0.5*1920-image.size[0]/2,0.5*1080-225))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    print(fullcaption)
                    caption=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=25,color='white',method='caption',size= (image.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image.size[0]/2,0.5*1080-image.size[1]/2-45))
                    caption=me.TextClip(fullcaption, font='Amiri-Bold',bg_color='black', fontsize=25,color='white',method='caption',size= (image.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image.size[0]/2,0.5*1080-image.size[1]/2-caption.size[1]))
                clip=video.subclip(timestamp[2],timestamp[2]+timestamp[1])
                image_clips.append(me.CompositeVideoClip([clip,image,caption]))
                i=i+1
            elif x=="2":
                if images[i]==[]:
                    image1=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption1=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image1=me.ImageClip("./images/"+images[i][0])
                    if image1.size[1]<=image1.size[0]:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.5*1920-225,0.5*1080-image1.size[1]/2))
                    else:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450).set_position((0.5*1920-image1.size[0]/2,0.5*1080-225))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black',fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-45))
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold',bg_color='black', fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-caption1.size[1]))
                    i=i+1
                if images[i]==[]:
                    image2=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption2=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                else:
                    image2=me.ImageClip("./images/"+images[i][0])
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((0.025*1920,0.075*1080))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption2=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=25,bg_color="black",color='white',method='caption',size= (image2.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,0.075*1080-45))
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                clip=video.subclip(timestamp[2],timestamp[2]+timestamp[1])
                image_clips.append(me.CompositeVideoClip([clip,image1,image2,caption1,caption2]))
                i=i+1
            elif x=="3":
                if images[i]==[]:
                    image1=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption1=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image1=me.ImageClip("./images/"+images[i][0])
                    if image1.size[1]<=image1.size[0]:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.5*1920-225,0.5*1080-image1.size[1]/2))
                    else:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450).set_position((0.5*1920-image1.size[0]/2,0.5*1080-225))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black',fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-45))
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold',bg_color='black', fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-caption1.size[1]))
                    i=i+1
                if images[i]==[]:
                    image2=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption2=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image2=me.ImageClip("./images/"+images[i][0])
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((0.025*1920,0.075*1080))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption2=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=25,bg_color='black',color='white',method='caption',size= (image2.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,0.075*1080-45))
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                    i=i+1
                if images[i]==[]:
                    image3=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption3=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                else:
                    image3=me.ImageClip("./images/"+images[i][0])
                    if image3.size[1]<=image3.size[0]:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((1920-450-0.025*1920,0.075*1080))
                    else:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((1920-image3.size[0]-0.025*1920,0.075*1080))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption3=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=25,bg_color='black',color='white',method='caption',size= (image3.size[0],None)).set_duration(timestamp[1]).set_position((1920-image3.size[0]-0.025*1920,0.075*1080-45))
                    if image3.size[1]<=image3.size[0]:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((1920-450-0.025*1920,0.075*1080-45+caption3.size[1]))
                    else:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((1920-image3.size[0]-0.025*1920,0.075*1080-45+caption3.size[1]))
                clip=video.subclip(timestamp[2],timestamp[2]+timestamp[1])
                image_clips.append(me.CompositeVideoClip([clip,image1,image2,image3,caption1,caption2,caption3]))
                i=i+1
            elif x=="4":
                if images[i]==[]:
                    image1=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption1=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image1=me.ImageClip("./images/"+images[i][0])
                    if image1.size[1]<=image1.size[0]:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.5*1920-225,0.5*1080-image1.size[1]/2))
                    else:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450).set_position((0.5*1920-image1.size[0]/2,0.5*1080-225))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black',fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-45))
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold',bg_color='black', fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-caption1.size[1]))
                    i=i+1
                if images[i]==[]:
                    image2=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption2=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image2=me.ImageClip("./images/"+images[i][0])
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((0.025*1920,0.075*1080))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption2=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=20,bg_color='black',color='white',method='caption',size= (image2.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,0.075*1080-45))
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                    i=i+1
                if images[i]==[]:
                    image3=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption3=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image3=me.ImageClip("./images/"+images[i][0])
                    if image3.size[1]<=image3.size[0]:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((1920-450-0.025*1920,0.075*1080))
                    else:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((1920-image3.size[0]-0.025*1920,0.075*1080))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption3=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=20,bg_color='black',color='white',method='caption',size= (image3.size[0],None)).set_duration(timestamp[1]).set_position((1920-image3.size[0]-0.025*1920,0.075*1080-45))
                    if image3.size[1]<=image3.size[0]:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((1920-450-0.025*1920,0.075*1080-45+caption3.size[1]))
                    else:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=375).set_position((1920-image3.size[0]-0.025*1920,0.075*1080-45+caption3.size[1]))
                    i=i+1
                if images[i]==[]:
                    image4=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption4=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                else:
                    image4=me.ImageClip("./images/"+images[i][0])
                    if image4.size[1]<=image4.size[0]:
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,1080-0.025*1080-image4.size[1]))
                    else:
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((0.025*1920,1080-0.025*1080-300))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption4=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black', fontsize=20,color='white',method='caption',size= (image4.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,1080-0.025*1080-image4.size[1]-45))
                    caption4=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black', fontsize=20,color='white',method='caption',size= (image4.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,1080-0.025*1080-image4.size[1]-caption4.size[1]))
                clip=video.subclip(timestamp[2],timestamp[2]+timestamp[1])
                image_clips.append(me.CompositeVideoClip([clip,image1,image2,image3,image4,caption1,caption2,caption3,caption4]))
                i=i+1
            elif x=="5":
                if images[i]==[]:
                    image1=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption1=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image1=me.ImageClip("./images/"+images[i][0])
                    if image1.size[1]<=image1.size[0]:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.5*1920-225,0.5*1080-image1.size[1]/2))
                    else:
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450)
                        image1=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=450).set_position((0.5*1920-image1.size[0]/2,0.5*1080-225))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black',fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-45))
                    caption1=me.TextClip(fullcaption, font='Amiri-Bold',bg_color='black', fontsize=25,color='white',method='caption',size= (image1.size[0],None)).set_duration(timestamp[1]).set_position((0.5*1920-image1.size[0]/2,0.5*1080-image1.size[1]/2-caption1.size[1]))
                    i=i+1
                if images[i]==[]:
                    image2=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption2=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image2=me.ImageClip("./images/"+images[i][0])
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((0.025*1920,0.075*1080))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption2=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=20,bg_color='black',color='white',method='caption',size= (image2.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,0.075*1080-45))
                    if image2.size[1]<=image2.size[0]:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                    else:
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image2=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((0.025*1920,0.075*1080-45+caption2.size[1]))
                    i=i+1
                if images[i]==[]:
                    image3=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption3=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image3=me.ImageClip("./images/"+images[i][0])
                    if image3.size[1]<=image3.size[0]:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((1920-450-0.025*1920,0.075*1080))
                    else:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((1920-image3.size[0]-0.025*1920,0.075*1080))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption3=me.TextClip(fullcaption, font='Amiri-Bold', fontsize=20,bg_color='black',color='white',method='caption',size= (image3.size[0],None)).set_duration(timestamp[1]).set_position((1920-image3.size[0]-0.025*1920,0.075*1080-45))
                    if image3.size[1]<=image3.size[0]:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((1920-450-0.025*1920,0.075*1080-45+caption3.size[1]))
                    else:
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image3=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((1920-image3.size[0]-0.025*1920,0.075*1080-45+caption3.size[1]))
                    i=i+1
                if images[i]==[]:
                    image4=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption4=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                    i=i+1
                else:
                    image4=me.ImageClip("./images/"+images[i][0])
                    if image4.size[1]<=image4.size[0]:
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((0.025*1920,1080-0.025*1080-image4.size[1]))
                    else:
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image4=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((0.025*1920,1080-0.025*1080-300))
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption4=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black', fontsize=20,color='white',method='caption',size= (image4.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,1080-0.025*1080-image4.size[1]-45))
                    caption4=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black', fontsize=20,color='white',method='caption',size= (image4.size[0],None)).set_duration(timestamp[1]).set_position((0.025*1920,1080-0.025*1080-image4.size[1]-caption4.size[1]))
                    i=i+1
                if images[i]==[]:
                    image5=me.ColorClip(color=[0, 0, 0], size=(1, 1), duration=timestamp[1])
                    caption5=me.TextClip(" ", fontsize=25, color="white", size=(1,1), bg_color="transparent").set_duration(timestamp[1])
                else:
                    image5=me.ImageClip("./images/"+images[i][0])
                    if image5.size[1]<=image5.size[0]:
                        image5=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450)
                        image5=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(width=450).set_position((1920-450-0.025*1920,1080-0.025*1080-image5.size[1]))
                    else:
                        image5=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300)
                        image5=me.ImageClip("./images/"+images[i][0]).set_duration(timestamp[1]).resize(height=300).set_position((1920-image5.size[0]-0.025*1920,1080-0.025*1080-300))    
                    fullcaption=""
                    for c in captions[i]:
                        fullcaption=fullcaption+c
                        fullcaption=fullcaption+' '
                    caption5=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black', fontsize=20,color='white',method='caption',size= (image5.size[0],None)).set_duration(timestamp[1]).set_position((1920-image5.size[0]-0.025*1920,1080-0.025*1080-image5.size[1]-45))
                    caption5=me.TextClip(fullcaption, font='Amiri-Bold', bg_color='black', fontsize=20,color='white',method='caption',size= (image5.size[0],None)).set_duration(timestamp[1]).set_position((1920-image5.size[0]-0.025*1920,1080-0.025*1080-image5.size[1]-caption5.size[1]))
                clip=video.subclip(timestamp[2],timestamp[2]+timestamp[1])
                image_clips.append(me.CompositeVideoClip([clip,image1,image2,image3,image4,image5,caption1,caption2,caption3,caption4,caption5]))
                i=i+1
            else:
                print("This input is not recognizable. Enter your input again")
                continue
            break
j=0
for i in range(len(voidclips)):
    if voidclips[i]=='':
        voidclips[i]=image_clips[j]
        j=j+1

for void in voidclips:
    print(void)
print(voidclips)
final=concatenate_videoclips(voidclips)
final.write_videofile("./output/new_filename.mp4",fps=24)







