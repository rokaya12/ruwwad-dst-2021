#for l in range(5):
  #  if l==2:
  #      line=""
  #      for x in range(5):
   #         if (x==0 or x==3):
    #            line=line+"|"
   #         else:
    #            line=line+"_"
#print(line)
line=""
s=0
while s in  range (3):
    for s in range(5):
        if (s==0 or s==2 or s==4):
            line=line+"_"
        else:
            line=line+"|"
s=s+1
print(line)