import csv
file=open(r"details.csv","r")
content=csv.reader(file)

for i in content:
    print(i)
file.close()
