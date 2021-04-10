from flask import Flask, render_template
import requests
import random
import datetime as dt

AGIFY_API = "https://api.agify.io"
GENDERIZE_API = "https://api.genderize.io"
API_PARAM = {"name": None}

BLOG_API = "https://api.npoint.io/5abcca6f4e39b4955965"


app = Flask(__name__)
cp_year = dt.datetime.now().year

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, cp_year=cp_year)

@app.route("/guess/<name>")
def guess(name):
    API_PARAM["name"] = name

    response = requests.get(AGIFY_API, API_PARAM)
    response.raise_for_status()
    age = response.json()["age"]

    response = requests.get(GENDERIZE_API, API_PARAM)
    response.raise_for_status()
    gender = response.json()["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def blog():
    response = requests.get(BLOG_API)
    response.raise_for_status()
    all_post = response.json()

    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)