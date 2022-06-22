#pip install playwright
#playwright install

import json
from warnings import catch_warnings
from playwright.sync_api import sync_playwright

with open('pw.txt','r') as f: 
    pw = f.read()

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
        user_input.type("Sudden_Worth7157")

        pass_input = page.query_selector('[id="loginPassword"]')
        pass_input.type(pw)

        with page.expect_navigation():
            page.query_selector('[type="submit"]').click()

        context.storage_state(path="data/state.json") # Saved here

        context.close()
        browser.close()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="data/state.json")

        page = context.new_page()

        i = 2

        # / / / Take SS of the Title
        with page.expect_navigation():
            page.goto(data[i]["thread_url"])

        # NSFW Warning

        NSFWYes = page.locator("text=Yes")
        if NSFWYes.count() > 0:
            NSFWYes.click()

        NSFWWarning = page.locator("text=Click to see nsfw")
        if NSFWWarning.count() > 0:
            NSFWWarning.click()

        title = page.query_selector('[data-test-id="post-content"]')
        title.screenshot(path="images/"+str(i)+".png")

        #  / / / Take SS of Best Comments

        



        #page.wait_for_timeout(5000)

        # ----------------------
        context.close()
        browser.close()

if __name__ == "__main__":
    main()

