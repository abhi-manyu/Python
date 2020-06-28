# There is a method that converts everything to complex type called complex(value1) and
#  complex(value1, value2)

# from int to complex
value = 156
print("the value is {} and type is {}".format(value, type(value)))
print('the complex value is {} and type is {}'.format(complex(value), type(complex(value))))
print('-' * 30)
# from float to complex
value = 15.23
print("the value is {} and type is {}".format(value, type(value)))
print('the complex value is {} and type is {}'.format(complex(value), type(complex(value))))
print('-' * 30)

# float to complex
value = 45.89
value2 = 89.56
print("the value is {} and value2 is {}and type is {} and {}".
      format(value, value2, type(value), type(value2)))
print('the complex value is {} and type is {}'.format(complex(value, value2),
                                                      type(complex(value, value2))))
print('-' * 30)

# from string to complex
value = "45"
print("the value is {} and type is {}".format(value, type(value)))
print('the complex value is {} and type is {}'.format(complex(value), type(complex(value))))
print('-' * 30)

# from string to complex
value = "45.89"
print("the value is {} and type is {}".format(value, type(value)))
print('the complex value is {} and type is {}'.format(complex(value), type(complex(value))))
print('-' * 30)

# from boolean to complex
value = True
print("the value is {} and type is {}".format(value, type(value)))
print('the complex valuex is {} and type is {}'.format(complex(value), type(complex(value))))
print('-' * 30)

print(complex(True, False));
print('-' * 30)
# print(complex(False,"6")) # error will come saying that the imaginary part can not be
# String
print('-' * 30)

print('coverting string to complex is : {}'.format(complex("five")))


print(complex("78.89", False))  # throwing error , saying that can not take the second
# argument if the first argument is a string





