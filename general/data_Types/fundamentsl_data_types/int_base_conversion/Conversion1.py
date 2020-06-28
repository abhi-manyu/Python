# we can convert the any integer of any base to our required base
# i.e from decimal to binary , octal to binary and hexadecimal to binary ane also vice versa.

number = 23
print('in decimal : --{}'.format(number))  # this is decimal

number = 0b011010
print('binary in decimal format --{} '.format(number))  # this is binary input but while displaying the number it
# auto converts into
# decimal format, bcz by default python displays decimal value of integer.

number = 0O4573
print('octal in decimal format --{} '.format(number))  # this octal , but while displaying the number it auto
# converts into decimal

number = 0Xac56bD
print('hexa decimal in decimal format --{} '.format(number))  # this hexa-decimal , but while displaying the number
# it auto converts into decimal

#  so as we saw python auto converts al the base of int type into decimal base while displaying
#  then what is the way to get required base type ?

# well, there is few inbuilt function that provide our required base.

print(60*'-')
print('to Binary base')
print(60*'-')

# there is a inbuilt function bin() that convert any base to binary.
number = 10
print('the decimal {} in binary base : {}'.format(number,bin(number)))

number = 0o12576
print('the octal {} in binary base : {}'.format(number,bin(number)))

number = 0x01cda56d
print('the hexa decimal {} in binary base : {}'.format(number,bin(number)))

# name = 0b110111101011
print(hex(0b110111101011)[2:])