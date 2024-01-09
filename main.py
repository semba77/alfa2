import datetime
"""method with the purpose of opening the file choosen by user to be compresed and creating the compresed file. it uses the count_text() method and text_compresion() method"""
def file_compres(file):
    with open(file) as f:
        log_writer(f"{datetime.datetime}opening file: {file} ", 1)
        contents = f.read()
        word_list = contents.split()
        word_dict =count_text(word_list)
        compresed_text = text_compresion(word_dict, contents)
        compresed_file = open("data/compresed_file.txt", "w")
        compresed_file.write(compresed_text)
        compresed_file.close()
        log_writer(f"program ended", 1)
        log_writer("", 0)

"""the purpose of this method is to count the use of every word in the text and return a dictionary of words and the count of usage"""
def count_text(str_list):
    log_writer(f"counting the repetense of words in text ", 3)
    word_dict = {}
    for x in str_list:
        word_dict[x] = str_list.count(x)
    return word_dict

"""this method takes the dictionary of words and their usage and decide if they are to be shortened. it uses create_shorter_word() method"""
def text_compresion(word_dict, contents):
    repeting_word = 1
    for key in word_dict.keys():
        log_writer(f" making sure that the word: {key} meets the conditions", 2)
        if word_dict[key] >= 10 and len(key) >= 6:
            log_writer("conditions met", 3)
            new_word = create_shorter_word(key)
            if contents.find(new_word) != -1:
                new_word = new_word[:new_word.find(".")]+f"{repeting_word}."
                repeting_word+=1
            contents = contents.replace(key, new_word)
            first_word_end = contents.find(".", contents.find(new_word))+1
            contents = contents[:contents.find(new_word)] + key + f"({new_word})" + contents[first_word_end:]
    return contents
"""method wich decides what type of shortening the word gets"""
def create_shorter_word(word):
    log_writer(f"deconstructing {word} ", 3)
    characters =list(word)
    if len(word) <= 8:
        log_writer(f"{word} is in 1. category of lenght ", 2)
        characters.pop()
        characters.pop()
        characters.pop()
        characters.append(".")
    elif len(word) <= 11:
        log_writer(f"{word} is in 2. category of lenght ", 2)
        characters.pop()
        characters.pop()
        characters.pop()
        characters.pop()
        characters.pop()
        characters.append(".")
    elif len(word) <= 18:
        log_writer(f"{word} is in 3. category of lenght ", 2)
        characters.pop()
        characters.pop()
        characters.pop()
        characters.pop()
        characters.pop()
        characters.pop()
        characters.pop()
        characters.pop()
        characters.append(".")
    word =""
    for index in characters:
        word += index
    log_writer(f"reconstructing {word} ", 3)
    return word

def log_writer(text, text_detail):
    if text_detail == 0:
        open_log.write("\n")
        open_log.close()
    if text_detail <= log_detail:
        open_log.write(text)
        open_log.flush()





if __name__ == '__main__':
    global log_detail
    global open_log
    open_log = open("log/log_file.txt", "a")
    choice =0
    while log_detail != 1 or log_detail != 2 or log_detail != 3:
        log_detail = input('Enter 1 for log in minimal detail. 2 for log in some detail or 3 for log in full detail')
    file_compres(file)



