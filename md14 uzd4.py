import tkinter 
def koordinatu_ass():
    kanva.create_line(300,500,300,100,arrow='last')
    kanva.create_line(100,300,500,300,arrow='last')
    for i in range (125,500,25):
        kanva.create_line(300-5,i,300+5,i)
        kanva.create_line(i,300+5,i,300-5)
def f_zimesana():
    try:
        kanva.delete("Line")
        a=float(logs_a.get())
        b=float(logs_b.get())
        c=float(logs_c.get())
        d=float(logs_d.get())
        e=float(logs_e.get())
        koordinatu_ass()
        ieprieksejais_x = 300-(13*25)
        ieprieksejais_y = (a*((-13)**4) + b*((-13)**3) + c*((-13)**2) + d*(-13) +e )*25 +300
        for i in range (-13000,13000):
            x=i/1000
            koord_x = 300+(x*25)
            y = a*(x**4) + b*(x**3) + c*(x**2) + d*x +e
            koord_y = 300+(y*25)
            kanva.create_line(ieprieksejais_x,ieprieksejais_y,koord_x,koord_y, tag="Line")
            ieprieksejais_x = koord_x
            ieprieksejais_y = koord_y
    except:
        print("Ievadiet visas vērtības")
#loga izveide
logs = tkinter.Tk()
logs.geometry("650x650")
kanva = tkinter.Canvas(logs, bg="white", height=600, width=600)
kanva.place(x=10 , y=30)
#teksta un ievades logu izveide
label_x4 = tkinter.Label(text="*(x^4) +")
label_x3 = tkinter.Label(text="*(x^3) +")
label_x2 = tkinter.Label(text="*(x^2) +")
label_x1 = tkinter.Label(text="*(x) +")
label_x4.place(x=30, y=10)
label_x3.place(x=100, y=10)
label_x2.place(x=170, y=10)
label_x1.place(x=240, y=10)
logs_a = tkinter.Entry(width = 3)
logs_b = tkinter.Entry(width = 3)
logs_c = tkinter.Entry(width = 3)
logs_d = tkinter.Entry(width = 3)
logs_e = tkinter.Entry(width = 3)
logs_a.place(x=5, y=10)
logs_b.place(x=80, y=10)
logs_c.place(x=150, y=10)
logs_d.place(x=220, y=10)
logs_e.place(x=280, y=10)
poga_sakt = tkinter.Button(text="=y", command=f_zimesana)
poga_sakt.place(x=320, y=5)
logs.mainloop()