"""Lesson04 - Activity 2: Files."""

import os
import tkinter as tk
from tkinter import filedialog


def print_curr_dir_files():
    """Print the full path for all files in the current dir, 1 per line."""
    for file in os.listdir():
        print(os.path.abspath(file))


def copy_any_binary(source, destination):
    """Copy  a file from a source, to a destination."""
    with open(source, 'rb') as fromF, open(destination, 'wb') as toF:
        source_size = os.path.getsize(source)
        steps = source_size // 1000000
        remainder = source_size % 1000000
        for megabyte in range(steps):
            toF.write(fromF.read(megabyte))
        toF.write(fromF.read(remainder))


def copy_file_user_interaction():
    """Interact with the user on file copying operations."""
    root = tk.Tk()
    root.withdraw()

    # Get the name of the source file from the user.
    source_path = filedialog.askopenfilename()
    # print(source_path)

    # Get the target directory for the source copy from the user.
    target_dir = filedialog.askdirectory()
    # print(target_dir)

    # Construct the full path name for the copy of the source file.
    source_name = os.path.split(source_path)[1]
    # print(source_name)
    target_path = "{}/copy_of_{}".format(target_dir, source_name)
    # print(target_path)

    # Copy the source to the target destination.
    copy_any_binary(source_path, target_path)
    msg = "Copied {} to {}"
    print(msg.format(source_path, target_path))


if __name__ == "__main__":
    # print_curr_dir_files()
    copy_file_user_interaction()
