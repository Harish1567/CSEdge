import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the website
url = "https://www.5paisa.com/share-market-today/nifty-50"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div with the data
div = soup.find('div', {'class': 'table-responsive'})

if div is None:
    print("Could not find div with class 'table-responsive'")
else:
    tr = div.find('tr')
    if tr is None:
        print("Could not find tr element in div")
    else:
        # Extract the table headers
        headers = [th.text.strip() for th in tr.find_all('th')]

        # Extract the table data
        data = []
        for row in div.find_all('tr')[1:]:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            data.append([col for col in cols])

        # Save the data to a CSV file
        with open('nifty50_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(data)

        print("Data saved to nifty50_data.csv")
