n = int(input("Enter the limit: "))
lst = []
occ = 0
for i in range(1, n+1):
    inpt = int(input(f"Enter Value for {i}"))
    lst.append(inpt)
    
srch = int(input("Enter the digit you want to search: "))
for i in lst:
    if i == srch:
        print(f"Occurance of {srch} found at location {occ} for the first time")
        break
    occ = occ + 1


        
        
        
