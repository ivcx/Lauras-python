print ("Ievadiet skaitļu virki, nulle pārtrauc ievadi")
aa=[]
N=float(input())
i=0
while N!=0:
    aa.append(N)
    N = float(input())
    i +=1

if i>2:
    d = aa[0] - aa[1] 
    ir_arit = True
    for j in range (1,i):
        if aa[j-1]-aa[j]!=d:
            ir_arit = False   
    if ir_arit == True:
        print("Virkne ir aritmētiskā progresija")
    else: 
        print("Virkne nav aritmētiskā progresija")
else:
    print("Ievadiet vairāk skaitļus")