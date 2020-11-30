from tkinter import *  # imported everything from tkinter
from tkinter.ttk import * # Imported everything


from time import strftime  # imported module to get system time


# creating tkinter window
root = Tk()
root.title('Life Clock')



# displaying time on label
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 

  
lbl = Label(root, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'green') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
time() 
  
mainloop() 
