#Everyone IDE by Jesse K. and M4-4TechGuns

import tkinter as tk
from tkinter import messagebox as mb
import os
from tkinter import filedialog as fd
from tkinter import ttk
import shutil

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

def get_lb(root_l):
    item = root_l.get(root_l.curselection())
    return item

def set_entry(e,text):
    e.delete(0,tk.END)
    e.insert(0,text)
    return

def editor(proname,propath,procode,protype):
    print(proname)
    print(propath)
    print(procode)
    print(protype)

def newpro_create():
    global protype
    protype = newpro2_cb.get()

    try:
        newpro2.destroy()
    except:
        pass

    prdf = open("./prd/" + proname + ".eprd","w")
    prdf.write(proname + "\n" + propath + "\n" + procode + "\n" + protype)
    prdf.close()

    os.mkdir(propath + "/" + proname)

    editor(proname,propath,procode,protype)

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

        newpro2_btn = tk.Button(newpro2,text="Create",bg=btn,fg=fg,font="Arial",width=40,height=5,command=newpro_create)
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

def load_load():
    global proname
    global propath
    global procode
    global protype
    try:
        sel = get_lb(load_lb)

        with open("./prd/" + sel + ".eprd") as data:
            lines = data.readlines()
        proname = lines[0]
        propath = lines[1]
        procode = lines[2]
        protype = lines[3]

        try:
            load.destroy()
        except:
            pass

        editor(proname,propath,procode,protype)
    except:
        mb.showerror("Error loading project","Woops, you forgot to select a project to load!")

def load_screen():
    try:
        home.destroy()
    except:
        pass

    global load
    load = tk.Tk()
    load.title("Load Project")
    load.config(bg=bg)
    load.geometry("365x350")
    load.iconbitmap("res/icon.ico")

    load_lblfr = tk.LabelFrame(load,text="Select project",padx=87,pady=30)
    load_lblfr.grid(row=0,column=0)

    global load_lb
    load_lb = tk.Listbox(load_lblfr,selectmode=tk.SINGLE)
    load_lb.grid(row=0,column=0)
    load_lb.delete(0,tk.END)
    for file in os.listdir("./prd/"):
        load_lb.insert(1,os.path.splitext(str(file))[0])

    load_btn = tk.Button(load,text="Load",bg=btn,fg=fg,font="Arial",width=40,height=5,command=load_load)
    load_btn.grid(row=1,column=0)

    load.mainloop()

def sts_backup_do():
    shutil.copyfile("./prd/" + get_lb(bau_lb) + ".eprd","./backup/" + get_lb(bau_lb) + ".eprd")
    mb.showinfo("Done","Backuped " + get_lb(bau_lb))

def sts_loadbackup_do():
    shutil.copyfile("./backup/" + get_lb(bau_lb) + ".eprd","./prd/" + get_lb(bau_lb) + ".eprd")
    mb.showinfo("Done","Loaded " + get_lb(bau_lb) + " from backup")

def sts_backup():
    global bau
    bau = tk.Tk()
    bau.title("Backup Project")
    bau.config(bg=bg)
    bau.geometry("365x350")
    bau.iconbitmap("res/icon.ico")

    bau_lblfr = tk.LabelFrame(bau,text="Select backup",padx=87,pady=30)
    bau_lblfr.grid(row=0,column=0)

    global bau_lb
    bau_lb = tk.Listbox(bau_lblfr,selectmode=tk.SINGLE)
    bau_lb.grid(row=0,column=0)
    bau_lb.delete(0,tk.END)
    for file in os.listdir("./prd/"):
        bau_lb.insert(1,os.path.splitext(str(file))[0])

    bau_btn = tk.Button(bau,text="Backup",bg=btn,fg=fg,font="Arial",width=40,height=5,command=sts_backup_do)
    bau_btn.grid(row=2,column=0)

def sts_loadbackup():
    global bau
    bau = tk.Tk()
    bau.title("Load Backup Project")
    bau.config(bg=bg)
    bau.geometry("365x350")
    bau.iconbitmap("res/icon.ico")

    bau_lblfr = tk.LabelFrame(bau,text="Select project",padx=87,pady=30)
    bau_lblfr.grid(row=0,column=0)

    global bau_lb
    bau_lb = tk.Listbox(bau_lblfr,selectmode=tk.SINGLE)
    bau_lb.grid(row=0,column=0)
    bau_lb.delete(0,tk.END)
    for file in os.listdir("./backup/"):
        bau_lb.insert(1,os.path.splitext(str(file))[0])

    bau_btn = tk.Button(bau,text="Load",bg=btn,fg=fg,font="Arial",width=40,height=5,command=sts_loadbackup_do)
    bau_btn.grid(row=2,column=0)

def settings():
    try:
        home.destroy()
    except:
        pass

    global settings
    sts = tk.Tk()
    sts.title("Preferences")
    sts.config(bg=bg)
    sts.geometry("675x500")
    sts.iconbitmap("res/icon.ico")

    sts_lblfr = tk.LabelFrame(sts,text="Backups",padx=250,pady=30)
    sts_lblfr.grid(row=0,column=0)

    sts_lbl = tk.Label(sts_lblfr,text="Backup project: ",bg=bg,fg=fg,font="Arial")
    sts_lbl.grid(row=0,column=0)

    sts_btn = tk.Button(sts_lblfr,text="Select project",bg=btn,fg=fg,font="Arial",command=sts_backup)
    sts_btn.grid(row=0,column=1)

    sts_lbl2 = tk.Label(sts_lblfr,text="Load backup: ",bg=bg,fg=fg,font="Arial")
    sts_lbl2.grid(row=1,column=0)

    sts_btn2 = tk.Button(sts_lblfr,text="Select project",bg=btn,fg=fg,font="Arial",command=sts_loadbackup)
    sts_btn2.grid(row=1,column=1)

    sts.mainloop()

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

    home_btn2 = tk.Button(home_lblfr2,text="Load",bg=btn,fg=fg,font="Arial",command=load_screen)
    home_btn2.grid(row=1,column=1)

    home_lblfr3 = tk.LabelFrame(home,text="Preferences",padx=55,pady=30)
    home_lblfr3.grid(row=3,column=0)

    home_lbl3 = tk.Label(home_lblfr3,text="Would you like to set up the IDE to your liking? You're at the right place.",bg=bg,fg=fg,font="Arial")
    home_lbl3.grid(row=1,column=0)

    home_btn3 = tk.Button(home_lblfr3,text="Preferences",bg=btn,fg=fg,font="Arial",command=settings)
    home_btn3.grid(row=1,column=1)

    home_lbl4 = tk.Label(home,text="",bg=bg,fg=fg,font="Arial")
    home_lbl4.grid(row=4,column=0)

    home_lbl5 = tk.Label(home,text="© Everyone IDE",bg=bg,fg=fg,font="Arial")
    home_lbl5.grid(row=5,column=0)

    home.mainloop()

if __name__ == "__main__":
    home()
