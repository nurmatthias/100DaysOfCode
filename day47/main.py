import random
from flask import Flask

app = Flask(__name__)
number_to_guess = None


def text_style(style):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            value = "<" + style + ">"
            value += func(*args, **kwargs)
            value += "</" + style + ">"
            return value
        return wrapped_func
    return decorator

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=300 >"


@app.route("/<int:number>")
def guess(number):
    if number < number_to_guess:
        return "<h2>to low...</h2>"\
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=300 >"
    elif number > number_to_guess:
        return "<h2>to high...</h2>"\
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=300 >"
    else:
        return "<h2>That's it!</h2>"\
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=300 >"


if __name__ == "__main__":
    number_to_guess = random.randint(0, 9)

    # run the app in debugmode for autoreload
    app.run(debug=True)
