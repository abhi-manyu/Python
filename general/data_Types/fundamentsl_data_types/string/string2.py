# for example if i want to print characters by escaping next characters, then
# there is a method for that.
name = 'Arabinda Moharana'
print(name[0:15:2])  # Aaid oaa starting from first index i.e 0 to 14th index, this will print
#                     characters by escaping one by one

name = 'Abhimanyu Moharana'
print(name[::2])  # AhmnuMhrn this will automaticaly take from first to last index of the string
#                  and print characters escaping by next character

name = 'abhimanyu moharana'
print(name[::3])  # will print from first to last characters by escaping next 2 characters

# suppose i want to print one string 10 times, in other programming laguage like java, we have to
# take the help of loops, but here in python it provides inbuilt support bu just multiplying
# the number with required string
name = 'arabinda '
print(5*name)

name = 'abhi'
print(3*name)
# like in java, python also , finding length of the string, one method is there,i.e len(string)
name='abhi manyu moha rana'
print('the length  of the string is {}'.format(len(name)))
