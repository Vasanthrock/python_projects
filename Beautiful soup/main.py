from bs4 import BeautifulSoup
import lxml
import requests

# with open("website.html", encoding='utf-8') as file:
#     contents=file.read()
#
# soup = BeautifulSoup(contents,"html.parser" )
#
# print(soup.title)

response = requests.get(url="https://news.ycombinator.com/")
data = response.text

soup = BeautifulSoup(data,"html.parser")

articles = soup.find_all(name= "span" ,class_ = "titleline")
article_text = []
article_link = []
for article_tag in articles:
    text = article_tag.get_text()
    article_text.append(text)
    link = article_tag.find(name="a").get("href")
    article_link.append(link)
article_upvote = [int(vote.get_text().split()[0]) for vote in soup.find_all(name = "span" , class_="score")]
print(article_upvote)
highest_vote = article_upvote[0]
hight = 0
for high in range(len(article_upvote)):
    if article_upvote[high] > highest_vote:
        highest_vote = article_upvote[high]
        hight = high

# print(highest_vote)
print(article_text[hight])
print(article_link[hight])