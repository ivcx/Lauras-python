import math
def malas_garums(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def izliekums(x1,y1,x2,y2,x3,y3,x4,y4):
    z1 = (x1-x4)*(y3-y4) - (y1-y4)*(x3-x4)
    z2 = (x2-x4)*(y3-y4) - (y2-y4)*(x3-x4)
    return z1 * z2 > 0


try:
    print("Ievadiet koordinātes pirmajam punktam")
    x1 = float(input("x:"))
    y1 = float(input("y:"))
    print("Ievadiet koordinātes otrajam punktam")
    x2 = float(input("x:"))
    y2 = float(input("y:"))
    print("Ievadiet koordinātes trešajam punktam")
    x3 = float(input("x:"))
    y3 = float(input("y:"))
    print("Ievadiet koordinātes ceturtajam punktam")
    x4 = float(input("x:"))
    y4 = float(input("y:"))
    print("Ievadiet koordinātes piektajam punktam")
    x5 = float(input("x:"))
    y5 = float(input("y:"))
except:
    print("Nēsat ievadījis derīgas vērtības")
else:
    izliekts = False
    if izliekums(x1,y1,x2,y2,x3,y3,x4,y4) == True and izliekums(x1,y1,x2,y2,x3,y3,x5,y5) == True: #pret pirmo malu 
        if izliekums(x2,y2,x3,y3,x1,y1,x4,y4) == True and izliekums(x2,y2,x3,y3,x1,y1,x5,y5) == True: #pret otro malu
            if izliekums(x3,y3,x4,y4,x2,y2,x1,y1) == True and izliekums(x3,y3,x4,y4,x2,y2,x5,y5) == True: #pret trešo malu  
                if izliekums(x4,y4,x5,y5,x3,y3,x2,y2) == True and izliekums(x4,y4,x5,y5,x3,y3,x1,y1) == True: #pret ceturto malu 
                    if izliekums(x1,y1,x5,y5,x3,y3,x4,y4) == True and izliekums(x1,y1,x5,y5,x3,y3,x2,y2) == True: #pret piekto malu 
                        izliekts = True
if izliekts == True:
    print("Daudzsturis nav izliekts")
else: 
    print("Daudzsturis nav izliekts")
