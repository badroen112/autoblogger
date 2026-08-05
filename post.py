import os

files = os.listdir("articles")

if len(files)==0:
    exit()

article = files[0]

print("Posting:", article)

# upload ke Blogger API

os.rename(
    "articles/"+article,
    "posted_"+article
)
