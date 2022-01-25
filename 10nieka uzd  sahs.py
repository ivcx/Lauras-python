import tkinter
from tkinter import *
import math
import time

logs = tkinter.Tk()
logs.geometry("750x500")
kanva = tkinter.Canvas(logs, bg="white", height=480, width=480)
kanva.place(x=10 , y=10)
krasa = "white"

def notirit():
    #notīra figūras no laukuma
    kanva.delete("figura")
    kanva.delete("green")

def nosauksana(x):
    #nosauc globālo mainīgo, kurš pēctam tiek izmantots zīmējot figūras
    global figura
    figura=x
    
def get_coordinates(laucina_nosaukums):
# kā globālos mainīgos nosaka objekta (lauciņa vai figūras) rindu un kollonu
    global rinda
    global kolonna
    aa=kanva.coords(laucina_nosaukums)                    
    kolonna = math.floor(aa[2]/60)
    rinda = math.floor(aa[3]/60)
    if laucina_nosaukums[0:4] != "move" and laucina_nosaukums !="figura":
        try: 
            #pārbauda, vai ir izvēlēta figūra, kuru novietot uz laukuma
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
        
def kustiba(zala_kvadrata_nosaukums):
    # pakustina figūru no vietas, kur tā sākotnēji tika novietota uz izvēlēto laukumu no figūras iespējamiem gājieniem
    get_coordinates(zala_kvadrata_nosaukums)
    kanva.delete("green")
    starpiba_x = kolonna-x_figura
    starpiba_y = rinda-y_figura
    for i in range(0,60):
        kanva.move("figura", starpiba_x , starpiba_y)
        time.sleep(0.001)
        logs.update()       

def green_bind(zala_kvadrata_nosaukums):
    # pievieno zaļajiem lauciņiem funkciju, lai varētu pārvietot figūru.
    kanva.tag_bind(zala_kvadrata_nosaukums,"<Button-1>",lambda event: kustiba(zala_kvadrata_nosaukums))

def gajienu_paradisana(figuras_nosaukums):
    # izveido zaļos lauciņus, kuri parāda, uz kurieni var paiet izvēlētā figūra.
    global x_figura
    global y_figura
    aa=kanva.coords(figuras_nosaukums)
    x_figura = math.ceil(aa[2]/60)
    y_figura = math.ceil(aa[3]/60)
    match figuras_nosaukums:
            case "bandinieks":
                get_coordinates("figura")
                if rinda == 6:
                    atlautais = 2
                else:
                    atlautais = 1
                for i in range(1,atlautais+1):
                    kanva.create_rectangle(60*(x_figura-1),60*(y_figura-1)-(i*60),60*(x_figura),60*(y_figura)-(i*60), fill="lightgreen", tag="move"+str(i)+" green" )
                    green_bind("move"+str(i))
            case "tornis":
                get_coordinates("figura")
                for i in range (1,9):
                    if kolonna != i-1:
                        kanva.create_rectangle(60*(i-1),60*(y_figura-1),60*i,60*(y_figura), fill="lightgreen", tag="move"+str(i)+str(y_figura)+" green" )
                        green_bind("move"+str(i)+str(y_figura))
                for j in range (1,9):
                    if rinda != j-1:
                        kanva.create_rectangle(60*(x_figura-1),60*(j-1),60*(x_figura),60*j, fill="lightgreen", tag="move"+str(x_figura)+str(j)+" green" )
                        green_bind("move"+str(x_figura)+str(j))                         
            case "laidnis":
                get_coordinates("figura")
                for i in range (1,9):
                    for j in range (1,9):
                        if kolonna-i == rinda-j or kolonna-i == -(rinda-j)-2:
                            if kolonna != i-1 and rinda != j-1:
                              kanva.create_rectangle(60*(i-1),60*(j-1),60*(i),60*j, fill="lightgreen", tag="move"+str(i)+str(j)+" green" )
                              green_bind("move"+str(i)+str(j))
            case "dama":
                get_coordinates("figura")
                for i in range (1,9):
                    for j in range (1,9):
                        if kolonna-i == rinda-j or kolonna-i == -(rinda-j)-2:
                            if kolonna != i-1 and rinda != j-1:
                              kanva.create_rectangle(60*(i-1),60*(j-1),60*(i),60*j, fill="lightgreen", tag="move"+str(i)+str(j)+" green" )
                              green_bind("move"+str(i)+str(j))
                        elif kolonna != i-1:
                            kanva.create_rectangle(60*(i-1),60*(y_figura-1),60*i,60*(y_figura), fill="lightgreen", tag="move"+str(i)+str(j)+" green" )
                            green_bind("move"+str(i)+str(j))
                        elif rinda != j-1:
                            kanva.create_rectangle(60*(x_figura-1),60*(j-1),60*(x_figura),60*j, fill="lightgreen", tag="move"+str(i)+str(j)+" green" )
                            green_bind("move"+str(i)+str(j))
            case "karalis":
                for i in range (-1,2):
                    for j in range (-1,2):
                        if i != 0 or j != 0:
                            kanva.create_rectangle(60*(x_figura-1)-(i*60),60*(y_figura-1)-(j*60),60*(x_figura)-(i*60),60*(y_figura)-(j*60), fill="lightgreen", tag="move"+str(i)+str(j)+" green" )
                            green_bind("move"+str(i)+str(j))
            case "zirgs":
                x_figura = math.ceil(aa[0]/60)
                y_figura = math.ceil(aa[1]/60)
                for i in (-1,1,-2,2):
                    for j in (-1,1,-2,2):
                        if j != i and j != -i  :
                            kanva.create_rectangle(60*(x_figura-1)-(i*60),60*(y_figura-1)-(j*60),60*(x_figura)-(i*60),60*(y_figura)-(j*60), fill="lightgreen", tag="move"+str(i)+str(j)+" green" )
                            green_bind("move"+str(i)+str(j))
    
