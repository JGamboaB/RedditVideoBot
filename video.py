# Resolution: 1080-1920px <--> 9:16

'''
TODO:
* Background music?
* Channel logo in between transitions

FIXME:
* Reduce video download time (~30 min) <-------------------------------------------------
'''

import os
from random import randint
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
trans_name = "Loud Whip.mp3"
trans_track = AudioFileClip("./audios/trans_sounds/"+trans_name)
trans_time = trans_track.duration
background_clip_path = "./backgrounds/minecraftparkour1.mp4"

def createAudio(post_index):
    audio_clips = []
    
    #title
    audio_clips.append(AudioFileClip("./audios/"+str(post_index)+"/0.mp3"))

    #comments
    audios = os.listdir('./audios/'+str(post_index))
    audios.remove("0.mp3") #remove title

    total_len, min_len, i = audio_clips[0].duration, 45, len(audio_clips)

    for audio in audios:
        if min_len > total_len:
            audio_clips.append(trans_track)
            audio_clips.append(AudioFileClip('./audios/'+str(post_index)+"/"+audio))
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
        ImageClip("./images/"+str(post_index)+"/0.png")
        .set_duration(audio_clips[0].duration)
        .set_position("center")
        .resize(width = W-100)
        .set_opacity(float(0.8))
    )

    #comments
    imgs = os.listdir('./images/'+str(post_index))
    imgs.remove("0.png") #removed title

    num_of_comments = len(audio_clips)/2 +1

    for i in range(1, int(num_of_comments)):
        img_clips.append(
            ImageClip("./images/"+str(post_index)+"/"+str(i)+".png")
            .set_duration(trans_time + audio_clips[2+(i-1)*2].duration)
            .set_position("center")
            .resize(width= W-100)
            .set_opacity(float(0.8))
        )
    
    audio_concat = concatenate_audioclips(audio_clips)
    audio_composite = CompositeAudioClip([audio_concat])
    img_concat = concatenate_videoclips(img_clips).set_position(("center", "center"))
    img_concat.audio = audio_composite

    background = VideoFileClip(background_clip_path)
    STARTTIME = randint(0, int(background.duration - audio_composite.duration)-1) 

    background_clip = (
        VideoFileClip(background_clip_path)
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

def downloadVideo(post_index):
    video = createVideo(post_index)
    video.set_fps(30) #Supposedly for optimizing in the download
    video.write_videofile("./result/output.mp4")

#Test
#a = createVideo(0)
#a.save_frame("./result/frame.png", t=10.5)

if __name__ == '__main__':
    downloadVideo(0)