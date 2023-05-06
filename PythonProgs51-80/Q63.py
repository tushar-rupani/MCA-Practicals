str = input("Enter a string: ")

sortStr = sorted(str)
print(sortStr)



descStr = sorted(str, reverse=True)
print(descStr)


count = 0
for i in str:
    count = count + 1

print("Length of String: ", count)
