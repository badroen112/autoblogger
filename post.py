import feedparser

feed = feedparser.parse(
    "https://reviewaplikasi123.blogspot.com/feeds/posts/default?alt=rss"
)

entry = feed.entries[0]

print(entry.title)
print(entry.link)
