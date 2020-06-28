# in like java , in python also we can slice or devide the whole string into small pieces
# those are called , sub string or slice of strings
# for that we have to slice the string into following manner :
# while accessing the large indexed value than specified we will get index out of range error
# while slicing the string , the parameters are not mandatory. if the first parameter is not
#   not present , then it will consider from first index upto the specified index.
# if the second parameter is not present it will consider from specified index upto last index
# if no parameter is present then it will simply print the whole string
# always exclude the end index i.e upto end - 1
# while slicing the string , the negative indexes also can be used,
#  But there is a rule , the starting point should be smaller than the ending value.
#  but while using -ve indexes for slicing , we wrote it oppositely like(s[-5:-1]),though
#  the -1 index stating from the end of the string, so we can not write like that.bcz no output
#  will come by this way. so we have to write as the rule.
#  i.e s[-4:-1]  this way starting point(-4) is less than the ending point(-1).
# while accessing the larger indexed vlue that is not at all there ,we'll get index out of
#  range error, but same thing while used in slice operator,  it would not show error.
#  rather it will consider this as a empty.

# like in java tere was 2 part for variable, declaration and initialisation
# but here there is no declaration with out initialisation, this will through error
# example
# x
# print(x) this will through error

# slice operator of string is string[stat:end] by deault it includes the starting boundary
# and excludes ending boundary.
# python also provides inbuilt support for accessing alternate indexed number like:
# suppose i want to access the every alternate one after another character of a string
# example :
name = "Arabinda moharana"
print("the orginal name is : {}".format(name))
print("the sliced name is {}".format(name[1:10]))  # prints from 1 to 5 index
print("the stepped and sliced string is : {}".format(name[1:10:2]))
# default value of the stepping value is 1, that does nothing. cuz main purpose of stepping
# values are to skipp the number of index after printing one index value.
# but if we will use stepping value as 1, then it would not skipp, the behaviour is same as
# like we have not used the stepping value

name = 'abhi manyu moha rana'
print(name)
name2 = name[0:5]
print(name2)
print(len(name2))
print(name[-1])
# print(name[-55]) here error index out of range error will come
name = 'Arabinda Moharana'
print(name[:])  # prints all the string from first to last
print(name[:10])
# using -ve indexes for scilcing
name = 'Arabinda Abimanyu'
print(name)
print(name[-1:-5])  # prints nothing
print('using -ve index : {}'.format(name[-5:-1]))

name = 'Arabinda'
print(name)
# print(name[100])  # error
print('by slice operator : {}'.format(name[2:5]))  # includesthe starting index and excludes
# ending index here print from second index to 4t index

name = 'Abhimanyu'
print("the name is {}".format(name))
print("second slice operator example : {}".format(name[1:-1]))  # prints from b to y i.e
# excludes both the starting boundary and ending boundary

name = "abhi"
print("the separated strings are {}".format(3*name), sep="%")

name = 0b110111101011;
print("name is  :  {} and format is : {}".format(hex(name),type(hex(name))));
print('new name is : {} and format is : {}'.format(hex(name)[2:],type(hex(name)[2:])))
print('second new name is : {} and format is : {}'.format(oct(name),type(oct(name)[2:])))

name = 'debjani'
print(name[1:5])



