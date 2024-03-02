input_file_path = r'C:\Users\adiro\OneDrive\Desktop\majorV3\utils\test.test.txt' 
output_file_path = r'C:\Users\adiro\OneDrive\Desktop\majorV3\utils\test.txt'  

# Define the mapping of punctuation characters to their replacements
punctuation_mapping = {
    ',': 'COMMA',
    '.': 'PERIOD',
    '?': 'QUESTIONMARK',
    ';': 'SEMICOLON'
}

# Read the input file
with open(input_file_path, 'r', encoding='ansi') as file:
    text = file.read()

# Process the text to add the replacements after punctuation characters
for char, replacement in punctuation_mapping.items():
    text = text.replace(char, f' {char}{replacement} ')

# Write the modified text to the output file
with open(output_file_path, 'w') as file:
    file.write(text)

print(f"Text has been processed and saved to {output_file_path}")
