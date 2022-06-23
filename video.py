# pip install moviepy

# Video Length ~ min: 0:45
# Resolution: 1080-1920px <--> 9:16

'''
TODO:
* Change trans_track to some sound effect used in reddit videos
* Random STARTTIME (taking into account duration of video)

FIXME:
* Reduce video download time (~30 min) <-------------------------------------------------
'''

import os
from moviepy.editor import (
    VideoFileClip, 
    AudioFileClip, 
    concatenate_videoclips, 
    concatenate_audioclips, 
    CompositeAudioClip, 
    CompositeVideoClip,
    ImageClip
)

#Variables
H, W = 1920, 1080
trans_track = AudioFileClip("./audios/silence.mp3")
trans_time = trans_track.duration
STARTTIME = 5

def createAudio(post_index):
    audio_clips = []
    
    #title
    audio_clips.append(AudioFileClip("./audios/"+str(post_index)+".mp3"))
    audio_clips.append(trans_track)

    #comments
    audios = os.listdir('./audios/')
    audios.remove(str(post_index)+".mp3") #removed title
    audios.remove("silence.mp3") #remove silence track ##########################################

    total_len, min_len, i = audio_clips[0].duration + trans_time, 45, 2

    for audio in audios:
        if min_len > total_len: 
            audio_clips.append(AudioFileClip("./audios/"+audio))
            audio_clips.append(trans_track)
            total_len += audio_clips[i].duration + trans_time
            i+=2
        else: # Acceptable Len
            break 

    return audio_clips 
    
    #a = createAudio(0)
    #c = concatenate_audioclips(a)
    #c.write_audiofile("audiotest.mp3")

def createVideo(post_index):
    img_clips = []
    audio_clips = createAudio(post_index)
    
    #title
    img_clips.append(
        ImageClip("./images/"+str(post_index)+".png")
        .set_duration(audio_clips[0].duration + trans_time)
        .set_position("center")
        .resize(width = W-100)
        .set_opacity(float(0.8))
    )

    #comments
    imgs = os.listdir('./images')
    imgs.remove(str(post_index)+".png") #removed title

    num_of_comments = len(audio_clips)/2 - 1

    for i in range(0, int(num_of_comments)):
        img_clips.append(
            ImageClip("./images/"+str(post_index)+"-"+str(i)+".png")
            .set_duration(audio_clips[2+i*2].duration+trans_time)
            .set_position("center")
            .resize(width= W-100)
            .set_opacity(float(0.8))
        )
    
    audio_concat = concatenate_audioclips(audio_clips)
    audio_composite = CompositeAudioClip([audio_concat])
    img_concat = concatenate_videoclips(img_clips).set_position(("center", "center"))
    img_concat.audio = audio_composite

    background_clip = (
        VideoFileClip("./backgrounds/minecraftparkour1.mp4")
        .without_audio()
        .resize(height = H)
        .crop(x1=1166.6, x2=2246.6)
        .subclip(STARTTIME,STARTTIME + audio_composite.duration)
    )

    final = CompositeVideoClip([background_clip, img_concat])

    # For testing (frame): final.save_frame("./result/frame.png", t=10.5)
    #   final.ipython_display()
    #   final.write_videofile("./result/output.mp4")

    return final

#Test
a = createVideo(0)
a.save_frame("./result/frame.png", t=10.5)