Basic Tiktok Reddit Video Maker. 
Only for AskReddit, and it uses the format of: 'title + top comments'.
For other subreddits must change the functions to the format of 'top titles' or 'title & description' (for example: r/UnethicalLifeProTips, r/LetsNotMeet).

To run:
1. run prawAPI.py
2. run playwrightSS.py
3. run tts.py
4. Must add a background clip to the folder backgrounds and write the path to it in the variable 'background_clip_path' in video.py (Video must be at least 2:30 minutes just in case)
5. run video.py

Libraries needed:
* praw 
* playwright
* moviepy

To improve:
* Text-to-speech filter: censor swear words, delete hyperlinks and delete certain special characters for better pronunciation.
* Generate a Text-to-speech audio for every paragraph ('\n') instead of the whole text.
* If long text, screenshots of every paragraph ('\n') instead of the whole text.