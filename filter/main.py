def sort_and_remove_duplicates(file_path):
    with open(file_path, 'r') as file:
        # Read the contents of the file
        text = file.read()

    # Split the text into words
    words = text.split("\n")

    # Remove leading and trailing whitespaces from words
    words = [word.strip() for word in words]

    # Sort the words alphabetically
    sorted_words = sorted(set(words))

    # Join the sorted words back into a single text
    sorted_text = '\n'.join(sorted_words)

    return sorted_text

# Example usage
input_file_path = 'fsocity.txt'
output_file_path = 'output.txt'

sorted_text = sort_and_remove_duplicates(input_file_path)

# Save the sorted text to a new file
with open(output_file_path, 'w') as file:
    file.write(sorted_text)

print("Sorted and duplicate-free text saved to", output_file_path)