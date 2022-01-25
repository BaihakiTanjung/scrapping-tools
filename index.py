# import json

# import requests from BeautifulSoup as bs

from itertools import product
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from selenium import webdriver

url = "https://segari.id/"

browser = webdriver.Chrome('/Users/david/Downloads/chromedriver')

browser.get(url)

nav = browser.find_element_by_id("body")

print(nav.text)
# result:
# site_json = json.loads(rows)

# items = site_json['props']['initialProps']['pageProps']['productGroupSelected']['products']['items']

# data = []
# for item in items:
#     obj = {
#         "name": item['name'],
#         "price": item['salesPrice']
#     }
# data.append(obj)

# data.append(item['name'])

# df = pd.DataFrame(data)
# df.to_csv('myfile.csv')

print(soup.prettify())


# printing for entrezgene, do the same for name and symbol
# print()
# divs = rows.find
# divs = rows.findAll("div", class_="cardProductContent-0-2-145")
# data = []
# for row in rows:
#     data.append(row)
