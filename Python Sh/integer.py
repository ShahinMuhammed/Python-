len=int(input("How many number do you want to store:"))
inpvalueList=[]
for num in range(0,len):
    inpvalue=int(input("Enter value"))
    if(inpvalue>100):
        inpvalueList.append("over")
    else:
        inpvalueList.append(inpvalue)
print(inpvalueList)
