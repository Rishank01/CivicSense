import requests
from bs4 import BeautifulSoup
import trafilatura
from PyPDF2 import PdfReader
from io import BytesIO
import time

# Define category URLs
CATEGORY_URLS = {
    "bills": "https://prsindia.org/billtrack",
    "budgets": "https://prsindia.org/budgets",
    "legislatures": "https://prsindia.org/legislature",
    "policy": "https://prsindia.org/policy",
    "lamp": "https://prsindia.org/lamp"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def extract_text_from_pdf(pdf_url):
    try:
        response = requests.get(pdf_url, headers=HEADERS)
        if response.status_code == 200:
            with BytesIO(response.content) as data:
                reader = PdfReader(data)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() or ""
                return text.strip()
    except Exception as e:
        print(f"[PDF ERROR] {e}")
    return None

def extract_text_from_html(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            extracted = trafilatura.extract(response.text, url=url)
            return extracted.strip() if extracted else None
    except Exception as e:
        print(f"[HTML ERROR] {e}")
    return None

def scrape_category(category, url, max_articles=5):
    print(f"\n=== Scraping Category: {category.upper()} (max {max_articles}) ===")
    try:
        page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")

        links = soup.find_all("a", href=True)
        visited = set()
        count = 0

        for link in links:
            href = link["href"]

            # Skip bad links
            if "mailto" in href or "javascript" in href:
                continue

            # Make full URL
            if not href.startswith("http"):
                href = "https://prsindia.org" + href

            # Skip Hindi site and duplicates
            if "hi.prsindia.org" in href or href in visited:
                continue

            visited.add(href)

            print(f"\n→ Processing: {href}")

            # Extract content
            if href.lower().endswith(".pdf"):
                text = extract_text_from_pdf(href)
            else:
                text = extract_text_from_html(href)

            if text:
                print(f"\n--- Content from: {href} ---\n{text[:1000]}...\n")
                count += 1
            else:
                print("⚠️ No content extracted.")

            time.sleep(1)

            if count >= max_articles:
                break

    except Exception as e:
        print(f"[SCRAPE ERROR] {e}")



# Main loop with limit per category
if __name__ == "__main__":
    max_articles = 1  # or set dynamically via input
    for category, url in CATEGORY_URLS.items():
        scrape_category(category, url, max_articles=max_articles)

