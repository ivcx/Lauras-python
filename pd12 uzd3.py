N = int(input("Ievadiet naturālu skaitli: "))
a =N
j =2
sv = str(N) + "="
while a>1:
    k=0
    while (a%j)==0:
        a =a//j
        k =k+1
    if k>0:
        sv =sv+str(j) + "^" +str(k) + "*"
    j =j+1

sv = sv[:-1]
print(sv)