import tkinter as t

window = t.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

window.config(padx=10, pady=10)

input = t.Entry(width=10)
input.insert(t.END, string="0")
input.grid(row=0, column=1, padx=(10, 1), pady=(5, 5))

label_miles = t.Label(text="Miles")
label_miles.grid(row=0, column=2, padx=(1, 10), pady=(5, 5))

label_equal = t.Label(text="is equal to")
label_equal.grid(row=1, column=0, padx=(10, 1), pady=(5, 5))

label_km_value = t.Label(text="0")
label_km_value.grid(row=1, column=1, padx=(10, 1), pady=(5, 5))

label_km = t.Label(text="Km")
label_km.grid(row=1, column=2, padx=(1, 10), pady=(5, 5))

def calc():
    new_value = round(float(input.get()) * 1.609, 2)
    label_km_value.config(text=f"{new_value}")

calculate = t.Button(text="Calculate", command=calc)
calculate.grid(row=2, column=1, padx=(10, 10), pady=(5, 5))

window.mainloop()