import requests
import feedparser

rss_url = "https://pib.gov.in/rssfeed2.aspx?catid=40"  # Law & Justice
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}

# Step 1: Fetch the RSS feed
response = requests.get(rss_url, headers=headers)
response.raise_for_status()

# Step 2: Parse with feedparser
feed = feedparser.parse(response.content)

# Step 3: Print the entries
print("✅ Latest PIB Legal News:\n")
for entry in feed.entries[:5]:
    print(f"📰 Title: {entry.title}")
    print(f"🔗 Link: {entry.link}")
    print(f"📅 Published: {entry.published}")
    print(f"📝 Summary: {entry.summary[:300]}...\n")
