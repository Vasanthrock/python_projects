import smtplib
import random
import datetime as dt
import pandas as pd
import os

email = os.getenv("email")
password = os.getenv("password")
to_address= os.getenv("to_address")

now = dt.datetime.now()
day=now.weekday()
if day == 4:

    with open("./quotes.txt") as file:
        read = file.readlines()
        quote = random.choice(read)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs= to_address,
                           msg=f"Subject:Motivaion\n\n {quote}")

