from flask import Flask, render_template
import requests
from post import Post

articles = Post()

response = requests.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSeg15H9Ry2k1SoBLF0PW_iV-Nfh5WQDAcpzyaLXjt3b16jdpw/viewform?usp=sf_link")

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", posts=articles.posts)


@app.route("/<page>")
def get_page(page):
    if (page == "about"):
        return render_template("about.html")
    if (page == "contact"):
        return render_template("contact.html")
    if (page == "home"):
        return render_template("index.html")
    else:
        return "Page not found"


@app.route("/post/<int:num>")
def get_post(num):
    if (num == 1):
        return render_template("post.html", posts=articles.posts[0])
    if (num == 2):
        return render_template("post.html", posts=articles.posts[1])
    if (num == 3):
        return render_template("post.html", posts=articles.posts[2])
    else:
        return "Page not found"


if __name__ == "__main__":
    app.run()