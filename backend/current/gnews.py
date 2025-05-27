# import requests

# API_KEY = 'c463ee4ca3cb64bb2f3cd58e0396030e'  # Replace with your GNews API key
# query = "India"
# url = f"https://gnews.io/api/v4/search?q={query}&lang=en&country=in&max=10&apikey={API_KEY}"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print("Top News Articles Related to India:\n")
#     for article in data['articles']:
#         print(f"Title: {article['title']}")
#         print(f"Source: {article['source']['name']}")
#         print(f"URL: {article['url']}")
#         print(f"Published: {article['publishedAt']}\n")
#         print("article -> ",article)
# else:
#     print(f"Failed to fetch news. Status code: {response.status_code}")




import requests
import time
from newspaper import Article

# —————————————————————————
# Configuration
# —————————————————————————
API_KEY = 'c463ee4ca3cb64bb2f3cd58e0396030e'  # Your GNews API key
QUERY   = 'India'
MAX     = 5   # Number of GNews results to fetch
DELAY   = 1   # Seconds between requests

# GNews search URL
GNEWS_URL = (
    f"https://gnews.io/api/v4/search?"
    f"q={QUERY}&lang=en&country=in&max={MAX}&apikey={API_KEY}"
)

# —————————————————————————
# Fetch article metadata from GNews
# —————————————————————————
resp = requests.get(GNEWS_URL)
resp.raise_for_status()
articles = resp.json().get('articles', [])

if not articles:
    print("No articles returned from GNews.")
    exit()

# —————————————————————————
# Loop through and extract full text
# —————————————————————————
for idx, art in enumerate(articles, start=1):
    title     = art.get('title')
    source    = art.get('source', {}).get('name')
    url       = art.get('url')
    published = art.get('publishedAt')

    print(f"\n=== Article #{idx} ===")
    print(f"Title    : {title}")
    print(f"Source   : {source}")
    print(f"Published: {published}")
    print(f"URL      : {url}\n")

    try:
        # Initialize newspaper Article
        a = Article(url)
        a.download()
        a.parse()
    except Exception as e:
        print(f"⚠️  Failed to download/parse article: {e}")
        continue

    # Print the full text (truncate for console)
    full_text = a.text or "[No text extracted]"
    print(full_text)  # first 2000 chars
    if len(full_text) > 2000:
        print("\n[Output truncated...]\n")

    # Be polite with a delay
    time.sleep(DELAY)
