def eikida_algor(a,b):
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

n1 = int(input("Ievadi pirmo skaitli: "))
n2 = int(input("Ievadi otro skaitli: "))
n3 = int(input("Ievadi trešo skaitli: "))
n4 = int(input("Ievadi ceturto skaitli: "))

#lielākais kopīgais dalītājs
LKD=eikida_algor(n1,n2)
LKD=eikida_algor(LKD,n3)
LKD=eikida_algor(LKD,n4)

print("LKD = " +str(LKD))

#mazākais kopīgais dalāmais
#sakārtošana secībā
sk = (n1,n2,n3,n4)
sk = sorted(sk)
n1 = sk[0]
n2 = sk[1]
n3 = sk[2]
n4 = sk[3]
MKD = n1
while True:
    if MKD%n1==0 and MKD%n2==0 and MKD%n3==0 and MKD%n4==0 :
        print("MKD = "+str(MKD))
        break
    MKD=MKD+1

    
