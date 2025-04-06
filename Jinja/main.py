import requests
from flask import Flask, render_template
import datetime
import random
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    currentyear = datetime.datetime.now().year
    return render_template("index.html",num = random_number,date = currentyear)


@app.route("/guess/<name>")
def guess(name):
    ageresponse = requests.get(f"https://api.agify.io?name={name}")
    agedata = ageresponse.json()
    age = agedata["age"]

    genderresponse = requests.get(f"https://api.genderize.io?name={name}")
    genderdata = genderresponse.json()
    gender = genderdata["gender"]
    return render_template("guess.html",name=name.title(),age=age,gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    return render_template("blog.html",blog_posts =all_blogs)

if __name__ == "__main__":
    app.run(debug=True)






