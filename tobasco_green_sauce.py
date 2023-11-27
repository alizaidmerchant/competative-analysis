import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://shop.tabasco.com/products/green-sauce"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")
name = soup.find("h1",{"class":"value heading text-size--xlarge--fluid"})
print(name.text)

price = soup.find("span",{"class":"price"})
print(price.text)

des = soup.find("div",{"class":"product attribute description"})
print(des.text)

ingredients = soup.find("div",{"class":"product attribute ingredients"})
print(ingredients.text)

nutritions = soup.find("div",{"class":"product attribute nutrition_information col-md col-xs-12"})
print(nutritions.text)

# df = pd.DataFrame({"product_name":'name'})
# print(df)
print('aa')
print('assd')