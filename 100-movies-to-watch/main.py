import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
data = response.text

soup = BeautifulSoup(data,"html.parser")
titles = soup.find_all(name="h3",class_="title")
reverse = []
for title in titles:
    reverse.insert(0,title.get_text())
print(reverse)

with open("movies.txt","w",encoding="utf-8") as file:
    for titl in reverse:
        file.write(f"{titl}\n")
