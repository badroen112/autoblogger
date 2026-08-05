import os
import feedparser
import tweepy

# ==========================
# Konfigurasi
# ==========================
RSS_URL = "https://reviewaplikasi123.blogspot.com/feeds/posts/default?alt=rss"
LAST_POST_FILE = "last_post.txt"

# ==========================
# Membaca RSS
# ==========================
print("Mengambil RSS...")

feed = feedparser.parse(RSS_URL)

if not feed.entries:
    print("❌ RSS kosong atau gagal dibaca.")
    exit()

entry = feed.entries[0]

title = entry.title
link = entry.link

print(f"Artikel terbaru : {title}")
print(f"Link            : {link}")

# ==========================
# Membaca artikel terakhir
# ==========================
if os.path.exists(LAST_POST_FILE):
    with open(LAST_POST_FILE, "r", encoding="utf-8") as f:
        last = f.read().strip()
else:
    last = ""

# ==========================
# Cek apakah artikel baru
# ==========================
if link == last:
    print("✅ Tidak ada artikel baru.")
    exit()

print("🆕 Artikel baru ditemukan.")

# ==========================
# Membuat Tweet
# ==========================
tweet = f"""🤖 Artikel Baru!

{title}

Baca selengkapnya di:
{link}

#AI #Teknologi #Blogger #Indonesia
"""

# Twitter/X membatasi panjang tweet
if len(tweet) > 280:
    tweet = tweet[:277] + "..."

print("\nIsi Tweet:")
print("--------------------------------")
print(tweet)
print("--------------------------------")

# ==========================
# Login Twitter/X
# ==========================
client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET"),
)

# ==========================
# Kirim Tweet
# ==========================
try:
    response = client.create_tweet(text=tweet)

    print("✅ Tweet berhasil dikirim.")
    print(response)

    with open(LAST_POST_FILE, "w", encoding="utf-8") as f:
        f.write(link)

    print("✅ last_post.txt diperbarui.")

except Exception as e:
    print("❌ Gagal mengirim tweet")
    print(e)
    exit(1)
