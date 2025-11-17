dic={}
limit=int(input("Enter the limit:"))
for i in range(limit):
    k=input("Enter the key:")
    val=input("Enter the value:")
    dic[k]=val
print("In ascenting order")
print(dict(sorted(dic.items())))
print("In decenting order")
print(dict(sorted(dic.items(),reverse=True)))

