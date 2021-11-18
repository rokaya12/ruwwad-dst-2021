#def hello(name):
 #   print("welcome",name)
#n=int(input("enter a nb:"))
#for i in range(n):
  #  name=input("enter a name:")
   # hello(name)


#def sum(a,b,c):
 #   print(a+b+c)
#a=int(input("enter a nb:"))
#b=int(input("enter a nb:"))
#c=int(input("enter a nb:"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#sum(a,b,c)

sum=0
total=nb[0]
n=int input('enter a nb:')
for i in range(n):
    nb=int(input("enter a nb:"))
    sum=sum+nb
    total=total+nb[i]
    break
print("the average is:",sum/total)
