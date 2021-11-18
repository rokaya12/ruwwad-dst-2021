def intilist(list1):
    for i in range(10):
        nb=int(input("enter a nb:"))
        list1.append(nb)
    intilist(list1)
def printlist1(list1):
    for i in list1:
        print(i)
    printlist1(list1)
