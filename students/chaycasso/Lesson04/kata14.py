#!/usr/bin/env python3
#
# Kata 14
# Chay Casso, 2/15/18

import random

starter_file = "sherlock_small.txt"
with open(starter_file, 'r')as infile:
    body_text = infile.read()
    body_text = body_text.replace("\n"," ")
    body_text = body_text.replace("--",", ")
    body_text = body_text.replace(" (", ", ")
    body_text = body_text.replace(")", ", ")
    body_text = body_text.replace(", ", ". ")
    body_text = body_text.replace(" .", "")
    body_text.strip()
    print(body_text)
    tbl_body_text = body_text.split(". ")
    print(tbl_body_text)
    