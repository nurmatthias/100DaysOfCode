import tkinter as t

window = t.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=500)

window.config(padx=10, pady=10)

#Labels
label = t.Label(text="This is old text")
label.config(text="This is new text")
#label.pack()
#label.place(x=100, y=50)
label.grid(column=0, row=0)

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = t.Button(text="Click Me", command=action)
#button.pack()
button.grid(column=1, row=1)

#calls action() when pressed
button2 = t.Button(text="Click Me 2", command=action)
#button.pack()
button2.grid(column=2, row=0)

#Entries
entry = t.Entry(width=30)
#Add some text to begin with
entry.insert(t.END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
#entry.pack()
entry.grid(column=3, row=2)


window.mainloop()