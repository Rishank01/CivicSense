import requests
from bs4 import BeautifulSoup

def fetch_passed_bills():
    url = 'https://prsindia.org/billtrack'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    bills = []

    # Find all bill entries
    for bill_entry in soup.find_all('div', class_='views-row'):
        title_tag = bill_entry.find('h3')
        status_tag = bill_entry.find('div', class_='field-content')

        if title_tag and status_tag:
            title = title_tag.get_text(strip=True)
            status = status_tag.get_text(strip=True)

            if 'Passed' in status:
                bills.append({
                    'title': title,
                    'status': status
                })

    return bills

if __name__ == "__main__":
    passed_bills = fetch_passed_bills()
    for bill in passed_bills:
        print(f"Title: {bill['title']}, Status: {bill['status']}")
