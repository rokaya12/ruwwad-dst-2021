#def max(a,b,c):
 #   if ( a>b and a>c):
  #      return a
   # elif (b>a and b>c):
   #     return b
   # elif (c>a and c>b):
    #    return c

#x1=int(input("enter a nb:"))
#x2=int(input("enter a nb:"))
#x3=int(input("enter a nb:"))
#print("the max is:",max(x1,x2,x3))



#def sum():
    #list1=[]
    #sum1=0
    #for i in range(5):
    #    nb=int(input("enter a nb:"))
     #   list1.append(nb)
    #for i in list1:
     #   sum1=sum1+i
   # print('the sum is:',sum1)
#sum()

#def reverce():
 #   name=input("enter a string:")
   # for i in range (len(name)-1,-1,-1):
   #     print(name[i],end="")
#reverce()
def factorial():

  n=int(input("enter a nb :"))
  fact=1
  for i in range (n,0,-1):

    fact= fact*i
  print('fact of',n,'=',fact)
factorial()