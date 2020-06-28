# in python boolean value true or false is mentioned in Camelcase like below
# if we will write first letter in small it will through error
# like 'c' in python True and False are treated as '1' and '0'
# for string formatting we can use either '\n' or '''something''' or """something"""
# this will exactly print our output in the way we want


value = True
print(value)
print(type(value))

print(True + True)  # 1+1=2
print(True + False)  # 1+0=1

print(30 * '-')
print('string')
print(30 * '-')

name = input('enter ur name\n')
print('hello{}, \nu r welcome'.format(name))

address = input('enter ur country\n')
# print('sorry, {} got you,\nwelcome to {}'.format(name,address))
print('''sorry i got u "{}"
welcome to "{}"'''.format(name, address))
