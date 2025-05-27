import requests
from bs4 import BeautifulSoup
import trafilatura

BASE_URL = "https://prsindia.org"
HOME_URL = f"{BASE_URL}/"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_tab_links(section_id, limit=5):
    """
    Fetch article/blog links from a tab (e.g., blog, article)
    """
    response = requests.get(HOME_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    section_div = soup.find("div", id=section_id)
    if not section_div:
        print(f"[!] Could not find section #{section_id}")
        return []

    links = []
    for a in section_div.find_all("a", href=True):
        href = a['href']
        if not href.startswith("http"):
            href = BASE_URL + href
        if href not in links:
            links.append(href)
        if len(links) >= limit:
            break

    return links

def extract_full_content(url):
    """
    Extracts full text content using trafilatura
    """
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        content = trafilatura.extract(downloaded)
        return content
    return None

if __name__ == "__main__":
    # Limit for each section
    blog_limit = 3
    article_limit = 3

    print("\n📝 Fetching Blogs...")
    blog_links = fetch_tab_links("blog", blog_limit)
    for i, link in enumerate(blog_links, 1):
        print(f"\nBlog {i}: {link}")
        content = extract_full_content(link)
        # print(content[:800] + "...\n" if content else "Failed to extract.\n")
        print(content + "...\n" if content else "Failed to extract.\n")

    print("\n📄 Fetching Articles...")
    article_links = fetch_tab_links("article", article_limit)
    for i, link in enumerate(article_links, 1):
        print(f"\nArticle {i}: {link}")
        content = extract_full_content(link)
        # print(content[:800] + "...\n" if content else "Failed to extract.\n")
        print(content + "...\n" if content else "Failed to extract.\n")
