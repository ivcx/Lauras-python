import tkinter 
from tkinter import ttk
#=============================================================================================================================#
def notirit():
    kanva.delete("figura")

def nosauksana(kaulina_nosaukums):
    global figura 
    figura = kaulina_nosaukums


def get_coordinates(laucina_nosaukums):
# kā globālos mainīgos nosaka lauciņa rindu un kollonu
    try:
        global rinda
        global kollona
        aa=kanva.coords(laucina_nosaukums)                      
        kollona = aa[2]/60
        rinda = aa[3]/60
        match figura:
            case "bandinieks":
                izveidot_bandinieku()
            case "tornis":
                izveidot_torni()
            case "laidnis":
                izveidot_laidni()            
            case "dama":
                izveidot_damu() 
            case "karalis":
                izveidot_karali()
            case "zirgs":
                izveidot_zirgu()
    except:
        print("Izvēlaties figūru")
    

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
        kanva.create_arc(60*(kollona-1)+15,60*(rinda-1)+10, (60*kollona)-10, (60*rinda)-15, start=90, extent=180, fill=krasa, tag="figura laidnis")
        kanva.create_arc(60*(kollona-1)+10,60*(rinda-1)+10, (60*kollona)-15, (60*rinda)-15, start=270, extent=180, fill=krasa, tag="figura laidnis" , outline=krasa)
        kanva.create_arc(60*(kollona-1)+10,60*(rinda-1)+10, (60*kollona)-15, (60*rinda)-15, start=270, extent=180, tag="figura laidnis", style="arc")
        kanva.create_arc(60*(kollona-1)+10,60*(rinda-1)+40, (60*kollona)-10, (60*rinda)+5, start=0, extent=180, fill=krasa, tag="figura laidnis")
        kanva.create_oval(60*(kollona-1)+26,60*(rinda-1)+5, (60*kollona)-26, (60*rinda)-47,fill=krasa, tag="figura laidnis")
        kanva.create_rectangle(60*(kollona-1)+29,60*(rinda-1)+23, (60*kollona)-29, (60*rinda)-23, fill=preteja_krasa, tag="figura laidnis")
        kanva.create_rectangle(60*(kollona-1)+25,60*(rinda-1)+29, (60*kollona)-25, (60*rinda)-29, fill=preteja_krasa, tag="figura laidnis")
    except:
        print("Vispirms izvēlaties lauciņu")

def izveidot_damu():
    try:
        kanva.create_rectangle(60*(kollona-1)+5,60*(rinda-1)+50, (60*kollona)-5, (60*rinda)-5, fill=krasa, tag="figura dama")
        kanva.create_polygon((60*(kollona-1)+10,60*(rinda-1)+50,
                            (60*kollona)-10, (60*rinda)-10,
                            60*(kollona)-5, 60*(rinda-1)+20,
                            60*(kollona)-20, 60*(rinda-1)+35,
                            60*(kollona-1)+30, 60*(rinda-1)+10,
                            60*(kollona-1)+20, 60*(rinda-1)+35,
                            60*(kollona-1)+5, 60*(rinda-1)+20,
                             ),fill=krasa, outline="black", tag="figura dama")
        kanva.create_oval(60*(kollona-1)+25, 60*(rinda-1)+5,60*(kollona-1)+35, 60*(rinda-1)+15, fill=krasa, tag="figura dama")
        kanva.create_oval(60*(kollona-1)+50, 60*(rinda-1)+15,60*(kollona-1)+59, 60*(rinda-1)+25, fill=krasa, tag="figura dama")
        kanva.create_oval(60*(kollona-1)+1, 60*(rinda-1)+15,60*(kollona-1)+10, 60*(rinda-1)+25, fill=krasa, tag="figura dama")
    except:
        print("Vispirms izvēlaties lauciņu")

def izveidot_karali():
    try:
        kanva.create_oval(60*(kollona-1)+25,60*(rinda-1)+10,(60*kollona)-25,(60*rinda)-20,fill=krasa, tag="figura karalis")
        kanva.create_arc(60*(kollona-1)+30,60*(rinda-1)+20,(60*kollona),(60*rinda), style="chord", start=50, extent=130, fill=krasa, tag="figura karalis" , outline=krasa) 
        kanva.create_arc(60*(kollona-1),60*(rinda-1),(60*kollona)-6,(60*rinda)-8, style="chord", start=240, extent=120, fill=krasa, tag="figura karalis", outline=krasa ) 
        kanva.create_arc(60*(kollona-1)+30,60*(rinda-1)+20,(60*kollona),(60*rinda), style="arc", start=50, extent=130, tag="figura karalis" ) 
        kanva.create_arc(60*(kollona-1),60*(rinda-1),(60*kollona)-6,(60*rinda)-8, style="arc", start=240, extent=120, tag="figura karalis") 
        kanva.create_arc(60*(kollona-1),60*(rinda-1)+20,(60*kollona)-30,(60*rinda), style="chord", start=0, extent=130, fill=krasa, tag="figura karalis" ,outline=krasa) 
        kanva.create_arc(60*(kollona-1)+5,60*(rinda-1),(60*kollona)-6,(60*rinda)-8, style="chord", start=180, extent=120, fill=krasa, tag="figura karalis",outline=krasa)
        kanva.create_arc(60*(kollona-1),60*(rinda-1)+20,(60*kollona)-30,(60*rinda), style="arc", start=0, extent=130,  tag="figura karalis") 
        kanva.create_arc(60*(kollona-1)+5,60*(rinda-1),(60*kollona)-6,(60*rinda)-8, style="arc", start=180, extent=120,  tag="figura karalis") 
        kanva.create_rectangle(60*(kollona-1)+15,60*(rinda-1)+50, (60*kollona)-15, (60*rinda)-5, fill=krasa, tag="figura karalis")
        kanva.create_rectangle(60*(kollona-1)+10,60*(rinda-1)+40, (60*kollona)-10, (60*rinda)-10, fill=krasa, tag="figura karalis") 
    except:
        print("Vispirms izvēlaties lauciņu")

