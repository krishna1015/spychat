import time
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:

            break


    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    while True:
        age =int(input("enter the age "))
        if age>18 and age<40:
            break

        else:
            print("invalid")


    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"

    time.sleep(1)
    print("Hello " +(username))



users = {
}


message=input("Are you Mr/Miss  ")
while True:
    if message=="Krishna":
        print("Hello Krishna")
        break

    else:
        print("register your name")
        print(register())
        break



from stegano import lsb
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as mBox
import datetime
import re

root = Tk()
root.geometry("400x400")
root.resizable(0,0)

tabcontrol = ttk.Notebook(root)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)

tabcontrol.add(tab1 , text = "Encoding the image")
tabcontrol.add(tab2 , text = "Decoding the image")
tabcontrol.pack(expand = 1 , fill = "both")


def browse():
    filename = filedialog.askopenfilename()

    if re.search(r'\.png$', filename) or re.search(r'\.jpg$', filename):
        path_entry.config(text='Path to the file: ' + filename)
        path_entry.insert(0, filename)

    else:
        mBox.showinfo("Error","Not accepted file")


def image(path):
    print(path)

def clear(widget):
    widget.delete(0,END)

def hide_msg(path,message):
    hide = lsb.hide(path,message)
    message_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    hide.save('secret_pic'+message_time+'.jpg')
    mBox.showinfo("Saved")



bbtn = Button(tab1,text = "Search Image",fg = 'powder blue',bg = 'red',width = 20,bd = 15,command = lambda: browse())
bbtn.place(relx = 0.25 , rely = 0.02)

path_entry = Entry(tab1, width = 40,borderwidth = 2, relief = "groove",bd = 15)
path_entry.place(relx = 0.15 , rely = 0.2)

reset = Button(tab1,text = "Clear",fg = 'powder blue',bg = 'red',command = lambda: clear(path_entry),bd = 15)
reset.place(relx = 0.0 , rely = 0.85)

sms = StringVar()
message = Label(tab1 , text = "Message",fg = 'powder blue',bg = 'red',font = ("",15)).place(relx = 0.35,rely = 0.35)
msg_entry = Entry(tab1 ,width = 40,borderwidth = 2, relief = "groove",bd = 15 ,textvariable = sms).place(relx = 0.15,rely = 0.45)

enc = Button(tab1,text = "Encode" ,fg = 'powder blue',bg = 'red', bd =15,command = lambda: hide_msg(path_entry.get(),sms.get()))
enc.place(relx = 0.4,rely = 0.85)

upload_btn = Button(tab1 , text = "Upload",fg = 'powder blue',bg = 'red',bd = 15,command = lambda : image(path_entry.get()))
upload_btn.place(relx = 0.8 , rely = 0.85)

                # for decoding #


def browses():
    filename = filedialog.askopenfilename()
    path_entry2.config(text='Path to the file: '+filename )
    path_entry2.insert(0, filename)

def images(path):
    print(path)

def clears(widget):
    widget.delete(0,END)

def enco(path):
    msg = lsb.reveal(path)
    print(msg)
    mBox.showinfo("Decoded")

bbtn2 = Button(tab2,text = "Search Image",fg = 'powder blue',bg = 'red',width = 20,bd = 15,command = lambda: browses())
bbtn2.place(relx = 0.25 , rely = 0.02)

path_entry2 = Entry(tab2, width = 40,borderwidth = 2, relief = "groove",bd = 15)
path_entry2.place(relx = 0.15 , rely = 0.2)

reset2 = Button(tab2,text = "Reset",fg = 'powder blue',bg = 'red',command = lambda: clears(path_entry2),bd = 15)
reset2.place(relx = 0.4 , rely = 0.82)

def show_details():
    toplevel = Toplevel(tab2)
    Label(toplevel,text = sms.get(),font = ("",15)).place(relx = 0.2,rely = 0.3)

msg = Button(tab2 , text = "View Message",fg = 'powder blue',bg = 'red',bd = 15, command = show_details).place(relx = 0.35,rely = 0.38)

root.mainloop()


