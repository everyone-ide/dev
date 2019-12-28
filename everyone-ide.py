#Everyone IDE by Jesse K. and M4-4TechGuns

import tkinter as tk
from tkinter import messagebox as mb
import os
from tkinter import filedialog as fd
from tkinter import ttk

#Settings
bg = "#ededed"
btn = "#dbdbdb"
fg = "#000"

#Vars
possible_chars = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "0","2","3","4","5","6","7","8","9","0","-","_","=","+","~","`","!","@","#","$","%","^","&","(",")",
    "[","]","{","}",";",",","."
]

def set_entry(e,text):
    e.delete(0,tk.END)
    e.insert(0,text)
    return

def newpro_browsepath():
    path = fd.askdirectory()
    set_entry(newpro_e2,path)

def create_screen2():
    global proname
    proname = newpro_e.get()
    global propath
    propath = newpro_e2.get()
    global procode
    procode = newpro_cb.get()

    if any(char in proname for char in possible_chars):
        try:
            newpro.destroy()
        except:
            pass
        global newpro2
        newpro2 = tk.Tk()
        newpro2.title("Create new Project")
        newpro2.config(bg=bg)
        newpro2.geometry("500x225")
        newpro2.iconbitmap("res/icon.ico")

        newpro2_lblfr = tk.LabelFrame(newpro2,text="Project type",padx=150,pady=30)
        newpro2_lblfr.grid(row=0,column=0)

        newpro2_lbl = tk.Label(newpro2_lblfr,text="Project type: ",bg=bg,fg=fg,font="Arial")
        newpro2_lbl.grid(row=0,column=0)

        global newpro2_cb
        newpro2_cb = ttk.Combobox(newpro2_lblfr, values=["Program","Game","Website"])
        newpro2_cb.grid(row=0,column=1)
        newpro2_cb.current(0)

        newpro2_btn = tk.Button(newpro2,text="Create",bg=btn,fg=fg,font="Arial",width=40,height=5)
        newpro2_btn.grid(row=1,column=0)

        newpro2.mainloop()
    else:
        mb.showerror("Error creating project","Woops, you forgot to fill in a project name!")

def create_screen():
    global proname
    proname = home_e.get()
    global propath
    propath = os.path.dirname(os.path.abspath(__file__))
    global procode
    procode = "Visual coding"

    if any(char in proname for char in possible_chars):
        try:
            home.destroy()
        except:
            pass
        global newpro
        newpro = tk.Tk()
        newpro.title("Create new Project")
        newpro.config(bg=bg)
        newpro.geometry("500x300")
        newpro.iconbitmap("res/icon.ico")

        newpro_lblfr = tk.LabelFrame(newpro,text="Settings",padx=75,pady=30)
        newpro_lblfr.grid(row=0,column=0)

        newpro_lbl = tk.Label(newpro_lblfr,text="Name: ",bg=bg,fg=fg,font="Arial")
        newpro_lbl.grid(row=0,column=0)

        global newpro_e
        newpro_e = tk.Entry(newpro_lblfr,font="Arial")
        newpro_e.grid(row=0,column=1)

        newpro_lbl2 = tk.Label(newpro_lblfr,text="Path to save project: ",bg=bg,fg=fg,font="Arial")
        newpro_lbl2.grid(row=1,column=0)

        global newpro_e2
        newpro_e2 = tk.Entry(newpro_lblfr,font="Arial")
        newpro_e2.grid(row=1,column=1)

        newpro_btn = tk.Button(newpro_lblfr,text="Browse",bg=btn,fg=fg,font="Arial",command=newpro_browsepath)
        newpro_btn.grid(row=1,column=3)

        newpro_lbl3 = tk.Label(newpro_lblfr,text="Way of coding: ",bg=bg,fg=fg,font="Arial")
        newpro_lbl3.grid(row=2,column=0)

        global newpro_cb
        newpro_cb = ttk.Combobox(newpro_lblfr, values=["Text coding","Visual coding"])
        newpro_cb.grid(row=2,column=1)
        newpro_cb.current(1)

        newpro_btn2 = tk.Button(newpro,text="Next",bg=btn,fg=fg,font="Arial",width=40,height=5,command=create_screen2)
        newpro_btn2.grid(row=1,column=0)

        set_entry(newpro_e,proname)
        set_entry(newpro_e2,propath)

        newpro.mainloop()
    else:
        mb.showerror("Error creating project","Woops, you forgot to fill in a project name!")

def home():
    global home
    home = tk.Tk()
    home.title("Everyone IDE")
    home.config(bg=bg)
    home.geometry("675x500")
    home.iconbitmap("res/icon.ico")

    home_title = tk.Label(home,text="Everyone IDE",bg=bg,fg=fg,font="Arial 57 bold")
    home_title.grid(row=0,column=0)

    home_lblfr = tk.LabelFrame(home,text="Create new project",padx=87,pady=30)
    home_lblfr.grid(row=1,column=0)

    home_lbl = tk.Label(home_lblfr,text="Name (Do not use \, /, :, *, ?, \", <, > or |): ",bg=bg,fg=fg,font="Arial")
    home_lbl.grid(row=1,column=0)

    global home_e
    home_e = tk.Entry(home_lblfr,font="Arial")
    home_e.grid(row=1,column=1)

    home_btn = tk.Button(home_lblfr,text="Create",bg=btn,fg=fg,font="Arial",command=create_screen)
    home_btn.grid(row=1,column=2)

    home_lblfr2 = tk.LabelFrame(home,text="Load project",padx=243,pady=30)
    home_lblfr2.grid(row=2,column=0)

    home_lbl2 = tk.Label(home_lblfr2,text="Load your project here.",bg=bg,fg=fg,font="Arial")
    home_lbl2.grid(row=1,column=0)

    home_btn2 = tk.Button(home_lblfr2,text="Load",bg=btn,fg=fg,font="Arial")
    home_btn2.grid(row=1,column=1)

    home_lblfr3 = tk.LabelFrame(home,text="Preferences",padx=55,pady=30)
    home_lblfr3.grid(row=3,column=0)

    home_lbl3 = tk.Label(home_lblfr3,text="Would you like to set up the IDE to your liking? You're at the right place.",bg=bg,fg=fg,font="Arial")
    home_lbl3.grid(row=1,column=0)

    home_btn3 = tk.Button(home_lblfr3,text="Preferences",bg=btn,fg=fg,font="Arial")
    home_btn3.grid(row=1,column=1)

    home_lbl4 = tk.Label(home,text="",bg=bg,fg=fg,font="Arial")
    home_lbl4.grid(row=4,column=0)

    home_lbl5 = tk.Label(home,text="© Everyone IDE",bg=bg,fg=fg,font="Arial")
    home_lbl5.grid(row=5,column=0)

    home.mainloop()

if __name__ == "__main__":
    home()
