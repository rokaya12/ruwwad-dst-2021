list1=["lara","ahmad"]
set1=set(())
for i in range(3):
    a=input("enter an element:")
    set1.add(a)
print(set1)
set1.update(list1)
print(set1)
nb=int(input("enter a nb to remove:"))
for i in range(nb):
     set1.pop()
                                                                                                                                                                                       