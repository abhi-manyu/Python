# for casting any other format to float there is a method in python called float().
# from into to float
value = 125
print('old value is {} and the type is : {}'.format(value, type(value)))
print('the new value is {} and the type is {}'.format(float(value), type(float(value))))
print(60 * '-')

# from string to float
value = "148"
print('old value is {} and the type is : {}'.format(value, type(value)))
print('the new value is {} and the type is {}'.format(float(value), type(float(value))))
print(60 * '-')  # 148.0

# from string to float 2nd example
value = '458.563'
print('old value is {} and the type is : {}'.format(value, type(value)))
print('the new value is {} and the type is {}'.format(float(value), type(float(value))))
print(60 * '-')  # 458.563  (which was not possible in int type)

# from double to float type
value = True
print('old value is {} and the type is : {}'.format(value, type(value)))
print('the new value is {} and the type is {}'.format(float(value), type(float(value))))
print(60 * '-')

# from complex to float
value = 10 + 20j
print('old value is {} and the type is : {}'.format(value, type(value)))
# print('the new value is {} and the type is {}'.format(float(value), type(float(value))))
#  here in this case this is not possible, complex can not be converted to float format
print(60 * '-')

# only int of base 10 can be converted to float.
value=0B111
print(float(value))  # 7.0

value= '0B111'
print(float(value))  # error




