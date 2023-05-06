n = int(input("Enter Limit: "))
sett = set([])
for i in range(n):
    inpt = int(input("Enter Value: "))
    sett.add(inpt)

print(sett)

lst = list(sett)
print("Maximum character of set is", max(lst))
    
