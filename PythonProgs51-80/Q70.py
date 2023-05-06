str = input("Enter the String: ")


wordlst = str.split(" ")
charlst = list(str)

wcount = 0
cCount = 0

for i in wordlst:
    wcount = wcount + 1

for i in charlst:
    cCount = cCount + 1


print("total words: ", wcount)
print("total characters: ", cCount)
    

