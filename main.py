import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# set constants
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
BUY_PRICE = 45

# set url
url = "https://www.amazon.com/Ninja-BC151NV-Smoothies-Rechargeable-Dishwasher/dp/B0C2FF74J6/ref=lp_289914_1_9?pf_rd_p=53d84f87-8073-4df1-9740-1bf3fa798149&pf_rd_r=3C8ZS7Z8TY42S507Q0H8&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&th=1"
response = requests.get(url)
website = response.text

# scrap site
soup = BeautifulSoup(website, "html.parser")
# print(soup.prettify())

# get price
price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# get item title
title = soup.find(id="productTitle").get_text().strip()

# send email
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr="MY_EMAIL",
                            to_addrs="maheshchaulagain8@gmail.com",
                            msg=f"Subject:Amazon Low Price Alert!\n"
                                f"{message}\n")
else:
    message = f"{title} is currently {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr="MY_EMAIL",
                            to_addrs="maheshchaulagain8@gmail.com",
                            msg=f"Subject:Amazon High Price Alert!\n"
                                f"{message}\n")
