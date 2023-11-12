import tkinter as tk
from tkinter import filedialog

def openFile():
    global filepath
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r', encoding='utf-8')
    for line in file:
        txt_file.insert(tk.END, line)
    file.close()

def saveFile():
    file = open(filepath, 'w', encoding='utf-8')
    text = txt_file.get("1.0", tk.END)
    file.write(text)
    file.close()

window = tk.Tk()
window.title("Notepad")

window.rowconfigure((0, 1), minsize=200, weight=1)
window.columnconfigure(0, minsize=70, weight=1)
window.columnconfigure(1, minsize=200, weight=1)

txt_file = tk.Text(master=window)
txt_file.grid(column=1, rowspan=2, sticky="nsew")

btn_open = tk.Button(master=window, text="Open", command=openFile)
btn_open.grid(row=0, column=0, sticky="nsew")

btn_save = tk.Button(master=window, text="Save", command=saveFile)
btn_save.grid(row=1, column=0, sticky="nsew")

window.mainloop()