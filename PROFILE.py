from PIL import Image, ImageTk
import tkinter as tk


path = 'background.png'

#master = tk.Tk()
#master.geometry('800x600')

canvas = tk.Canvas( width=800, height=600)
canvas.pack()
i = ImageTk.PhotoImage(Image.open(path).resize((800,600),Image.ANTIALIAS))
background = canvas.create_image(0, 0, anchor=tk.NW, image=i)


#label
top = tk.Label(canvas, text="Choose Your Profile", fg="white")
top.config(font=("sans-serif",44))
canvas.create_window(100,600,window=top)


profiles = ['this','is','a','test']

pixel = tk.PhotoImage(width=1,height=1)
buttons = []
for p in profiles:
    button = tk.Button(text=p)
    button.config(height=100,width=600,image=pixel)
    canvas.create_window(100,150+(len(buttons)*110),anchor=tk.NW,window=button)
    buttons.append(button)
    
tk.mainloop()
