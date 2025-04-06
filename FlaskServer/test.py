from flask import Flask
import random
app = Flask(__name__)
random_number = random.randint(0,9)

def bold(function):
    def wrap():
        return f"<b>{function()}</b>"
    return wrap

def italic(function):
    def wrap():
        return f"<em>{function()}</em>"
    return wrap

def underline(function):
    def wrap():
        return f"<u>{function()}</u>"
    return wrap

@app.route("/")
# @bold
# @italic
# @underline
def hello():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src = https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>")


@app.route("/<int:num>")
def numbers(num):
    if num == random_number:
        return ("<h1 style='color:purple'>You found me</h1>"
                "<img src = https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>")
    elif num > random_number:
        return ("<h1 style='color:red'>Too High try again</h1>"
                "<img src = https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>")
    else:
        return ("<h1 style='color:green'>Too Low try again</h1>"
                "<img src = https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>")


if __name__ == "__main__":
    app.run(debug=True)