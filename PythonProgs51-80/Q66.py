str = input("Enter any string: ")
count = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']

for i in str:
    if i in vowels:
        count = count + 1

print(f"There is total {count}vowels in the {str}")
