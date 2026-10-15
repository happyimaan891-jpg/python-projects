import requests
from bs4 import BeautifulSoup
import pandas as pd

# Web Scraper Example
url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    
    for item in soup.find_all('div', class_='product'):
        title = item.find('h2').text
        price = item.find('span', class_='price').text
        data.append({'Title': title, 'Price': price})
        
    df = pd.DataFrame(data)
    df.to_csv('scraped_products.csv', index=False)
    print("Data Scraped & Saved Successfully!")
