import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Ninja-BC151NV-Smoothies-Rechargeable-Dishwasher/dp/B0C2FF74J6/ref=lp_289914_1_9?pf_rd_p=53d84f87-8073-4df1-9740-1bf3fa798149&pf_rd_r=3C8ZS7Z8TY42S507Q0H8&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&th=1"
response = requests.get(url)
website = response.text

soup = BeautifulSoup(website, "html.parser")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)