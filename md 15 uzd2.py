import tkinter
from tkinter import *
import time
import random
import math
from threading import Thread

logs= Tk()
logs.title("Ziemassvētki")
logs.geometry("850x550")
pamatne = Canvas(logs,width=800, height=500, bg='#1E6091')
pamatne.pack()
pamatne.place(x=25, y=25)

def izveidot_kocinu(x,y,lielums=35,garums=25, **kwargs):
    #izveido koku, x,y bus kā stumbra koordinātes
     # **kwargs izmanto lai varētu padot tipiskās canvas.create_ parametrus, kā piemēram {fill="white"}
    a = round(lielums/5,3) 
    punkti = [
        x,y,
        x-lielums-5,y,
        x-lielums+a,y-garums,
        x-lielums+a-5,y-garums,
        x-lielums+a*2,y-garums*2,
        x-lielums+(a*2)-5,y-garums*2,
        x-lielums+(a*3),y-garums*3,
        x-lielums+(a*3)-5,y-garums*3,
        x-lielums+(a*4),y-garums*4,
        x-lielums+(a*4)-5,y-garums*4,
        x-2.5,y-garums*5,
        x+lielums-(a*4),y-garums*4,
        x+lielums-(a*4)-5,y-garums*4,
        x+lielums-(a*3),y-garums*3,
        x+lielums-(a*3)-5,y-garums*3,
        x+lielums-(a*2),y-garums*2,
        x+lielums-(a*2)-5,y-garums*2,
        x+lielums-(a),y-garums,
        x+lielums-(a)-5,y-garums,
        x+lielums,y,
    ]
    return pamatne.create_polygon(punkti, **kwargs)

def apalots_trijsturis(x1, y1, x2, y2,x3,y3, radius=5, **kwargs):
    #izveido noapalotu trijsturi
    # **kwargs izmanto lai varētu padot tipiskās canvas.create_ parametrus, kā piemēram {fill="white"}
    punkti = [x1+radius,y1+radius, 
                x1+radius,y1+radius,
                x2-radius,y2-radius,
                x2-radius,y2-radius,
                x2,y2,
                x2-radius,y2,
                x2-radius,y2,
                x3+radius,y3,
                x3+radius,y3,
                x3,y3,
                x3+radius,y3-radius,
                x3+radius,y3-radius,
                x1-radius,y1+radius,
                x1-radius,y1+radius,
                x1,y1
                ]
    return pamatne.create_polygon(punkti, **kwargs, smooth=True) # (smooth = True) noapaļo galus, taču lai to izdarītu koordinātes jāpadod divas reizes 

def izveidot_gaisminas_kokam(x,y,lielums=35,garums=25,):
#izveidojam kokam gaismiņas ar nosaukumu no "spigulis0" lidz "spigulis2"
#funkcijai padod tos pašus parametrus, kādus kokam uz kura tiks izveidoti spīgulīši
    a = round(lielums/5,3)
    tag=1 
    for i in range (int(x-lielums+a),int(x+lielums-a-5),3):  #iet cauri x koordinātām no viena zara uz nākamo
        j = y-(tag**2)*(1/15) -2 #apreiķina y koordinātas izmantojot kvadrātfunkciju. punkti sekos parabolas grafikam 
        pamatne.create_oval(i,j,i+1,j+1, tags="spigulis"+str(tag%3), outline="white")
        tag+=1
    tag=1
    for i in range (int(x-lielums+a),int(x+lielums-(a*2)-5), 3): #nākamie cikli iet cauri augstākiem zariem
        j = y-garums-(tag**2)*(1/10)
        pamatne.create_oval(i,j,i+1,j+1, tags="spigulis"+str(tag%3), outline="white")
        tag+=1
    tag=1
    for i in range (int(x-lielums+a*2),int(x+lielums-(a*3)-5), 3):
        j = y-garums*2-(tag**2)*(1/6)
        pamatne.create_oval(i,j,i+1,j+1, tags="spigulis"+str(tag%3), outline="white")
        tag+=1
    tag=1
    for i in range (int(x-lielums+a*3),int(x+lielums-(a*4)), 3):
        j = y-garums*3-(tag**2)*(1/4)
        pamatne.create_oval(i,j,i+1,j+1, tags="spigulis"+str(tag%3), outline="white")
        tag+=1

def izveidot_jaunu_piku(nosaukums):
    #izveido jaunu piku ar random koordinātēm un specifisku tag
    x1= (800*random.random())
    x2= x1 + (5*random.random())
    y1 = (495*random.random())
    starpiba = abs(x1-x2) # lai izveidotos riņķis nevis ovāls
    pamatne.create_oval(x1,-y1-starpiba,x2,-y1, fill="white", tag=nosaukums, outline="white")

def izvedot_piku():
    #izsauc procedūru un padod viņai kā mainīgos piku nosaukumus no "pika1" lidz "pika200"
    i=0
    while i<200:
        i+=1
        izveidot_jaunu_piku("pika"+str(i))

