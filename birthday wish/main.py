import smtplib
import random
import datetime as dt
import pandas as pd

now = dt.datetime.now()
day = now.day
month = now.month
today=(month,day)
email = "chiyaanvasanth0@gmail.com"
password = 'ksgk fxcl wwoo pvbb'
df = pd.read_csv("birthdays.csv")
birthdays_dict= {(value.month,value.day):value for (key,value) in df.iterrows()}
if today in birthdays_dict:
    birthday=birthdays_dict[today]
    random = random.randint(1,3)
    with open(f"letter_templates/letter_{random}.txt") as file:
        read  = file.read()
        msg=read.replace("[NAME]",birthday["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs=birthday["email"],
                           msg=f"Subject:BirthdayWish\n\n {msg}")