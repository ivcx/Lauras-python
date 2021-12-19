import random
import tkinter 
def izveido_ausekli(x,y,R,krasa):
    #uzzīmē ausekli ar centru [x,y]
    kanva.create_polygon(
            x+(2*R),y     ,   #x1,y1
            x+(3*R),y+R   ,   #x2,y2
            x+R,y+R       ,   #x3,y3
            x+R,y+(3*R)   ,   #x4,y4
            x,y+(2*R)     ,   #x5,y5
            x-R,y+(3*R)   ,   #x6,y6
            x-R,y+R       ,   #x7,y7
            x-(3*R),y+R   ,   #x8,y8
            x-(2*R),y     ,   #x9,y9
            x-(3*R),y-R   ,   #x10,y10
            x-R,y-R       ,   #x11,y11
            x-R,y-(3*R)   ,   #x12,y12
            x,y-(2*R)     ,   #x13,y13
            x+R,y-(3*R)   ,   #x14,y14
            x+R,y-R       ,   #x15,y15
            x+(3*R),y-R   ,   #x16,y16
            fill=krasa
    )
def sakt():
    kanva.delete("all")
    N =50
    sk =int(N*random.random())
    print("Datora izveletais auseklīšu skaits ir: " + str(sk))
    for i in range (0,sk):
        x=int(600*random.random())
        y=int(600*random.random())
        R=int(N*random.random())
        krasa="#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        print("[",x,",",y,",",R,",",krasa,"]")
        izveido_ausekli(x,y,R,krasa)
#loga izveide
logs = tkinter.Tk()
logs.geometry("650x650")
kanva = tkinter.Canvas(logs, bg="white", height=600, width=600)
kanva.place(x=10 , y=30)
poga_sakt = tkinter.Button(logs, text="Sākt", width=30, command=sakt)
poga_sakt.place(x=10, y =5)

logs.mainloop()