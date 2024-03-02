def split_text_file(original_file, output_files):
    with open(original_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Calculate the length of each split section
    total_length = len(text)
    section_length1 = int(0.75 * total_length)
    section_length2 = int(0.15 * total_length)

    # Split the text into three sections
    section1 = text[:section_length1]
    section2 = text[section_length1:section_length1 + section_length2]
    section3 = text[section_length1 + section_length2:]

    # Write each section to a separate file
    with open(output_files[0], 'w') as f:
        f.write(section1)

    with open(output_files[1], 'w') as f:
        f.write(section2)

    with open(output_files[2], 'w') as f:
        f.write(section3)

# Example usage
original_file = 'data.txt'
output_files = ['train.train.txt', 'dev.dev.txt', 'test.test.txt']

split_text_file("corpus.txt", output_files)