def kustiba():
    #procedūra atbild par visiem elementiem kuri kustās
    try:
        while True :
            #pikas
            for i in range (70): # 3 dažādi cikli kas katrs atbild par pikām ar nosaukumu "pika{i}", rzultātā var uztaisit ka pikas krit ar savādāku ātrumu
                pamatne.move("pika"+str(i), 0 ,2)
                aa=pamatne.coords("pika"+str(i)) # nosaka pikas koordinātes, mainigais aa ir skaitļu saraksts [x1,y1,x2,y2]
                try: 
                    if aa[3]>= 500:
                        pamatne.delete("pika"+str(i)) # izdzēš pikas kuras nokritušas parak talu lai butu redzamas
                except:
                    izveidot_jaunu_piku("pika"+str(i)) #ja pika ar tadu nosaukumu ir beigusi eksistet tad ta tiek izveidota jaunās koordinatās 
            for i in range (70,140):
                pamatne.move("pika"+str(i), 0 ,1)
                aa=pamatne.coords("pika"+str(i))
                try: 
                    if aa[3]>= 500:
                        pamatne.delete("pika"+str(i))
                except:
                    izveidot_jaunu_piku("pika"+str(i)) 
            for i in range (140,200):
                pamatne.move("pika"+str(i), 0 ,1.5)
                aa=pamatne.coords("pika"+str(i))
                try: 
                    if aa[3]>= 500:
                        pamatne.delete("pika"+str(i))
                except:
                    izveidot_jaunu_piku("pika"+str(i))                
            #makonisi
            try: 
                pamatne.move("makonis1", 0.8 ,0)
                aa=pamatne.coords("makonis1")
                if aa[0]>= 940:
                    pamatne.delete("makonis1") 
            except:
                #ja makonitis izdzēsts tad izveido jaunu kreisajā pusē
                pamatne.create_arc(250-400,100,370-400,140 , start=-90,extent=180 ,fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(170-400,60,250-400,140, start=0,extent=180 , fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(250-400,70,350-400,160, start=0,extent=180 , fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(200-400,80,270-400,160, start=0,extent=180 , fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(160-400,80,240-400,100, start=0,extent=270 , fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(130-400,90,250-400,130, start=0,extent=270 , fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(140-400,100,300-400,160, start=90,extent=90 , fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(250-400,100,350-400,160, start=90,extent=90 , fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_arc(120-400,120,200-400,142, start=90,extent=270, fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_rectangle(210-400,100,340-400,130, fill="#cad2c5", outline="", tag="makonis1")
                pamatne.create_rectangle(170-400,130,320-400,142, fill="#cad2c5", outline="", tag="makonis1")

            
            try: 
                pamatne.move("makonis2", 0.8 ,0)
                aa=pamatne.coords("makonis2")
                if aa[0]>= 900:
                    pamatne.delete("makonis2") 
            except:
                #ja makonitis izdzēsts tad izveido jaunu kreisajā pusē
                pamatne.create_rectangle(650-750,70,700-750,90, fill="#979dac", outline="", tag="makonis2")
                pamatne.create_arc(610-750,60,700-750,90, start=90,extent=270,fill="#979dac", outline="", tag="makonis2")
                pamatne.create_arc(630-750,50,670-750,90, start=0,extent=180,fill="#979dac", outline="", tag="makonis2")
                pamatne.create_arc(660-750,40,710-750,90, start=0,extent=180,fill="#979dac", outline="", tag="makonis2")
                pamatne.create_oval(650-750,60,730-750,90,fill="#979dac", outline="", tag="makonis2")
            logs.update()
            time.sleep(0.001)
    except: # programma izmet execpition ja tā tiek aizvērta kamer darbojas, taču tā darbojas mūžīgi. 
        print("Programmas beigas")

def spiguli():
    try:
        #maina spigulīšu krāsas
        krasa = ["red","blue","white"]
        while True:
            pamatne.itemconfig("spigulis"+str(2),outline=krasa[2])
            pamatne.itemconfig("spigulis"+str(1),outline=krasa[1])
            pamatne.itemconfig("spigulis"+str(0),outline=krasa[0])
            logs.update()
            time.sleep(0.5)
            pamatne.itemconfig("spigulis"+str(2),outline=krasa[0])
            pamatne.itemconfig("spigulis"+str(1),outline=krasa[2])
            pamatne.itemconfig("spigulis"+str(0),outline=krasa[1])
            logs.update()
            time.sleep(0.5)
            pamatne.itemconfig("spigulis"+str(2),outline=krasa[1])
            pamatne.itemconfig("spigulis"+str(1),outline=krasa[0])
            pamatne.itemconfig("spigulis"+str(0),outline=krasa[2])
            logs.update()
            time.sleep(0.5)
    except:
        print("Programmas beigas")
        


    
#sākuma objeti
#koki
for x in range(-50,850,50):
    a = random.randrange(25,40)
    y = math.sin(x+500/900)*20+400
    izveidot_kocinu(x+25,y, lielums=40 , garums = a, fill="#012A4A")
    izveidot_kocinu(x+5,y, lielums=40 , garums = a, fill="#2A6F97")
    izveidot_kocinu(x-10,y, garums=a-5, fill="#014F86")
#tiek izveidots priekšplāns    
pamatne.create_arc(-400,350,1000,650, style="chord", start=0,extent=180 , fill="#5CC0FF", outline="white", width="3")
pamatne.create_arc(-500,400,800,650, style="chord", start=0,extent=180 , fill="#70C8FF", outline="white", width="3")
izveidot_kocinu(550,500,lielums=40, garums=55, fill="#013A63")
izveidot_kocinu(500,500,lielums=50, garums=45, fill="#468FAF")
izveidot_kocinu(525,500,lielums=40, garums=40, fill="#61A5C2")
pamatne.create_rectangle(296,375,304,386, fill="#540b0e", outline="")
izveidot_kocinu(300,382,lielums=30, garums=15, fill="#036666")
izveidot_gaisminas_kokam(300,382,lielums=30,garums=15)
pamatne.create_arc(100,450,1500,650, style="chord", start=30,extent=180 , fill="#70C8FF", outline="white", width="3")
#maja
#pirmais stavs
pamatne.create_rectangle(80,340,140,380, fill="#9D1B1B", outline="")
pamatne.create_rectangle(140,340,220,380, fill="#B5201F", outline="")
pamatne.create_rectangle(185,350,200,380, fill="#9D1B1B", outline="")
pamatne.create_rectangle(200,350,230,380, fill="#B5201F", outline="")
#otrais stavs
pamatne.create_rectangle(110,295,170,340, fill="#9D1B1B", outline="") 
pamatne.create_polygon(155,320,135,340,80,340,100,320, fill="lightblue")
pamatne.create_polygon(200,260,165,295,110,295,145,260, fill="lightblue")
apalots_trijsturis(200,255,240,295,160,295, radius=20, fill="white")
pamatne.create_rectangle(170,295,230,340, fill="#B5201F", outline="")
#logi
for x in (90,117,150):
    pamatne.create_rectangle(x,350,x+15,370, fill="#FFEF85" , outline="#38618C", width=2)
for x in (180,208):
    pamatne.create_rectangle(x,305,x+15,325, fill="#FFEF85" , outline="#38618C", width=2)
#durvis
pamatne.create_rectangle(210,355,223,380, fill="#59260B" , outline="")
pamatne.create_line(210,355,223,355,fill="#361707" ,width=3)
pamatne.create_line(213,358,213,378,fill="#361707")
pamatne.create_line(213,358,220,358,fill="#361707")
pamatne.create_line(220,358,220,378,fill="#361707")
pamatne.create_line(220,378,213,378,fill="#361707")
pamatne.create_line(220,365,213,365,fill="#361707")
#jumsts
pamatne.create_polygon(215,330,200,350,185,350,200,330, fill="lightblue")
apalots_trijsturis(155,315,180,340,130,340, radius=20, fill="white")
apalots_trijsturis(215,325,240,350,190,350, radius=20, fill="white")
pamatne.create_polygon(215,335,230,350,200,350, fill="#B5201F")
pamatne.create_polygon(156,325,171,340,141,340, fill="#B5201F")
pamatne.create_polygon(200,265,230,295,170,295, fill="#B5201F")
pamatne.create_arc(60,375,150,395, style="chord", start=0, extent=180, outline="", fill="#5CC0FF")
pamatne.create_arc(140,375,200,395, style="chord", start=0, extent=180, outline="", fill="#5CC0FF")
#mēness
pamatne.create_oval(450,20,550,120, tag="moon", outline="", fill="#FDD38C")
#makoņi
#makonis1
pamatne.create_arc(250,100,370,140 , start=-90,extent=180 ,fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(170,60,250,140, start=0,extent=180 , fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(250,70,350,160, start=0,extent=180 , fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(200,80,270,160, start=0,extent=180 , fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(160,80,240,100, start=0,extent=270 , fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(130,90,250,130, start=0,extent=270 , fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(140,100,300,160, start=90,extent=90 , fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(250,100,350,160, start=90,extent=90 , fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_arc(120,120,200,142, start=90,extent=270, fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_rectangle(210,100,340,130, fill="#cad2c5", outline="", tag="makonis1")
pamatne.create_rectangle(170,130,320,142, fill="#cad2c5", outline="", tag="makonis1")
#makonis2
pamatne.create_rectangle(650,70,700,90, fill="#979dac", outline="", tag="makonis2")
pamatne.create_arc(610,60,700,90, start=90,extent=270,fill="#979dac", outline="", tag="makonis2")
pamatne.create_arc(630,50,670,90, start=0,extent=180,fill="#979dac", outline="", tag="makonis2")
pamatne.create_arc(660,40,710,90, start=0,extent=180,fill="#979dac", outline="", tag="makonis2")
pamatne.create_oval(650,60,730,90,fill="#979dac", outline="", tag="makonis2")

#procedūru izsaukšana
izvedot_piku()
#izsauc divas procedūras, lai tās strādātu vienlaicīgi
Thread(target = kustiba).start()
Thread(target = spiguli).start()
logs.mainloop()