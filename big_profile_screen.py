from tkinter import *
import tkinter as tk


master = Tk()
master.title("Choose Your Profile")
master.geometry('800x600')
b_im = tk.PhotoImage()


#frame
mainframe = tk.Frame(master)
mainframe.pack_propagate(0)

#title
top = Label(master, text="Choose Your Profile", fg="blue")
top.config(font=("sans-serif",44))
top.pack()


#button/profile
profiles = ['this','is','a','test']

pixel = tk.PhotoImage(width=1,height=1)
buttons = []
for p in profiles:
    button = Button(master,text=p)
    button.config(height=100,width=600,image=pixel)
    button.pack(pady=10)
    buttons.append(button)


mainloop()
