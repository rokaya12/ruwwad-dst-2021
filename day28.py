birthdays={}
ans="y"
while ans=="y":
    name=input('enter a name:')
    bday=input('enter a bday:')
    if name not in birthdays:
        birthdays[name]=bday
    else:
        print('the entry already exists.')
    print("\nthe birthdays dictionary contains :",birthdays)
    ans=input('\nenter another entry?(yes or no)')
print('\nname \t\t birthdays')
print('--------------------------')
for name in birthdays:
    print(name \t\t 