#Bubble Sort:
n = int(input("Enter the limit: "))
lst = []
occ = 0
for i in range(1, n+1):
    inpt = int(input(f"Enter Value for {i}"))
    lst.append(inpt)
    
for i in range(0, len(lst) - 1):
    for j in range(len(lst) - 1):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            
print("Ascending Order", lst)


for i in range(len(lst) - 1):
    for j in range(len(lst) - 1):
        if lst[j] < lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
print("Descending Order", lst)
            

        
        
        