def figuras_bind(figuras_nosaukums):
    #uzspiežot katru figūru, izpildīsies funkcija gajienu_paradisana
    kanva.tag_bind(figuras_nosaukums,"<Button-1>",lambda event: gajienu_paradisana(figuras_nosaukums))    
        
#Figūru zīmēšana
def izveidot_bandinieku():
    #uzzīmē bandinieku izvēlētajā lauciņā
        kanva.delete("figura")
        kanva.delete("green")
        kanva.create_polygon(60*(kolonna-1)+25,60*(rinda-1)+20,60*(kolonna-1)+18,60*(rinda-1)+45,60*(kolonna-1)+25,60*(rinda-1)+45, fill=krasa ,outline=krasa, tag="figura bandinieks")
        kanva.create_polygon(60*(kolonna-1)+35,60*(rinda-1)+20,60*(kolonna-1)+42,60*(rinda-1)+45,60*(kolonna-1)+35,60*(rinda-1)+45, fill=krasa ,outline=krasa, tag="figura bandinieks") 
        kanva.create_rectangle(60*(kolonna-1)+25,60*(rinda-1)+20,60*(kolonna-1)+35,60*(rinda-1)+45, fill=krasa, outline=krasa, tag="figura bandinieks")
        kanva.create_rectangle(60*(kolonna-1)+5,60*(rinda-1)+50,(60*kolonna)-5,(60*rinda)-5 , fill=krasa,tag="figura bandinieks")
        kanva.create_rectangle(60*(kolonna-1)+10,60*(rinda-1)+45,(60*kolonna)-10,(60*rinda)-10, fill=krasa,tag="figura bandinieks")
        kanva.create_line(60*(kolonna-1)+25,60*(rinda-1)+20,60*(kolonna-1)+18,60*(rinda-1)+45,tag="figura bandinieks")
        kanva.create_line(60*(kolonna-1)+35,60*(rinda-1)+20,60*(kolonna-1)+42,60*(rinda-1)+45,tag="figura bandinieks")
        kanva.create_oval(60*(kolonna-1)+20,60*(rinda-1)+5,(60*kolonna)-20,(60*rinda)-35, fill=krasa,tag="figura bandinieks")
        figuras_bind("bandinieks")

def izveidot_torni():
    #uzzīmē torni izvēlētajā lauciņā
        kanva.delete("figura")
        kanva.delete("green")
        kanva.create_rectangle(60*(kolonna-1)+5,60*(rinda-1)+50,(60*kolonna)-5,(60*rinda)-5 , fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kolonna-1)+10,60*(rinda-1)+45,(60*kolonna)-10,(60*rinda)-10, fill=krasa, tag="figura tornis")
        kanva.create_rectangle(60*(kolonna-1)+18,60*(rinda-1)+20,60*(kolonna)-18,60*(rinda)-15, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kolonna-1)+10,60*(rinda-1)+15,60*(kolonna)-10,60*(rinda)-40, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kolonna-1)+10,60*(rinda-1)+5,60*(kolonna-1)+20,60*(rinda-1)+15, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kolonna-1)+40,60*(rinda-1)+5,60*(kolonna-1)+50,60*(rinda-1)+15, fill=krasa,tag="figura tornis")
        kanva.create_rectangle(60*(kolonna-1)+25,60*(rinda-1)+5,60*(kolonna-1)+35,60*(rinda-1)+15, fill=krasa,tag="figura tornis")
        figuras_bind("tornis")

