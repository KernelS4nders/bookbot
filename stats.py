def word_count(book_content):
    count = 0
    split_words = book_content.split()
    for word in split_words:
        count += 1
    return count


def char_count(book_content):
    char_dict_vals = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    split_words = book_content.split()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # starts to go word by word in the text
    for word in split_words:
        for character in word.lower():
            if character in alphabet:
                char_dict_vals[character] += 1
    return char_dict_vals


def sorted_list(all_char_counts):
    def sort_on(items):
        return items["num"]

    new_list = []
    new_dict = {}
    for key, val in all_char_counts.items():
        new_list.append({"char": key, "num": val})
    new_list.sort(reverse=True, key=sort_on)

    for test in new_list:
        char = test["char"]
        count = test["num"]
        new_dict[char] = count
    for key, val in new_dict.items():
        print(f"{key}: {val}")
    # for
    # new_list.sort(reverse=True, key=)
    # return empty_list
