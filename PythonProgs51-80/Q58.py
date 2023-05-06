r = int(input("Enter amount of Rows: "))
c = int(input("Enter amount of Columns: "))

matrix = []
result = [[0,0,0], [0,0,0],[0,0,0]]
for i in range(r):
    a = []
    for j in range(c):
        inpt = int(input())
        a.append(inpt)
    matrix.append(a)
r = int(input("Enter amount of Rows for matrix 2: "))
c = int(input("Enter amount of Columns for matrix 2: ")) 
matrix2 = []
for i in range(r):
    a2 = []
    for j in range(c):
        inpt = int(input())
        a2.append(inpt)
    matrix2.append(a2)
    
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[i][j] = matrix[i][j] + matrix2[i][j]
    
print(result)
        