def izveidot_laidni():
    #uzzīmē laidni izvēlētajā lauciņā
        kanva.delete("figura")
        kanva.delete("green")
        kanva.create_arc(60*(kolonna-1)+15,60*(rinda-1)+10, (60*kolonna)-10, (60*rinda)-15, start=90, extent=180, fill=krasa, tag="figura laidnis")
        kanva.create_arc(60*(kolonna-1)+10,60*(rinda-1)+10, (60*kolonna)-15, (60*rinda)-15, start=270, extent=180, fill=krasa, tag="figura laidnis" , outline=krasa)
        kanva.create_arc(60*(kolonna-1)+10,60*(rinda-1)+10, (60*kolonna)-15, (60*rinda)-15, start=270, extent=180, tag="figura laidnis", style="arc")
        kanva.create_arc(60*(kolonna-1)+10,60*(rinda-1)+40, (60*kolonna)-10, (60*rinda)+5, start=0, extent=180, fill=krasa, tag="figura laidnis")
        kanva.create_oval(60*(kolonna-1)+26,60*(rinda-1)+5, (60*kolonna)-26, (60*rinda)-47,fill=krasa, tag="figura laidnis")
        kanva.create_rectangle(60*(kolonna-1)+29,60*(rinda-1)+23, (60*kolonna)-29, (60*rinda)-23, fill="black", tag="figura laidnis")
        kanva.create_rectangle(60*(kolonna-1)+25,60*(rinda-1)+29, (60*kolonna)-25, (60*rinda)-29, fill="black", tag="figura laidnis")
        figuras_bind("laidnis")

def izveidot_damu():
    #uzzīmē dāmu izvēlētajā lauciņā
        kanva.delete("figura")
        kanva.delete("green")
        kanva.create_rectangle(60*(kolonna-1)+5,60*(rinda-1)+50, (60*kolonna)-5, (60*rinda)-5, fill=krasa, tag="figura dama")
        kanva.create_polygon((60*(kolonna-1)+10,60*(rinda-1)+50,
                            (60*kolonna)-10, (60*rinda)-10,
                            60*(kolonna)-5, 60*(rinda-1)+20,
                            60*(kolonna)-20, 60*(rinda-1)+35,
                            60*(kolonna-1)+30, 60*(rinda-1)+10,
                            60*(kolonna-1)+20, 60*(rinda-1)+35,
                            60*(kolonna-1)+5, 60*(rinda-1)+20,
                             ),fill=krasa, outline="black", tag="figura dama")
        kanva.create_oval(60*(kolonna-1)+25, 60*(rinda-1)+5,60*(kolonna-1)+35, 60*(rinda-1)+15, fill=krasa, tag="figura dama")
        kanva.create_oval(60*(kolonna-1)+50, 60*(rinda-1)+15,60*(kolonna-1)+59, 60*(rinda-1)+25, fill=krasa, tag="figura dama")
        kanva.create_oval(60*(kolonna-1)+1, 60*(rinda-1)+15,60*(kolonna-1)+10, 60*(rinda-1)+25, fill=krasa, tag="figura dama")
        figuras_bind("dama")

def izveidot_karali():
    #uzzīmē karali izvēlētajā lauciņā
        kanva.delete("figura")
        kanva.delete("green")
        kanva.create_oval(60*(kolonna-1)+25,60*(rinda-1)+10,(60*kolonna)-25,(60*rinda)-20,fill=krasa, tag="figura karalis")
        kanva.create_arc(60*(kolonna-1)+30,60*(rinda-1)+20,(60*kolonna),(60*rinda), style="chord", start=50, extent=130, fill=krasa, tag="figura karalis" , outline=krasa) 
        kanva.create_arc(60*(kolonna-1),60*(rinda-1),(60*kolonna)-6,(60*rinda)-8, style="chord", start=240, extent=120, fill=krasa, tag="figura karalis", outline=krasa ) 
        kanva.create_arc(60*(kolonna-1)+30,60*(rinda-1)+20,(60*kolonna),(60*rinda), style="arc", start=50, extent=130, tag="figura karalis" ) 
        kanva.create_arc(60*(kolonna-1),60*(rinda-1),(60*kolonna)-6,(60*rinda)-8, style="arc", start=240, extent=120, tag="figura karalis") 
        kanva.create_arc(60*(kolonna-1),60*(rinda-1)+20,(60*kolonna)-30,(60*rinda), style="chord", start=0, extent=130, fill=krasa, tag="figura karalis" ,outline=krasa) 
        kanva.create_arc(60*(kolonna-1)+5,60*(rinda-1),(60*kolonna)-6,(60*rinda)-8, style="chord", start=180, extent=120, fill=krasa, tag="figura karalis",outline=krasa)
        kanva.create_arc(60*(kolonna-1),60*(rinda-1)+20,(60*kolonna)-30,(60*rinda), style="arc", start=0, extent=130,  tag="figura karalis") 
        kanva.create_arc(60*(kolonna-1)+5,60*(rinda-1),(60*kolonna)-6,(60*rinda)-8, style="arc", start=180, extent=120,  tag="figura karalis") 
        kanva.create_rectangle(60*(kolonna-1)+15,60*(rinda-1)+50, (60*kolonna)-15, (60*rinda)-5, fill=krasa, tag="figura karalis")
        kanva.create_rectangle(60*(kolonna-1)+10,60*(rinda-1)+40, (60*kolonna)-10, (60*rinda)-10, fill=krasa, tag="figura karalis") 
        figuras_bind("karalis")

