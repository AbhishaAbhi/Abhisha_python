list1=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    element1=input("Enter the color:")
    list1.append(element1)
print(list1)
list2=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    element2=input("Enter the colour:")
    list2.append(element2)
print(list2)
for i in list1:
    if i not in list2:
        print(i)

          
