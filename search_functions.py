from bs4 import BeautifulSoup
import requests

def newegg_search(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    product_name = soup.h1.string

    price_div_tag = soup.find('div', class_ = 'product-price')
    #print(price_div_tag.prettify())
    price_tag_dollar = price_div_tag.find('strong').string
    price_tag_cent = price_div_tag.find('sup').string
    price = price_tag_dollar+price_tag_cent
    
    return [product_name, price]