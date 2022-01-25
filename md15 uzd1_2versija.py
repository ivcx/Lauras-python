import tkinter
from tkinter import *
import math 
logs = tkinter.Tk()
logs.geometry("750x500")

def parbaude(x):
    #iekraso lauciņu ja nav float vērtība. mainīgie start ir kontrole tam vai apreiķināšanu var sākt vai nē. 
    global start1
    global start2
    global start3
    global start4
    global start5
    global start6
    global start7
    global start8
    global start9
    a1 = logs_1.get()
    a2 = logs_2.get()
    a3 = logs_3.get()
    a4 = logs_4.get()
    a5 = logs_5.get()
    a6 = logs_6.get()
    a7 = logs_7.get()
    a8 = logs_8.get()
    a9 = logs_9.get()
    try:
        float(a1)
    except:
        if len(a1)!=0:
            logs_1.configure(bg="red")
        start1 = False
    else:
        logs_1.configure(bg="white")
        start1 = True
    try:
        float(a2)
    except:
        if len(a2)!=0:
            logs_2.configure(bg="red")
        start2 = False
    else:
        logs_2.configure(bg="white")
        start2 = True
    try:
        float(a3)
    except:
        if len(a4)!=0:
            logs_3.configure(bg="red")
        start3 = False
    else:
        logs_3.configure(bg="white")
        start3 = True
    try:
        float(a4)
    except:
        if len(a4)!=0:
            logs_4.configure(bg="red")
        start4 = False
    else:
        logs_4.configure(bg="white")
        start4 = True
    try:
        float(a5)
    except:
        if len(a5)!=0:
            logs_5.configure(bg="red")
        start5 = False
    else:
        logs_5.configure(bg="white")
        start5 = True
    try:
        float(a6)
    except:
        if len(a6)!=0:
            logs_6.configure(bg="red")
        start6 = False
    else:
        logs_6.configure(bg="white")
        start6 = True

    try:
        float(a7)
    except:
        if len(a7)!=0:
            logs_7.configure(bg="red")
        start7 = False
    else:
        logs_7.configure(bg="white")
        start7 = True

    try:
        float(a8)
    except:
        if len(a8)!=0:
            logs_8.configure(bg="red")
        start8 = False
    else:
        logs_8.configure(bg="white")
        start8 = True

    try:
        float(a9)
    except:
        if len(a9)!=0:
            logs_9.configure(bg="red")
        start9 = False
    else:
        logs_9.configure(bg="white")
        start9 = True

def malas(x1,y1,x2,y2):
    #apreiķina malas garumu
    return  math.sqrt((x2-x1)**2+(y2-y1)**2)
    

def koordinatas(a1,b1,c1,a2,b2,c2):
    #izmantojam krāmera formulas lai iegūtu taišņu krustpunktu
    try:
        x0 = (b2*(-c1) - b1*(-c2))/(a1*b2-a2*b1)
        y0 = ((-c2)*a1 - (-c1)*a2)/(a1*b2-a2*b1)
    except:
        print("Neizveidojas trijstūris")
        # ja sistēmas determinants ir 0 tad taisnes ir paralelas vai sakrīt
    else:
        return x0,y0

def laukums():
    ab = koordinatas(float(logs_1.get()), float(logs_2.get()) , float(logs_3.get()), float(logs_4.get()) , float(logs_5.get()), float(logs_6.get()))
    x1 = ab[0] 
    y1 = ab[1]
    ab = koordinatas (float(logs_4.get()), float(logs_5.get()) , float(logs_6.get()), float(logs_7.get()) , float(logs_8.get()), float(logs_9.get()))
    x2 = ab[0]
    y2 = ab[1]
    ab = koordinatas (float(logs_1.get()), float(logs_2.get()) , float(logs_3.get()), float(logs_7.get()) , float(logs_8.get()), float(logs_9.get()))
    x3 = ab[0]
    y3 = ab[1]
    # no skaitļu korteža ab[x0,y0] dabūnam ārā vērtības lai varētu ar tām strdāt
    garums1 = malas(x1,y1,x2,y2)
    garums2 = malas(x2,y2,x3,y3)
    garums3 = malas(x1,y1,x3,y3)
    Per = garums1+garums2+garums3 #perimetrs
    Per = Per/2 #pusperimetrs
    S = math.sqrt(Per*(Per-garums1)*(Per-garums2)*(Per-garums3)) # laukums
    S = round(S,13)
    return S

