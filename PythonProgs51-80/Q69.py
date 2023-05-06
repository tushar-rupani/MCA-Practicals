str = input("Enter the String: ")
word = input("Enter the word you are looking for")

lst = str.split(" ")
print(lst)
count = 0

for i in lst:
    if i == word:
        count = count + 1

print(f"Word {word} occured for {count} times");
