list1=[]
list2=[]
n=int(input("enter a number:"))
for i in range(n):
    name=input("enter a name"+str(i+1)+":")
    list1.append(name)
for i in range(len(list1)):
    list1[i]=list1[i].capitalize()
print(list1)
for x in list1:
    if x not in list2:
        list2.append(x)
print("after removing:",list2)