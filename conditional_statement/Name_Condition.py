name=input('enter ur  full name please \n')
if len(name)<5:
    print('name should be within 5 to 20 character long')
elif len(name)>20:
    print('name should not be greater than 20 character ')
else:
    print('ur name {} looks good'.format(name))