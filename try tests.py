for w in range (1,4):
    x= input("Ievadi reālu skaitli: ")
    x=x.strip()
   
    r=len(x)

    for i in range (0, r):
        if (x[0]=="-" or x[0]=="+") and i==0:
            i=i+1

        if (x[i]=="." or x[i]==",") and i!=0:
            continue

        a=x[i]

        if a.isdigit()==True:
            p=True
        else:
            p=False
            break
    
    if p==True:
        print("Ir reāls skaitlis")
        break

    else:
        print("Nav reāls skaitlis")


            