import tkinter as tk
import random

def roll():
    result = random.randint(0, 6)
    lbl_result["text"] = f"{result}"

window = tk.Tk()
window.title("Dice")

window.rowconfigure((0, 1), minsize=10, weight=1)
window.columnconfigure(0, minsize=200, weight=1)

btn_roll = tk.Button(master=window, text="I'll be lucky!", command=roll)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_result = tk.Label(master=window)
lbl_result.grid(row=1, column=0)

window.mainloop()