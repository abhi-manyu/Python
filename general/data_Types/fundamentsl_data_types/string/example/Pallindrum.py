def findPallindrum(message):
    counter = 0
    while counter <= len(message) // 2:
        if message[counter] != message[len(message) - 1 - counter]:
            print('not palindrome')
            break
        else:
            counter += 1
    else:
        print('pallindrume')


message = input('enter the text i will tell ou that is palliindrum or not ? ')
findPallindrum(message)
