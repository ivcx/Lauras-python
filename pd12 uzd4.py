A=input("ievadi intervāla sākumu A ===> ")
B=input("ievadi intervāla beigas B ===> ")
A=A.strip()
B=B.strip()

r1=len(A)
r2=len(B)

for i in range (0, r1):
        if (A[0]=="-" or A[0]=="+") and i==0:
            i=i+1

        if (A[i]=="." or A[i]==",") and i!=0:
            continue

        a=A[i]

        if a.isdigit()==True:
            p1=True
        else:
            p1=False
            break

for i in range (0, r2):
        if (B[0]=="-" or B[0]=="+") and i==0:
            i=i+1

        if (B[i]=="." or B[i]==",") and i!=0:
            continue

        a=B[i]

        if a.isdigit()==True:
            p2=True
        else:
            p2=False
            break

 
   
if p1==True and p2==True:
    A=float(A)
    B=float(B)  
    if A>=B:
        print("Nav ievadīts derīgs intervāls")
    else:
        for i in range (0,3):
            x=input("ievadi naturālu skaitli x ===> ")
            x=x.strip()

            r3=len(x)

            for i in range (0, r3):
                a=x[i]
                if a.isdigit()==True:
                    p3=True
                else:
                    p3=False
                    break
        
            if p3==True and int(x)>=A and int(x)<=B:
                print("x ir naturāls skaitlis intervālā [A;B]")
                break
            else:
                print("x nav naturāls skaitlis intervālā [A;B]")

else:
    print("Nav ievadīts derīgs intervāls")                  





