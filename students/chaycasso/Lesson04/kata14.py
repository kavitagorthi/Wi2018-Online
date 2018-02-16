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
    body_text = body_text.replace(";", ",")
    body_text = body_text.replace('\"', '')
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
            # print(kata_input)
            if kata_input in kata_dict:
                kata_dict[kata_input].append(tbl_word_list[i])
            else:
                kata_dict[kata_input]=[tbl_word_list[i]]

    # So we generate an initial seed for the Kata from a random draw of the list of possible initial keys.
    tbl_key_list = list(kata_dict.keys())
    kata_seed = (tbl_key_list[random.randrange(0, len(tbl_key_list))])
    tbl_kata_words=[]
    tbl_kata_words.append(kata_seed.split(" ")[0].capitalize())
    tbl_kata_words.append(kata_seed.split(" ")[1])
    print(tbl_kata_words)
    kata_length = 50
    for i in range(2, kata_length):
        if ((tbl_kata_words[i - 2]).lower() + " " + tbl_kata_words[i - 1].lower()) in kata_dict:
            kata_next_word_list = (kata_dict[(tbl_kata_words[i - 2]).lower() + " " + tbl_kata_words[i - 1].lower()])
            kata_next_word = kata_next_word_list[random.randrange(0,len(kata_next_word_list))]
            tbl_kata_words.append(kata_next_word)
        else:
            tbl_kata_words[i - 1] = tbl_kata_words[i - 1] + ". "
        print(tbl_kata_words)

