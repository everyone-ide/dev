#Everyone IDE by Jesse K. and M4-4TechGuns

import tkinter as tk
from tkinter import messagebox as mb
import os
from tkinter import filedialog as fd
from tkinter import ttk
import shutil
import sys

#Settings
with open("sts.ests") as data:
    lines = data.readlines()
bg = lines[0]
btn = lines[1]
fg = lines[2]

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

def editor_text():
    pass

def editor(proname,propath,procode,protype):
    global editor
    editor = tk.Tk()
    editor.title("Editor")
    editor.config(bg=bg)
    editor.state('zoomed')
    editor.iconbitmap("./res/icon.ico")

    if procode == "Text coding":
        editor_text()
    elif procode == "Visual coding":
        mb.showerror("Sorry","Sorry... This is coming soon...")

def newpro_create():
    global protype
    protype = newpro2_cb.get()

    prdf = open("./prd/" + proname + ".eprd","w")
    prdf.write(proname + "\n" + propath + "\n" + procode + "\n" + protype)
    prdf.close()

    try:
        os.mkdir(propath + "/" + proname)

        try:
            newpro2.destroy()
        except:
            pass

        editor(proname,propath,procode,protype)
    except Exception as e:
        mb.showerror("Error",e)

def newpro_browsepath():
    path = fd.askdirectory()
    set_entry(newpro_e2,path)

def newpro2_back():
    newpro2.destroy()
    create_screen()

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
        newpro2.geometry("500x325")
        newpro2.iconbitmap("res/icon.ico")

        newpro2_lblfr = tk.LabelFrame(newpro2,text="Project type",bg=bg,fg=fg,padx=150,pady=30)
        newpro2_lblfr.grid(row=0,column=0)

        newpro2_lbl = tk.Label(newpro2_lblfr,text="Project type: ",bg=bg,fg=fg,font="Arial")
        newpro2_lbl.grid(row=0,column=0)

        global newpro2_cb
        newpro2_cb = ttk.Combobox(newpro2_lblfr, values=["Program","Game","Website"])
        newpro2_cb.grid(row=0,column=1)
        newpro2_cb.current(0)

        newpro2_btn = tk.Button(newpro2,text="Create",bg=btn,fg=fg,font="Arial",width=40,height=5,command=newpro_create)
        newpro2_btn.grid(row=1,column=0)

        newpro2_btn2 = tk.Button(newpro2,text="Back",bg=btn,fg=fg,font="Arial",width=40,height=5,command=newpro2_back)
        newpro2_btn2.grid(row=2,column=0)

        newpro2.mainloop()
    else:
        mb.showerror("Error creating project","Woops, you forgot to fill in a project name!")

def newpro_back():
    newpro.destroy()
    home_screen()

def create_screen():
    global proname
    try:
        proname = home_e.get()
    except:
        pass
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
        newpro.geometry("500x400")
        newpro.iconbitmap("res/icon.ico")

        newpro_lblfr = tk.LabelFrame(newpro,text="Settings",bg=bg,fg=fg,padx=75,pady=30)
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

        newpro_btn3 = tk.Button(newpro,text="Back",bg=btn,fg=fg,font="Arial",width=40,height=5,command=newpro_back)
        newpro_btn3.grid(row=2,column=0)

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

def load_back():
    load.destroy()
    home_screen()

