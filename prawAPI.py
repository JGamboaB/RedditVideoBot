# Write 'python' in terminal -> Select Text -> Shit + Enter -> Run Python in Python Terminal

'''
TODO:
* Remove hyperlinks
* Remove special characters -> .replace()
* Make Tiktok Friendly -> censor swear words

MAYBE:
* Grab Comments with few text (?)

'''

import praw
import json
from ..RedditVideoBot.data.config import PASSWORD, USERNAME, USER_AGENT, CLIENT_ID, SECRET_KEY

MAX_COMMENTS = 6

# Create reddit instance
reddit = praw.Reddit(
    client_id= CLIENT_ID,
    client_secret= SECRET_KEY,
    password= PASSWORD,
    user_agent= USER_AGENT,
    username=USERNAME
)

# Example
# hot_posts = reddit.subreddit('AskReddit').hot(limit=10)
# for post in hot_posts:
#     print(post.title)

def getComments(submission):
    comments = []

    submission.comment_sort ='best'
    submission.comments.replace_more(limit=0) #Remove MoreComments

    for top_level_comment in submission.comments:
        if top_level_comment.body in ["[removed]", "[deleted]"]:
            continue
        
        # Max comments
        if len(comments) >= MAX_COMMENTS:
            break
        
        comments.append({
            "comment_body":top_level_comment.body,
            "comment_url":top_level_comment.permalink,
            "comment_id": "t1_" + top_level_comment.id #Only for top-level-comments
        })
    
    return comments

# Returns a dictionary of a thread and it's top comments from the AskReddit subreddit

def getAskReddit1():
    content = {}

    thread = reddit.subreddit('askreddit').hot(limit=1)
    submission = next(thread)
    
    #if submission is None: 
    #    return getAskReddit()

    #Thread info
    content['thread_url'] = f"http://reddit.com{submission.permalink}"
    content['thread_title'] = submission.title
    content['comments'] = getComments(submission)
    return content

def getAskRedditN(n):
    content= []

    threads = reddit.subreddit('askreddit').hot(limit=n)

    for submission in threads:
        if submission is None: 
            continue
    
        #Thread info
        content.append({
            "thread_url": f"http://reddit.com{submission.permalink}",
            "thread_title": submission.title,
            "comments": getComments(submission)
        })

        #content.append(thread)

    return content

json_object = json.dumps(getAskRedditN(5), indent=4)

with open("data/data.json", "w") as outfile:
    outfile.write(json_object)