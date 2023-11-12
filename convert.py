import tkinter as tk

def convert():
    temp = float(ent_fahr.get())
    result = (temp - 32) * 5/9
    lbl_cels["text"] = f"{result} °C"

window = tk.Tk()
window.title("Converter")

window.rowconfigure(0, minsize=10, weight=1)
window.columnconfigure((0, 1, 2), minsize=80, weight=1)

ent_fahr = tk.Entry(master=window, width=10)
ent_fahr.insert(0, "0")
ent_fahr.grid(row=0, column=0, sticky="nsew")

btn_convert = tk.Button(master=window, width=10, text="->", command=convert)
btn_convert.grid(row=0, column=1, sticky="nsew")

lbl_cels = tk.Label(master=window)
lbl_cels.grid(row=0, column=2, sticky="nsew")

window.mainloop()