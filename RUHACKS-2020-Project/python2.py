import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import csv
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=36, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Distraction Blocker", font=controller.title_font, fg='blue')
        label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        button1 = tk.Button(self, text="Make New Profile",padx=100, pady=30,
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Load From Profile",padx=100, pady=30,
                            command=lambda: controller.show_frame("PageTwo"))

        button1.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        button2.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


class PageOne(tk.Frame):

    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.output()
        label = tk.Label(self, text="Create a New Profile", font=controller.title_font)
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def output(self):
        self.name = tk.Label(self, text='Name:')
        self.name.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
        self.e = tk.Entry(self, width=10)
        self.e.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.b = tk.Button(self, text='Submit', command=self.writeToFile)
        self.b.place(relx=0.7,rely=0.4, anchor=tk.CENTER)

    def writeToFile(self):
        with open('profiles.csv', 'a') as f:
            w=csv.writer(f, quoting=csv.QUOTE_ALL)
            w.writerow([self.e.get()])

        #def printtext(e):
        #    string = e.get()
        #    print (string)

        #e = tk.Entry(self)
        #e.pack()
        #e.focus_set()

        #get_text = tk.Button(self, text="Submit",
        #                   command=printtext(e))
        #get_text.pack()
        
        
    
      

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        
        #e.focus_set()

    #def printtext():
    #    global e
    #    string = e.get()
    #    print string

    #b = Button(root,text='okay',command=printtext)
    #b.pack(side='bottom')
    #root.mainloop()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()