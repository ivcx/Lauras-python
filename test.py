import tkinter as tk
from tkinter import *

def parbaude(a):
    a = e1.get()
    print(a)
    try:
      float(a)
    except:
      e1.configure(bg="red")
    else: 
      e1.configure(bg="white")
      print(a)
logs = tk.Tk()
logs.geometry("750x500")
logs.title("Pārbaude")
e1=tk.Entry(logs)
e1.place(x=100,y=150)

e1.bind("<KeyRelease>",parbaude)

logs.mainloop()