def load_screen():
    try:
        home.destroy()
    except:
        pass

    global load
    load = tk.Tk()
    load.title("Load Project")
    load.config(bg=bg)
    load.geometry("365x475")
    load.iconbitmap("res/icon.ico")

    load_lblfr = tk.LabelFrame(load,text="Select project",bg=bg,fg=fg,padx=87,pady=30)
    load_lblfr.grid(row=0,column=0)

    global load_lb
    load_lb = tk.Listbox(load_lblfr,selectmode=tk.SINGLE)
    load_lb.grid(row=0,column=0)
    load_lb.delete(0,tk.END)
    for file in os.listdir("./prd/"):
        load_lb.insert(1,os.path.splitext(str(file))[0])

    load_btn = tk.Button(load,text="Load",bg=btn,fg=fg,font="Arial",width=40,height=5,command=load_load)
    load_btn.grid(row=1,column=0)

    load_btn2 = tk.Button(load,text="Back",bg=btn,fg=fg,font="Arial",width=40,height=5,command=load_back)
    load_btn2.grid(row=2,column=0)

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

    bau_lblfr = tk.LabelFrame(bau,text="Select backup",bg=bg,fg=fg,padx=87,pady=30)
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

    bau_lblfr = tk.LabelFrame(bau,text="Select project",bg=bg,fg=fg,padx=87,pady=30)
    bau_lblfr.grid(row=0,column=0)

    global bau_lb
    bau_lb = tk.Listbox(bau_lblfr,selectmode=tk.SINGLE)
    bau_lb.grid(row=0,column=0)
    bau_lb.delete(0,tk.END)
    for file in os.listdir("./backup/"):
        bau_lb.insert(1,os.path.splitext(str(file))[0])

    bau_btn = tk.Button(bau,text="Load",bg=btn,fg=fg,font="Arial",width=40,height=5,command=sts_loadbackup_do)
    bau_btn.grid(row=2,column=0)

def sts_theme_save():
    global bg
    global btn
    global fg

    sel = sts_cb.get()

    stsf = open("sts.ests","w")

    if sel == "Light":
        stsf.write("#ededed\n#dbdbdb\n#000")
        bg = "#ededed"
        btn = "#dbdbdb"
        fg = "#000"
    elif sel == "Dark":
        stsf.write("#303030\n#505050\n#fff")
        bg = "#303030"
        btn = "#505050"
        fg = "#fff"

    stsf.close()

    sts.destroy()
    home_screen()
    
def sts_back():
    sts.destroy()
    home_screen()

def smp_del():
    ask = mb.askquestion("Watch out!","Are you sure you want to delete '" + get_lb(smp_lb) + "'?")
    if ask == 'yes':
        with open("./prd/" + get_lb(smp_lb) + ".eprd","r") as data:
            lines = data.readlines()
        try:
            shutil.rmtree(lines[1].replace("\n","") + "/" + get_lb(smp_lb))
        except Exception as e:
            mb.showerror("Error",e)
        try:
            os.remove("./prd/" + get_lb(smp_lb) + ".eprd")
        except Exception as e:
            mb.showerror("Error",e)
    else:
        pass

def sts_manpro():
    global smp
    smp = tk.Tk()
    smp.title("Manage Projects")
    smp.config(bg=bg)
    smp.geometry("365x350")
    smp.iconbitmap("res/icon.ico")

    smp_lblfr = tk.LabelFrame(smp,text="Select project",bg=bg,fg=fg,padx=87,pady=30)
    smp_lblfr.grid(row=0,column=0)

    global smp_lb
    smp_lb = tk.Listbox(smp_lblfr,selectmode=tk.SINGLE)
    smp_lb.grid(row=0,column=0)
    smp_lb.delete(0,tk.END)
    for file in os.listdir("./prd/"):
        smp_lb.insert(1,os.path.splitext(str(file))[0])

    smp_btn = tk.Button(smp,text="Delete",bg=btn,fg=fg,font="Arial",width=40,height=5,command=smp_del)
    smp_btn.grid(row=2,column=0)

    smp.mainloop()

