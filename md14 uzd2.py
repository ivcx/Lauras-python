import math
def pirmskaitlis(x):
    y=round(math.sqrt(x))
    paz=True
    for i in range (2, y+1):
        if x%i==0:
            paz=False
            break
    return paz
def draugi(n):
    ps1=3
    sv=""
    for i in range (5, n+1, 2):
        if pirmskaitlis (i):
            ps2=i
            if ps2-ps1==2:
                sv=sv+str(ps1)+" un "+str(ps2)+"\n"
            ps1=ps2
    return (sv)
sk = 1
while  True:
    try:
        n=int(input("Ievadiet naturālu skaitli N==> "))

    except:
        sk+=1
        if sk > 3 : 
            print("Pārāk daudz reizes ievadīts nepareizi.")
            break
    else:
        if n<0:
            sk+=1
            if sk > 3 : 
                print("Pārāk daudz reizes ievadīts nepareizi.")
                break            
        else:
            print (draugi(n))
            break            
            

