from tkinter import *
import tkinter as tk
import csv



def exists(url,file): #returns true if site exists in csv; returns false in it is new
    exists = False
    with open(file,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            if len(row) != 0:
                if url in row[0]:
                    exists = True
                    break
    return exists



#print(exists('twitter.com','popup.csv'))
#should i run?
    

def pop(url,file):
    clicked = False
    
    root = tk.Tk() #declares window
    
    root.geometry("500x100")
    popup = Frame(root)
    popup.pack_propagate(0)
    
    #popup with everything
    text = Label(root,text="{} was not listed in any list. What would you like to label it?".format(url))
    text.pack(side=tk.TOP)
    
    prod = Button(root,text="Productive",fg='green',command= lambda: add_prod(url,file,clicked,root))
    prod.pack(side=tk.LEFT)

    dist = Button(root,text="Distracting",fg='red',command= lambda: add_dist(url,file,clicked,root))
    dist.pack(side=tk.RIGHT)


    mainloop()


#i'll try with the functions

            
def add_dist(url,file,clicked,root): #adds to file
    dist_opener = open(file,'a')
    x = csv.writer(dist_opener)
    x.writerow([url,'F'])
    clicked = True
    dist_opener.close()
    root.destroy()
    #print('i printed that')

def add_prod(url,file,clicked,root): #adds to file
    prod_opener = open(file,'a')
    x = csv.writer(prod_opener)
    x.writerow([url,'T'])
    clicked = True
    prod_opener.close()
    root.destroy() #im just really tired

#pop("woah.com","popup.csv") #test 
