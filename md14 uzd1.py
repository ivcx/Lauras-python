def LKD(a,b):
    #lielākais kopīgais dalītājs
    while b!=0:
        c=a%b
        a=b
        b=c
    return a

def MKD(n1,n2,n3,n4,n5):
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
        if MKD%n1==0 and MKD%n2==0 and MKD%n3==0 and MKD%n4==0 and MKD%n5==0:
            return MKD
        MKD=MKD+1


try:
    n1 = int(input("Ievadi pirmo skaitli: "))
    n2 = int(input("Ievadi otro skaitli: "))
    n3 = int(input("Ievadi trešo skaitli: "))
    n4 = int(input("Ievadi ceturto skaitli: "))
    n5 = int(input("Ievadi piekto skaitli: "))      
except:
    print("Nēsat ievadījis naturālus skaitļus.")
else:
    if n1<1 or n2<1 or n3<1 or n4<1 or n5<1:
        print("Nēsat ievadījis naturālus skaitļus.")
    else:
        print("LKD = " +str(LKD(LKD(LKD(LKD(n1,n2),n3),n4),n5)))
        print("MKD = " +str(MKD(n1,n2,n3,n4,n5)))
        

