import requests
from bs4 import BeautifulSoup

# ————————————————————————————————
# 1. SCRAPE PRSIndia “Recent Acts”
# ————————————————————————————————
def fetch_prs_recent_acts(max_items=10):
    url = "https://prsindia.org/recent-acts"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, "html.parser")
    acts = []

    # On this page, each act is in a <div class="view-content"> → <div class="views-row">
    for node in soup.select("div.view-content div.views-row")[:max_items]:
        title_el = node.select_one("h3 a")
        date_el  = node.select_one(".views-field-created span")
        link     = title_el["href"] if title_el else None

        acts.append({
            "title": title_el.get_text(strip=True) if title_el else None,
            "date":  date_el.get_text(strip=True) if date_el else None,
            "link":  ("https://prsindia.org" + link) if link and link.startswith("/") else link
        })

    return acts

# ————————————————————————————————
# 2. FETCH FROM Data.gov.in API (“Bills and Acts”)
#    Resource ID: f733ff8a-8213-4852-9f8a-2d2032f400de
# ————————————————————————————————
def fetch_data_gov_acts(api_key, limit=10):
    url = "https://api.data.gov.in/resource/f733ff8a-8213-4852-9f8a-2d2032f400de"
    params = {
        "api-key": api_key,
        "format":  "json",
        "limit":   limit
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json().get("records", [])

    # normalize fields you care about
    return [
        {
            "title": rec.get("bill_title") or rec.get("act_title") or rec.get("title"),
            "ministry": rec.get("ministry"),
            "status": rec.get("status"),
            "last_updated": rec.get("last_updated")
        }
        for rec in data
    ]

# ————————————————————————————————
# MAIN
# ————————————————————————————————
if __name__ == "__main__":
    print("\n🔹 Recent Acts from PRSIndia.org:\n")
    for act in fetch_prs_recent_acts():
        print(f"- {act['date']} | {act['title']}")
        print(f"  Link: {act['link']}\n")

    # Replace with your own Data.gov.in API key
    API_KEY = "YOUR_DATA_GOV_IN_API_KEY"
    print("\n🔹 Recent Bills/Acts from data.gov.in API:\n")
    for rec in fetch_data_gov_acts(API_KEY):
        print(f"- {rec['title']} ({rec['status']})")
        print(f"  Ministry: {rec['ministry']}")
        print(f"  Last Updated: {rec['last_updated']}\n")
