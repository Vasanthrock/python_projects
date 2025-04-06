import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://appbrewery.github.io/instant_pot/"
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=headers)
data = response.content

soup = BeautifulSoup(data,"lxml")
# print(soup)
price = soup.find(name= "span" ,class_= "a-price-whole").get_text()

float_price = float(price)
print(float_price)

title = soup.find(id="productTitle").get_text()
print(title)

BUY_PRICE = 90

if float_price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=os.getenv('EMAIL'), password=os.getenv('PASSWORD'))
        connection.sendmail(
            from_addr=os.getenv('EMAIL'),
            to_addrs=os.getenv('TO_EMAIL'),
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
        print(result)
else:
    print(f"\nStill too expensive")