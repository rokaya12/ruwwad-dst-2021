#n=int(input("enter a number:"))
#m=int(input("enter a number:"))
#i=n
#sum=0
#print("the sum of",end="")
#while(i<m):
 #   sum=sum+i
  #  print(i,end="+")
  #  i=i+1
#sum=sum+m
#print(m,"=",sum)
#i=0
#oddnb=0
#evennb=0
#while(i<5):
 #   n=int(input("enter a number:"))
  #  if((n % 2)==0):
   #     print("even")
 #       evennb=evennb+1
 #  else:
  #      print("odd")
  #      oddnb=oddnb+1
  #  i=i+1
#print("the nb of evennb:",evennb)
#print("the nb of oddnb:",oddnb)
alarm="start"
time=(input("give a time to alert you:"))
print("so you should get up at:",time)
while(alarm=="start"):
    n=input("now time to get up :")
    if(n=="close"):
        print("alarm stop")
    break
print("wake up")



