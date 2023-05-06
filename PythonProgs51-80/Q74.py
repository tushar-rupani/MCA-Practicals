str = input("Enter String: ")
sub_str = input("Enter Sub String: ")

if str.find(sub_str) == -1:
    print("We did not find Substr")
else:
    print(str.find(sub_str))
