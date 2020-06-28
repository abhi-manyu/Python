# There are few methods present for type casting from one type to another types
# i.e
#   int()------always accepts the value base 10 only
#   float()
#   str()
#   bool
#   complex()

# from float to int
value = 23.45
print('old value is {} and the type is : {}'.format(value, type(value)))
print('the new value is {} and the type is {}'.format(int(value), type(int(value))))
print(60 * '-')
# from string to int
value = '45'
print('old value is {} and the type is : {}'.format(value, type(value)))
print('the new value is {} and the type is : {}'.format(int(value), type(int(value))))
value = '56.89'  # here it is taking as the string
print('old value is {} and the type is : {}'.format(value, type(value)))
# print('the new value is {} and the type is : {}'.format(int(value), type(int(value))))
#   here in this example it will through error , bcz in python we only can convert from
#    string to int , if the content is a whole number or the content is only in
# decimal format, or else it will through error
# even we try to convert a string content of binary or octal format also it will through
# error.

print(60 * '-')
# from boolean to int
value = True
print('old value is {} and the type is : {}'.format(value, type(value)))
print('new value is {} and the type is : {}'.format(int(value), type(int(value))))
value = False
print('old value is {} and the type is : {}'.format(value, type(value)))
print('new value is {} and the type is : {}'.format(int(value), type(int(value))))
print(60 * '-')
# from complex to int
value = 10 + 20j
print('old value is {} and the type is : {}'.format(value, type(value)))
print('real part is : {} of type {} and imaginary part is {} of type {}'.
      format(value.real, type(value.real), value.imag, type(value.imag)))
# print('new value is {} and the type is : {}'.format(int(value),type(int(value))))
#   This will through error bcz we know before that in complex number every part
#   (real and imaginary) are represented as float number

# **  Note  **
# we can not covert String of non decimal number , complex number into the int type

# Binary to the int type
# here both are int type, but in different format
value = 0B1110101
print('0B1110101 {}'.format(type(0B1110101)))
print('the int from binary to int is {}'.format(int(0B1110101)))  # 117

value = '0B1110101'
# print(int(value)) # will through error,bcz it is expecting the content with base 10
# but we are giving with base 2 that is in binary format
print('{} {}'.format(value, type(value)))

# from float to int conversion
value = 78.5689
print('the converted int value is : {}'.format(int(value)))

# from 







