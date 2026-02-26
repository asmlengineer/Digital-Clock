import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    String = strftime('%H:%M:%S %p\n %D')
    label.config(text = String)
    label.after(1000,time)
    
label = tk.Label(root, font = ('calibiri', 50, 'bold'),background = 'yellow',foreground='black')
label.pack(anchor = 'center')

time() 

root.mainloop()   