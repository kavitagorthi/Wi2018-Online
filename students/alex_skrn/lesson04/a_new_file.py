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
        seed = random.choice(list(a_dict.keys()))
        # Need an upper case first word and no \n\n in the second position.
        if seed[0].isupper() and len(seed.split()) == 2:
            break
    return seed


def get_new_value(a_dict, key):
    """Return a str -- a new value for the text, or False if no value."""
    try:
        value = a_dict[key]  # The value here is a list
    except KeyError:
        # print("KeyEroor: Dead end occured on the pair {}".format(key))
        return False

    # If for our key there are several values, choose one randomly
    if len(value) > 1:
        value = random.choice(value)
    else:
        value = value[0]
    return value


# Construct the output text.
def generate_text(source_dict, size):
    """Return a list with the generateed text of the given size."""
    output = []

    # Choose the first 2 words for the text
    seed = get_seed(source_dict)
    output.extend(seed.split())

    # Make sure my list has 2 elements at this point
    assert len(output) == 2

    # Collect all the other words for the final text.
    # print_flag = False
    while len(output) < size:
        key = ' '.join([output[-2], output[-1]])
        value = get_new_value(source_dict, key)
        # Handle the case where the dict has no such key
        if not value:
            # print_flag = True
            counter = len(output)
            # Go back along the output list to find a suitable key
            while counter > 1:
                key = ' '.join([output[counter-3], output[counter-2]])
                value = get_new_value(source_dict, key)
                # print(key)
                # Find a key capable of producing an alternative value
                if value != output[counter-1]:
                    # print("Alt value: ", value)
                    # Start the output list anew from that point
                    output = output[:counter-1]
                    break
                counter -= 1
            # print(output)
            # raise ValueError("get_new_value returned False!!!")
        # print(value, type(value))
        # print("Appended value:", value)
        output.append(value)

    # print("Len of output before return", len(output))
    # if print_flag:
    #     print("\nLen of output :", len(output))
        # print(output)
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
    # destination_d = get_destination_path("resulting_dict.txt")
    # write_file(source_dict, destination_d)
    text_L = generate_text(source_dict, 200)  # Get text as a list
    # destination_L = get_destination_path("book_as_list.txt")
    # write_file(book, destination_L)
    text_S = formatter(text_L)  # Convert the list into a string
    # write_file(text_L, "output_as_list.txt")
    destination = get_destination_path("masterpiece.txt")
    write_file(text_S, destination)
    print_onscreen(text_S)


def test_generate_text():
    """Find KeyValue errors on multiple runs of generate_text()."""
    path = "C:/Users/Alexey/Desktop/sherlock.txt"
    book = load_file(path)
    source_dict = get_dict(book)
    n_value_count = 0
    list_value_count = 0
    loop_count = 0
    # l_lengths = []
    for _ in range(1000):
        loop_count += 1
        val = generate_text(source_dict, 100)
        # l_lengths.append(len(val))
        if val is None:
            n_value_count += 1
        elif isinstance(val, list):
            list_value_count += 1
    print("Nones = ", n_value_count, "Lists = ", list_value_count)
    print("Num of loops = ", loop_count)
    # print(l_lengths)


if __name__ == "__main__":
    process_main()
    # test_generate_text()
