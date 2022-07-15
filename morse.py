from morse_table import morse_table


def convert_to_morse():

    in_sentence = input('Enter the sentence you want to code (morse): \n')
    out_morse_sentence = ''.join([morse_table[a_char]+'  ' for a_char in in_sentence])
    print(out_morse_sentence)


# Run main component.
if __name__ == '__main__':
    convert_to_morse()
