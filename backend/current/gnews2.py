import requests
import time
import trafilatura

# —————————————————————————
# Configuration
# —————————————————————————
API_KEY = 'c463ee4ca3cb64bb2f3cd58e0396030e'  # Replace with your GNews API key
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
try:
    resp = requests.get(GNEWS_URL)
    resp.raise_for_status()
    articles = resp.json().get('articles', [])
except Exception as e:
    print(f"❌ Error fetching articles: {e}")
    exit()

if not articles:
    print("⚠️ No articles returned from GNews.")
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
        # Fetch the HTML content
        html = requests.get(url, timeout=10).text

        # Use trafilatura to extract full article text
        extracted_text = trafilatura.extract(html, include_comments=False, include_tables=True)

        full_text = extracted_text if extracted_text else "[No text extracted]"
    except Exception as e:
        print(f"⚠️ Failed to fetch/parse article: {e}")
        continue

    # Print full text (truncated to 2000 chars for console)
    print(full_text)
    if len(full_text) > 2000:
        print("\n[Output truncated...]\n")

    # Be polite with a delay
    time.sleep(DELAY)
