import requests
from bs4 import BeautifulSoup

search = 'rtx+3070'

params = {
    'd' : search
}

response = requests.get("https://www.newegg.com/p/pl", params = params)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

item_divs = soup.find_all('div', class_ = "item-container")

for i in item_divs:
    print(i.prettify())