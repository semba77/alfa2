import re

def file_compres(file):
    with open(file) as f:
        contents = f.read()
        word_list = contents.split()
        word_dict =count_text(word_list)
        text_compresion(word_dict, contents)


def count_text(str_list):
    word_dict = {}
    for x in str_list:
        word_dict[x] = str_list.count(x)
    return word_dict

def text_compresion(word_dict, contents):
    for key in word_dict.keys():
        if word_dict[key] >= 20 and len(key) >= 6:
            new_word = create_shorter_word()
            contents.replace(key, new_word)
    return contents

def create_shorter_word():


if __name__ == '__main__':
    file = "startfile.txt"
    file_compres(file)
