from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/post/<int:id>')
def post(id):

    post = [entry for entry in post_objects if entry.id == id]

    return render_template("post.html", post=post[0])


if __name__ == "__main__":
    app.run(debug=True)
