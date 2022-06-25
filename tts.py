'''
FIXME:
* Separate text for tts for better quality of tts
'''

import os
import json
from moviepy.editor import AudioFileClip

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

    #Create directory for post
    if not os.path.exists('./audios/'+str(post_index)):
        os.makedirs('./audios/'+str(post_index))

    # Title
    writeFile(data[post_index]['thread_title'])
    TTSFile(voice, './data/tmp.txt')

    if os.path.exists("./audios/"+str(post_index)+"/0.mp3"):
        os.remove("./audios/"+str(post_index)+"/0.mp3")

    os.rename('voice.mp3', "./audios/"+str(post_index)+"/0.mp3")

    # Comments
    i = 1
    for comment in data[post_index]['comments']:
        ##
        '''
        lines = comment['comment_body'].split('\n')
        lines = list(filter(lambda a: a != '', lines))

        for line in lines:
            writeFile(line)
            TTSFile(voice, './data/tmp.txt')
            
            if os.path.exists("./audios/"+str(post_index)+"/"+str(i)+".mp3"):
                os.remove("./audios/"+str(post_index)+"/"+str(i)+".mp3")

            os.rename('voice.mp3', "./audios/"+str(post_index)+"/"+str(i)+".mp3")

            i += 1
        '''
        ##

        ## Only 1 audio tts
        writeFile(comment['comment_body'])
        TTSFile(voice, './data/tmp.txt')

        if os.path.exists("./audios/"+str(post_index)+"/"+str(i)+".mp3"):
            os.remove("./audios/"+str(post_index)+"/"+str(i)+".mp3")

        os.rename('voice.mp3', "./audios/"+str(post_index)+"/"+str(i)+".mp3")
        
        i += 1
        ##


if __name__ == '__main__':
    TTSPost(0, 'en_us_010')

# Best voices in my opinion: en_us_001 (Female), en_us_010 (Male), en_us_ghostface