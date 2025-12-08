import csv
f=open("mark.csv","r")
content=csv.reader(f)
next(content)
for i in content:

    if int(i[3])>=90:
        print (i)