def izveidot_zirgu():
    try:
        kanva.create_arc(60*(kollona-1)+15,60*(rinda-1)+5, (60*kollona)-5, (60*rinda)+35,style="pieslice", fill=krasa, tag="figura zirgs", outline=krasa)
        kanva.create_arc(60*(kollona-1)+15,60*(rinda-1)+5, (60*kollona)-5, (60*rinda)+35,style="arc", tag="figura zirgs")
        kanva.create_arc(60*(kollona-1)+20,60*(rinda-1)+25, (60*kollona)-5, (60*rinda)+15,style="pieslice", start=90, extent=90, fill=krasa, tag="figura zirgs", outline=krasa)
        kanva.create_arc(60*(kollona-1)+20,60*(rinda-1)+25, (60*kollona)-5, (60*rinda)+15,style="arc", start=90, extent=90, tag="figura zirgs")
        kanva.create_arc(60*(kollona-1)+5,60*(rinda-1)+5, (60*kollona)+10, (60*rinda)+20,style="chord", start=90, extent=60, fill=krasa, tag="figura zirgs", outline=krasa)
        kanva.create_arc(60*(kollona-1)+5,60*(rinda-1)+5, (60*kollona)+10, (60*rinda)+20,style="arc", start=90, extent=60, tag="figura zirgs")
        kanva.create_polygon(
                        60*(kollona-1)+40,60*(rinda-1)+5,
                        60*(kollona-1)+40,60*(rinda-1)+25,
                        60*(kollona-1)+10,60*(rinda-1)+30,
                        60*(kollona-1)+10,60*(rinda-1)+24,
                        fill=krasa, outline=krasa ,tag="figura zirgs"
        )
        kanva.create_arc(60*(kollona-1)+5,60*(rinda-1)+23,60*(kollona-1)+15,60*(rinda-1)+35,style="pieslice", fill=krasa, tag="figura zirgs", outline=krasa)

        kanva.create_rectangle(60*(kollona-1)+15,60*(rinda-1)+50, (60*kollona)-5, (60*rinda)-5, fill=krasa, tag="figura zirgs")
        
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
poga_bandinieks = tkinter.Button(logs, text="Bandinieks", width=30, command=lambda : nosauksana("bandinieks"))
poga_bandinieks.place(x=500, y =10)
poga_tornis = tkinter.Button(logs, text="Tornis", width=30, command=lambda : nosauksana("tornis"))
poga_tornis.place(x=500, y =40)
poga_zirgs = tkinter.Button(logs, text="Zirgs", width=30, command=lambda : nosauksana("zirgs"))
poga_zirgs.place(x=500, y =70)
poga_laidnis = tkinter.Button(logs, text="Laidnis", width=30, command=lambda : nosauksana("laidnis"))
poga_laidnis.place(x=500, y =100)
poga_dama = tkinter.Button(logs, text="Dāma", width=30, command=lambda : nosauksana("dama"))
poga_dama.place(x=500, y =130)
poga_karalis = tkinter.Button(logs, text="Karalis", width=30, command=lambda : nosauksana("karalis"))
poga_karalis.place(x=500, y =160)
poga_notirit = tkinter.Button(logs, text="Notīrīt", width=30, command=notirit)
poga_notirit.place(x=500, y =400)
#=============================================================================================================================#
#Visi lauciņi darbojas kā pogas kuras uzpiežot tiek izsaukta get_coordinates kura nosaka kurā rindā un kollonā atrodas lauciņš

def tagi(x,y):
     kanva.tag_bind("laucins"+str(x)+str(y),"<Button-1>",lambda event: get_coordinates("laucins"+str(x)+str(y)))

for i in range (1,9):
        for j in range (1,9):
            x=i
            y=j
            tagi(x,y)


#=============================================================================================================================#

logs.mainloop()