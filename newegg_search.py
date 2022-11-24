import requests, sys
from bs4 import BeautifulSoup

#---------------------------------------------------------#
# Takes a newegg url and parses for product name and 
# price shown on the website
# Returns an array looking like : [ Product Name , Price]
#---------------------------------------------------------#
def newegg_product_data(url):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    product_name = soup.h1.string

    price_div_tag = soup.find('div', class_ = 'product-price')
    price_tag = price_div_tag.find('strong')
    if price_tag == None:
        price = 'None'
    else:
        price_tag_dollar = price_div_tag.find('strong').string
        price_tag_cent = price_div_tag.find('sup').string
        price = price_tag_dollar+price_tag_cent
    
    return [product_name, price]

#---------------------------------------------------------#
# Takes the search string and sets as parameter for url
# Gets html response and parses for top 10 searches
# Calls product data function with item url
# Returns an array of top 10 searches from product data
#---------------------------------------------------------#
def newegg_search(search):
    data = []
    params = {
        'd' : search
    }

    response = requests.get("https://www.newegg.com/p/pl", params = params)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    item_divs = soup.find_all('div', class_ = "item-container")
    item_links = []

    for i in item_divs:
        item_links.append(i.a['href'])

    for i in range(1, 11, 1):
        inf = newegg_product_data(item_links[i])
        data.append(inf)

    return data

