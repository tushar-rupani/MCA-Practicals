n = int(input("Enter the limit: "))
lst = []
for i in range(1, n+1):
    inpt = int(input(f"Enter Value for {i}"))
    lst.append(inpt)
    
print(sum(lst))
print(max(lst))
print(min(lst))

print(sum(lst) / len(lst))
        