def izveidot_zirgu():
    #uzzīmē zirgu  izvēlētajā lauciņā
        kanva.delete("figura")
        kanva.delete("green")
        kanva.create_arc(60*(kolonna-1)+15,60*(rinda-1)+5, (60*kolonna)-5, (60*rinda)+35,style="pieslice", fill=krasa, tag="figura zirgs", outline=krasa)
        kanva.create_arc(60*(kolonna-1)+15,60*(rinda-1)+5, (60*kolonna)-5, (60*rinda)+35,style="arc", tag="figura zirgs")
        kanva.create_arc(60*(kolonna-1)+20,60*(rinda-1)+25, (60*kolonna)-5, (60*rinda)+15,style="pieslice", start=90, extent=90, fill=krasa, tag="figura zirgs", outline=krasa)
        kanva.create_arc(60*(kolonna-1)+20,60*(rinda-1)+25, (60*kolonna)-5, (60*rinda)+15,style="arc", start=90, extent=90, tag="figura zirgs")
        kanva.create_arc(60*(kolonna-1)+5,60*(rinda-1)+5, (60*kolonna)+10, (60*rinda)+20,style="chord", start=90, extent=60, fill=krasa, tag="figura zirgs", outline=krasa)
        kanva.create_arc(60*(kolonna-1)+5,60*(rinda-1)+5, (60*kolonna)+10, (60*rinda)+20,style="arc", start=90, extent=60, tag="figura zirgs")
        kanva.create_polygon(
                        60*(kolonna-1)+40,60*(rinda-1)+5,
                        60*(kolonna-1)+40,60*(rinda-1)+25,
                        60*(kolonna-1)+10,60*(rinda-1)+30,
                        60*(kolonna-1)+10,60*(rinda-1)+24,
                        fill=krasa, outline=krasa ,tag="figura zirgs"
        )
        kanva.create_arc(60*(kolonna-1)+5,60*(rinda-1)+23,60*(kolonna-1)+15,60*(rinda-1)+35,style="pieslice", fill=krasa, tag="figura zirgs", outline=krasa)
        kanva.create_line(60*(kolonna-1)+10,60*(rinda-1)+30,60*(kolonna-1)+10,60*(rinda-1)+22,tag="figura zirgs")
        kanva.create_line(60*(kolonna-1)+10,60*(rinda-1)+30,60*(kolonna-1)+40,60*(rinda-1)+25,tag="figura zirgs")
        kanva.create_rectangle(60*(kolonna-1)+15,60*(rinda-1)+50, (60*kolonna)-5, (60*rinda)-5, fill=krasa, tag="figura zirgs")
        figuras_bind("zirgs")

#lauciņa izveide
for i in range (1,9):
    for j in range (1,9):
        if(i+j)%2 == 0 :
            kanva.create_rectangle(60*(j-1),60*(i-1),60*j,60*i, fill="#BD875E", width=0, tags=("laucins"+str(i)+str(j)))
        else:
            kanva.create_rectangle(60*(j-1),60*(i-1),60*j,60*i, fill="#F3DAB2", width=0, tags=("laucins"+str(i)+str(j)))
            
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

#Visi lauciņi darbojas kā pogas, kuras uzpiežot tiek izsaukta funkcija get_coordinates, kura nosaka, kurā rindā un kollonā atrodas lauciņš#
def tagi(x,y):
    #uztaisa tag bind katram lauciņam
    kanva.tag_bind("laucins"+str(x)+str(y),"<Button-1>",lambda event: get_coordinates("laucins"+str(x)+str(y)))

for i in range (1,9):
        for j in range (1,9):
            x=i
            y=j
            tagi(x,y)

logs.mainloop()