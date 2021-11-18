#name1=[]
#nb_cars=int(input("enter the nimber of cars:"))
#for i in range(nb_cars):
 #   car_name=input("enter the name of the car:")
  #  while car_name in name1:
  #      car_name=input("eror,duplicate cars,enter a new car:")
  #  else:
    #    name1.append(car_name)
#print(name1)
#for i in range(len(name1)):
 #   print(name1[i],end="_")
#fruit=["banana","apple","apple","banana"]
#newlist=[x if x != "banana" else "orange" for x in fruit]
#print(newlist)
a=[1,2,3,4,5]
b=[10,9,8,7,5]
c=[]
for i in range(len(a)):
    sum=a[i]+b[-i-1]
    c.apend(sum)
print(c)