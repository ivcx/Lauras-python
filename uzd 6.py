vards = str(input("Ievadiet vardu: "))
apgriests=''
garums = len(vards)
for x in range (garums ,0 ,-1):
    apgriests += vards[ x - 1 ] 
print(apgriests) 

if vards.lower() == apgriests.lower():
    print("Simbolu virkne lasās vienādi no abām pusēm")