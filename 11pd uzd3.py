 = float(input("Ievadiet skaitli: "))
if N>0:
    a=1
    b=1
    c=0
    while c<=N:
        c=a+b
        if c>N:
            print("Mazākais fibonači skaitlis ,kas ir lielāks par jūsu ievadīto skaitli ir: " + str(c))
        a=b
        b=c
else: 
    print("Ievadiet pozitīvu skaitli")