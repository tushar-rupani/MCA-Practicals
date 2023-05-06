n = int(input("Enter the limit: "))
lst = []
occ = 0
for i in range(1, n+1):
    inpt = int(input(f"Enter Value for {i}"))
    lst.append(inpt)
    
srch = int(input("Enter the digit you want to search: "))
occ = lst.count(srch)

if occ % 2 != 0:
    print(f"{srch} appearing in the list for {occ} times, which is odd.. then we're displaying..")

        
        
        