def settings():
    try:
        home.destroy()
    except:
        pass

    global sts
    sts = tk.Tk()
    sts.title("Preferences")
    sts.config(bg=bg)
    sts.geometry("675x525")
    sts.iconbitmap("res/icon.ico")

    sts_lblfr = tk.LabelFrame(sts,text="Backups",bg=bg,fg=fg,padx=263,pady=30)
    sts_lblfr.grid(row=0,column=0)

    sts_lbl = tk.Label(sts_lblfr,text="Backup project: ",bg=bg,fg=fg,font="Arial")
    sts_lbl.grid(row=0,column=0)

    sts_btn = tk.Button(sts_lblfr,text="Select project",bg=btn,fg=fg,font="Arial",command=sts_backup)
    sts_btn.grid(row=0,column=1)

    sts_lbl2 = tk.Label(sts_lblfr,text="Load backup: ",bg=bg,fg=fg,font="Arial")
    sts_lbl2.grid(row=1,column=0)

    sts_btn2 = tk.Button(sts_lblfr,text="Select project",bg=btn,fg=fg,font="Arial",command=sts_loadbackup)
    sts_btn2.grid(row=1,column=1)

    sts_lblfr2 = tk.LabelFrame(sts,text="Theming",bg=bg,fg=fg,padx=250,pady=30)
    sts_lblfr2.grid(row=1,column=0)

    sts_lbl3 = tk.Label(sts_lblfr2,text="Theme preset: ",bg=bg,fg=fg,font="Arial")
    sts_lbl3.grid(row=0,column=0)

    global sts_cb
    sts_cb = ttk.Combobox(sts_lblfr2, values=["Light","Dark"])
    sts_cb.grid(row=0,column=1)
    sts_cb.current(0)

    sts_lblfr3 = tk.LabelFrame(sts,text="Manage projects",bg=bg,fg=fg,padx=330,pady=30)
    sts_lblfr3.grid(row=2,column=0)

    sts_btn3 = tk.Button(sts_lblfr3,text="Manage projects",bg=btn,fg=fg,command=sts_manpro)
    sts_btn3.grid(row=0,column=0)

    sts_btn4 = tk.Button(sts_lblfr2,text="Save",bg=btn,fg=fg,font="Arial",command=sts_theme_save)
    sts_btn4.grid(row=2,column=0)

    sts_btn5 = tk.Button(sts,text="Back",bg=btn,fg=fg,font="Arial",width=40,height=5,command=sts_back)
    sts_btn5.grid(row=3,column=0)

    sts.mainloop()

def home_screen():
    global home
    home = tk.Tk()
    home.title("Everyone IDE")
    home.config(bg=bg)
    home.geometry("675x500")
    home.iconbitmap("res/icon.ico")

    home_title = tk.Label(home,text="Everyone IDE",bg=bg,fg=fg,font="Arial 57 bold")
    home_title.grid(row=0,column=0)

    home_lblfr = tk.LabelFrame(home,text="Create new project",bg=bg,fg=fg,padx=87,pady=30)
    home_lblfr.grid(row=1,column=0)

    home_lbl = tk.Label(home_lblfr,text="Name (Do not use \, /, :, *, ?, \", <, > or |): ",bg=bg,fg=fg,font="Arial")
    home_lbl.grid(row=1,column=0)

    global home_e
    home_e = tk.Entry(home_lblfr,font="Arial")
    home_e.grid(row=1,column=1)

    home_btn = tk.Button(home_lblfr,text="Create",bg=btn,fg=fg,font="Arial",command=create_screen)
    home_btn.grid(row=1,column=2)

    home_lblfr2 = tk.LabelFrame(home,text="Load project",bg=bg,fg=fg,padx=243,pady=30)
    home_lblfr2.grid(row=2,column=0)

    home_lbl2 = tk.Label(home_lblfr2,text="Load your project here.",bg=bg,fg=fg,font="Arial")
    home_lbl2.grid(row=1,column=0)

    home_btn2 = tk.Button(home_lblfr2,text="Load",bg=btn,fg=fg,font="Arial",command=load_screen)
    home_btn2.grid(row=1,column=1)

    home_lblfr3 = tk.LabelFrame(home,text="Preferences",bg=bg,fg=fg,padx=55,pady=30)
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
    home_screen()
