from morse_table import morse_table
import re


def convert_to_morse():

    # Compile regex expression that accepts only letters, numbers and spaces.
    pattern = re.compile('[A-Z0-9 ]+')

    while True:

        # Input sentence.
        in_sentence = input('Enter the sentence you want to code (morse): \n').upper()

        # Check regex expression.
        if not re.fullmatch(pattern, in_sentence):

            print('ERROR: Invalid sentence! Try again.')

            continue

        # Output in morse.
        out_morse_sentence = ''.join([morse_table[a_char]+'  ' for a_char in in_sentence])
        print(out_morse_sentence)

        if in_sentence == 'EXIT':

            break


# Run main component.
if __name__ == '__main__':
    convert_to_morse()
