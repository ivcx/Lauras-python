import tkinter
from tkinter import *
global start 

def my_callback(var, index, mode):
    for arg in my_var:
        parbaudit = my_var[arg].get()
        try:
            parbaudit = float(parbaudit)
        except:
            if len(parbaudit)>=1:
                globals()["logs_{}".format(arg[6:8])].configure({"background": "red"})
            else:
                globals()["logs_{}".format(arg[6:8])].configure({"background": "white"})
        else:
            globals()["logs_{}".format(arg[6:8])].configure({"background": "white"})

def paral(x1,y1,x2,y2):
    a = True
    if float(x1)*float(y2) == float(x2)*float(y1):
        a = False
    return a 

def starts():
        if True:
            label_kluda.configure({"text":" "})
            a = paral(logs_a1.get() , logs_b1.get() , logs_a2.get() , logs_b2.get())
            b = paral(logs_a2.get() , logs_b2.get() , logs_a3.get() , logs_b3.get())
            c = paral(logs_a3.get() , logs_b3.get() , logs_a1.get() , logs_b1.get())
            if a ==True and b==True and c==True :
                print("Taisnes veido trijstūri, šī trijstūra laukums ir: " + laukums())
            else:
                print("ir paralēlas")
        else:
            label_kluda.configure({"text":"Ievades kļūda lūdzu ievadiet reālus skaitļus"})

logs = tkinter.Tk()
logs.geometry("750x500")
# datu ievades kontrole
start = True
my_var = {}
for i in ("a","b","c"):
    for j in range (1,4):
        my_var["my_var{0}{1}".format(i,j)] = StringVar()
        my_var["my_var{0}{1}".format(i,j)].trace_add('write', my_callback)

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
logs_a1 = tkinter.Entry(width = 3, textvariable = my_var['my_vara1'])
logs_b1 = tkinter.Entry(width = 3, textvariable = my_var['my_varb1'])
logs_c1 = tkinter.Entry(width = 3, textvariable = my_var['my_varc1'])
logs_a2 = tkinter.Entry(width = 3, textvariable = my_var['my_vara2'])
logs_b2 = tkinter.Entry(width = 3, textvariable = my_var['my_varb2'])
logs_c2 = tkinter.Entry(width = 3, textvariable = my_var['my_varc2'])
logs_a3 = tkinter.Entry(width = 3, textvariable = my_var['my_vara3'])
logs_b3 = tkinter.Entry(width = 3, textvariable = my_var['my_varb3'])
logs_c3 = tkinter.Entry(width = 3, textvariable = my_var['my_varc3'])
logs_a1.place(x=30, y=20)
logs_b1.place(x=90, y=20)
logs_c1.place(x=160, y=20)
logs_a2.place(x=30, y=40)
logs_b2.place(x=90, y=40)
logs_c2.place(x=160, y=40)
logs_a3.place(x=30, y=60)
logs_b3.place(x=90, y=60)
logs_c3.place(x=160, y=60)
poga_sakt = tkinter.Button(text="apriķināt", command=starts)
poga_sakt.place(x=320, y=5)

logs.mainloop()