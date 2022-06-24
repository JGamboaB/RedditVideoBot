'''
FIXME:
* Separate text for tts for better quality of tts and then combine multiple audios into one
'''

import os
import json
from moviepy.editor import (
    AudioFileClip, 
    concatenate_audioclips, 
    CompositeAudioClip
)

f = open('data/data.json')
data = json.load(f)

def TTSFile(voice, file):
    os.system("py ./tiktok-voice/main.py -v " + voice + " -f " + file)

def writeFile(text):
    with open ('./data/tmp.txt', 'w', encoding='utf-8') as f:
        f.write(text)
        f.close()

def TTSPost(post_index, voice):
    print(post_index)

    if os.path.exists("./batch/"):
        os.remove("./batch/")

    # Title
    writeFile(data[post_index]['thread_title'])
    TTSFile(voice, './data/tmp.txt')

    if os.path.exists("./audios/"+str(post_index)+".mp3"):
        os.remove("./audios/"+str(post_index)+".mp3")

    os.rename('voice.mp3', "./audios/"+str(post_index)+".mp3")

    # Comments
    i = 0
    for comment in data[post_index]['comments']:
        ##
        '''
        lines = comment['comment_body'].split('. ')
        audio_clips = []

        j = 0 ## DELETEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

        for line in lines:
            writeFile(line)
            TTSFile(voice, './data/tmp.txt')

            audio = AudioFileClip("./voice.mp3")
            audio_clips.append(audio)
            audio.write_audiofile("./result/"+str(i)+"---"+str(j)+".mp3")
            j+=1
            
        audio_concat = concatenate_audioclips(audio_clips)
        audio_concat.write_audiofile("./audios/"+str(post_index)+"-"+str(i)+".mp3")

        i += 1
        '''
        ##

        ## Only 1 audio tts
        writeFile(comment['comment_body'])
        TTSFile(voice, './data/tmp.txt')

        if os.path.exists("./audios/"+str(post_index)+"-"+str(i)+".mp3"):
            os.remove("./audios/"+str(post_index)+"-"+str(i)+".mp3")

        os.rename('voice.mp3', "./audios/"+str(post_index)+"-"+str(i)+".mp3")
        
        i += 1
        ##


if __name__ == '__main__':
    TTSPost(0, 'en_us_010')

# Best voices in my opinion: en_us_001 (Female), en_us_010 (Male), en_us_ghostface