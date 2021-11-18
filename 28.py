farm={'cats':10, 'dogs':7, 'cows':5, 'horses':1}
print(farm['cats'])
print(farm.keys())
print('hen'in farm)
farm['dogs']=farm['dogs']+2
print(farm)
farm['rabit']=1
print(farm)
farm.pop('horses')
print(farm)
total_nb = sum(farm.values())
print(total_nb)
minm_nb=min(farm.values())
print(minm_nb)
m1=max(farm.values())
for x in farm:
    if farm[x]==m1:
        print('the animal that is exist the most:',x)