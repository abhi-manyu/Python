def reverse_string(message):
    rev_string = ''
    counter = len(message) - 1
    while counter >= 0:
        rev_string += message[counter]
        counter -= 1
    print(rev_string)


message = input('plz enter ur string over here \n ')
reverse_string(message)
