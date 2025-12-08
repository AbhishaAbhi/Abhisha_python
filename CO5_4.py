import csv
f=open("details.csv","r")
content=csv.reader(f)
n=int(input("Enter the index:"))
for i in content:
    print(i[n])
f.close()
      
