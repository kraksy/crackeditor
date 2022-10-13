import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = tk.Tk()
root.title("crack editor")
root.wm_iconbitmap("icon.ico")
root.geometry('500x400')

txt = scrolledtext.ScrolledText(root, height=999)
txt.grid(row=1,sticky=N+S+E+W)

txt_edit = tk.Text(root)

def hello():
    tkinter.messagebox.showinfo("wip","made in arch powered toaster")

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    root.title(f"Text Editor Application - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    root.title(f"Text Editor Application - {filepath}")

hlavniMenu = Menu(root)

menuSoubor = Menu(hlavniMenu, tearoff=0)
menuSoubor.add_command(label="Otevřít", command=open_file)
menuSoubor.add_command(label="Uložit", command=save_file)
menuSoubor.add_separator()
menuSoubor.add_command(label="Pryč", command=root.quit)
hlavniMenu.add_cascade(label="Soubor", menu=menuSoubor)

menuNapoveda = Menu(hlavniMenu, tearoff=0)
menuNapoveda.add_command(label="O aplikaci", command=hello)
hlavniMenu.add_cascade(label="Nápověda", menu=menuNapoveda)

root.config(menu=hlavniMenu)

root.mainloop()