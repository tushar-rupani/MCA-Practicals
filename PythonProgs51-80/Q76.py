#know the type of character entered by user:

str = input("Enter Only One Character: ")
ch = str[0]

if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
    print("Character is Alphabetic")
elif ch >= '0' and ch <= '9':
    print("Digit character")
else:
    print("Given Character is special character")


str1 = input("Enter string: ")
al = 0
alnm = 0
dig = 0
sc =0
for i in str1:
    if i.isalpha() == True:
        al = al + 1
    elif i.isalnum() == True:
        alnm = alnm + 1
    elif i.isdigit() == True:
        dig = dig + 1
    else:
        sc = sc + 1

print("Alphabetic: ", al)
print("Digit: ", dig)
print("Alnum: ", alnm)
print("Special Character: ", sc)


    
