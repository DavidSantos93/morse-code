# Dictionary representing the morse code translation chart
translation = {'A': '.-', 'B': '-..', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.-..', 'K': '-.-', 'L': '.---', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
               '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}


# Function will encrypt the string according to the morse code dictionary 'translation'
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the corresponding translation with spaces
            cipher += translation[letter] + ' '
        else:
            # 1 space = different characters; 2 spaces = different words
            cipher += ' '
    return cipher


# Function to decrypt the string from morse code back to english
def decrypt(message):
    # extra space added at the end to access the last morse code
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if letter != ' ':
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(translation.keys())[list(translation.values()).index(citext)]
                citext = ''
    return decipher


def main():
    choice = input('Do you want to translate "from" or "to" Morse Code? (Use "to" or "from" to answer):')
    if choice == 'to':
        message = input('What would you like to translate to Morse Code?')
        result = encrypt(message.upper())
        print(result)
    else:
        message = input('What would you like to translate from Morse Code?')
        result = decrypt(message)
        print(result)


# Executes the main function
if __name__ == '__main__':
    main()
