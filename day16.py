#for i in range(1,5):
   # for j in range (4-i,0,-1):
 #      print("",end="")
 #   for k in range (1,2*i):
 #       print("*",end="")
  #   print()
#print("",3*"*")

n=int(input("enter number:"))
names=""
for i in range(1,n+1):
    name=input("enter a name"+str(i)+":")
    names=names+name+"\n"
print(names)