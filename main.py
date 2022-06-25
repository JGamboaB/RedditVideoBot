import json
import os

from prawAPI import getAskRedditN
from tts import TTSPost
from video import downloadVideo


def createAskRedditVideo():
    json_object = json.dumps(getAskRedditN(1), indent=4) #get data from reddit
    with open("data/data.json", "w") as outfile:
        outfile.write(json_object) #write into data/data.json

    post_index_in_json = 0 #first value in data/data.json
    print('Data: done')

    #Get Screenshots of the post
    os.system("py playwrightSS.py")
    print('SS: done')

    #Get audios by TTS
    TTSPost(post_index_in_json, 'en_us_010') #Different voices, best ones in my opinion: 'en_us_001' (Female), 'en_us_010' (Male) & 'en_us_ghostface'
    print('TTS: done')

    #Create video
    downloadVideo(post_index_in_json)
    print('Video: done')
    

if __name__ == '__main__':
    createAskRedditVideo()
