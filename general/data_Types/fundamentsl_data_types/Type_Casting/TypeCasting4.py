# coverting other types to Boolean type
# here if the argument is zero(0) or empty string then the result is False , other than zero, for all non
# zero and non empty string values, the result will be true.
# int to boolean
value = 0
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))
print("-" * 40)

# for non zero int
value = 820
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# for non zero binary int
value = 0b101011
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# for non zero octal int
value = 0O16117
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# for float value
value = 4.5897
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# for zero floating value
value = 0.00
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# for non zero hexadecimal int
value = 0x10dc4a
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# from String
value = 'abhi'
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# for empty string
value = ''
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

# if imaginary number is passed to the bool method,then following rules works
# if both the real and imaginary part are zero(0), then result is false or otherwise true
#example :
value = 0+0j
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

value = 0-5j
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))

value = -89+0j
print("{},{}".format(value, type(value)))
print("{},{}".format(bool(value), type(bool(value))))
