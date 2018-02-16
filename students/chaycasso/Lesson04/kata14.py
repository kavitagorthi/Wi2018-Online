#!/usr/bin/env python3
#
# Kata 14
# Chay Casso, 2/15/18

import random

starter_file = "sherlock.txt"
with open(starter_file, 'r')as infile:
    body_text = infile.read()
    body_text = body_text.replace("\n"," ")
    body_text = body_text.replace("--",", ")
    body_text = body_text.replace(" (", ", ")
    body_text = body_text.replace(")", ", ")
    body_text = body_text.replace(" ,", "")
    # body_text = body_text.replace(", ", ". ")
    # Specifically flipping the ", " to " ," here to attempt to keep commas as valid objects.
    body_text = body_text.replace(", ", " ,")
    body_text = body_text.strip()
    # print(body_text)
    tbl_body_text = body_text.split(". ")
    # print(tbl_body_text)
    kata_dict = {}
    for element in tbl_body_text:
        tbl_word_list = element.split(" ")
        # print(tbl_word_list)
        for i in range(len(tbl_word_list)):
            if i < 2: continue
            kata_input = tbl_word_list[i-2] + " " + tbl_word_list[i-1]
            kata_input = kata_input.replace(",", "")
            print(kata_input)
            if kata_input in kata_dict:
                kata_dict[kata_input].append(tbl_word_list[i])
            else:
                kata_dict[kata_input]=[tbl_word_list[i]]
    print(kata_dict)