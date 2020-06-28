# in python there is inbuilt support for complex data type and related mathematics.
# like in math we had complex number in format of (a + bj), where
# a is the real part and the b is the imaginary part
# 'a' and 'b' can b both decimal or float value
# in python the complex number can be represented by only 'j' notation,
# we can not replace it with any other character like a + bi, it will thorough error
# there is no character data type in python

# the real part can be defined in any integer type(decimal, binary, octal, hexadecimal), but the
# imaginary part should be only in decimal format

# we can get the real value of the complex number by python given 2 inbuilt attributes
# those are real 'and' and 'image'
number = 5 + 8j
print(number)
print(type(number))

number2 = 0b110101 + 8.9j  # that binary real part is auto converted to decimal
print(number2)
print(type(number2))

# number3=56+0b1101j
# print(number3)                 this will through error, though the imaginary part only can be
#                                decimal value

number3 = 0xadb34 + 56j
print(number3)
print(type(number3))

# operation with real numbers
num1 = 10 + 20j
num2 = 8 + 45j
print('the addition is {}'.format(num1 + num2))
print('the subtraction is : {}'.format(num1 - num2))
print('the multiplication is : {}'.format(num1 * num2))

num1 = 45 + 50j
print("the number is {}".format(num1))
print('the real part is : {}'.format(num1.real))
print('the imaginary part is : {}'.format(num1.imag))


number = 10.5+90j
print(number)