# for converting from any base type to binary type integer, we can take  help of bin()
# from decimal to binary
number1 = 89756
print("the decimal number {} in binary form is : {}".format(number1, bin(number1)))

# from octal to binary
number = 0o756
print("the octal number {} in binary form is : {}".format(number, bin(number)))

# from  hexadecimal to binary
print('the hexadecimal number : 0xcb45 in binary form : {}'.format(bin(0xcb45)))
print(60 * '-')

#                         to octal integer
# from decimal to octal
print('the decimal number 42345 to octal is {}'.format(oct(42345)))

# from binary to octal
print('the binary number : 101111011 in octal format is : {}'.format(oct(0b101111011)))

# from hexadecimal to octal number:
print('the hexadecimal number dca45b in octal is {}'.format(oct(0xdca45b)))
print(60 * '-')

#               for hexadecimal format : there is one method : hex()
# from binary to hexadecimal number
print('the binary number 101011101001 in hexadecimal is : {}'.format(hex(0b101011101001)))
