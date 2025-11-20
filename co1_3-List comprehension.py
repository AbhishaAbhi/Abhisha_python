#generate positive list of numbers from a given list of numbers
n=[-5,3,0,8,-2,7,-1]
pn=[i for i in n if i > 0]
print(pn)

#Square of N numbers
s=int (input("Enter the number:"))
sq=[j*j for j in range(1, s+1)]
print("demo.csv",sq)

#form a list of vowel from a given word
w=input("Enter a word:")
v= [i for i in w if i.lower() in "aeiou"]
print("vowels in the word:",v)

#list ordinal values of a word
t=input("Enter a word:")
ov=[ord(i) for i in t]
print("Ordinal values:",ov)
