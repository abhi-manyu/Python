name = 4525
print(name)
print(id(name))

name2= 4525
print('the vlaue is : {} and address is : {} '.format(name2,id(name2)))
print(name2 is name)


name3 = 4525
print(name3)
print(name3 is name2)
print(name3 is name)
print(name is name2)

num1 = 3216456
num2 = 3216456
print(num1 is num2)


value = True
value2=True
print('the boolean example is : {} '.format(value is value2))

# from string to int type, if the content is only a decimal value, even if it is a float
# value also it can not convert, and will through error
value = '16556.45'
print('the value is  : {} and type is {} '.format(value,type(value)))
print('the value is  : {} and type is {} '.format(value,type(int(value))))
