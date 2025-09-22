import requests
from bs4 import BeautifulSoup

# Target website
url = "http://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quote blocks
    quotes = soup.find_all('div', class_='quote')

    # Loop through and extract quote text and author
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"{text} — {author}")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
