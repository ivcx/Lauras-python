import random 
N =int(input("Ievadi pozitīvu skaitli:  "))
if N>0:
    iedomatais = random.randint(0,N)
if N<0:
    iedomatais = random.randint(N,0)
atminets= False
ievaditais= int(input("Uzmini skaitli ko esmu iedomājies: "))
i=1
while True:
    if ievaditais>iedomatais:
        ievaditais=int(input("Esmu iedomājies mazāku skaitli, mini vēlreiz: ")) 
        i+=1
        continue
    elif ievaditais<iedomatais:
        ievaditais=int(input("Esmu iedomājies lielāku skaitli, mini vēlreiz: "))
        i+=1
        continue
    else:
        print("Uzminēji ar " + str(i) + ". meiģinājumu")
        break