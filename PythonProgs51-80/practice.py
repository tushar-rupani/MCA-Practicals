r = int(input("Enter Amount Of Rows: "))
c = int(input("Enter Amount Of Columns: "))

matrix1 = []


for i in range(r):
    a = []
    for j in range(c):
        inpt = int(input("Enter a value: "))
        a.append(inpt)
    matrix1.append(a)


print(matrix1)


print("MATRIX 2 STARTS FROM HERE!!!!!")


matrix2 = []

for i in range(r):
    a2 = []
    for j in range(c):
        inpt = int(input("Enter the value: "))
        a2.append(inpt)
    matrix2.append(a2)

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print(result)



for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
print(result)
            
