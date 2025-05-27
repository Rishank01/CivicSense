import feedparser
import requests

# -------------------------------
# 1. PRS Legislative Research - RSS
# -------------------------------
def fetch_prs_bills():
    print("📘 PRSIndia.org - Recent Bills:\n")
    rss_url = "https://prsindia.org/media/rss-feeds/bills-introduced"
    feed = feedparser.parse(rss_url)
    print(feed)
    if feed.entries:
        for entry in feed.entries[:5]:
            print(f"🧾 Title: {entry.title}")
            print(f"📅 Published: {entry.published}")
            print(f"🔗 Link: {entry.link}\n")
    else:
        print("ℹ️ No recent bills found.")

# -------------------------------
# 2. IndiaCode.nic.in - Official Central Acts
# -------------------------------
def fetch_india_code():
    print("\n⚖️ IndiaCode - Recent Acts:\n")
    url = "https://www.indiacode.nic.in/acts-list.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            acts = response.json()
            for act in acts[:5]:
                print(f"📘 Act Title: {act.get('acttitle')}")
                print(f"🏛️ Ministry: {act.get('ministry')}")
                print(f"📄 Act ID: {act.get('actid')}\n")
        else:
            print("❌ Failed to fetch IndiaCode data (status code:", response.status_code, ")")
    except Exception as e:
        print(f"❌ Error: {e}")

# -------------------------------
# 3. PIB - Press Information Bureau - RSS
# -------------------------------
def fetch_pib_press_releases():
    print("\n📰 PIB Press Releases - Laws & Acts:\n")
    rss_url = "https://pib.gov.in/PressReleaseRSS.aspx"
    feed = feedparser.parse(rss_url)

    count = 0
    for entry in feed.entries:
        # Only show entries with keywords like 'bill', 'act', or 'law'
        if any(keyword in entry.title.lower() for keyword in ['bill', 'act', 'law']):
            print(f"📌 Title: {entry.title}")
            print(f"📅 Published: {entry.published}")
            print(f"🔗 Link: {entry.link}\n")
            count += 1
        if count >= 5:
            break
    if count == 0:
        print("ℹ️ No recent law-related updates in PIB feed.")

# -------------------------------
# Main Function
# -------------------------------
def main():
    print("🧠 Fetching Recent Indian Laws, Bills, and Acts...\n")
    fetch_prs_bills()
    fetch_india_code()
    fetch_pib_press_releases()

if __name__ == "__main__":
    main()
