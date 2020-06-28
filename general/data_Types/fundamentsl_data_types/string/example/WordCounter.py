wordCounter = 0

def find_reverseAnother(message):
    char_counter = 0
    global wordCounter
    word = ''
    while char_counter < len(message):
        if message[char_counter] != ' ':
            word += message[char_counter]
            char_counter += 1
        else:
            print(word)
            word = ''
            char_counter += 1
            wordCounter += 1
    else:
        wordCounter += 1
        print(word)


message = input('enter the whole string to count the number of words \n ')
find_reverseAnother(message)
print('total {} number of word found in the String '.format(wordCounter))