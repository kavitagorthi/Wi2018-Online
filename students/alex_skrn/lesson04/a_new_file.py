"""Assignment: Kata Fourteen: Tom Swift Under Milk Wood."""

# import os
import random
import tkinter as tk
from tkinter import filedialog

# def tokenize(line):
#     '''Split string into separate tokens. Return a list.'''
#     assert isinstance(line, str), 'must be string'
#     res = ''
#     for char in line:
#         if char.isalnum() or char == ' ': ## .isalpha()
#             res += char
#         else:
#             res += ' ' + char + ' '
#     return res.split()


# load a file containing a book.
def load_file():
    """Return a list containing the whole book split on blank space."""
    root = tk.Tk()
    root.withdraw()

    # Container for the whole text of the loaded book.
    book = []

    # Get the name of the source file from the user.
    source_path = filedialog.askopenfilename()

    # Convert the whole book into a list.
    with open(source_path, 'r') as fromF:
        for line in fromF:
            if line == "\n" or line == "\r\n":
                line = line.strip()
                line = line.split()
                line.append("\n\n")  # Take care of paragraphs
            else:
                line = line.strip()  # Get rid of \r\n if any
                line = line.split()
            # line.append("\n")
            book.extend(line)
            # if len(line) > 2:
            #     for token in line:
    return book


def get_dict(a_list):
    """Return a dict for trigram-style text generation. Return a list."""
    d = {}
    for index, _ in enumerate(a_list):
        try:
            key = " ".join([a_list[index], a_list[index+1]])
            value = a_list[index+2]
            if key in d:
                d[key].append(value)
            else:
                d[key] = [value]
        except IndexError:
            break
    return d


# Construct the output text.
def generate_text(source_dict, size=200):
    """Return a list with the generateed text of the given size."""
    output = []

    # Choose the first 2 words for the text. Must be an upper case word.
    for key in source_dict:
        # print(key)
        try:
            if key[0].isupper():
                seed = key
                break
        except IndexError:
            pass
    output.extend(seed.split())
    # print(output)

    # Collect all the other words for the final text.
    for _ in range(size):
        key = ' '.join([output[-2], output[-1]])
        try:
            value = source_dict[key]
            # print(key, value)
            if len(value) > 1:
                value = random.choice(value)
                output.append(value)
            else:
                output.extend(value)
        except KeyError:
            print("KeyEroor: Dead end occured on the pair {}".format(key))
            break

    return output


def formatter(a_list):
    """Return a string containing the formatted text."""
    result = ""
    for token in a_list:
        if token == "\n\n":
            result += token
        else:
            result += (token + " ")
    return result


# Print on screen /
def print_onscreen(text):
    """Print the generated text on screen."""
    print(text)


# Write the output text to a file.
def write_file(text, filename):
    """Write the output text to a file."""
    # Get the target directory from the user.
    target_dir = filedialog.askdirectory()
    target_path = "{}/{}".format(target_dir, filename)

    # Write the text to the file.
    with open(target_path, 'w') as toF:
        if isinstance(text, str):
            toF.write(text)
        else:
            toF.write(str(text))

    # Display the message on screen.
    msg = "Wrote your text to the file {}\n"
    print(msg.format(target_path))


def process_main():
    """Process all operations to generate some trigram-style text."""
    book = load_file()
    write_file(book, "book_as_list.txt")
    source_dict = get_dict(book)
    write_file(source_dict, "resulting_dict.txt")
    text_L = generate_text(source_dict)
    write_file(text_L, "output_as_list.txt")
    text_S = formatter(text_L)
    write_file(text_S, "masterpiece.txt")  # Remove str later
    print_onscreen(text_S)


if __name__ == "__main__":
    process_main()
