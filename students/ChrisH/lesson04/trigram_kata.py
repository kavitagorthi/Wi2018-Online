#!/usr/bin/env python3
# -----------------------------------------------------------
# trigram_kata.py
#  Implements a trigram algorithm that generates a couple of
#  hundred words of text using a book-sized file as input
# -----------------------------------------------------------


# word pair as key in the form 'word1 word2'
# book_trigram_data = { 'word pair': ['list of possible next words']}

trigram = {}


def generate_trigram(book):
    word1 = ''
    word2 = ''

    with open(book, 'r') as f_name:
        book_text = f_name.read()
        book_text = book_text.replace('\n', ' ')
        book_text = book_text.replace('  ', ' \n ')   # See double new lines as word choices

        words = book_text.split(' ')

        for word in words:

            if word1 and word2:
                newkey = "{} {}".format(word1, word2)
                if not newkey in trigram:
                    trigram[newkey] = [word]
                else:
                    trigram[newkey].append(word)
                word1 = word2
                word2 = word

            elif not word1:
                word1 = word

            elif not word2:
                word2 = word

    print(trigram)
    count = 0
    for key in trigram:
        if len(trigram[key]) > 1:
            print(key, trigram[key])
            count += 1
    print(count)


def main():
    generate_trigram('TSAHA.txt')


if __name__ == "__main__":
    main()
