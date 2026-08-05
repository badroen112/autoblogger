import feedparser

feed = feedparser.parse(
    "https://reviewaplikasi123.blogspot.com/feeds/posts/default?alt=rss"
)

entry = feed.entries[0]

print(entry.title)
print(entry.link)

with open("last_post.txt") as f:
    last = f.read().strip()

latest = feed.entries[0].link

if latest == last:
    print("Tidak ada artikel baru.")
    exit()

tweet = f"""
{entry.title}

{entry.link}

#AI #Blogger
"""

import tweepy

client = tweepy.Client(
    consumer_key=...,
    consumer_secret=...,
    access_token=...,
    access_token_secret=...
)

client.create_tweet(text=tweet)

with open("last_post.txt","w") as f:
    f.write(latest)
