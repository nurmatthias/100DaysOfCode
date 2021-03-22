import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from password_gen import generate_password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password = generate_password()
    inp_password.delete(0, END)
    inp_password.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = inp_website.get()
    user = inp_user.get()
    password = inp_password.get()
    new_data = {website: {"email": user,"password": password,}}

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops...", message="Please don't leave any fields empty!")
    
    else:
        try:
            with open("day30/data.json", mode="r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            with open("day30/data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
        
            with open("day30/data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:    
            reset_ui()
    

def reset_ui():
    inp_website.delete(0, END)
    inp_website.focus()

    inp_user.delete(0, END)
    inp_user.insert(0, "dienst@mail.org")

    inp_password.delete(0, END)

def search_passwd():
    try:
        with open("day30/data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="The data file was not found! Safe your first password...")
    else:
        # TODO: keiner guter Stil, besser umstellen auf if/else
        try:
            website_data = data[inp_website.get()]
        except KeyError:
            messagebox.showwarning(title="Not found", message="No details for the website exists!")
        else:
            messagebox.showinfo(title=inp_website.get(), message=f"User: {website_data['email']} \nPassword: {website_data['password']}")



# ---------------------------- UI SETUP ------------------------------- #
app = Tk()
app.title("PyPa-Manager")
app.config(padx=30, pady=30)
#app.resizable(False, False)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


lbl_website = Label(text="Website:")
lbl_website.grid(column=0, row=1, pady=(5, 0), sticky="e")
inp_website = Entry(width=30)
inp_website.grid(column=1, row=1, pady=(5, 0), sticky="w")
btn_search = Button(text="Search", width=8, command=search_passwd)
btn_search.grid(column=2, row=1, pady=(5, 0), sticky="e")

lbl_user = Label(text="Email/Username:")
lbl_user.grid(column=0, row=2, pady=(5, 0), sticky="e")
inp_user = Entry(width=43)
inp_user.grid(column=1, row=2, pady=(5, 0), columnspan=2, sticky="w")

lbl_password = Label(text="Password:")
lbl_password.grid(column=0, row=3, pady=(5, 0), sticky="e")
inp_password = Entry(width=30)
inp_password.grid(column=1, row=3, pady=(5, 0), sticky="w")
btn_password = Button(text="Generate", width=8, command=gen_password)
btn_password.grid(column=2, row=3, pady=(5, 0), sticky="e")

btn_add = Button(text="Add", width=36, command=save_password)
btn_add.grid(column=1, row=4, pady=(10, 0), columnspan=2, sticky="e")


reset_ui()

app.mainloop()