def remove_punctuation(input_file, output_file):
    with open(input_file, 'r', encoding='ansi') as f_in:
        text = f_in.read()

    # Remove punctuation characters
    punctuation = ",.?!;"
    for char in punctuation:
        text = text.replace(char, ' ')

    # Write the modified text to the output file
    with open(output_file, 'w') as f_out:
        f_out.write(text)

# Example usage
input_file = 'test.test.txt'
output_file = 'output.txt'

remove_punctuation(input_file, output_file)
