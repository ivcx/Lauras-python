N = float(input("Ivadi lielākā zara garumu: "))
if N>0:
    a=1
    b=1
    c=1
    print("*")
    while c<=N:
        print("*"*c)
        c=a+b
        a=b
        b=c
else: 
    print("Ievadiet pozitīvu skaitli")