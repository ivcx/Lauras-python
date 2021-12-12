import tkinter 
from tkinter import ttk
from typing import get_args
#=============================================================================================================================#
def notirit():
    kanva.delete("figura")
    kanva.delete("selected")

def get_coordinates(laucina_nosaukums):
# kā globālos mainīgos nosaka lauciņa rindu un kollonu
    global aa
    global rinda
    global kollona
    aa=kanva.coords(laucina_nosaukums)                      
    kollona = aa[2]/60
    rinda = aa[3]/60
    #iekraso izveleto lauciņu
    kanva.delete("selected")
    kanva.create_rectangle(60*(kollona-1),60*(rinda-1),60*kollona,60*rinda, fill="green", width=0, tags="selected")
#=============================================================================================================================#
#figūru zīmēšana
def izveidot_bandinieku():
    try:
        kanva.delete("selected")
        kanva.create_polygon(60*(kollona-1)+25,60*(rinda-1)+20,60*(kollona-1)+18,60*(rinda-1)+45,60*(kollona-1)+25,60*(rinda-1)+45, fill=krasa ,outline=krasa, tag="figura bandinieks")
        kanva.create_polygon(60*(kollona-1)+35,60*(rinda-1)+20,60*(kollona-1)+42,60*(rinda-1)+45,60*(kollona-1)+35,60*(rinda-1)+45, fill=krasa ,outline=krasa, tag="figura bandinieks") 
        kanva.create_rectangle(60*(kollona-1)+25,60*(rinda-1)+20,60*(kollona-1)+35,60*(rinda-1)+45, fill=krasa, outline=krasa, tag="figura bandinieks")
        kanva.create_rectangle(60*(kollona-1)+5,60*(rinda-1)+50,(60*kollona)-5,(60*rinda)-5 , fill=krasa,tag="figura bandinieks")
        kanva.create_rectangle(60*(kollona-1)+10,60*(rinda-1)+45,(60*kollona)-10,(60*rinda)-10, fill=krasa,tag="figura bandinieks")
        kanva.create_line(60*(kollona-1)+25,60*(rinda-1)+20,60*(kollona-1)+18,60*(rinda-1)+45,tag="figura bandinieks")
        kanva.create_line(60*(kollona-1)+35,60*(rinda-1)+20,60*(kollona-1)+42,60*(rinda-1)+45,tag="figura bandinieks")
        kanva.create_oval(60*(kollona-1)+20,60*(rinda-1)+5,(60*kollona)-20,(60*rinda)-35, fill=krasa,tag="figura bandinieks")
    except:
        print("Vispirms izvēlaties lauciņu")

def izveidot_torni():
    try:
        kanva.delete("selected")
        kanva.create_rectangle(60*(kollona-1)+5,60*(rinda-1)+50,(60*kollona)-5,(60*rinda)-5 , fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kollona-1)+10,60*(rinda-1)+45,(60*kollona)-10,(60*rinda)-10, fill=krasa, tag="figura tornis")
        kanva.create_rectangle(60*(kollona-1)+18,60*(rinda-1)+20,60*(kollona)-18,60*(rinda)-15, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kollona-1)+10,60*(rinda-1)+15,60*(kollona)-10,60*(rinda)-40, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kollona-1)+10,60*(rinda-1)+5,60*(kollona-1)+20,60*(rinda-1)+15, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kollona-1)+40,60*(rinda-1)+5,60*(kollona-1)+50,60*(rinda-1)+15, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kollona-1)+25,60*(rinda-1)+5,60*(kollona-1)+35,60*(rinda-1)+15, fill=krasa,tag="figura tornis")
    except:
        print("Vispirms izvēlaties lauciņu")

def izveidot_laidni():
    try:
        kanva.delete("selected")
        kanva.create_arc(60*(kollona-1)+15,60*(rinda-1)+10, (60*kollona)-10, (60*rinda)-15, start=90, extent=180, fill=krasa, tag="figura laidnis")
        kanva.create_arc(60*(kollona-1)+10,60*(rinda-1)+10, (60*kollona)-15, (60*rinda)-15, start=270, extent=180, fill=krasa, tag="figura laidnis" , outline=krasa)
        kanva.create_arc(60*(kollona-1)+10,60*(rinda-1)+10, (60*kollona)-15, (60*rinda)-15, start=270, extent=180, tag="figura laidnis", style="arc")
        kanva.create_arc(60*(kollona-1)+10,60*(rinda-1)+40, (60*kollona)-10, (60*rinda)+5, start=0, extent=180, fill=krasa, tag="figura laidnis")
        kanva.create_oval(60*(kollona-1)+26,60*(rinda-1)+5, (60*kollona)-26, (60*rinda)-47,fill=krasa, tag="figura laidnis")
        kanva.create_rectangle(60*(kollona-1)+29,60*(rinda-1)+23, (60*kollona)-29, (60*rinda)-23, fill=preteja_krasa)
        kanva.create_rectangle(60*(kollona-1)+25,60*(rinda-1)+29, (60*kollona)-25, (60*rinda)-29, fill=preteja_krasa)
    except:
        print("Vispirms izvēlaties lauciņu")



