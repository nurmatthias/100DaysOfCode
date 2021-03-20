from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

rounds = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global rounds
    rounds = 0
    lbl_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    lbl_checkmark.config(text="")
    app.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rounds
    rounds += 1

    if rounds % 8 == 0:
        lbl_title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif rounds % 2 == 0:
        lbl_title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        lbl_title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = str(math.floor(count/60))
    seconds = str(count % 60)
    text_to_show = f"{minutes}:{seconds.zfill(2)}"

    canvas.itemconfig(timer_text, text=text_to_show)
    if count > 0:
        global timer
        timer = app.after(1000, count_down, (count - 1))
    else:
        start_timer()

        marks = ""
        for _ in range(math.floor(rounds/2)):
            marks += "✓"
        lbl_checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
app = Tk()
app.title("Pomodoro")
app.config(padx=10, pady=10, bg=YELLOW)
#app.geometry('380x420')
app.resizable(False, False)


lbl_title = Label(text="Timer", width=11, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 26, "bold"))
lbl_title.grid(column=1, row=0, pady=(5, 20))

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

btn_start = Button(text="Start", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 12, "bold"), command=start_timer)
btn_start.grid(column=0, row=3, pady=(5, 5))

lbl_checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
lbl_checkmark.grid(column=1, row=2, pady=(20, 5))

btn_reset = Button(text="Reset", bg=YELLOW, fg=GREEN, highlightthickness=0, font=(FONT_NAME, 12, "bold"), command=reset_timer)
btn_reset.grid(column=2, row=3, pady=(5, 5))

app.mainloop()