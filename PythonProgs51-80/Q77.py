n = int(input("Enter how many elements"))
d = {}
for i in range(n):
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    if key in d.keys():
        print("Key already exists")
    else:
        d.update({key:value})


print("Current data in the dictionary")   
for k,v in d.items():
    print(k, v)
