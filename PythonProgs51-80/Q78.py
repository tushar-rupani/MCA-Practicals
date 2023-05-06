n = int(input("How many players you want in this game: "))
dic = {}
for i in range(n):
    key = input("Enter Player Name: ")
    value = input("Enter Score: ")
    dic.update({key:value})


for k, v in dic.items():
    print(k,v)

src = input("Enter the player name you want to find")

print(dic[src])
    
