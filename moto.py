motoposition=9
motocontrol=""
while motocontrol!="s":
    print("-----------------")
    break
for x in range (10):
        print("|               |")
if x==motoposition:
    print("|      oMo      |")
for x in range(x>0):
    motocontrol=input("f.forward or r.reverse or s.stop game:")
if motocontrol=="f" and motoposition!=0:
    motoposition=motoposition-1
elif motocontrol == "r" and motoposition!=9:
    motoposition=motoposition+1
    print("-----------------")
for x in range (10):
    print("|               |")
if x==motoposition:
    print("|       oMo       |")
    

