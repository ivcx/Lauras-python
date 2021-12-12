import math
import tkinter 
from tkinter import ttk
from typing import get_args
def uzd3():
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
    #r =a*cos(6f)
    a = float(logs_a.get())
    ieprieksejais_x = 0
    ieprieksejais_y = 0
    for f in range (0,360001):
        vertiba_f = f/1000
        vertiba_r = a*(math.cos(vertiba_f*6))
        vertiba_x = math.cos(vertiba_f)*vertiba_r
        vertiba_y = math.sin(vertiba_f)*vertiba_r
        kanva.create_line(300+(ieprieksejais_x*20),300-(ieprieksejais_y*20),300+(vertiba_x*20),300-(vertiba_y*20))
        ieprieksejais_x = vertiba_x
        ieprieksejais_y = vertiba_y

       


    


logs = tkinter.Tk()
logs.geometry("750x700")
kanva = tkinter.Canvas(logs, bg="white", height=600, width=600)
kanva.place(x=10 , y=50)
 
#pogas 
poga2 = ttk.Button(logs, text="r=a*cos(6f)", command=uzd3)
poga2.place(x=10, y=10, width=70)
#ievades logi
logs_a = ttk.Entry(logs)
logs_a.place(x=110, y=10, width=30)

teksts_a = ttk.Label(logs, text="a=")
teksts_a.place(x=85, y=10)



logs.mainloop()