# pip install moviepy
# Video Length ~ 0:50 - 1:30
# Resolution: 1080-1920px <--> 9:16

from moviepy.editor import (
    VideoFileClip, 
    AudioFileClip, 
    concatenate_videoclips, 
    concatenate_audioclips, 
    CompositeAudioClip, 
    CompositeVideoClip
)

# Get full audio with timestamps to each part

STARTTIME = 5
ENDTIME = STARTTIME + 2 # Max 1:30 min

background_clip = (
    VideoFileClip("./backgrounds/minecraftparkour1.mp4")
    .without_audio()
    .resize(height = 1920)
    .crop(x1=1166.6, x2=2246.6)
    .subclip(STARTTIME,ENDTIME)
)

trans_clip = 

##

ax = AudioFileClip("./audios/0.mp3")
ax0 = AudioFileClip("./audios/0-0.mp3")
ax1 = AudioFileClip("./audios/0-1.mp3")

combined = concatenate_audioclips([ax, ax0, ax1] )
a = concatenate_videoclips([], transition=)

##

#image_clip.audio = CompositeAudioClip([combined])
image_concat = concatenate_videoclips(image_clip).set_position(("center","center"))

final = CompositeVideoClip([background_clip, image_concat])
final.ipython_display()

#background.write_videofile("./result/output.mp4")