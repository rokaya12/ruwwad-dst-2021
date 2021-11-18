#for i in range(1,5):
   # for j in range(1,5-i):
   #     print("-",end="")
   # for k in range(1,i):
   #         print("+",end="")
   # for l in range(1,4):
  #      print("*",end="")   
  #  print()   
name=input("enter a name:")
for i in range(len(name)-1,-1,-1):
    print(name[i],end="")
     