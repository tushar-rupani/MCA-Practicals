n = int(input("Enter how many strings you want to enter: "))
numLst = []
for i in range(1, n+1):
    inpt = input(f"Enter string {i}:")
    numLst.append(inpt)


numLst.sort()

print(numLst)
