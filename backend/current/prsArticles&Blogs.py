from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time


def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    return webdriver.Chrome(options=options)


def get_filtered_url(base_url, year, month):
    if year and month:
        return f"{base_url}/{year}/{month.lower()}"
    elif year:
        return f"{base_url}/{year}"
    return base_url

def fetch_prs_links(content_type='article', max_count=5, year=None, month=None):
    base_urls = {
        'article': "https://prsindia.org/articles-by-prs-team",
        'blog': "https://prsindia.org/theprsblog"
    }
    base_url = base_urls.get(content_type)
    if not base_url:
        return []

    url = get_filtered_url(base_url, year, month)
    driver = setup_driver()
    driver.get(url)
    time.sleep(2)

    links_data = []

    try:
        items = driver.find_elements(By.CSS_SELECTOR, "div.views-row")[:max_count]
        for item in items:
            link_tag = item.find_element(By.CSS_SELECTOR, 'a')
            title = link_tag.text.strip() or "Untitled"
            href = link_tag.get_attribute('href')
            if href:
                links_data.append({"title": title, "url": href})
    except NoSuchElementException:
        print(f"No elements found for {content_type}s.")

    driver.quit()
    return links_data


def fetch_blog_content(url):
    """Fetch content text from a single blog post URL using provided class selectors."""
    driver = setup_driver()
    driver.get(url)
    time.sleep(2)
    content = ""

    try:
        main_div = driver.find_element(By.CSS_SELECTOR, "div.card.p-4.mt-3.shadow.bg-white.rounded")
        heading = ""
        body = ""

        try:
            heading = main_div.find_element(By.CSS_SELECTOR, ".top_heading").text.strip()
        except NoSuchElementException:
            heading = ""

        try:
            body = main_div.find_element(By.CSS_SELECTOR, ".top_content").text.strip()
        except NoSuchElementException:
            body = ""

        content = (heading + "\n\n" + body).strip()
    except NoSuchElementException:
        print(f"Could not find content container for blog URL: {url}")

    driver.quit()
    return content


def fetch_article_content(url):
    """Fetch full content from a single article URL and inject 'Read more' separator if applicable."""
    driver = setup_driver()
    driver.get(url)
    time.sleep(2)

    before_read_more = ""
    after_read_more = ""
    full_content = ""

    try:
        main_div = driver.find_element(By.CSS_SELECTOR, "div.other_fields")

        try:
            content_div = main_div.find_element(By.CSS_SELECTOR, "div.views-field.views-field-body > span.field-content")
            paragraphs = content_div.find_elements(By.TAG_NAME, "p")

            content_chunks = []
            external_link = None

            for p in paragraphs:
                text = p.text.strip()
                if not text:
                    continue
                link_elem = p.find_elements(By.TAG_NAME, "a")
                if link_elem:
                    href = link_elem[0].get_attribute("href")
                    if "indianexpress.com" in href:
                        external_link = href
                        break  # Stop collecting here; link is the 'Read more'
                else:
                    content_chunks.append(text)

            before_read_more = "\n\n".join(content_chunks)

            # Now fetch after_read_more from the Indian Express page if link found
            if external_link:
                try:
                    driver.get(external_link)
                    time.sleep(2)

                    after_read_more = fetch_redirected_indianexpress_content(driver)

                except Exception as e:
                    print(f"Error loading external article link: {external_link}\n{e}")

            # Combine both with separator
            if after_read_more:
                full_content = after_read_more
            else:
                full_content = before_read_more

        except NoSuchElementException:
            print(f"Could not find article body content for URL: {url}")

    except NoSuchElementException:
        print(f"Could not find content container for article URL: {url}")

    driver.quit()
    return full_content.strip()


def fetch_redirected_indianexpress_content(driver):
    """Extract full content from Indian Express redirected article pages using multiple strategies."""
    selectors = [
        "div.section-article-template.native_story.iestory_9812480",  # Known full content class
        "div.full-details",  # Generic fallback
        "div.story-content",  # Sometimes used
        "div.native_story",  # Broader selector
        "article"  # Last fallback for article content
    ]

    for selector in selectors:
        try:
            container = driver.find_element(By.CSS_SELECTOR, selector)
            paragraphs = container.find_elements(By.TAG_NAME, "p")
            if paragraphs:
                return "\n\n".join(p.text.strip() for p in paragraphs if p.text.strip())
        except NoSuchElementException:
            continue
        except Exception as e:
            print(f"Error while trying selector {selector}: {e}")
            continue

    print(f"[!] Could not extract redirected content from {driver.current_url}")
    return ""



def fetch_full_contents(content_type='article', max_count=5, year=None, month=None):
    # Step 1: fetch urls + titles
    links = fetch_prs_links(content_type=content_type, max_count=max_count, year=year, month=month)

    # Step 2: for each url, fetch content
    full_data = []
    for item in links:
        url = item['url']
        title = item['title']
        if content_type == 'blog':
            content = fetch_blog_content(url)
        else:
            content = fetch_article_content(url)
        full_data.append({
            "title": title,
            "url": url,
            "content": content
        })
    return full_data


# 🔧 Example usage:
if __name__ == "__main__":
    print("Fetching Blogs with Content...")
    # blogs_with_content = fetch_full_contents(content_type='blog', max_count=3, year='2025', month='may')
    # blogs_with_content = fetch_full_contents(content_type='blog', max_count=3)
    # for b in blogs_with_content:
    #     print(f"\nTitle: {b['title']}\nURL: {b['url']}\nContent snippet: {b['content']}...\n")

    print("\nFetching Articles with Content...")
    articles_with_content = fetch_full_contents(content_type='article', max_count=3)
    for a in articles_with_content:
        print(f"\nTitle: {a['title']}\nURL: {a['url']}\nContent snippet: {a['content']}...\n")
