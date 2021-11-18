import random
#randlist=[]
#for i in range(100):
#    x=random.randint(0,100)
 #   randlist.append(x)
#print(randlist)
list1=[]
for i in range(10):
    x=random.randint(0,10)
    list1.append(x)
print(list1)
max=list1[0]
for i in list1: 
    if max < list1[i]:
        max=list1[i]

min=list1[0]
for i in list1 :
    if min > list1[1]:
        min=list1[i]

sum=0
for nb in list1:
    sum+=nb


    



