def listify(string):
    # separate string into a list of words
    string_list = []
    words = ""
    for char in string:
        if char == " " or char == "," or char == ".":
            string_list.append(words)
            words = ""
        else:
            words += char
    if words:
        string_list.append(words)
    return string_list

def repeated_word(string_list):
    # find first duplicate of a word
    # for word in string_list:
    for word in string_list:
        if word == "":
            string_list.remove(word)
    return string_list

if __name__ == "__main__":
    string = "Once upon a time, there was a brave princess who..."
    string_list = listify(string)
    print(repeated_word(string_list))