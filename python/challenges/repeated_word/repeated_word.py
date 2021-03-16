from hashtable import Hashtable

hashtable = Hashtable()

def cleaner(string):
    filtered = string.translate({ord(i): None for i in '.,'})
    lower = filtered.lower()
    words = ""
    string_list = []
    for char in lower:
        if char == " ":
            string_list.append(words)
            words = ""
        else:
            words += char
    if words:
        string_list.append(words)
    return string_list

def counter(cleaned):
    final = {}
    for char in cleaned:
        if char not in final.keys():
            final[char] = 0
        final[char] += 1
    return final

def add_to_hashtable(dictionary):
    listify = list(dictionary.items())
    for pairs in listify:
        hashtable.add(pairs[0], pairs[1])

def repeated_word(string):
    cleaned = cleaner(string)
    dictionary = counter(cleaned)
    add_to_hashtable(dictionary)
    keys = dictionary.keys()
    for key in keys:
        value = hashtable.get(key)
        if value >= 2:
            return key
    return "No repeating words found"

if __name__ == "__main__":
    string = "Once upon a time, there was a brave princess who..."
    string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."

    print(repeated_word(string))
    print(repeated_word(string2))

#     dictionary = counter(cleaner(string2))
#     print('dictionary: ', dictionary)
#     # print(dictionary.keys())
#     # add_to_hashtable(dictionary)

#     # print("contains: ", hashtable.contains('upon'))
#     # print("contains: ", hashtable.contains('a'))
#     # print("contains: ", hashtable.contains('Once'))
#     # print(hashtable.get('upon'))
