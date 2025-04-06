from flask import Flask, render_template , request
import requests
import os
import smtplib

email = os.getenv("email")
password = os.getenv("password")


posts = requests.get("https://api.npoint.io/9b171125d97f28c527ae").json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html" , all_posts = posts)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/form-data", methods=["GET","POST"])
def form_data():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone_no"], data["message"])
        return  render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, to_email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {to_email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(email, email ,email_message)

if __name__ == "__main__":
    app.run(debug=True)
