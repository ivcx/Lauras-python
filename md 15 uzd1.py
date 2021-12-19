import tkinter
def parbaude1(self):
    parbaudamais = self.get()
    try:
        parbaudamais = float(parbaudamais)
    except:
        self.configure({"background": "red"})
    else:
        self.configure({"background": "white"})





logs = tkinter.Tk()
logs.geometry("750x500")

#logu izveide
iekava = tkinter.Label(text="{", font=("Arial", 55))
iekava.place(x=1, y=1)
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
logs_a1 = tkinter.Entry(width = 3)
logs_b1 = tkinter.Entry(width = 3)
logs_c1 = tkinter.Entry(width = 3)
logs_a2 = tkinter.Entry(width = 3)
logs_b2 = tkinter.Entry(width = 3)
logs_c2 = tkinter.Entry(width = 3)
logs_a3 = tkinter.Entry(width = 3)
logs_b3 = tkinter.Entry(width = 3)
logs_c3 = tkinter.Entry(width = 3)
logs_a1.place(x=30, y=20)
logs_b1.place(x=90, y=20)
logs_c1.place(x=160, y=20)
logs_a2.place(x=30, y=40)
logs_b2.place(x=90, y=40)
logs_c2.place(x=160, y=40)
logs_a3.place(x=30, y=60)
logs_b3.place(x=90, y=60)
logs_c3.place(x=160, y=60)
poga_sakt = tkinter.Button(text="apriķināt")
poga_sakt.place(x=320, y=5)
# datu ievades kontrole
parbaude1(logs_b1)

logs.mainloop()