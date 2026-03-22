import requests #fetches data from URLs
import pandas as pd #organizes it into a table
import time #built in python library used to create delay between requests so that Reddit doesnt block us

def fetch_reddit_posts(subreddit, limit=100): #defined a function, takes 2 inputs: which subreddit to fetch from and no. of posts we want 
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit=100"
    headers = {"User-Agent": "re-marketing-intelligence/0.1"} #reddit requires you to identify your scripts before making requests or else it would think of us as a random bot and block us immediately
    
    posts = []
    after = None
    
    while len(posts) < limit:
        params = {"after": after} if after else {}
        response = requests.get(url, headers=headers, params=params) #req.get hits the URL and gets the response
        data = response.json() #.json converts raw response into a Python Dictionary
        
        children = data["data"]["children"]
        if not children:
            break
            
        for post in children:
            p = post["data"]
            posts.append({
                "title": p["title"],
                "text": p["selftext"],
                "score": p["score"],
                "num_comments": p["num_comments"],
                "created_utc": p["created_utc"],
                "url": p["url"]
            })
        
        after = data["data"]["after"]
        time.sleep(1)
    
    return posts

posts = fetch_reddit_posts("royalenfield", limit=500)
df = pd.DataFrame(posts)
df.to_csv("data/posts.csv", index=False)
print(f"Saved {len(df)} posts")