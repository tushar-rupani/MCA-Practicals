import re
str = input("Enter String: ")
tchar = 0
cap = 0
slet = 0
dig = 0
sc = 0


for i in str:
    if i.islower() == True:
        slet = slet + 1
    elif i.isupper() == True:
        cap = cap + 1
    elif i.isdigit() == True:
        dig = dig + 1
    else:
        sc = sc + 1
    tchar = tchar + 1

print("total characters", tchar)
print("upper case", cap)
print("lower case", slet)
print("digits", dig)
print("Special Characters", sc)
