"""Assignment: Kata Fourteen: Tom Swift Under Milk Wood."""

import random
import tkinter as tk
from tkinter import filedialog


# load the file containing the book.

def get_filepath():
    """Return the path to the source file obtained from the user."""
    # Get the name of the source file from the user.
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    return path


def load_file(source_path):
    """Return a list containing the whole book split on blank space."""
    # Container for the whole text of the loaded book.
    book = []

    # Convert the whole book into a list.
    with open(source_path, 'r') as fromF:
        for line in fromF:
            if line == "\n" or line == "\r\n":
                line = line.strip()  # Get rid of "\r" or "\n" if any
                line = line.split()
                line.append("\n\n")  # Take care of paragraphs
            else:
                line = line.strip()
                line = line.split()
            # line.append("\n")
            book.extend(line)

    return book


def get_dict(a_list):
    """Return a dict for trigram-style text generation."""
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


def get_seed(a_dict):
    """Choose _randomly_ the first 2 words for the text."""
    while True:
        key = random.choice(list(a_dict.keys()
                                 )
                            )
        if key[0].isupper():  # Need an upper case first word
            seed = key
            break
    return seed


# Construct the output text.
def generate_text(source_dict, size):
    """Return a list with the generateed text of the given size."""
    output = []

    # Choose the first 2 words for the text. Must be an upper case word.
    seed = get_seed(source_dict)
    output.extend(seed.split())

    # Collect all the other words for the final text.
    for _ in range(size):
        key = ' '.join([output[-2], output[-1]])
        try:
            value = source_dict[key]  # The value here is a list
        except KeyError:
            print("KeyEroor: Dead end occured on the pair {}".format(key))
            break
        # If for our key there are several values, choose one randomly
        if len(value) > 1:
            value = random.choice(value)  # The value here is a list
            output.append(value)  # The value here is a string
        else:
            output.extend(value)  # The value here is a list

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


def get_destination_path(filename):
    """Get the destination directory from the user."""
    destination_dir = filedialog.askdirectory()
    destination_path = "{}/{}".format(destination_dir, filename)
    return destination_path


# Write the output text to a file.
def write_file(text, destination):
    """Write the output text to a file."""
    # Write the text to the file.
    with open(destination, 'w') as toF:
        if isinstance(text, str):
            toF.write(text)
        else:
            toF.write(str(text))

    # Display the message on screen.
    msg = "Wrote your masterpiece to the file {}\n"
    print(msg.format(destination))


def process_main():
    """Process all operations to generate some trigram-style text."""
    path = get_filepath()
    book = load_file(path)
    source_dict = get_dict(book)
    text_L = generate_text(source_dict, 200)  # Get text as a list
    text_S = formatter(text_L)  # Convert the list into a string
    # write_file(book, "book_as_list.txt")
    # write_file(source_dict, "resulting_dict.txt")
    # write_file(text_L, "output_as_list.txt")
    destination = get_destination_path("masterpiece.txt")
    write_file(text_S, destination)
    print_onscreen(text_S)


if __name__ == "__main__":
    process_main()
