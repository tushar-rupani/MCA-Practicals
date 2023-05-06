n = int(input("Enter the limit: "))
lst = []
for i in range(1, n+1):
    inpt = int(input(f"Enter Value for {i}"))
    lst.append(inpt)
    
srch = int(input("Enter the digit you want to search: "))

if srch in lst:
    print('Exists')
else:
    print("Doesn't exist")
        
        
        
