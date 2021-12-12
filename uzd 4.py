#uzdevums - vai ievadītais ir pirmskaitlis?

skaitlis = int(input("Ievadiet skaitli: "))
parbaude = True
if skaitlis <=1 :
    parbaude = False 
for x in range (2,skaitlis):
    if skaitlis%x == 0 :
        parbaude = False

if parbaude == False:
    print("Skaitklis nav pirmskaitlis")
else:
    print("Skaitlis ir pirmskaitlis")