def starts():
    if start1 == True and start2 == True and start3 == True and start4 == True and start5 == True and start6 == True and start7 == True and start8 == True and start9 == True:
        label_kluda.configure({"text":" "})
        try:
            print("Taisnes veido trijstūri, šī trijstūra laukums ir: " + str(laukums()))
            label_kluda.configure({"text":"Taisnes veido trijstūri, šī trijstūra laukums ir: " + str(laukums())})
        except:
            pass
    else:
        label_kluda.configure({"text":"Ievades kļūda lūdzu ievadiet reālus skaitļus"})

#parbaude
start1 = True
start2 = True
start3 = True
start4 = True
start5 = True
start6 = True
start7 = True
start8 = True
start9 = True

#logu izveide
iekava = tkinter.Label(text="{", font=("Arial", 55))
label_kluda = tkinter.Label(text="" )
iekava.place(x=1, y=1)
label_kluda.place(x=320, y=30)
label_13 = tkinter.Label(text="*x+")
label_y12 = tkinter.Label(text="*y+")
label_x11 = tkinter.Label(text="= 0")
label_23 = tkinter.Label(text="*x+")
label_y22 = tkinter.Label(text="*y+")
label_x21 = tkinter.Label(text="= 0")
label_33 = tkinter.Label(text="*x+")
label_y32 = tkinter.Label(text="*y+")
label_x31 = tkinter.Label(text="= 0")
label_13.place(x=50, y=20)
label_y12.place(x=120, y=20)
label_x11.place(x=190, y=20)
label_23.place(x=50, y=40)
label_y22.place(x=120, y=40)
label_x21.place(x=190, y=40)
label_33.place(x=50, y=60)
label_y32.place(x=120, y=60)
label_x31.place(x=190, y=60)
logs_1 = tkinter.Entry(width = 3)
logs_2 = tkinter.Entry(width = 3)
logs_3 = tkinter.Entry(width = 3)
logs_4 = tkinter.Entry(width = 3)
logs_5 = tkinter.Entry(width = 3)
logs_6 = tkinter.Entry(width = 3)
logs_7 = tkinter.Entry(width = 3)
logs_8 = tkinter.Entry(width = 3)
logs_9 = tkinter.Entry(width = 3)
logs_1.place(x=30, y=20)
logs_2.place(x=90, y=20)
logs_3.place(x=160, y=20)
logs_4.place(x=30, y=40)
logs_5.place(x=90, y=40)
logs_6.place(x=160, y=40)
logs_7.place(x=30, y=60)
logs_8.place(x=90, y=60)
logs_9.place(x=160, y=60)
poga_sakt = tkinter.Button(text="apriķināt", command=starts)
poga_sakt.place(x=320, y=5)
#Entry piesaistīšana funkcijai parbaude
logs_1.bind("<KeyRelease>", parbaude)
logs_2.bind("<KeyRelease>", parbaude)
logs_3.bind("<KeyRelease>", parbaude)
logs_4.bind("<KeyRelease>", parbaude)
logs_5.bind("<KeyRelease>", parbaude)
logs_6.bind("<KeyRelease>", parbaude) 
logs_7.bind("<KeyRelease>", parbaude)
logs_8.bind("<KeyRelease>", parbaude) 
logs_9.bind("<KeyRelease>", parbaude) 

logs.mainloop()