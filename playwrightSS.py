#pip install playwright
#playwright install

import json
from playwright.sync_api import sync_playwright
from ..RedditVideoBot.data.config import PASSWORD, USERNAME

f = open('data/data.json')
data = json.load(f)

# Login Example and saved state in data/state.json

def LoginSaveState():
   with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        #Login into reddit
        page.goto("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")
       
        user_input = page.query_selector('[id="loginUsername"]')
        user_input.type(USERNAME)

        pass_input = page.query_selector('[id="loginPassword"]')
        pass_input.type(PASSWORD)

        with page.expect_navigation():
            page.query_selector('[type="submit"]').click()

        context.storage_state(path="data/state.json") # Saved here

        context.close()
        browser.close()

def generateSS(i):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(storage_state="data/state.json")

        page = context.new_page()

        # / / / Take SS of the Title
        with page.expect_navigation():
            page.goto(data[i]["thread_url"])

        NSFWYes = page.locator("text=Yes")
        if NSFWYes.count() > 0:
            NSFWYes.click() # NSFW Warning

        NSFWWarning = page.locator("text=Click to see nsfw")
        if NSFWWarning.count() > 0:
            NSFWWarning.click() # Remove "Click to see nsfw" Button in Screenshot

        title = page.query_selector('[data-test-id="post-content"]')
        title.screenshot(path="images/"+str(i)+".png")

        #  / / / Take SS of Best Comments

        j = 0
        for comment in data[i]["comments"]:
            outline = page.locator('[id="'+comment["comment_id"]+'"]')
            outline.screenshot(path="images/"+str(i)+"-"+str(j)+".png")
            j += 1

        # ----------------------
        context.close()
        browser.close()

if __name__ == "__main__":
    generateSS(0)

