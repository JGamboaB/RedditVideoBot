import os
import json

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

    # Title
    writeFile(data[post_index]['thread_title'])
    TTSFile(voice, './data/tmp.txt')

    if os.path.exists("./audio/"+str(post_index)+".mp3"):
        os.remove("./audio/"+str(post_index)+".mp3")

    os.rename('voice.mp3', "./audio/"+str(post_index)+".mp3")

    # Comments
    i = 0
    for comment in data[post_index]['comments']:
        writeFile(comment['comment_body'])
        TTSFile(voice, './data/tmp.txt')

        if os.path.exists("./audio/"+str(post_index)+"-"+str(i)+".mp3"):
            os.remove("./audio/"+str(post_index)+"-"+str(i)+".mp3")

        os.rename('voice.mp3', "./audio/"+str(post_index)+"-"+str(i)+".mp3")
        i += 1


if __name__ == '__main__':
    TTSPost(0, 'en_us_001')

# Best voices in my opinion: en_us_001 (Female), en_us_010 (Male), en_us_ghostface