#=============================================================================================================================#
logs = tkinter.Tk()
logs.geometry("750x500")
kanva = tkinter.Canvas(logs, bg="white", height=480, width=480)
kanva.place(x=10 , y=10)
global krasa 
krasa = "white"
preteja_krasa = "black"
#=============================================================================================================================#
 #lauciņa izveide
for i in range (1,9):
    for j in range (1,9):
        if(i+j)%2 == 0 :
            kanva.create_rectangle(60*(j-1),60*(i-1),60*j,60*i, fill="#BD875E", width=0, tags=("laucins"+str(i)+str(j)))
        else:
            kanva.create_rectangle(60*(j-1),60*(i-1),60*j,60*i, fill="#F3DAB2", width=0, tags=("laucins"+str(i)+str(j)))
#=============================================================================================================================#
#pogas 
poga_bandinieks = tkinter.Button(logs, text="Bandinieks", width=30, command=izveidot_bandinieku)
poga_bandinieks.place(x=500, y =10)
poga_tornis = tkinter.Button(logs, text="Tornis", width=30, command=izveidot_torni)
poga_tornis.place(x=500, y =40)
poga_zirgs = tkinter.Button(logs, text="Zirgs", width=30)
poga_zirgs.place(x=500, y =70)
poga_laidnis = tkinter.Button(logs, text="Laidnis", width=30, command=izveidot_laidni)
poga_laidnis.place(x=500, y =100)
poga_dama = tkinter.Button(logs, text="Dāma", width=30)
poga_dama.place(x=500, y =130)
poga_karalis = tkinter.Button(logs, text="Karalis", width=30)
poga_karalis.place(x=500, y =160)
poga_notirit = tkinter.Button(logs, text="Notīrīt", width=30, command=notirit)
poga_notirit.place(x=500, y =400)
#=============================================================================================================================#
#Visi lauciņi darbojas kā pogas kuras uzpiežot tiek izsaukta get_coordinates kura nosaka kurā rindā un kollonā atrodas lauciņš
#1rinda
kanva.tag_bind("laucins11","<Button-1>",lambda event: get_coordinates("laucins11"))
kanva.tag_bind("laucins12","<Button-1>",lambda event: get_coordinates("laucins12"))
kanva.tag_bind("laucins13","<Button-1>",lambda event: get_coordinates("laucins13"))
kanva.tag_bind("laucins14","<Button-1>",lambda event: get_coordinates("laucins14"))
kanva.tag_bind("laucins15","<Button-1>",lambda event: get_coordinates("laucins15"))
kanva.tag_bind("laucins16","<Button-1>",lambda event: get_coordinates("laucins16"))
kanva.tag_bind("laucins17","<Button-1>",lambda event: get_coordinates("laucins17"))
kanva.tag_bind("laucins18","<Button-1>",lambda event: get_coordinates("laucins18"))
#2rinda
kanva.tag_bind("laucins21","<Button-1>",lambda event: get_coordinates("laucins21"))
kanva.tag_bind("laucins22","<Button-1>",lambda event: get_coordinates("laucins22"))
kanva.tag_bind("laucins23","<Button-1>",lambda event: get_coordinates("laucins23"))
kanva.tag_bind("laucins24","<Button-1>",lambda event: get_coordinates("laucins24"))
kanva.tag_bind("laucins25","<Button-1>",lambda event: get_coordinates("laucins25"))
kanva.tag_bind("laucins26","<Button-1>",lambda event: get_coordinates("laucins26"))
kanva.tag_bind("laucins27","<Button-1>",lambda event: get_coordinates("laucins27"))
kanva.tag_bind("laucins28","<Button-1>",lambda event: get_coordinates("laucins28"))
#3rinda
kanva.tag_bind("laucins31","<Button-1>",lambda event: get_coordinates("laucins31"))
kanva.tag_bind("laucins32","<Button-1>",lambda event: get_coordinates("laucins32"))
kanva.tag_bind("laucins33","<Button-1>",lambda event: get_coordinates("laucins33"))
kanva.tag_bind("laucins34","<Button-1>",lambda event: get_coordinates("laucins34"))
kanva.tag_bind("laucins35","<Button-1>",lambda event: get_coordinates("laucins35"))
kanva.tag_bind("laucins36","<Button-1>",lambda event: get_coordinates("laucins36"))
kanva.tag_bind("laucins37","<Button-1>",lambda event: get_coordinates("laucins37"))
kanva.tag_bind("laucins38","<Button-1>",lambda event: get_coordinates("laucins38"))
#4rinda
kanva.tag_bind("laucins41","<Button-1>",lambda event: get_coordinates("laucins41"))
kanva.tag_bind("laucins42","<Button-1>",lambda event: get_coordinates("laucins42"))
kanva.tag_bind("laucins43","<Button-1>",lambda event: get_coordinates("laucins43"))
kanva.tag_bind("laucins44","<Button-1>",lambda event: get_coordinates("laucins44"))
kanva.tag_bind("laucins45","<Button-1>",lambda event: get_coordinates("laucins45"))
kanva.tag_bind("laucins46","<Button-1>",lambda event: get_coordinates("laucins46"))
kanva.tag_bind("laucins47","<Button-1>",lambda event: get_coordinates("laucins47"))
kanva.tag_bind("laucins48","<Button-1>",lambda event: get_coordinates("laucins48"))
#5rinda
kanva.tag_bind("laucins51","<Button-1>",lambda event: get_coordinates("laucins51"))
kanva.tag_bind("laucins52","<Button-1>",lambda event: get_coordinates("laucins52"))
kanva.tag_bind("laucins53","<Button-1>",lambda event: get_coordinates("laucins53"))
kanva.tag_bind("laucins54","<Button-1>",lambda event: get_coordinates("laucins54"))
kanva.tag_bind("laucins55","<Button-1>",lambda event: get_coordinates("laucins55"))
kanva.tag_bind("laucins56","<Button-1>",lambda event: get_coordinates("laucins56"))
kanva.tag_bind("laucins57","<Button-1>",lambda event: get_coordinates("laucins57"))
kanva.tag_bind("laucins58","<Button-1>",lambda event: get_coordinates("laucins58"))
#6rinda
kanva.tag_bind("laucins61","<Button-1>",lambda event: get_coordinates("laucins61"))
kanva.tag_bind("laucins62","<Button-1>",lambda event: get_coordinates("laucins62"))
kanva.tag_bind("laucins63","<Button-1>",lambda event: get_coordinates("laucins63"))
kanva.tag_bind("laucins64","<Button-1>",lambda event: get_coordinates("laucins64"))
kanva.tag_bind("laucins65","<Button-1>",lambda event: get_coordinates("laucins65"))
kanva.tag_bind("laucins66","<Button-1>",lambda event: get_coordinates("laucins66"))
kanva.tag_bind("laucins67","<Button-1>",lambda event: get_coordinates("laucins67"))
kanva.tag_bind("laucins68","<Button-1>",lambda event: get_coordinates("laucins68"))
#7rinda
kanva.tag_bind("laucins71","<Button-1>",lambda event: get_coordinates("laucins71"))
kanva.tag_bind("laucins72","<Button-1>",lambda event: get_coordinates("laucins72"))
kanva.tag_bind("laucins73","<Button-1>",lambda event: get_coordinates("laucins73"))
kanva.tag_bind("laucins74","<Button-1>",lambda event: get_coordinates("laucins74"))
kanva.tag_bind("laucins75","<Button-1>",lambda event: get_coordinates("laucins75"))
kanva.tag_bind("laucins76","<Button-1>",lambda event: get_coordinates("laucins76"))
kanva.tag_bind("laucins77","<Button-1>",lambda event: get_coordinates("laucins77"))
kanva.tag_bind("laucins78","<Button-1>",lambda event: get_coordinates("laucins78"))
#8rinda
kanva.tag_bind("laucins81","<Button-1>",lambda event: get_coordinates("laucins81"))
kanva.tag_bind("laucins82","<Button-1>",lambda event: get_coordinates("laucins82"))
kanva.tag_bind("laucins83","<Button-1>",lambda event: get_coordinates("laucins83"))
kanva.tag_bind("laucins84","<Button-1>",lambda event: get_coordinates("laucins84"))
kanva.tag_bind("laucins85","<Button-1>",lambda event: get_coordinates("laucins85"))
kanva.tag_bind("laucins86","<Button-1>",lambda event: get_coordinates("laucins86"))
kanva.tag_bind("laucins87","<Button-1>",lambda event: get_coordinates("laucins87"))
kanva.tag_bind("laucins88","<Button-1>",lambda event: get_coordinates("laucins88"))

#=============================================================================================================================#

logs.mainloop()