from tkinter import *
import pandas as p
import random


BACKGROUND_COLOR = "#B1DDC6"

LANG_TO_LEARN = "französisch"
LANG_TO_TRANS = "englisch"

timer = None
actual_word = None

dictionary_lvl1 = p.read_csv("day31/data/french_words.csv").to_dict(orient="records")

try:
    dictionary_lvl2 = p.read_csv("day31/data/french_words_learned.csv").to_dict(orient="records")
except:
    dictionary_lvl2 = []
else:
    dictionary_lvl1 = [entry for entry in dictionary_lvl1 if entry not in dictionary_lvl2]


def present_next_word():
    global actual_word
    actual_word = random.choice(dictionary_lvl1)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(lang_text, text=str(LANG_TO_LEARN))
    canvas.itemconfig(word_text, text=str(actual_word["French"]))

    btn_wrong.config(state="disabled")
    btn_right.config(state="disabled")

    global timer
    timer = app.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(lang_text, text=str(LANG_TO_TRANS))
    canvas.itemconfig(word_text, text=str(actual_word["English"]))

    btn_wrong.config(state="normal")
    btn_right.config(state="normal")
    

def right():
    dictionary_lvl2.append(actual_word)
    if actual_word in dictionary_lvl1:
        dictionary_lvl1.remove(actual_word)
    p.DataFrame(dictionary_lvl2).to_csv("day31/data/french_words_learned.csv", index = False)
    present_next_word()

def wrong():
    dictionary_lvl1.append(actual_word)
    if actual_word in dictionary_lvl2:
        dictionary_lvl2.remove(actual_word)
    present_next_word()


# ---------------------------- UI ------------------------------- #
app = Tk()
app.title("PyPa-Manager")
app.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
#app.resizable(False, False)

card_front_img = PhotoImage(file="day31/images/card_front.png")
card_back_img = PhotoImage(file="day31/images/card_back.png")
btn_right_img = PhotoImage(file="day31/images/right.png")
btn_wrong_img = PhotoImage(file="day31/images/wrong.png")

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 265, image=card_front_img)
lang_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic") )
word_text = canvas.create_text(400, 265, font=("Ariel", 60, "bold") )
canvas.grid(column=0, row=0, columnspan=2)

btn_wrong = Button(image=btn_wrong_img, highlightthickness=0, command=wrong)
btn_wrong.grid(column=0, row=1, pady=(10, 0))

btn_right = Button(image=btn_right_img, highlightthickness=0, command=right)
btn_right.grid(column=1, row=1, pady=(10, 0))

# ------------------------------ App-flow handling -------------------#
present_next_word()

app.mainloop()