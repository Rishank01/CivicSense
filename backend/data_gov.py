import requests

API_KEY = 'YOUR_DATA_GOV_API_KEY'  # Replace with your Data.gov.in API key
query = "health"
limit = 5

url = f"https://api.data.gov.in/resource/catalog.json?api-key={API_KEY}&format=json&filters[keyword]={query}&limit={limit}"

response = requests.get(url)

if response.status_code == 200:
    datasets = response.json().get('records', [])
    print("Top Government Datasets (Health):\n")
    for d in datasets:
        print(f"Title: {d.get('title')}")
        print(f"Organization: {d.get('org')}")
        print(f"Department: {d.get('sector')}")
        print(f"Last Updated: {d.get('last_updated')}")
        print(f"Download URL: {d.get('landing_url')}\n")
else:
    print("Failed to fetch datasets.")
