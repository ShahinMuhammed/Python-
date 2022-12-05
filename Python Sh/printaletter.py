firstnamelist=[]
len=int(input("How many names do you want to enter:"))
for i in range(0,len):
    fname=input("Enter the name:")
    firstnamelist.append(fname)
    count_a=0
for names in firstnamelist:
    count_a+=names.count('a')
print(count_a)
