import tkinter 
from tkinter import ttk
from typing import get_args
#y = ax^3 +bx^2 +cx +d 
def uzd2():
    #x un y asis
    kanva.create_line(50,300,550,300, arrow='last')
    kanva.create_line(300,50,300,550,arrow='first')
    kanva.create_text(310,50, text="y")
    kanva.create_text(550,310, text="x")
    for x in range (1,12):
        #līnijas
        kanva.create_line(300+(x*20),297,300+(x*20),303)
        kanva.create_line(300-(x*20),297,300-(x*20),303)
        kanva.create_line(297,300+(x*20),303,300+(x*20))
        kanva.create_line(297,300-(x*20),303,300-(x*20))
        #teksts
        kanva.create_text(300+(x*20),310, text=x)
        kanva.create_text(300-(x*20),290, text=x)
        kanva.create_text(310,300-(x*20), text=x)
        kanva.create_text(290,300+(x*20), text=x)


    #funkcijas zimesana
    a = float(logs_a.get())
    b = float(logs_b.get())
    c = float(logs_c.get())
    d = float(logs_d.get())
    ieprieksejais_x = -12
    ieprieksejais_y = a*(ieprieksejais_x**3)+b*(ieprieksejais_x**2)+c*(ieprieksejais_x)+d
    for x in range (-12000,12000):
        vertiba_x = x/1000
        vertiba_y = a*(vertiba_x**3)+b*(vertiba_x**2)+c*(vertiba_x)+d
        kanva.create_line(300+(vertiba_x*20),300-(vertiba_y*20),300+(ieprieksejais_x*20),300-(ieprieksejais_y*20))
        ieprieksejais_x = vertiba_x
        ieprieksejais_y = vertiba_y
       
logs = tkinter.Tk()
logs.geometry("750x650")
kanva = tkinter.Canvas(logs, bg="white", height=600, width=600)
kanva.place(x=10 , y=50)
 
#pogas 
poga2 = ttk.Button(logs, text="y=", command=uzd2)
poga2.place(x=10, y=10, width=50)
#ievades logi
logs_a = ttk.Entry(logs)
logs_a.place(x=65, y=10, width=30)
logs_b = ttk.Entry(logs)
logs_b.place(x=135, y=10, width=30)
logs_c = ttk.Entry(logs)
logs_c.place(x=205, y=10, width=30)
logs_d = ttk.Entry(logs)
logs_d.place(x=265, y=10, width=30)

teksts_a = ttk.Label(logs, text="x^3 +")
teksts_a.place(x=100, y=10)
teksts_b = ttk.Label(logs, text="x^2 +")
teksts_b.place(x=170, y=10)
teksts_c = ttk.Label(logs, text="x + ")
teksts_c.place(x=240, y=10)


logs.mainloop()