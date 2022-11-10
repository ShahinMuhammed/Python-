element=input("Enter a word :")
vowels=['a','e','i','o','u']
list_b=[]
for x in element:
    if x in vowels:
        list_b.append(x)
print("vowels present in the given word are :",list_b)
